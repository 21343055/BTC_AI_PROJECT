import os
import requests


def send_telegram_message(message):

    token = os.getenv(
        "TELEGRAM_BOT_TOKEN"
    )

    chat_id = os.getenv(
        "TELEGRAM_CHAT_ID"
    )

    if not token or not chat_id:

        print(
            "Telegram secret not found."
        )

        return

    url = (
        f"https://api.telegram.org/"
        f"bot{token}/sendMessage"
    )

    payload = {

        "chat_id": chat_id,

        "text": message
    }

    try:

        requests.post(
            url,
            json=payload,
            timeout=30
        )

    except Exception as e:

        print(
            f"Telegram error: {e}"
        )