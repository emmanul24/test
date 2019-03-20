from pymongo import MongoClient, errors
import asyncio
import time

start_time = time.time()


class Dbfirst:
    def __init__(self):
        self.client = MongoClient(host='192.168.20.120', port=27018)
        db1 = self.client.badoo_leaked_data
        self.collection1 = db1.data
        db2 = self.client.bitly_database
        self.collection2 = db2.data
        db3 = self.client.btc_collection_database
        self.collection3 = db3.data
        db4 = self.client.gaming_collection
        self.collection4 = db4.data
        db5 = self.client.gmail_data
        self.collection5 = db5.data

        self.lst = list()
        self.loop = asyncio.new_event_loop()

    async def database5(self, q):
        try:
            if self.collection5.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection5.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db5')
        except errors.ExecutionTimeout:
            pass

    async def database4(self, q):
        try:
            if self.collection4.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection4.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db4')
        except errors.ExecutionTimeout:
            pass

    async def database3(self, q):
        try:
            if self.collection3.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection3.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db3')
        except errors.ExecutionTimeout:
            pass

    async def database2(self, q):
        try:
            if self.collection2.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection2.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db2')
        except errors.ExecutionTimeout:
            pass

    async def database1(self, q):

        try:
            if self.collection1.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection1.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db1')
        except errors.ExecutionTimeout:
            pass

    def searching1(self, q):
        task = [
            self.database1(q),
            self.database2(q),
            self.database3(q),
            self.database4(q),
            self.database5(q),
        ]

        self.loop.run_until_complete(asyncio.wait(task))
        self.loop.close()
        return self.lst


if __name__ == '__main__':
    obj = Dbfirst()
    print(obj.searching1(q="abounkml@yahoo.co.uk"))
