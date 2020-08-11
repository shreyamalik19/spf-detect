# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from uv_detect import detect_zip
from django.template import Context, loader, RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.loader import render_to_string


# Create your views here.
def index(request):

    homeTemplate = loader.get_template('spfhome.html')

    if (request.method=="POST"):
        return detect(request);

    return render(request, 'spfhome.html')

def detect(request):

    csrfContext = RequestContext(request)

    print("post request: ", request.POST.get('loc').encode('ascii', 'ignore'))

    detection = detect_zip(request.POST.get('loc').encode('ascii', 'ignore'))

    print("detection value: ", detection)

    resultTemplate = loader.get_template('spfresult.html')

    context = {
        'message' : detection[0],
        'city' : detection[1]
    }

    return HttpResponse(resultTemplate.render(context, request))
