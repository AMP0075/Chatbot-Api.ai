import requests
import json
from chat_ml.models import *
import numpy
from sklearn.externals import joblib
def getResult(q,key):
    masteritem={}
    masteritem['type']='speech'
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


    masteritem['res']=j['result']['fulfillment']['speech']
    return masteritem



def jobfunc(l,exp):
    items=[]
    myskills=""
    cv=joblib.load('chat_ml/Data/skillvector.pkl')
    for i in l:
        myskills=myskills+i.replace(" ","")+" "

    myskillvector=cv.transform([myskills])
    p = set(Jobs.objects.filter(skillset__name__in=l))


    #print(serializers.serialize('json', p))
    for i in p:
        jobskills=""

        for j in i.skillset.all():
            jobskills=jobskills+ j.name.replace(" ","")+" "

        jobskillvector=cv.transform([jobskills])


        commonskill=numpy.logical_and(myskillvector.toarray(),jobskillvector.toarray())
        item={}
        item['jobname']=i.name
        item['jobdesc']=i.desc
        item['skill']=", ".join(cv.inverse_transform(commonskill)[0])
        items.append(item)

    masteritem={}
    masteritem['type']='jobs'
    masteritem['res']=items

    return masteritem

