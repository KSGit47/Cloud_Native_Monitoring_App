import psutil
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory()
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message  = "High Load. Please Scale Up."
    return f"CPU : {cpu_percent} & Memory : {mem_percent}"
if __name__ == '__main'