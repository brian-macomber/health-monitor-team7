from pymongo import MongoClient, DeleteMany
from datetime import date, datetime
import blood_oxygen
import pulse
import random
import time
import blood_pressure
from threading import Timer
from bson import ObjectId
import json

client = MongoClient("mongodb+srv://ec500:ruby@cluster0-092qv.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("ec500-HW5")
records = db.heartRateMonitor


# function to create data entry

def create():
    new_patient = {
        'createAt': str(datetime.now()),
        'pulse':pulse.read_pulse(),
        'bloodOx':blood_oxygen.read_blood_oxygen(),
        'bloodPreSys': blood_pressure.get_bp_sys(),
        'bloodPreDia': blood_pressure.get_bp_dia()
    }
    return new_patient

#functoin to get latest data entry
def find():
    x = []
    cur = db.heartRateMonitor.find().sort('createdAt')
    #latest = db.heartRateMonitor.find_one()#.sort('createdAt')
    for i in cur:
        x.append(i)
    size = len(x)
    latest = x[size-1]
    return latest

def find_all():
    x = []
    cur = records.find()
    for i in cur:
        x.append(i)
    #size = len(x)
    #all = x[size-1]

    return x

def delete_all():
    print('test delete')
    x = db.heartRateMonitor.delete_many({})
    print(x.deleted_count, " documents deleted.")
#function to create a bunch of data in 30 seconds
# this ^ generates too much data but we can still use it?
"""
def timedEntry():
   start = time.process_time()
   my_data = []
   while time.process_time() - start < 1:
       entry = create()
       my_data.append(entry)

   return my_data
"""

#function that uploads that data every 30 seconds.
# run this function and a single dat entry will be uploaded every 30 seconds.
def timedDataInsert():
    new_patient = create()
    records.insert_one(new_patient)
    Timer(30,timedDataInsert).start()
