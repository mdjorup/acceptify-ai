from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()


app = Flask(__name__)
CORS(app, origins="*")
limiter = Limiter(key_func=get_remote_address, app=app, default_limits=["10/minute"])


