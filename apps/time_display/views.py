from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
# Create your views here.
def index(request):
    time1 = {
        't1': strftime('%Y-%m-%d %H:%S', gmtime()),
        't2':{'time2':strftime('%Y-%m-%d %H:%S', gmtime())}
    }
    return render(request, 'index.html', time1)


