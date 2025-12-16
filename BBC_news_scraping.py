# -*- coding: utf-8 -*-
"""
Created on Fri May  2 14:55:22 2025
@author: akanksha
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# -------------------- CONFIGURATION --------------------
SENDER_EMAIL = "akankshawaghamode2001@gmail.com"
SENDER_PASSWORD = "ogkr cxku jiab zcut"  # Use App Password
RECEIVER_EMAILS = ["reciever_email.com"] # List of recipient emails

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

BBC_URL = "https://www.bbc.com/news"
NDTV_URL = "https://www.ndtv.com/health"
# -------------------------------------------------------

def send_email(subject, html_body, recipients):
    msg = MIMEMultipart()
    msg["From"] = "Akanksha's Daily News Bot <" + SENDER_EMAIL + ">"
    msg["To"] = SENDER_EMAIL
    msg["Bcc"] = ", ".join(recipients)
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print(f"Email sent successfully (BCC) to: {', '.join(recipients)}")

def scrape_bbc():
    print("Scraping BBC...")
    response = requests.get(BBC_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    base_url = "https://www.bbc.com"
    headlines = []

    for a_tag in soup.select('a[href^="/news"]'):
        headline = a_tag.get_text(strip=True)
        link = base_url + a_tag["href"]
        if headline and link not in [h['link'] for h in headlines]:
            headlines.append({"headline": headline, "link": link, "source": "BBC"})
        if len(headlines) >= 10:
            break
    return headlines

def scrape_ndtv():
    print("Scraping NDTV...")
    response = requests.get(NDTV_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = []

    for div in soup.select("div.news_Itm"):
        headline_tag = div.find("h2")
        link_tag = div.find("a", href=True)
        if headline_tag and link_tag:
            headline = headline_tag.get_text(strip=True)
            link = link_tag["href"]
            if headline and link not in [h['link'] for h in headlines]:
                headlines.append({"headline": headline, "link": link, "source": "NDTV"})
            if len(headlines) >= 10:
                break
    return headlines

def scrape_and_send():
    bbc_headlines = scrape_bbc()
    ndtv_headlines = scrape_ndtv()

    all_headlines = bbc_headlines + ndtv_headlines
    unique_headlines = []
    seen_links = set()

    for item in all_headlines:
        if item['link'] not in seen_links:
            unique_headlines.append(item)
            seen_links.add(item['link'])

    if not unique_headlines:
        print("No headlines found.")
        return

    # Save to CSV
    date_str = datetime.now().strftime("%Y-%m-%d")
    df = pd.DataFrame(unique_headlines)
    filename = f"news_digest_{date_str}.csv"
    df.to_csv(filename, index=False)
    print(f"Combined headlines saved to {filename}")

    # Create HTML email body
    html_content = f"""
    <html>
    <body style="font-family:Arial,sans-serif;">
        <h2 style="color:#2b6cb0;"> Daily News Digest – {date_str}</h2>
        <p>Here are the top headlines from BBC & NDTV:</p>
        <ul>
    """
    for item in unique_headlines:
        html_content += f"<li><a href='{item['link']}' style='color:#1a0dab;'>{item['headline']}</a> <span style='color:#555;'>({item['source']})</span></li>"

    html_content += f"""
        </ul>
        <hr>
        <p style="font-size:12px; color:gray;">
            This email was sent by an automated bot.<br>
            To stop receiving these, reply with <b>UNSUBSCRIBE</b>.<br>
            Delivered by <i>Akanksha's Daily News Bot</i> at {datetime.now().strftime("%Y-%m-%d %H:%M")} IST.
        </p>
    </body>
    </html>
    """

    send_email(f"Top News Digest – {date_str}", html_content, RECEIVER_EMAILS)

# Schedule daily at 03:30 PM
schedule.every().day.at("00:12").do(scrape_and_send)

print("Waiting for scheduled time... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)

