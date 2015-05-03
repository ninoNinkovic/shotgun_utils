import shotgun
import urllib
import os

sg1 = shotgun.Site('https://aau.shotgunstudio.com', 'kkirill2', 'Natoma250')
project1 = sg1.set_project('The Architect')
sg2 = shotgun.Site('https://aau.shotgunstudio.com', 'kkirill2', 'Natoma250')
project2 = sg2.set_project('Final KK')

thumbnails1 = sg1.list_thumbnails()
thumbnails2 = sg2.list_thumbnails()

# Create list of all shots of project2
finaKKShots = []
for shot in thumbnails2:
	finaKKShots.append(shot['code'])

# # If project1 has the same shot download the thumbnails from it
# for shot in thumbnails1:
# 	if shot['code'] in finaKKShots:
# 		filename = shot['code'] + '.jpg'
# 		urllib.urlretrieve(shot['image'], os.path.join(filename))
# 		print 'Downloaded ', shot['code']

thumbPath = 'G:/Code/Python/shotgun/sg_utilities/thumb'

thumbFile = os.listdir(thumbPath)

# For every thumbnail dile
for t in thumbFile:
	shotName =os.path.splitext(t)[0]

	# Iterate trough every shot on the project2
	# and find the matching shot for thumbnail file
	for shot in thumbnails2:
		if shot['code'] == shotName:
			thumbnail = os.path.join(thumbPath, t)
			# Upload the thumbnail
			sg2.upload_thumbnails(shot['id'], thumbnail)
			print shot['id'], shotName, 'Uploaded'


