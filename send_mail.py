import config
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from logging import getLogger

logger = getLogger(__name__)


def send_mail(target_date, check_file):
    try:
        logger.info('[CALL] send_mail')

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

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = config.smtp_user
        msg["To"] = config.mail_to_address
        msg.attach(MIMEText(body, "html"))

        filename = os.path.basename(check_file)
        with open(check_file, "rb") as f:
            mb = MIMEApplication(f.read())

        mb.add_header("Content-Disposition", "attachment", filename=filename)
        msg.attach(mb)

        to_list = config.mail_to_address.split(",")
        s = smtplib.SMTP(config.smtp_server, config.smtp_port)
        s.starttls()
        s.login(config.smtp_user, config.smtp_pass)
        s.sendmail(config.smtp_user, to_list, msg.as_string())
        s.quit()
    except Exception as e:
        logger.error(e)
