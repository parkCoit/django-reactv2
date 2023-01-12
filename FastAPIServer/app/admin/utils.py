from datetime import datetime

def current_time():
    today = datetime.now()
    return f"{today.time()}"
