import os
from dotenv import load_dotenv
from redis import ConnectionPool, Redis

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
QUEUES = ["emails", "default"]

if REDIS_URL:
    connection_pool = ConnectionPool.from_url(REDIS_URL)
    redis_connection = Redis(connection_pool=connection_pool)
else:
    print("Warning: REDIS_URL is not set. Using default Redis connection.")
    connection_pool = ConnectionPool.from_url('redis://localhost:6379/0')
    redis_connection = Redis(connection_pool=connection_pool)
    