from django.shortcuts import render
from django.views.generic import *
from productapi.models import Smartphone, Rated
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import re

class HomeView(TemplateView):
    template_name = 'home.html'
    model = Smartphone

    def get(self, request):
        if request.user.is_authenticated:
            user_session = request.session.get('user_id')
            user_info = request.user
            
            return render(request, 'home.html', {'user': request.user})   
            
        else:
            return HttpResponseRedirect(reverse('login:login'))

            
    def post(self, request):

        if 'people-hiddenfield' in request.POST:
            user_search = request.POST.get('people-search')
            print(user_search)
            return redirect(reverse('profile:users', args=(user_search,)))

        if 'product-hiddenfield' in request.POST:
            product = Smartphone()
        
            product_search = request.POST.get('product_search').strip(' ').lower()
            product_search = re.sub(' +', ' ',product_search)
            product_company = product_search.split(' ')[0]
            if product_search == '':
                error = "Please specify product name"
                return render(request, 'home.html', {'user': request.user, 'error': error})


            
            if self.model.objects.filter(name__contains=product_search):
                return HttpResponseRedirect(reverse('products:products_brand', args=(product_search,)))
            else:
                if self.model.objects.filter(name__contains=product_company):
                    return HttpResponseRedirect(reverse('products:products_brand', args=(product_company,)))
                return render(request, 'product_not_found.html')

        else:
            return render(request, 'home.html', {'user': request.user}) 

        




        