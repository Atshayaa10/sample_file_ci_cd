import datetime

# High-risk test - part 3
# Multiple files = HIGH RISK

def get_timestamp():
    return datetime.datetime.now()

def log_event(event):
    timestamp = get_timestamp()
    print(f"[{timestamp}] {event}")

if __name__ == "__main__":
    log_event("System started")
