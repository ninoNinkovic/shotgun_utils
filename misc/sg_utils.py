import shotgun_api3
from shotgun_api3 import Shotgun
from pprint import pprint

# Create SG instance with the given credentials
base_url = "https://aau.shotgunstudio.com"
sg = Shotgun(base_url, 'api_test', 'cf1e303b918f7cab09c73ae4a100d89f596410f25690a41ba21d6211797d1daf')

def getFields (entity):
    '''
    get the fields for a type/entity as a list
    so we can pass it as an arg easily
    this is used all the time to make sure we get
    all the fields that we may ever need for a type/entity
    '''
    allFields = []
    fields = sg.schema_field_read(entity)
    for field in fields:
        allFields.append(field)
    return allFields  

# Gets the Shotgun project name and ID
def project_info (project):
	retFields = getFields('Project')
	project = project.replace('_', ' ')
	return sg.find_one("Project", [["name", "is", project]], retFields )

# List all projects
def list_projects():
	# find(entity_type, filters, fields)
	projects = sg.find("Project",[],["name"])
	return projects

# List all shots in the project
def list_shots(project):
	filters = [['project','is',{'type':'Project','id':project(project)["id"]}]]
	shots = sg.find("Shot", filters, ["code"])
	return shots

# Return local storage paths specified in site global preferences
def list_local_sorages():
	paths_list = ["windows_path", "mac_path", "linux_path"]
	paths = sg.find("LocalStorage", [], paths_list)
	return paths

# Return pipeline configuration paths for a given project
def list_pipeline_config(project):
	paths_list = ["windows_path", "mac_path", "linux_path"]
	filters = [['project','is',{'type':'Project','id':project_info(project)["id"]}]]
	paths = sg.find("PipelineConfiguration", filters, paths_list)[0]
	return paths

def create_config(project, config_name, windows_path, mac_path, linux_path):

	data = {'project' : {'type':'Project','id':project_info(project)["id"]},
			'code' : config_name,
    		'windows_path': windows_path,
    		'mac_path' : mac_path,
    		'linux_path' : linux_path}

	create = sg.create("PipelineConfiguration", data)
	return create

def list_users():
	# find(entity_type, filters, fields)
	user = sg.find("HumanUser",[],["name", 
									"email",
									"sg_phone",
									"image",
									"firstname",
									"lastname",
									"sg_portfolio__url_"])
	return user

##################
# Example of usage

create_config('Pipeline Research Project', 'External', 'Z:\software\shotgun\pipeline_research_project', '/Volumes/mnt', '/Volumes/mnt')

# Print all registered user info or specific
# for user in list_users():
# 	print user["firstname"]

# Print windows pipeline config location for the project
# print list_pipeline_config("Boat_Builder")["windows_path"]

## Print all entity that exist on Shotgun
## Useful for findind a value to use fith find()
# result = sg.schema_read()
# pprint(result)

## List all shot for a given project
# pprint(list_shots("Boat_Builder"))

# pprint(getFields("Shot"))