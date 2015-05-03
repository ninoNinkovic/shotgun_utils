from lib.shotgun_api3 import Shotgun
from pprint import pprint
import csv
import sys
from lib import yaml

class Site(object):
	def __init__(self, base_url, login, password):
		# Create SG instance with the given credentials
		self.sg = Shotgun(base_url, login=login, password=password)

	def upload_thumbnails(self, id, thum_path):
		self.sg.upload_thumbnail("Shot", id, thum_path)

	def set_project(self, project):
		self.project = project
		self.project_id = self.project_info(self.project)["id"]

	def get_fields (self, entity):
	    '''
	    get the fields for a type/entity as a list
	    so we can pass it as an arg easily
	    this is used all the time to make sure we get
	    all the fields that we may ever need for a type/entity
	    '''
	    all_fields = []
	    fields = self.sg.schema_field_read(entity)
	    for field in fields:
	        all_fields.append(field)
	    return all_fields  

	# Gets the Shotgun project name and ID
	def project_info (self, project):
		retFields = self.get_fields('Project')
		project = project.replace('_', ' ')
		return self.sg.find_one("Project", [["name", "is", project]], retFields )

	# List all projects
	def list_projects():
		# find(entity_type, filters, fields)
		projects = sg.find("Project",[],["name"])
		return projects

	# List all shots in the project
	def list_shots(self):
		filters = [['project','is',{'type':'Project','id':self.project_id}]]
		shots = self.sg.find("Shot", filters, ["code"])
		return shots

	def list_assets(self):
		filters = [['project','is',{'type':'Project','id':self.project_id}]]
		fields = ['code', 'est_in_min']
		asset = self.sg.find("Asset", filters, fields)
		return asset

	def list_tasks(self, asset):
		filters = [['project','is',{'type':'Project','id':self.project_id}],
				   ['entity','is',{'type':asset['type'],'id':asset['id']}]]
		fields = ['content', 'est_in_mins']
		tasks = self.sg.find("Task", filters, fields)
		return tasks


	# Return local storage paths specified in site global preferences
	def list_local_storages(self):
		paths_list = ["windows_path", "mac_path", "linux_path"]
		paths = sg.find("LocalStorage", [], paths_list)
		return paths

	def layout_project(self):
		filters = [['project','is',{'type':'Project','id':self.project_info(project)["id"]}]]
		result = sg.find("PipelineConfiguration", filters, ['layout_project'])[0]
		return result

	# Return pipeline configuration paths for a given project
	def list_pipeline_config(self):
		paths_list = ["windows_path", "mac_path", "linux_path"]
		filters = [['project','is',{'type':'Project','id':self.project_info(project)["id"]}]]
		paths = sg.find("PipelineConfiguration", filters, paths_list)[0]
		return paths

	def list_thumbnails(self):
		filters = [['project','is',{'type':'Project','id':self.project_id}]]
		result = self.sg.find("Shot", filters, ["code", "image"])
		return result


	def list_users(self):
		# find(entity_type, filters, fields)
		user = sg.find("HumanUser",[],["name", 
										"email",
										"sg_phone",
										"image",
										"firstname",
										"lastname",
										"sg_portfolio__url_"])
		return user

	def sum_days_for_tasks(self, entity):
		# This function return a dictionary of all task for the give entry
		# with sum of the days required for every type of the task
		# entity - entity dictionary of Shots or or Assets
		total_man_days = {}
		for i in entity:
			# print i
			for task in sg.list_tasks(i):

				# If Bit is not define, set it to 0 days
				if task['est_in_mins'] == None:
					task['est_in_mins'] = 0

				# If task is not in the dictionary create one, otherwise sum the value
				if task['content'] in total_man_days:
					total_man_days[task['content']] += task['est_in_mins']/600
				else:
					total_man_days[task['content']] = task['est_in_mins']/600

		return total_man_days

	def total_man_weeks(self, days):
		# days - {task : days} dictionary
		total_man_weeks = {}
		for i in days.keys():
			total_man_weeks[i] = round(days[i] / 7.0, 1)
		return total_man_weeks

	def total_production_weeks(self, time):
		# time - {task : time} dictionary
		people_per_task = {'Shader Pack': 1, 
						  'Concept Art': 3, 
						  'Surface': 3, 
						  'Rig': 2, 
						  'Modeling': 3, 
						  'Model': 2, 
						  'Texture & Shader': 2}

		total_production_weeks = {}
		for i in time.keys():
			total_production_weeks[i] = round(time[i] / people_per_task[i])
		return total_production_weeks

	def save_to_csv(self, file_name, data):
		with open(file_name,'wb') as f:
			y = yaml.dump(data)
			f.write(y)

			# w = csv.writer(sys.stderr)
			# w.writerows(data.items())
			# for key, values in data.items():
				# print key
				# for value in values:
			# 		for i, j in value.items():
			# 			w.writerow(j)
						# print i
						# print j
			# with open(file_name,'wb') as f:
			#     # w = csv.writer(f)
			#     w = csv.writer(sys.stderr)
			#     w.writerows(i.items())

	def delete_key(self, dict, key):
		del dict[key]
		return dict

	def merge_entity_with_tasks(self, entity):
		merged = {}
		for i in entity:
			print  'ASSET: ', i
			tasks = {}
			tasks_prop = {}
			for task in sg.list_tasks(i):
				tasks[task['content']] = self.delete_key[task, 'content']
				# merged[i['code']] = 
				print merged
				# tasks.append(task)
				print 'TASK: ', task
			# merged[i['code']] = tasks
		return merged

##################
# Example of usage

sg = Site('https://aau.shotgunstudio.com', 'kkirill2', 'Natoma250')
print sg.set_project('KKovalevskiy_Producing_Final')

print sg.layout_project()

# thumbnails = sg.list_thumbnails()
# shots = sg.list_shots()

# merged = sg.merge_entity_with_tasks(assets)

# pprint(thumbnails)

# sg.save_to_csv('Assets.txt', merged)

# print assets

# asset_days = sg.sum_days_for_tasks(assets)
# total_man_weeks = sg.total_man_weeks(asset_days)
# total_prod_weeks = sg.total_production_weeks(total_man_weeks)

# sg.save_to_csv(total_prod_weeks)

# test_dict = {1: {'value': 'hello', 'value2': 'my friend'}, 2:{'value3': 'blaa', 'value4' : 'spamm'}}

# Print all registered user info or specific
# for user in list_users():
# 	print user["firstname"]

# Print windows pipeline config location for the project
# print list_pipeline_config("Boat_Builder")["windows_path"]

## Print all entity that exist on Shotgun
## Useful for findind a value to use fith find()
# result = sg.schema_read()
# pprint(result)

## List all of the projects
# for project in list_projects():
#  	print project

# List all shot for a given project
# pprint(list_assets("Zephyr Rose KK NA"))

# pprint(get_fields("Shot"))