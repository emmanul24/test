from pymongo import MongoClient, errors
import asyncio
import time

start_time = time.time()

class Dbsecond:
    def __init__(self):
        self.client = MongoClient(host='192.168.20.120', port=27018)

        db6 = self.client.hacking_related_collection
        self.collection6 = db6.data
        db7 = self.client.linkedin_leaked_data
        self.collection7 = db7.data
        db8 = self.client.mail_access_collection
        self.collection8 = db8.data
        db9 = self.client.mail_ru_database
        self.collection9 = db9.data
        db10 = self.client.money_related_collection
        self.collection10 = db10.data

        self.lst = list()
        self.loop = asyncio.new_event_loop()

    async def database10(self, q):
        try:
            if self.collection10.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection10.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db10')
        except errors.ExecutionTimeout:
            pass

    async def database9(self, q):
        try:
            if self.collection9.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection9.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db9')
        except errors.ExecutionTimeout:
            pass

    async def database8(self, q):
        try:
            if self.collection8.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection8.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db8')
        except errors.ExecutionTimeout:
            pass

    async def database7(self, q):
        try:
            if self.collection7.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection7.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db7')
        except errors.ExecutionTimeout:
            pass

    async def database6(self, q):
        try:
            if self.collection6.find_one({'email': q}, {"_id": 0}, max_time_ms=5000):
                doc = self.collection6.find_one({'email': q}, {"_id": 0}, max_time_ms=5000)
                self.lst.append(doc)
                print(time.time()-start_time)

            else:
                print('not fount in db6')
        except errors.ExecutionTimeout:
            pass

    def searching2(self, q):
        task = [

            self.database6(q),
            self.database7(q),
            self.database8(q),
            self.database9(q),
            self.database10(q),

        ]

        self.loop.run_until_complete(asyncio.wait(task))
        self.loop.close()
        return self.lst


if __name__ == '__main__':
    obj = Dbsecond()
    print(obj.searching2(q="abounkml@yahoo.co.uk"))
