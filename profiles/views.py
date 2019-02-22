from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from .forms import UpdateProfileForm
from django.contrib.auth.models import User
from productapi.models import Rated
from django.shortcuts import redirect, reverse



@login_required(login_url='login:login')
def ProfileView(request, username):

    if 'people-hiddenfield' in request.POST:
            user_search = request.POST.get('people-search')
            return redirect(reverse('profile:users', args=(user_search,)))

            
    user = User.objects.filter(username=username)
    user_obj = User.objects.get(username=username)
    user_info = Rated.objects.filter(user=user[0])
    user_profile = UserInfo.objects.get(Userinfo=request.user)
    form = UpdateProfileForm()

    if request.method == 'POST' and 'remove-pic-hiddenfield' in request.POST:
        user_profile.profile_pic = ''
        user_profile.save()
        return render(request, 'profile.html', {'user_data': user_obj, 'username': username, 'user_info': user_info, 'form': form})


    if request.method == 'POST' and 'profile-pic-hiddenfield' in request.POST:
        form = UpdateProfileForm(request.POST and request.FILES)
        if form.is_valid:
            if '.jpg' or '.jpeg' or '.png' in request.POST or request.FILES:
                profile_pic = request.FILES.get('profile_pic', )
                user_profile.profile_pic = profile_pic
                user_profile.save()
                return render(request, 'profile.html', {'user_data': user_obj, 'username': username, 'user_info': user_info, 'form': form})
            
            else:
                error = "Invalid Image. Try to use other format..."
                return render(request, 'profile.html', {'user_data': user_obj, 'username': username, 'user_info': user_info, 'form': form, 'error': error})

    
    return render(request, 'profile.html', {'user_data': user_obj, 'username': username, 'user_info': user_info, 'form': form})

@login_required
def UserProfileViews(request, user_search):
    user = User.objects.filter(username__startswith=user_search) or User.objects.filter(username__endswith=user_search)

    if user:
        count = 0
        comments_count = Rated.objects.filter(user=user[0], has_commented = True)

        for j in comments_count:
            count = count + 1

        return render(request, 'users.html', {'user_list': user, 'comments': comments_count, 'count': count})
    else:
        error = "No such User"
        return render(request, 'users.html', {'error': error})

@login_required
def ChangePasswordView(request):
    user = request.user
    user_obj = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        new_password = request.POST.get('password')
        user_obj.set_password(new_password)
        user_obj.save()
        return redirect('home:home')

    return render(request, 'change_password.html')