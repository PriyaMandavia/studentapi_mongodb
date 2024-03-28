from database import stud_collection
from schemas import Students
import pymongo



def create_data(stud : Students):
    stud_dict = stud.model_dump()
    stud_collection.insert_one(stud_dict)
    return {"msg" : "successfully add the data"}


def find_data(limit : int):
    show = stud_collection.find({} , {'_id': 0}).limit(limit).sort('last_name',pymongo.DESCENDING)
    total = stud_collection.count_documents({})
    d = [i for i in show ]
    return {"data" : d , "total" : total}

  

def find_name():
    name = stud_collection.distinct('first_name')
    return {"name_of_student" : name}


    
def find_field(name : str):
    pattern = f'^{name}.*'
    document = stud_collection.find_one({"first_name": {"$regex": pattern}})
    nm = document.get("first_name") 
    field = document.get("field")
    email = document.get("email")
    if document:
        return { "first_name" : nm ,"field": field ,"email" : email}
    else:
        return {"message": "No matching record found"}

        
    

    
def update_data(name : str,stud : Students):
        filter_data = {"first_name" : name}
        update_dta = stud.model_dump()
        stud_collection.update_one(filter_data , {"$set" : update_dta})
        return {"msg" : "successfully update the data"}


def delete_data(name : str):
     delete_name = {"first_name" : name}
     stud_collection.delete_one(delete_name)
     return {"msg" : "successfully delete the data"}