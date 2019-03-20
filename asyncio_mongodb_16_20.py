from pymongo import MongoClient, errors
import asyncio
import time

start_time = time.time()


class Dbforth:
    def __init__(self):
        self.client = MongoClient(host='192.168.20.120', port=27018)

        db16 = self.client.streaming_collection
        self.collection16 = db16.data
        db17 = self.client.trading_collection
        self.collection17 = db17.data
        db18 = self.client.twitter_data
        self.collection18 = db18.data
        db19 = self.client.unsorted_collection
        self.collection19 = db19.data
        db20 = self.client.usa_accounts_database
        self.collection20 = db20.data

        self.lst = list()
        self.loop = asyncio.new_event_loop()

    async def database16(self, q):
        try:
            if self.collection16.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection16.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db16')
        except errors.ExecutionTimeout:
            pass

    async def database17(self, q):
        try:
            if self.collection17.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection17.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db17')
        except errors.ExecutionTimeout:
            pass

    async def database18(self, q):
        try:
            if self.collection18.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection18.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db18')
        except errors.ExecutionTimeout:
            pass

    async def database19(self, q):
        try:
            if self.collection18.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection18.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db19')
        except errors.ExecutionTimeout:
            pass

    async def database20(self, q):
        try:
            if self.collection20.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection20.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db20')
        except errors.ExecutionTimeout:
            pass

    def searching4(self, q):
        task = [

            self.database16(q),
            self.database17(q),
            self.database18(q),
            self.database19(q),
            self.database20(q),

        ]

        self.loop.run_until_complete(asyncio.wait(task))
        self.loop.close()
        return self.lst


if __name__ == '__main__':
    obj = Dbforth()
    print(obj.searching4(q="abounkml@yahoo.co.uk"))
