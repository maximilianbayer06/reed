from pymongo import MongoClient
import webScraper

connect = "mongodb://localhost:27017"
client = MongoClient(connect)

db = client.reed
Articles = db.Articles

news = webScraper.News()

def setup():
    Articles.insert_one({'_id':'0'}, {"$set": {"test": "test"}})
    
result = Articles.update_one({'_id':'0'}, {"$set": news})

mongoStart = "sudo systemctl start mongod"
mongoStatus = "sudo systemctl status mongod"
mongoStop = "sudo systemctl stop mongod"