from datetime import datetime
import pytz

# Get IST timezone
ist = pytz.timezone('Asia/Kolkata')

# Display current IST time
current_ist = datetime.now(ist)
print(f"Current IST time: {current_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Continuous clock display (updates every second)
import time
print("\n--- Live IST Clock --- (Press Ctrl+C to stop)")
try:
    while True:
        now = datetime.now(ist)
        print(f"\r{now.strftime('%H:%M:%S')}", end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nStopped clock display.")
