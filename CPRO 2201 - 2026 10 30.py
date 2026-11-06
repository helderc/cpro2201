
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
#print(os.environ["URI"])

client = MongoClient(os.environ["URI"])

try:
    client.admin.command("ping")
    print("Connected!!!! \o/")
    client.close()
except Exception as e:
    print(f"ERROR: {e}")
    
    
    
    
    
    
    


