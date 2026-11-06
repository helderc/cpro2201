
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.environ["URI"])

try:
    # database connection
    db = client["course_demo"]
    
    # collection
    students = db["students"]
    
    students.update_one(
        {"_id": 1}, 
        {"$set": {"gpa": 4.0}}    
    )
    
    
    client.close()
except Exception as e:
    print(f"ERROR: {e}")

print("Finished!")
    
    
    
    
    
    


