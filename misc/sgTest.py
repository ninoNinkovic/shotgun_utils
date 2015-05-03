import sys
import os
import pprint

sgtkPath = "//netapp/mnt$/software/shotgun/pipeline_research_project/install/core/python"
# sgApiPath = os.path.join(os.getcwd(), "python-api-master")


sys.path.append(sgtkPath)
# sys.path.append(sgApiPath)

import sgtk
# from shotgun_api3 import Shotgun


# sgWebpage = "http://aau.shotgunstudio.com"
# sgSiteScript = "api_test"
# sgKey = "cf1e303b918f7cab09c73ae4a100d89f596410f25690a41ba21d6211797d1daf"

# Create SG object
#sg = Shotgun(sgWebpage, login = "kkirill2", password = "Natoma250")

# Create SG object
#sg = Shotgun(sgWebpage, sgSiteScript, sgKey)

# Set the project
#proj = sg.find_one("Project", [["name", "is", "Pipeline Research Project"]])

# Creat a shot
#shot = sg.create("Shot", {"code":"SH001test_02","project":proj})

file_to_publish = r'\\netapp\mnt$\projects\pipeline_research_project\sequence\SQ_A034\ADN_A034B\element\dpx\final.%04d.png'
# file_to_publish = "//netapp/mnt$/projects/pipeline_research_project/sequence/SQ_A034/ADN_A034B/comp/work/nuke/scene/test_v001.nk"

tk = sgtk.sgtk_from_path(file_to_publish)

ctx = tk.context_from_path(file_to_publish)


pprint.pprint (sgtk.util.register_publish(tk, ctx, file_to_publish, "final", 3, published_file_type = "Rendered Image" ))
#sgtk.util.register_publish(tk, ctx, file_to_publish, "test_nuke.nk", 5 )