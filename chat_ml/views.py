from django.shortcuts import render
from django.shortcuts import render,HttpResponse,render_to_response
from django.shortcuts import render, redirect
from sklearn.feature_extraction.text import CountVectorizer

from .Model.googleapimod import *
from random import choice
from string import ascii_uppercase
import json
# Create your views here.

def googleapi(request):

    if 'key' not in request.session:
        request.session['key']=''.join(choice(ascii_uppercase) for i in range(10))
    if request.is_ajax():
        q=request.POST['query']
        ans=getResult(q,request.session['key'])
        if ans['type']=='speech' and 'skills' in ans['res']:
            s = Skill.objects.all()
            ans['res']+=" You can choose from- "+ ', '.join([i.name.replace('_',' ').title() for i in s])

        return HttpResponse(json.dumps(ans), content_type="application/json")

    return render(request,'chat_ml/chatengine.html')