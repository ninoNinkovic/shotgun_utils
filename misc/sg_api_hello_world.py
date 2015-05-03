import shotgun_api3
from shotgun_api3 import Shotgun

# SG credentials
base_url = "https://aau.shotgunstudio.com"

# Create SG instance with the given credentials
sg = Shotgun(base_url, login="kkirill2", password="Natoma250")

# # List all projects
# # find(entity_type, filters, fields)
projects = sg.find("Project",[],["name"])

for project in projects:
    print project