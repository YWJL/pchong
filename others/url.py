import re
import requests
import numpy as np
import json
url = 'https://coronavirus.1point3acres.com/_next/static/chunks/874d9aceb19535760ef89ab5c0349f213ee6300b.cde18accd19cf6adf524.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('state_name":(.*?),"county":(.*?),"entries":(.*?)}',re.S)
end = list(re.findall(pattern,res.text))
state_name='state_name'
county='county'
entries='entries'
with open('data.json',"w") as f:
    for i in range(len(end)):  
        data={
            "state_name:":[],
            "county:":[],
            "entries:":[]
        } 
        data['state_name:'].append(end[i][0])
        data["county:"].append(end[i][1])
        data["entries:"].append(end[i][2])
        a = json.dumps(data)
        f.write(a)
        f.write(',')
##数组转字符串
