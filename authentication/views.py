from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.hashers import make_password,check_password
from chatRobo.settings import Session
from .models import User,Token
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from passlib.hash import pbkdf2_sha256


def login(req):
    return render_to_response('login.html')


def authenicate(username, password):
    session = Session()
    encoded = session.query(User).filter(User.user_name==username).one()
    print(encoded.check_password(password))

    return True


def createToken(username):
    pass


@csrf_exempt
def authentication(req):
    username = req.POST['username']
    password = req.POST['password']
    status = authenicate(username, password)
    respone = {
        'message': '',
        'status':''
    }
    if status:
        token = createToken(username)
        data = {'token':token}
        respone['data']=data
        respone['message']='successfully logged in'
        respone['status']=200
        return HttpResponse(respone)
    else:
        respone['message'] = 'invalid credentials'
        respone['status'] = 200
        return HttpResponse(respone)

@csrf_exempt
def createUser(req):
    session = Session()
    print(req.POST)
    user_name = req.POST.get('name')
    print(user_name)

    # username = req.POST.get('username',False)
    # password = req.POST.get('password','password')
    # encrypted_password = pbkdf2_sha256.hash(password,rounds=1200,salt_size=32)
    # user = User(name=user_name, user_name=username, password=password)
    # session.add(user)
    # session.commit()
    return HttpResponse('successfully created user')