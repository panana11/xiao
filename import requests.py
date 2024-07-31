import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# News API settings
api_key = 'your_newsapi_key_here'
url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + api_key

# Fetch news
response = requests.get(url)
news_data = response.json()

# Email settings
from_email = 'your_email@gmail.com'
to_email = 'daniel@thefullwiki.org'
password = 'your_email_password'  # Be cautious with email passwords

# Create MIME object
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = "Today's News Headlines"

# Email content
headlines = [article['title'] for article in news_data['articles'][:5]]  # Top 5 headlines
body = '\n'.join(headlines)
msg.attach(MIMEText(body, 'plain'))

# Send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, password)
text = msg.as_string()
server.sendmail(from_email, to_email, text)
server.quit()