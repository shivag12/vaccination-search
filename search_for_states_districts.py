import requests
import argparse
from prettytable import PrettyTable
x = PrettyTable()

parser = argparse.ArgumentParser(description='Search for District id by state')
parser.add_argument('-id',"--state_id", metavar="",type=int,help='state id (refer to state id in the config)',required=False)
parser.add_argument('-n','--district_name',metavar="",help="District name",required=False)
parser.add_argument('-s','--state_list',metavar="",help="District name",required=False)
args = parser.parse_args()

SEARCH_BY_STATE_ID = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(args.state_id)
SEARCH_STATES = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

district_name = args.district_name

if(args.district_name):
    r = requests.get(SEARCH_BY_STATE_ID)
    data = r.json()
    for i in data["districts"]:
        if(i["district_name"] == district_name):
            print("District id : "+str(i["district_id"]))
elif(args.state_list):
    r = requests.get(SEARCH_STATES)
    data = r.json()
    x.field_names = ["State name", "State id"]
    for i in data["states"]:
        x.add_row([i["state_name"],i["state_id"]])
    print(x)
else:
    r = requests.get(SEARCH_BY_STATE_ID)
    data = r.json()
    x.field_names = ["District name", "District id"]
    for i in data["districts"]:
        x.add_row([i["district_name"],i["district_id"]])
    print(x)



