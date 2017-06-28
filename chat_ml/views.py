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
        #print(json.dumps(items))
        #return HttpResponse(ans)
        return HttpResponse(json.dumps(ans), content_type="application/json")

    return render(request,'chat_ml/chatengine.html')