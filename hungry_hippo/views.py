from datetime import datetime

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def home(req):
    t = get_template('base.html')
    html = t.render(Context())
    return HttpResponse(html)


def hello(request):
    return HttpResponse("hello world")


def current_time(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def list_ingredients(request):
    pass

