from django.shortcuts import render
from django.shortcuts import render,HttpResponse,render_to_response
from django.shortcuts import render, redirect
from .Model.googleapimod import *
from random import choice
from string import ascii_uppercase

# Create your views here.

def googleapi(request):
    if 'key' not in request.session:
        request.session['key']=''.join(choice(ascii_uppercase) for i in range(10))
    if request.is_ajax():
        q=request.POST['query']
        ans=getResult(q,request.session['key'])
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})