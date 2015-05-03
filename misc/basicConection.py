import os

# Path to SG API library
sgApiPath = os.path.join(os.getcwd(), "python-api-master")
import sys

# Append sgApiPath to system PATH env variable
sys.path.append(sgApiPath)

from shotgun_api3 import Shotgun

sgWebpage = "http://aau.shotgunstudio.com"
sgSiteScript = "api_test"
sgKey = "cf1e303b918f7cab09c73ae4a100d89f596410f25690a41ba21d6211797d1daf"

# Create SG object
sg = Shotgun(sgWebpage, sgSiteScript, sgKey)

# Find project
proj = sg.find_one("Project", [["name", "is", "Pipeline Research Project"]])

print proj

### Creat a shot
##shot = sg.create("Shot", {"code":"SH001test","project":proj})
##
##print shot
##
### Update the shot status
##sg.update("Shot",shot["id"], {"sg_status_list":"ip"})

# Delete the shot
if True:
    if sg.delete("Shot", shot["id"]):
        print "Shot %s with id: %s has been deleted" %(shot["code"], shot["id"])
