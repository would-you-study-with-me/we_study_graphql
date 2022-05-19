from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token


class GoogleOauth2:

    def __init__(self):

        with build('drive', 'v3') as service:
            pass
