import os

TOKEN = os.environ.get("Token")
URL = os.environ.get("URL")
#TOKEN="1801579405:AAEyIi4t1YonxGkmfImAlhyyNotdJ0qDCxY"
#URL="https://c9115515a0c5.ngrok.io"
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
