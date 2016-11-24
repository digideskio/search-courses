import os

KEY = os.environ.get("KEY_GOOGLE")
CX = os.environ.get("CX_GOOGLE")

REDIS_HOST = os.environ.get("REDIS_HOST", "http://localhost:6379")
REDIS_PWD = os.environ.get("REDIS_PWD", "palomas")

