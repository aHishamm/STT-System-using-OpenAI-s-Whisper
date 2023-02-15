from pymongo import MongoClient
import datetime
username = input("Enter the username: ")
password = input("Enter the password: ")
CONNECTION_STRING = "mongodb+srv://"+username+":"+password+"@"+username+"cluster.uvb74h4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.transcription_records 
transcription = db.transcription 
# A function to create a document 
def create_document(user_input): 
  transcriptionDocument = { 
    "transcription": user_input
  } 
  insert_document(transcriptionDocument)
# A function to add the document to the collection to the database 
def insert_document(transciptionDocument):
  transcription.insert_one(transciptionDocument)

print(client)
#inserting the document in the collection 
#print(transcription.find_one({ "User": "Test User" }))
