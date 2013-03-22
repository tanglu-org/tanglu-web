from django.http import HttpResponse
from django.template import RequestContext, Context, loader

def index(request):
    message = "Welcome to Tanglu"
    template = loader.get_template('base.html')
    context = RequestContext(request, {'message': message})
    return HttpResponse(template.render(context))
