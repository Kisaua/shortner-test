from .models import Shortner
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import ShortnerForm
import hashlib
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    context = {}
    template = 'sh/index.html'
    if request.method == 'POST':
        form = ShortnerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url_orig = request.POST['urlOriginal'].strip()
            short_url = short_str(url_orig)
            short_link = request.build_absolute_uri('/')+short_str(url_orig)
            print(short_url)
            if Shortner.objects.filter(urlHash=short_url).exists():
                short = Shortner.objects.get(urlHash=short_url)
                if short.urlOriginal == url_orig:
                    short.createdDate = datetime.now()
                    short.expirationDate = datetime.now() + timedelta(hours=1)
                    short.save()
                    context['message'] = 'Your short link was updated:'
                    context['shortlink'] = request.build_absolute_uri('/')+short_url
                else:
                    short_url = short_str(url_orig+'some_salt')
                    short_link = request.build_absolute_uri('/')+short_str(url_orig)
                    context.update(create_shortner(short_link, url_orig))
            else:
                context.update(create_shortner(short_link, url_orig))
    else:
        form = ShortnerForm()
    context['form'] = form
    return render(request, template, context)


def redirect_url_view(request, urlHash):
    if Shortner.objects.filter(urlHash=urlHash).exists():
        shortner = Shortner.objects.get(urlHash=urlHash)
        if datetime.now() > shortner.expirationDate:
            shortner.delete()
            raise Http404('Time limit for your link is over :(')
        else:
            return HttpResponseRedirect(shortner.urlOriginal)
    else:
        raise Http404('Invalid short link :(')


def short_str(s, char_length=6):
    """Geneate hexadecimal string with given length from a string
    """
    hash_object = hashlib.sha512(s.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[0:char_length]


def create_shortner(short_link, url_orig):
    context = {}
    short = Shortner(urlHash=short_link.split('/')[-1], urlOriginal=url_orig)
    short.save()
    context['message'] = 'Your short link is:'
    context['shortlink'] = short_link
    return context
