from pymongo import MongoClient, errors
import asyncio
import time

start_time = time.time()


class Dbthird:
    def __init__(self):
        self.client = MongoClient(host='192.168.20.120', port=27018)

        db11 = self.client.mySpace_database
        self.collection11 = db11.data
        db12 = self.client.number_collection
        self.collection12 = db12.data
        db13 = self.client.porn_collection
        self.collection13 = db13.data
        db14 = self.client.private_collection
        self.collection14 = db14.data
        db15 = self.client.shopping_collection
        self.collection15 = db15.data

        self.lst = list()
        self.loop = asyncio.new_event_loop()

    async def database11(self, q):
        try:
            if self.collection11.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection11.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db11')
        except errors.ExecutionTimeout:
            pass

    async def database12(self, q):
        try:
            if self.collection12.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection12.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db12')
        except errors.ExecutionTimeout:
            pass

    async def database13(self, q):
        try:
            if self.collection13.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection13.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db13')
        except errors.ExecutionTimeout:
            pass

    async def database14(self, q):
        try:
            if self.collection14.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection14.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db14')
        except errors.ExecutionTimeout:
            pass

    async def database15(self, q):
        try:
            if self.collection15.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection15.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db15')
        except errors.ExecutionTimeout:
            pass

    def searching3(self, q):
        task = [

            self.database11(q),
            self.database12(q),
            self.database13(q),
            self.database14(q),
            self.database15(q),

        ]

        self.loop.run_until_complete(asyncio.wait(task))
        self.loop.close()
        return self.lst


if __name__ == '__main__':
    obj = Dbthird()
    print(obj.searching3(q="abounkml@yahoo.co.uk"))
