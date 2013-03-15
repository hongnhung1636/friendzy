# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt                                          
from users.models import User
import friendzy
from ast import literal_eval
import datetime


@csrf_exempt
def login(request):
    postrequest = literal_eval(request.body)
    userID = postrequest['userID']
    facebookFriends = postrequest['facebookFriends']
    friendStatuses = User.login(userID, facebookFriends)
    return HttpResponse(simplejson.dumps(friendStatuses), mimetype='application/json')

@csrf_exempt
def set_status(request):
    time = datetime.datetime.now()
    postrequest = literal_eval(request.body)
    userID = postrequest['userID']
    facebookFriends = postrequest['friends']
    matchingStatuses = User.set_status(userID, status, time)
    return HttpResponse(simplejson.dumps(matchingStatuses), mimetype='application/json')
