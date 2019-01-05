import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALTER_TIMEOUT = 10
COLLECTION = "alerts"