from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)

# Get IST timezone
ist = pytz.timezone('Asia/Kolkata')

@app.route("/")
def show_time():
    now = datetime.now(ist)
    return f"Current IST time: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}"

if __name__ == "__main__":
    # Run on all interfaces, port 3000
    app.run(host="0.0.0.0", port=3000)
