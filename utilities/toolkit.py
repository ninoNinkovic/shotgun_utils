from lib.shotgun_api3 import Shotgun
import os

base_url = 'https://aau.shotgunstudio.com'
script_name = 'Util'
app_key = 'cf1e303b918f7cab09c73ae4a100d89f596410f25690a41ba21d6211797d1daf'

sg = Shotgun(base_url, script_name, app_key)


def update_pipline_config(id, **kwargs):
	# example: 
	# update_pipline_config(42, windows_path='\\\\netapp\\mnt$\\software\\shotgun\\sX_Kicks')

	filters = [['project','is',{'type':'Project','id': 305}]]
	paths_list = ["windows_path"]
	paths = sg.update("PipelineConfiguration", id, kwargs)

def download_attachment():
	count = 1
	for id in range(47958, 48060):
		try:
			version = sg.find_one('Version', [['id', 'is', id]], ['sg_uploaded_movie'])
			print version
			file_name = version['sg_uploaded_movie']['name']
			if not os.path.isfile(file_name):
				attachment = sg.download_attachment(attachment=version['sg_uploaded_movie'], file_path=file_name)
			else:
				print file_name, 'exist'
			count += 1
		except TypeError:
			pass

download_attachment()