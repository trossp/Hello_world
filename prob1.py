import json


xs = ['dddd','a','bb','ccc']
xs.sort(key=len)


lst = [9,8,7,6,4,3,2,1]

lst.sort()

with open('111.txt','w') as fw:
    json.dump(xs, fw)

    json.dump(lst, fw)


