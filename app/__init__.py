# app/__init__.py
from flask import Flask

app = Flask(__name__)

# Import routes after app is created to avoid circular imports
from app import routes