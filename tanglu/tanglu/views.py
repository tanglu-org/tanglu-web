from django.http import HttpResponse
from django.template import RequestContext, Context, loader

# Home page View
def index(request):
    template = loader.get_template('home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

# Download View
def download(request):
    template = loader.get_template('download.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

# Contribute View
def contribute(request):
    template = loader.get_template('contribute.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
