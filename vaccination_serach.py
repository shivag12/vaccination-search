import requests
import json
import argparse
from win10toast import ToastNotifier
import datetime
import time

parser = argparse.ArgumentParser(description='Vaccination search by district and date')
parser.add_argument('-id',"--district_id", metavar="",type=int,help='District id (refer to attachment)')
#parser.add_argument('-d',"--date",metavar="",help='Format: mm-dd-yyyy, Show available slots for next 7 days')
args = parser.parse_args()

x = datetime.datetime.now()
date = x.strftime("%d-%m-%Y")

#Enable the win10-toaster
toaster = ToastNotifier()

#Encoding the District_id & Date to the URL
SEARCH_BY_DISTRICT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(args.district_id)+"&date="+date

r = requests.get(SEARCH_BY_DISTRICT)

toaster.show_toast("Vaccination Notification for 18+","Searching for slots in the region",icon_path="",duration=4)

#f = open("sample.json")
data = r.json()
#print(data)

center_names_with_pincode = []
available_slots_for_18 = {
    'results' : []
}
notification_string = ""

for i in data["centers"]:
    center_names_with_pincode.append(i["name"] +"_"+str(i["pincode"]))
    #print("Center name : "+i["name"] +"_"+str(i["pincode"]))
    #loop through sessions to find the available slots
    for s in i["sessions"]:
        if(s["min_age_limit"] == 18 and s["available_capacity"] > 0):
            # print("Center name : "+i["name"] +"_"+str(i["pincode"]))
            # print("Available slots " + str(s["available_capacity"]))
            temp_obj = {}
            temp_obj["center_name"] = i["name"] +"_"+str(i["pincode"])
            temp_obj["available_slots"] = str(s["available_capacity"])
            available_slots_for_18["results"].append(temp_obj)
            notification_string+=i["name"] +"_"+str(i["pincode"])+", "
 

#print(available_slots_for_18)
print(notification_string)
#f.close()

if(len(available_slots_for_18["results"]) > 0):
    toaster.show_toast("Vaccination Notification for 18+","Slots available at "+notification_string,duration=10)
    with open("available_slots.json",'w') as outfile:
        json.dump(available_slots_for_18,outfile)


#time.sleep(5)

#print(args.district_id)
#print(args.date)

#SEARCH_BY_DISTRICT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(args.district_id)+"&date="+args.date
#print(SEARCH_BY_DISTRICT)

#r = requests.get(SEARCH_BY_DISTRICT)

#print(r.text)
