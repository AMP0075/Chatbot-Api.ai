import requests
import json
import logging
def getResult(q,request):
    # return jobfunc(['data science','python','django','java'],3)
    logger=logging.getLogger(__name__)
    url = 'https://api.api.ai/v1/query'
    payload = {'v': '20170101', 'query':q, 'lang': 'en', 'sessionId': request.session.session_key}
    headers = {'Authorization': 'Bearer d3c00533fe4a43b584828eabdc146726'}
    r = requests.get(url, params=payload, headers=headers).text

    logger.info(request.session.session_key)
    j = json.loads(r)

    # if 'intentName' in j['result']['metadata'] and j['result']['metadata']['intentName']=='opportunity':
    #     l=j['result']['parameters']['SkillSet']
    #     exp=j['result']['parameters']['experience']
    #     if j['result']['actionIncomplete']==False:
    #         return jobfunc(l,exp)



    return j['result']['fulfillment']['speech']


