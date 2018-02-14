import json
from aip import AipImageClassify

APP_ID = '10833639'
API_KEY = 'U6gxjm6SXgbO9xvvnl0FzXOQ'
SECRET_KEY = '716Sk3F86ThEOG48Bxu5wz8a96iDKO8S'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('./xtl.jpg')
reply = client.logoSearch(image)

print str(reply)
print '+++++ get resultList'
resultList = reply['result']
print type(resultList)
print str(resultList)
print '++++++ get result name'
result = resultList[0]
print result['name']


image = get_file_content('./xigua.jpg')
plant = client.plantDetect(image)
print str(plant)
print '+++++ get resultList'
resultList = plant['result']
print type(resultList)
print str(resultList)
print '++++++ get result name'
result = resultList[0]
print result['name']

