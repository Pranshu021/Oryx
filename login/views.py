from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from .forms import UserForm
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from profiles.models import UserInfo

def LoginView(request):

    if request.user.is_authenticated:
        return redirect(reverse('home:home',))

    else:
        users = User()

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    request.session['user_id'] = user.id
                    request.session.set_expiry(0)
                    pk=user.id
                    userinfo_object = UserInfo()
                    if not UserInfo.objects.filter(Userinfo = request.user).exists():
                        userinfo_object.Userinfo = request.user
                        userinfo_object.save()
                        
                    return HttpResponseRedirect(reverse('home:home',))
                else:
                    return HttpResponse("Your account is disabled !")
            
            else:
                if User.objects.filter(email=username):
                    user = User.objects.get(email=username)
                    if user.check_password(password):
                        login(request, user)
                        request.session['user_id'] = user.id
                        request.session.set_expiry(0)
                        pk=user.id
                        userinfo_object = UserInfo()
                        if not UserInfo.objects.filter(Userinfo = request.user).exists():
                            userinfo_object.Userinfo = request.user
                            userinfo_object.save()

                        return HttpResponseRedirect(reverse('home:home',))
            
                    else:
                        error = "Wrong username or Password"
                        return render(request, 'login.html', {'error': error})    

                else:
                        error = "Wrong username or Password"
                        return render(request, 'login.html', {'error': error})    
                    
                error = "Wrong username or Password"
                return render(request, 'login.html', {'error': error})
        
        else:
            return render(request, 'login.html')