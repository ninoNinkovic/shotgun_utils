import requests
from StringIO import StringIO

link = r"https://sg-media-usor-01.s3.amazonaws.com/176041976d8a17ad3cc3a5035cb323a8ca2e42ba/4e9617d37090420f4826204e5872fbb39e7aab39/62208_10151340334398223_980225560_n.jpg?AWSAccessKeyId=AKIAIFHY52V77FIVWKLQ&Expires=1420247882&Signature=2Y38TUHskne8zWmRBRh%2Fm3gDHXU%3D"

r = requests.get(link)

with open("test.jpg", 'wb') as fd:
	fd.write(buffer(r.content))



# with open("request_test.txt", 'wb') as fd:
# 	for chunk in r.iter_content(1024):
# 	        fd.write(chunk)