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


###### Sample notifications.


