from pymongo import MongoClient
import pymongo.errors

from bson import ObjectId
import bson.errors


#MongoDB Connection actions

def mongo_connect() -> MongoClient:
    print("Conectando a MongoDB")
    return MongoClient("mongodb://root:example@mongo:27017/noteDatabase")


def test_mongodb_connection(db) -> str:
    try:
        db.command("serverStatus")
    except pymongo.errors.ConnectionFailure:
        return "ConnectionFailed: timeout"
    else:
        return "ConnectionSuccesful"
    



# MongoDB actions
    
def create_note(db,note):
    return db.notes.insert_one(note)


def find_note(db,id_note):
    
    try:
        return db.notes.find_one({"id_note":ObjectId(id_note)})
    except bson.errors.InvalidId:
        return "Id not found"


def find_all(db):
    db.notes.find()


def update_note(db,id_note,new_note):
    db.notes.update_one({"id_note":ObjectId(id_note)},{"$set":new_note})


def delete_note(db,id_note):
    db.notes.delete_one({"id_note":ObjectId(id_note)})