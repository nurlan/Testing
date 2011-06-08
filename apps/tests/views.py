from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from apps.tests.models import Test

def index(request):
#    tests = []
    tests = Test.objects.all()#SELECT * FROM TEST;
    
    rc = RequestContext(request,{'tests':tests,'title':'List of Tests'})
    return render_to_response('tests/list.html',rc)
