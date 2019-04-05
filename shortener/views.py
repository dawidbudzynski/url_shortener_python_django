import pyperclip

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView

from shortener.forms import UrlForm
from shortener.models import Urls
from .utils import generate_short_code


class ShortenUrlView(View):
    """Gets full url from user, shortens it as short_code
    and saves full_url, short_code and creation_date to database"""

    def get(self, request):
        ctx = {'form': UrlForm()}

        return render(
            request,
            template_name='shortener/shortener.html',
            context=ctx
        )

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            full_url = form.cleaned_data.get('full_url')
            url_code = generate_short_code()
            Urls.objects.create(
                url_code=url_code,
                full_url=full_url
            )
            pyperclip.copy(f'https://shorty.herokuapp.com/{url_code}')  # copies shortened url to clipboard
            return HttpResponseRedirect(
                reverse('shortener:success', kwargs={'url_code': url_code})
            )
        return HttpResponseRedirect(reverse('shortener:error'))


class RedirectToOriginalPageView(View):
    """Reads url_code from user and redirects to original page"""

    def get(self, request, url_code):
        url = Urls.objects.filter(url_code=url_code)
        if url:
            return HttpResponseRedirect(url[0].full_url)
        return HttpResponseRedirect(reverse('shortener:page_not_found'))


class SuccessView(TemplateView):
    template_name = 'shortener/success.html'


class PageNotFoundView(TemplateView):
    template_name = 'shortener/page_not_found.html'


class ErrorView(TemplateView):
    template_name = 'shortener/error.html'
