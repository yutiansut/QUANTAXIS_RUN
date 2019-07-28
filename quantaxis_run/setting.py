import os

qarun_amqp = os.getenv('QARUN_AMQP', 'pyamqp://guest:guest@localhost:5672//')
qarun_mongo_ip = os.getenv('MONGODB', 'localhost')
