import requests
import json
import logging
from chat_ml.models import *
import numpy
from sklearn.externals import joblib
def getResult(q,key):
    # return jobfunc(['data science','python','django','java'],3)
    logger=logging.getLogger(__name__)
    url = 'https://api.api.ai/v1/query'
    payload = {'v': '20170101', 'query':q, 'lang': 'en', 'sessionId': key}
    headers = {'Authorization': 'Bearer d3c00533fe4a43b584828eabdc146726'}
    r = requests.get(url, params=payload, headers=headers).text

    print(key)
    j = json.loads(r)

    if 'intentName' in j['result']['metadata'] and j['result']['metadata']['intentName']=='opportunity' and j['result']['actionIncomplete']==False:
        l=j['result']['parameters']['SkillSet']
        exp=j['result']['parameters']['experience']
        return jobfunc(l,exp)



    return j['result']['fulfillment']['speech']



def jobfunc(l,exp):
    res=""
    myskills=""
    cv=joblib.load('chat_ml/Data/skillvector.pkl')
    for i in l:
        myskills=myskills+i.replace(" ","")+" "

    myskillvector=cv.transform([myskills])

    p = set(Jobs.objects.filter(skillset__name__in=l))

    for i in p:
        jobskills=""
        res=res+i.name+"\n"

        for j in i.skillset.all():
            jobskills=jobskills+ j.name.replace(" ","")+" "

        jobskillvector=cv.transform([jobskills])


        commonskill=numpy.logical_and(myskillvector.toarray(),jobskillvector.toarray())
        res=res+ " for the skill/s-"+" ".join(cv.inverse_transform(commonskill)[0])+" "
        #print(type(i.skillset.))

    return res

