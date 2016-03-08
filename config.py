DEBUG = True

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = "you-will-never-guess"
DB_USERNAME = "root"
DB_PASSWORD = ''
BLOG_DATABASE_NAME = "test"
DB_HOST = os.getenv("IP", "0.0.0.0")
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False




THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = "secret"

AIRBRAKE_API_KEY = "5d60e20695e37dfdc71397b087922b20"

MANDRILL_API_KEY = "vU1J3t0AJAFpb8uQ53YlGg"



ENVIRONMENT = os.getenv('ENVIRONMENT', 'Development')


SITE_PATH = "http://0.0.0.0:1111"
# CREDIT_CARD_API_PATH = "https://test.gpaysafe.com"
# CREDIT_CARD_API_KEY = "dc570e59665a393709813aabe6ff3037"
# CREDIT_CARD_SECRET_KEY = "329d6850"

if ENVIRONMENT == "Production":
    SQLALCHEMY_DATABASE_URI = DB_URI
    DEBUG = False
    SITE_PATH = "https://www.paynet.website"
elif ENVIRONMENT == "Test":
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/dbname'
