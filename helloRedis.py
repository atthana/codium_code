# step 1: import the redis-py client package
import redis


class RedisConnection:

    # step 2: define our connection information for Redis
    # Replaces with your configuration information

    def __init__(self):
        self.r = None
        self.list_name = "task"

    def connect_server(self):
        """Example Hello Redis Program"""
        redis_host = "localhost"
        redis_port = 6379
        redis_password = ""
        # step 3: create the Redis Connection object
        try:

            # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
            # using the default encoding utf-8.  This is client specific.
            self.r = redis.StrictRedis(host=redis_host, port=redis_port,
                                       password=redis_password, decode_responses=True)

            # step 4: Set the hello message in Redis
            self.r.set("msg:hello", "Hello World!!!")

            # step 5: Retrieve the hello message from Redis
            msg = self.r.get("msg:hello")
            print(msg)

        except Exception as e:
            print(e)

    def set_name(self, item):
        self.r.rpush(self.list_name, item)

    def view_items(self):
        l = self.r.lrange(self.list_name, 0, -1)
        item_id = 0
        for x in l:
            item_id = 1 + item_id
            print("{} : {}".format(item_id, x))

    def remove_item(self, index):
        self.r.lset(self.list_name, index, "removed")
        self.r.lrem(self.list_name, 0, "removed")
