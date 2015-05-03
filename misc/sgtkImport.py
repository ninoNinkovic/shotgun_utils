import os
from pprint import pprint

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

pprint(dir(sg))
