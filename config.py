import os
from dotenv import load_dotenv

load_dotenv()

KEYCLOAK_SERVER_URL = os.environ['KEYCLOAK_SERVER_URL']
KEYCLOAK_REALM = os.environ['KEYCLOAK_REALM']
KEYCLOAK_CLIENT_ID = os.environ['KEYCLOAK_CLIENT_ID']
KEYCLOAK_CLIENT_SECRET_KEY = os.environ['KEYCLOAK_CLIENT_SECRET_KEY']
REDIRECT_URI = os.environ['REDIRECT_URI']

DEBUG = bool(os.getenv('DEBUG'))
