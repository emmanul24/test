from pymongo import MongoClient, errors
import asyncio
import time

start_time = time.time()


class Dbfifth:
    def __init__(self):
        self.client = MongoClient(host='192.168.20.120', port=27018)

        db21 = self.client.username_collection
        self.collection21 = db21.data
        db22 = self.client.vk_leaked_data
        self.collection22 = db22.data
        db23 = self.client.whois_database
        self.collection23 = db23.data
        db24 = self.client.yahoo_leaked_data
        self.collection24 = db24.data
        db25 = self.client.yandex_database
        self.collection25 = db25.data

        self.lst = list()
        self.loop = asyncio.new_event_loop()

    async def database21(self, q):
        try:
            if self.collection21.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection21.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db21')
        except errors.ExecutionTimeout:
            pass

    async def database22(self, q):
        try:
            if self.collection22.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection22.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db22')
        except errors.ExecutionTimeout:
            pass

    async def database23(self, q):
        try:
            if self.collection23.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection23.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db23')
        except errors.ExecutionTimeout:
            pass

    async def database24(self, q):
        try:
            if self.collection24.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection24.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db24')
        except errors.ExecutionTimeout:
            pass

    async def database25(self, q):
        try:
            if self.collection25.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection25.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db25')
        except errors.ExecutionTimeout:
            pass

    def searching5(self, q):
        task = [

            self.database21(q),
            self.database22(q),
            self.database23(q),
            self.database24(q),
            self.database25(q),

        ]

        self.loop.run_until_complete(asyncio.wait(task))
        self.loop.close()
        return self.lst


if __name__ == '__main__':
    obj = Dbfifth()
    print(obj.searching5(q="abounkml@yahoo.co.uk"))
