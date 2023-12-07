from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    "49.50.164.200",
    "https://floodingpoint.p-e.kr/",
    "https://dev--floodingpoint-seoul.netlify.app/",
    "https://floodingpoint-seoul.netlify.app/",
]

# https://dev--floodingpoint-seoul.netlify.app/
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://floodingpoint.p-e.kr/",
    "https://dev--floodingpoint-seoul.netlify.app/",
    "https://floodingpoint-seoul.netlify.app/",
]
