import os
# cross site request forgery
WTF_CSRF_ENABLED = True
# validatation token
SECRET_KEY = 'you-will-never-guess'


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db repo')