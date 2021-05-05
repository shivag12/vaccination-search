# Vaccine Appointment Tracker & Notification

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![visual studio code ](https://badges.aleen42.com/src/visual_studio_code.svg)]() [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)]()



# Setup

### Requirements
* Windows 10
* Python 3.x or greater (Dowload link (https://www.python.org/downloads/), in case not available)
* Python should added in the system PATH environmental variable.(Google it on how to setup this)
* Verify the python version by `python --version`

### Installing the libraries
* Clone the repository and navigate to the folder in the command prompt. 
* Run `pip install -r requirement.txt`

### Configure 
#### Finding the states & districts unique identifers
* Run `python search_for_states_districts.py -sl true`. This returns list of available states in india and its unique id. 
* After noting down on the **state-id**, search for associated districts by `python search_for_states_districts.py -sid <STATE_ID>`. Returns the registered districts & its id which are available for vaccination. 
* Note down the district-id, to which notifications needs to be configured.
* For list of available arguments, run `python search_for_states_districts.py --help`

#### Scheduling the vaccination slots notification. 
* Open the windows 10 task scheduler and create a task. 
* Give some name (vaccination_search_for_18+) and cick on trigger. 
* Click new under trigger tab, schedule the task as per your requirements.(Refer to image below).
* Click on action, navigate to **dist** folder of the repository and select the `vaccination_search.exe` executable. 
* In the add-arguments, enter `-d <DISTRICT_ID>`, example `-d 294`, gives the list of all available vaccination centers under BBMP, bangalore Karnataka. 
* Save the task. For testing the scheduler, select **Task scheduler library** on left hand side menu --> Find the task created --> right click --> select run. This should throw some notifications like searching..etc (Refer to sample notification section) 

![alt text](https://raw.githubusercontent.com/shivag12/vaccination-search/main/images/task_scheduler.png "Task Scheduler")

## Sample Notifications ##

![alt text](https://raw.githubusercontent.com/shivag12/vaccination-search/main/images/notifications.png "Task Scheduler")

## Disclaimer ##
 I take no warranty or responsibility of the code, as mentioned in license. Issues and emails are welcomed, and I will do by best to reply. However I generally do NOT have time to fix it oftenly, due to work. The code was written within 5 hours and I knew there are bugs/issues are in the code, will try as much as possible to fix it. if you found any issues or any idea to enhance this plugin, do create an github issue and PR's are accepted.

## Changelog ##

### 0.0.1

The first release of this plugin, containing:

* Windows 10 notifications for vaccination slots (only for INDIA) of age 18+
* Scheduling the search using windows task scheduler.
* Searching the states & districts unique id. 

