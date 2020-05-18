from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
from django.core.serializers.json import DjangoJSONEncoder
import json
def fun_session(request):
    #if request.method =="POST":
    name="rm"
    psd = "rm"
    u_c = authenticate(username=name,password = psd)
    if u_c:
        if u_c.is_active:
            print("type is  =",end=" ")
            print(type(u_c))
            print(dir(u_c))
            data_dic={"username ":u_c}
            """u_c1 = u_c.__dict__
            u_c1.pop('_state',None)
            u_c1=json.dumps(u_c1,cls=DjangoJSONEncoder)"""

            request.session['user1']=User.is_authenticated
            print(u_c)
             #  """request.session['user1']="krishna"
               #request.session['passward']="123"""
    #return fun(request)
    return HttpResponse("hii")

def fun(request):

    #print(request.session)
    return render(request,"home.html",{})
