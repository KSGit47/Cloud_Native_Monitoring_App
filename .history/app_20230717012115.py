import psutil
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory()
    Message = None
    if cpu_percent > 80 or 
