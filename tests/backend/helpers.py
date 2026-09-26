# helpers.py

import time
def get_userdata():
    timestamp = int(time.time() * 1000)
    return {"name": f"Test User {timestamp}",
            "email": f"user{timestamp}@expandtesting.com",
            "password": "password123"}