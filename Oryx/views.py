from django.views.generic import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.shortcuts import render
import os, re
from productapi.models import Smartphone, Rated

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        if request.session.get('user_id') is not None:
            return redirect(reverse('home:home',))
        else:
            # print(user_session)
            return render(request, self.template_name)

class TestView(TemplateView):
    template_name = 'new.html'

@login_required(login_url='login:login')
def LogoutView(request):
    logout(request)
    return redirect('index')


class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'people-hiddenfield' in request.POST:
            user_search = request.POST.get('people-search')
            print(user_search)
            return redirect(reverse('profile:users', args=(user_search,)))


class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'people-hiddenfield' in request.POST:
            user_search = request.POST.get('people-search')
            print(user_search)
            return redirect(reverse('profile:users', args=(user_search,)))

def TestView(request):
    return render(request, 'test.html')

def UploadView(request):
    os.chdir('..\\')
    for i in os.listdir('downloads'):
        obj = Smartphone()
        obj.name = re.sub('.jpeg' or '.jpg', '', i).lower()
        obj.image = i
        obj.save()

    return render(request, 'upload.html')
        


