import config
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(target_date, check_file):

    smtp_server = "smtp.office365.com"
    smtp_port = 587
    smtp_user = "inquiry@vital-service.com"

    to_address = config.mail_to_address
    from_address = smtp_user

    subject = "version check(対象日：{})".format(target_date.strftime('%Y-%m-%d'))
    body = """
    <html>
        <body>
            <p>
            ソフトウェアバージョンチェックメールです<br>
            添付ファイルをご確認お願いします。
            </p>
        </body>
    </html>"""

    filename = os.path.basename(check_file)

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address
    msg.attach(MIMEText(body, "html"))

    with open(check_file, "rb") as f:
        mb = MIMEApplication(f.read())

    mb.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(mb)

    to_list = to_address.split(",")
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()
    s.login(smtp_user, config.smtp_pass)
    s.sendmail(from_address, to_list, msg.as_string())
    s.quit()

