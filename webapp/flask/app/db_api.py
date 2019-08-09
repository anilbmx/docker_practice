from pymongo import MongoClient
import os
class MyMongo:
    def __init__(self):
        # print(os.environ)
        self.myclient = MongoClient(
            "mongodb://mongo:27017/",
            27017)
    def inset_to_collection(self, ijson):
        if (not ijson.get("fname")) or (not ijson.get("lname")):
            return '{"status":"data incomplete"}'

        mycol = self.myclient["customer"]
        mycol.customer_names.insert(ijson)
        # print("inserted")
        return '{"status":"inserted!!"}'

    def get_all_documents(self):
        mycol = self.myclient["customer"]
        x = mycol.customer_names.find()
        lst = []
        for i in x:
            lst.append(i["fname"]+"-"+i["lname"])
        data = {"res":lst}
        return str(data)
