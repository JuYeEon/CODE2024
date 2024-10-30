import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

def send_email_with_file():
    # Gmail 
    gmail_user = ''
    gmail_password = ''  
    subject = "마인드 메이트에서 전함"
    body = "귀하의 자녀가 어려움을 겪고 있는 것 같아요. 한 번 대화를 시도해 보세요."
    to_email = ""

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject


    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, to_email, text)
    server.quit()

send_email_with_file()
