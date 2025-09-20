# 📰 Automated Email-Based News Aggregator

An intelligent Python script that automatically scrapes top news headlines from BBC and NDTV websites, compiles them into a beautifully formatted HTML email digest, and sends daily updates to specified recipients.

## 🎯 Project Overview

This automated news aggregator eliminates the need to manually check multiple news websites by delivering a consolidated daily digest straight to your inbox. The system scrapes headlines, removes duplicates, saves data locally, and sends professionally formatted email notifications.

## ✨ Key Features

- 🌐 **Multi-Source Scraping**: Extracts headlines from BBC News and NDTV Health
- 📧 **Automated Email Delivery**: Sends HTML-formatted daily digests
- 🔄 **Duplicate Removal**: Ensures unique headlines across sources
- 💾 **Data Storage**: Saves daily news data to CSV files
- ⏰ **Scheduled Execution**: Runs automatically at specified times
- 🎨 **Professional Formatting**: Clean HTML email templates
- 📊 **Source Attribution**: Clearly labels news sources
- 🔒 **Secure Authentication**: Uses Gmail App Passwords

## 🛠️ Technical Stack

- **Python 3.12.6**
- **Libraries Used**:
  - `requests` - HTTP requests for web scraping
  - `BeautifulSoup` - HTML parsing and data extraction
  - `pandas` - Data manipulation and CSV export
  - `smtplib` - Email sending functionality
  - `schedule` - Task scheduling
  - `datetime` - Date and time handling

## 📁 Project Structure

```
news-aggregator/
├── news_aggregator.py          # Main script
├── news_digest_YYYY-MM-DD.csv  # Daily CSV outputs
├── README.md                   # This file
└── requirements.txt            # Dependencies
```

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/automated-news-aggregator.git
cd automated-news-aggregator
```

### 2. Install Dependencies
```bash
pip install requests beautifulsoup4 pandas schedule
```

### 3. Gmail Configuration
1. Enable **2-Factor Authentication** on your Gmail account
2. Generate an **App Password**:
   - Go to Google Account Settings → Security → App Passwords
   - Generate password for "Mail"
3. Update the configuration in the script:
```python
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"  # 16-digit app password
RECEIVER_EMAILS = ["recipient1@gmail.com", "recipient2@gmail.com"]
```

### 4. Customize Settings
```python
# Modify these URLs if needed
BBC_URL = "https://www.bbc.com/news"
NDTV_URL = "https://www.ndtv.com/health"

# Change schedule time (24-hour format)
schedule.every().day.at("15:30").do(scrape_and_send)  # 3:30 PM
```

## 🔧 Usage

### Run Once (Manual Execution)
```bash
python news_aggregator.py
```

### Automated Daily Execution
The script runs continuously and executes the news aggregation at the scheduled time. To run in background:

**Linux/Mac:**
```bash
nohup python news_aggregator.py &
```

**Windows:**
```bash
python news_aggregator.py
```

## 📊 Output Examples

### Email Format
- **Subject**: "📰 Top News Digest – 2025-01-15"
- **Content**: Clean HTML with clickable headlines
- **Attribution**: Source labels (BBC/NDTV)
- **Timestamp**: Delivery time and bot information

### CSV Export
Daily files saved as `news_digest_YYYY-MM-DD.csv` containing:
| headline | link | source |
|----------|------|--------|
| Breaking News Story | https://... | BBC |
| Health Update | https://... | NDTV |

## 🎨 Features Breakdown

### Web Scraping Engine
- **BBC**: Targets news articles with `/news` URL pattern
- **NDTV**: Focuses on health section content
- **Error Handling**: Graceful handling of network issues
- **Rate Limiting**: Respectful scraping practices

### Email System
- **HTML Templates**: Professional email formatting
- **BCC Delivery**: Privacy-conscious mass emailing
- **Unsubscribe Option**: User-friendly opt-out
- **Timestamp**: Clear delivery tracking

### Data Management
- **Deduplication**: Removes duplicate headlines across sources
- **CSV Export**: Daily data backup for analysis
- **Structured Data**: Organized headline, link, and source information

## ⚙️ Configuration Options

### Customize News Sources
```python
def scrape_custom_site():
    url = "https://your-news-site.com"
    # Add your scraping logic here
    return headlines
```

### Modify Email Template
```python
html_content = """
<html>
<body style="your-custom-styling">
    <!-- Your custom email template -->
</body>
</html>
"""
```

### Adjust Schedule
```python
# Multiple schedule options
schedule.every().day.at("09:00").do(scrape_and_send)  # 9 AM daily
schedule.every().monday.at("10:30").do(scrape_and_send)  # Weekly
schedule.every(6).hours.do(scrape_and_send)  # Every 6 hours
```

## 🔒 Security Considerations

- ✅ **App Passwords**: Uses Gmail App Passwords (not main password)
- ✅ **Environment Variables**: Consider using `.env` for credentials
- ✅ **BCC Emails**: Protects recipient privacy
- ⚠️ **Credential Storage**: Keep credentials secure and never commit to Git

### Environment Variables Setup (Recommended)
```python
import os
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
```

## 🚀 Future Enhancements

- [ ] **Multi-Language Support**: Headlines in different languages
- [ ] **RSS Feed Integration**: Support for RSS/Atom feeds
- [ ] **Web Dashboard**: Flask/Django web interface
- [ ] **Mobile Notifications**: Push notifications via Telegram/WhatsApp
- [ ] **ML Integration**: Sentiment analysis and news categorization
- [ ] **Database Storage**: PostgreSQL/MongoDB for historical data
- [ ] **API Development**: REST API for external access
- [ ] **Docker Support**: Containerized deployment

## 🐛 Troubleshooting

### Common Issues

**Email Not Sending:**
```
❌ Error: Authentication failed
✅ Solution: Check App Password and 2FA settings
```

**No Headlines Scraped:**
```
❌ Error: Website structure changed
✅ Solution: Update CSS selectors in scraping functions
```

**Schedule Not Working:**
```
❌ Error: Script stops unexpectedly
✅ Solution: Use process managers like supervisor or systemd
```

### Debug Mode
Add logging for troubleshooting:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

## 📄 Requirements

```txt
requests>=2.31.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
schedule>=1.2.0
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚖️ Legal & Ethics

- **Respectful Scraping**: Includes delays and respects robots.txt
- **Fair Use**: For personal/educational use only
- **Copyright**: Headlines are attributed to original sources
- **Terms of Service**: Users responsible for compliance with website ToS

## 👨‍💻 Author

**Akanksha Waghamode**
- 📧 Email: akankshawaghamode2001@gmail.com
- 🔗 GitHub: [@akanksha3-3](https://github.com/akanksha3-3)
- 💼 LinkedIn: [akanksha-waghamode](https://www.linkedin.com/in/akanksha-waghamode-25aa9724a/)

## 📜 License

This project is for educational purposes. Please respect the terms of service of the websites being scraped.

---

⭐ **If you found this project useful, please give it a star!** ⭐
