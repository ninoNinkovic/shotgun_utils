import sys
import os
import shutil
from pprint import pprint

# Path to SG Toolkit API
# API need to be related to the project in which publish are going to be
sgToolkitApiPath = "//netapp/mnt$/software/shotgun/sX_BoatBuilder/install/core/python"
# Append SG Toolkit API to system PATH env variable
sys.path.append(sgToolkitApiPath)
import sgtk

# List non dot files in directory
# Return a generator which can be expanded like that  list(listdir_nohidden(path))
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# Initial data that hardcoded for now
sequence = "001"
shot_code = "BB_001_010"
sequence_source_path = "H:/Event_Version 1_0001_0001"
sequence_target_path = "//netapp/collab/sX_BoatBuilder/sequence/%s/%s/element/%s" % (sequence, 
																					shot_code, 
																					shot_code)
exstension = "dpx"
padding = r"%04d"
# Publish data
published_file_type = "DPX Sequence"
version = 2
comment = "Test of stand alone publisher"

files = list(listdir_nohidden(sequence_source_path))

# If target directory not exists create one
if not os.path.exists(sequence_target_path):
	os.mkdir(sequence_target_path)

# Copy files to project
frame_num = 1
for f in files:
	old_path = "%s/%s" % (sequence_source_path, f)
	new_path = "%s/%s_%04d.%s" % (sequence_target_path,
								shot_code, 
								frame_num, 
								exstension)
	shutil.copy(old_path, new_path)
	print "%s created" % new_path
	frame_num += 1
print "Copy is finished"


file_to_publish = "%s/%s_%s.%s" % (sequence_target_path,
								shot_code, 
								padding, 
								exstension)
file_to_publish = file_to_publish.replace("/", "\\")

# Create Shotgun Toolkit object from path
tk = sgtk.sgtk_from_path(file_to_publish)

# Create context from path
ctx = tk.context_from_path(file_to_publish)

# Find current user
# "USER" environmental variable should mach user name on Shutgun web-site
current_user = sgtk.util.get_current_user(tk)

# Path to the firs frame of the sequence
thumbnail_path = file_to_publish.replace(padding, "0001")

# Publish entry on Shotgun
register_publish = sgtk.util.register_publish(tk, ctx, file_to_publish, shot_code, version,
							thumbnail_path = thumbnail_path,
							published_file_type = published_file_type, 
							current_user = current_user["id"],
							comment = comment)

print "Published successfuly!"