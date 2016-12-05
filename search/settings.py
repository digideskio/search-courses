import os

KEY = os.environ.get("KEY_GOOGLE")
CX = os.environ.get("CX_GOOGLE")

REDIS_HOST = os.environ.get("REDIS_HOST", "http://localhost:6379")
REDIS_PWD = os.environ.get("REDIS_PWD", "palomas")

PALOMA_DB_HOST = os.environ.get("MONGOLAB_HOST", 'localhost')
PALOMA_DB_PORT = os.environ.get("MONGOLAB_PORT", 27017)
PALOMA_DB_NAME = os.environ.get("MONGOLAB_NAME", 'paloma')

