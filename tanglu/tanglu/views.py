from django.http import HttpResponse
from django.template import RequestContext, Context, loader

def index(request):
    sentences = {
        'welcome': 'Welcome to the Tanglu website',
        'line1': 'Tanglu is a new GNU/Linux distribution based on Debian, designed for human beings.',
        'line2': 'Read the <a href="http://blog.tenstral.net/2013/03/tanglu.html">initial announcement</a>.',
        'line3': 'If you want to get in contact, check out <a href="http://webchat.freenode.net/?channels=tanglu-devel">#tanglu-devel</a> on Freenode.',
        'line4': 'You can also subscribe to one of our <a href="http://lists.tanglu.org/mailman/listinfo">mailinglists</a>.',
    }
    template = loader.get_template('home.html')
    context = RequestContext(request, sentences)
    return HttpResponse(template.render(context))
