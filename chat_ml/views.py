from django.shortcuts import render
from django.shortcuts import render,HttpResponse,render_to_response
from django.shortcuts import render, redirect
from .Model.googleapimod import *


# Create your views here.

def googleapi(request):
    if request.is_ajax():
        q=request.POST['query']
        ans=getResult(q,request)
        return HttpResponse(ans)

    return render(request,'chat_ml/chatengine.html',{'name':'manobhav'})