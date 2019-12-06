"""
Alerts for the conmon package.
"""

import smtplib
from email.message import EmailMessage
from conmon import utils
import logging

config = utils.config()


def alert(subject, content):
    """
    alert(subject, content) -> None

    where subject -> str; a subject line
          content -> str; a message body

    Send an alert through the configured SMTP server.
    """

    try:
        with smtplib.SMTP_SSL(config["email"]["server"],
                              config["email"]["port"]) as server:
            server.ehlo()
            server.login(config["email"]["user"],
                         config["email"]["pass"])

            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = config["email"]["from"]
            msg["To"] = ",".join(config["email"]["to"])
            msg.set_content(content)

            server.send_message(msg)
    except:
        logging.error("Exception occurred while sending alert", exc_info=True)
    return
