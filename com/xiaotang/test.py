import authcode_reader
import json
import time

print(authcode_reader.image_to_string('authcode.jpg'))

teststring = r'({"notnr":false,"success":"https://www.jd.com"})'
print(teststring)
print(type(teststring))
print(teststring[1:len(teststring)-1])
mydict = json.loads(teststring[1:len(teststring)-1])
#mydict = json.loads(teststring)
print(mydict.get('success'))

url = "https://item.jd.com/{}.html".format("1682719")
print(url)
print(int(time.time()))

print('42935.html'[0:-5])

for i in range(15):
    print(i)