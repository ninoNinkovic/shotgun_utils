from aau_site import sg
import os

project_id = 147
shot_code = 'SQ05_SH16'

shot = sg.find('Shot', [
			['project','is',{'type':'Project','id': project_id}],
			['code', 'is', shot_code]],
			['code', 'assets', 'sg_no__of_frames'])[0]

characters = [asset['name'] for asset in shot['assets']]
frame_number = shot['sg_no__of_frames']

print characters
print frame_number

def open_shot(shot):

	curpigeon_url = 'https://aau.shotgunstudio.com/page/6503'

	shot_url = '%s#Shot_%s_%s' %(curpigeon_url, 
								shot['id'],
								shot['code'])

	cmd = 'start chrome %s' %shot_url

	os.system(cmd)