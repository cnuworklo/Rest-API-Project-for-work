import os
from dotenv import load_dotenv
from redis import ConnectionPool, Redis

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
QUEUES = ["emails", "default"]

if REDIS_URL:
    try:
        connection = Redis.from_url(REDIS_URL)
    except ConnectionError as e:
        print(f"Error connecting to Redia: {e}")
    else:
        print("REDIS_URL is not set.")
            