from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from .forms import UserForm
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from productapi.models import Smartphone, Rated
from profiles.models import UserInfo

class SignUpView(FormView):
    form_class = UserForm
    user_obj = User
    template_name = 'signup.html'
    model = Smartphone
    

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home',))
        else:
            i=0
            top_two = []
            top_four = []
            best_smartphones = self.model.objects.all().order_by('-total_ratings')
            for i in range(0, 2):
                top_two.append(best_smartphones[i])

            for i in range(2, 4):
                top_four.append(best_smartphones[i])
            
            form = self.form_class(None)
            return render(request, self.template_name, {'form' : form, 'top_two': top_two, 'top_four': top_four})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username'].lower()
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if confirm_password != password:
                form.add_error('confirm_password', 'Passwords Donot Match !')
                top_two = []
                top_four = []
                best_smartphones = self.model.objects.all().order_by('-total_ratings')
                for i in range(0, 2):
                    top_two.append(best_smartphones[i])

                for i in range(2, 4):
                    top_four.append(best_smartphones[i])

                return render(request, self.template_name, {'form' : form, 'top_two': top_two, 'top_four': top_four})
            else:
                top_two = []
                top_four = []
                best_smartphones = self.model.objects.all().order_by('-total_ratings')
                for i in range(0, 2):
                    top_two.append(best_smartphones[i])

                for i in range(2, 4):
                    top_four.append(best_smartphones[i])
                user.set_password(password)
                user.save()

            return redirect('login:login')
        else:
            i=0
            top_two = []
            top_four = []
            best_smartphones = self.model.objects.all().order_by('-total_ratings')
            for i in range(0, 2):
                top_two.append(best_smartphones[i])

            for i in range(2, 4):
                top_four.append(best_smartphones[i])
            return render(request, self.template_name, {'form' : form, 'top_two': top_two, 'top_four': top_four})