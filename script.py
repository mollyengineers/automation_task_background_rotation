import os
import time
from datetime import datetime, time as dt_time
import pytz

def set_background(image_path):
    """Sets the desktop background image."""
    try:
        os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{image_path}'")
        os.system(f"gsettings set org.gnome.desktop.background picture-options 'stretched'")
        print(f"Background set to: {image_path}")
    except Exception as e:
        print(f"Error setting background: {e}")

def is_daytime():
    """Checks if the current time in Central Time is between 6:30 AM and 8:00 PM."""
    central_tz = pytz.timezone('America/Chicago')  # Central Time
    now_central = datetime.now(central_tz).time()
    start_time = dt_time(6, 30)
    end_time = dt_time(20, 0)  # 8:00 PM
    return start_time <= now_central < end_time

if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")
    downloads_path = os.path.join(desktop_path, "Downloads")
    nighttime_image = os.path.join(downloads_path, "nighttimebackground.jpg")
    daytime_image = os.path.join(downloads_path, "daytimebackground.jpg")

    # Ensure pytz is installed
    try:
        import pytz
    except ImportError:
        print("pytz not installed. Please install it using: pip install pytz")
        exit()

    while True:
        if is_daytime():
            set_background(daytime_image)
        else:
            set_background(nighttime_image)

        # Check the time again after a short interval (e.g., every minute)
        time.sleep(60)
