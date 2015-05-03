from lib.shotgun_api3 import Shotgun

SERVER_PATH = 'https://aau.shotgunstudio.com/' # change this to http if you have a local install not using HTTPS
SCRIPT_USER = 'util'
SCRIPT_KEY = 'cf1e303b918f7cab09c73ae4a100d89f596410f25690a41ba21d6211797d1daf'
sg = Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)

fields = ['layout_project']
project_id = 63 # Demo Project
filters = [
    ['project','is',{'type':'Project','id':project_id}]
    ]

lauout = sg.find_one("Project", [["name", "is", "KKovalevskiy_Producing_Final"]], ['layout_project'])

sg.update("Project", 63, {'layout_project':'TEST'})

# Damned 'layout_project' value is only aditable on project creation!