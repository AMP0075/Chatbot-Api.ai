import requests
import json

def getResult(q,sessionkey):
    # return jobfunc(['data science','python','django','java'],3)

    url = 'https://api.api.ai/v1/query'
    payload = {'v': '20170101', 'query':q, 'lang': 'en', 'sessionId': sessionkey}
    headers = {'Authorization': 'Bearer d3c00533fe4a43b584828eabdc146726'}
    r = requests.get(url, params=payload, headers=headers).text
    j = json.loads(r)

    # if 'intentName' in j['result']['metadata'] and j['result']['metadata']['intentName']=='opportunity':
    #     l=j['result']['parameters']['SkillSet']
    #     exp=j['result']['parameters']['experience']
    #     if j['result']['actionIncomplete']==False:
    #         return jobfunc(l,exp)



    return j['result']['fulfillment']['speech']


