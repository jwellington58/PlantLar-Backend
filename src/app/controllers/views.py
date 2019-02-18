from flask import Flask
from app import app, db
from app.models import tables

@app.route('/')
def hello():
  return "Hello, Flask"