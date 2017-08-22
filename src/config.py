# import sys
import os
from datetime import timedelta
import locale


BASE_DIR = os.path.abspath(os.getcwd())

try:
    locale.setlocale(locale.LC_ALL, 'russian')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "ThereIsNoSpoon"

    # USERNAME = 'admin'
    # PASSWORD = 'admin'

    LOG = {
        "FILENAME": os.path.join(BASE_DIR, "log", "execom.log"),
        "MAX_BYTES": 1024 * 1024,
        "BACKUP_COUNT": 10,
        "FORMAT": "%(asctime)s[%(levelname)s]:\t%(message)s\tin %(module)s at %(lineno)d",
    }

    # configuration db
    DB_PATH = os.path.join(BASE_DIR, "db")
    DB_FILENAME = "blog.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:////%s/%s" % (DB_PATH, DB_FILENAME)
    # SQLALCHEMY_DATABASE_URI = "sqlite:///../db/%s" % (DB_FILENAME)
    # SQLALCHEMY_DATABASE_URI = "sqlite:///db/%s" % (DB_FILENAME)
    # SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % ('root', 'root', '127.0.0.1', 'pythonpub1')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BACKUP_TIME = timedelta(minutes=30)
    BACKUP_PATH = os.path.join(BASE_DIR, "db", "backup")
    BACKUP_FILENAME = "blog-%s.db"

    VIEW_CASE = "edit_case"

    UPLOAD_PATH = os.path.join(BASE_DIR, "upload")
    # UPLOAD_FOLDER = './static/upload/'
    # ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    # configuration page num
    RECORDS_ON_PAGE = 50
    # PER_PAGE = 10

    # RECAPTCHA_PUBLIC_KEY = '6Ld4rwITAAAAAKUD5AntlHi7HL36W2vHJQOIjQmA'
    # RECAPTCHA_PRIVATE_KEY = '6Ld4rwITAAAAAFE8nTS852QbsqCBx1mN8D4BqenE'


class ProductionConfig(Config):
    pass


class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


app_config = {
    'development': DebugConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
