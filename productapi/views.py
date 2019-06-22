from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Smartphone, Rated
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AboutTheProductForm
from itertools import chain
import os, re
from django.shortcuts import redirect, reverse
from django.contrib.auth import login, authenticate

# @login_required(login_url='login:login')
def ProductView(request, product_search):
    user = request.user
    smartphones = Smartphone.objects.get(name=product_search)
    smartphones_comments = Rated.objects.filter(product=smartphones, has_written=True)
    if not user.is_authenticated:
        return render(request, 'product.html', {'smartphones': smartphones, 'comments': smartphones_comments})
    
    rated = Rated()
    form = AboutTheProductForm()
    error = "Thank you for Rating the Product"
    error2 = "Thank you for giving the Title"
    error3 = "Please Rate the Product First.."
    error4 = "Thank you for your Feedback !"

    if 'people-hiddenfield' in request.POST:
            user_search = request.POST.get('people-search')
            return redirect(reverse('profile:users', args=(user_search,)))

    if request.method == 'POST' and 'comments-hiddenfield' in request.POST:
        if not Rated.objects.filter(user=request.user, product=smartphones).exists():
            return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error3': error3, 'comments': smartphones_comments, 'user': request.user})

    if Rated.objects.filter(user=request.user, product=smartphones).exists():
        if Rated.objects.filter(user=request.user, product=smartphones, has_written=True).exists():
            if Rated.objects.filter(user=request.user, product=smartphones, has_commented=True).exists():
                return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error2': error2, 'error': error, 'error4': error4, 'comments': smartphones_comments, 'user': request.user})
            else:
                if request.method == 'POST' and 'hide' in request.POST:
                    choices = request.POST.getlist('checkboxes')
                    rated_item = Rated.objects.get(user=request.user, product=smartphones)
                    if '1' in choices:
                        smartphones.recommend += 1
                        rated_item.recommend = 1


                    if '2' in choices:
                        smartphones.not_recommend += 1
                        rated_item.not_recommend = 1


                    if '3' in choices:
                        smartphones.issues_with_the_product = smartphones.issues_with_the_product + 1
                        rated_item.issues_with_the_product = 1


                    if '4' in choices:
                        smartphones.overpriced = smartphones.overpriced + 1
                        rated_item.overpriced = 1


                    if '5' in choices:
                        smartphones.budget = smartphones.budget + 1
                        rated_item.budget = 1


                    if '6' in choices:
                        smartphones.smooth = smartphones.smooth + 1
                        rated_item.smooth = 1


                    smartphones.commented += 1
                    rated_item.has_commented = True
                    rated_item.save()
                    smartphones.save()

                    return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'error2': error2, 'error4': error4, 'comments': smartphones_comments, 'user': request.user})
                else:
                    return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'error4': error4, 'comments': smartphones_comments, 'user': request.user})
        else:
            if request.method == 'POST' and 'comments-hiddenfield' in request.POST:
                form = AboutTheProductForm(request.POST)
                if form.is_valid():
                    userobj = Rated.objects.get(user=request.user, product=smartphones)
                    about = form.cleaned_data['about']
                    userobj.about = about
                    userobj.has_written = True
                    userobj.save()
                    if Rated.objects.filter(user=request.user, product=smartphones, has_commented=True).exists():
                        return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'error2': error2, 'error4': error4, 'comments': smartphones_comments, 'user': request.user})
                    else:
                        return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'error4': error4, 'comments': smartphones_comments, 'user': request.user})

        if Rated.objects.filter(user=request.user, product=smartphones, has_commented=True).exists():
            if Rated.objects.filter(user=request.user, product=smartphones, has_written=True).exists():
                return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error2': error2, 'error4': error4, 'error': error, 'comments': smartphones_comments, 'user': request.user})
            else:
                if request.method == 'POST' and 'comments-hiddenfield' in request.POST:
                    form = AboutTheProductForm(request.POST)
                    if form.is_valid():
                        userobj = Rated.objects.get(user=request.user, product=smartphones)
                        about = form.cleaned_data['about']
                        userobj.about = about
                        userobj.has_written = True
                        userobj.save()
                        return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'error4': error4, 'error2': error2, 'comments': smartphones_comments, 'user': request.user})
                else:
                    return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error2': error2, 'error': error, 'comments': smartphones_comments, 'user': request.user})
        else:
            if request.method == 'POST' and 'hide' in request.POST:
                choices = request.POST.getlist('checkboxes')
                rated_item = Rated.objects.get(user=request.user, product=smartphones)
                if '1' in choices:
                    smartphones.recommend += 1
                    rated_item.recommend = 1


                if '2' in choices:
                    smartphones.not_recommend += 1
                    rated_item.not_recommend = 1


                if '3' in choices:
                    smartphones.issues_with_the_product = smartphones.issues_with_the_product + 1
                    rated_item.issues_with_the_product = 1


                if '4' in choices:
                    smartphones.overpriced = smartphones.overpriced + 1
                    rated_item.overpriced = 1


                if '5' in choices:
                    smartphones.budget = smartphones.budget + 1
                    rated_item.budget = 1


                if '6' in choices:
                    smartphones.smooth = smartphones.smooth + 1
                    rated_item.smooth = 1


                smartphones.commented += 1
                rated_item.has_commented = True
                rated_item.save()
                smartphones.save()

                return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'error2': error2, 'comments': smartphones_comments, 'user': request.user})
                    
        return render(request, 'product.html', {'smartphones': smartphones, 'error': error, 'form': form, 'comments': smartphones_comments, 'comments': smartphones_comments, 'user': request.user})

    else:
        if request.method == 'POST' and 'hidden' in request.POST:
            request.session['has_rated'] = 'true'
            performance = request.POST.get("performance_range")
            design = request.POST.get("design_range")
            camera = request.POST.get("camera_range")
            features = request.POST.get("features_range")
            sound = request.POST.get("sound_range")

            rated.user = User.objects.get(id=user.id)
            rated.product = smartphones
            rated.performance_ratings = performance
            rated.camera_ratings = camera
            rated.features_ratings = features
            rated.design_ratings = design
            rated.sound_ratings = sound
            rated.total_ratings = (float(performance) + float(camera) + float(features) + float(design) + int(sound)) / 5.0
            rated.save()

            smartphones.no_of_users += 1

            smartphones.performance_ratings = (smartphones.performance_ratings + int(performance)) / smartphones.no_of_users

            smartphones.design_ratings = (smartphones.design_ratings + int(design)) / smartphones.no_of_users

            smartphones.camera_ratings = (smartphones.camera_ratings + int(camera)) / smartphones.no_of_users

            smartphones.features_ratings = (smartphones.features_ratings + int(features)) / smartphones.no_of_users

            smartphones.sound_ratings = (smartphones.sound_ratings + int(sound)) / smartphones.no_of_users

            smartphones.total_ratings = (float(smartphones.performance_ratings) + float(smartphones.design_ratings) + float(smartphones.camera_ratings) + float(smartphones.features_ratings) + float(smartphones.sound_ratings)) / 5.0

            smartphones.save()
            return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'error': error, 'comments': smartphones_comments, 'user': request.user})

    return render(request, 'product.html', {'smartphones': smartphones, 'form': form, 'comments': smartphones_comments, 'user': request.user})




# @login_required(login_url='login:login')
def ProductsView(request, product_search):

    if 'people-hiddenfield' in request.POST:
            user_search = request.POST.get('people-search')
            return redirect(reverse('profile:users', args=(user_search,)))

    if 'product-hidden' in request.POST:           
        product = Smartphone()
    
        product_search = request.POST.get('product_search').strip(' ').lower()
        product_search = re.sub(' +', ' ',product_search)
        product_company = product_search.split(' ')[0]
        if product_search == '':
            error = "Please specify product name"
            return render(request, 'index.html', {'user': request.user, 'error': error})

        if Smartphone.objects.filter(name__contains=product_search):
            return redirect(reverse('products:products_brand', args=(product_search,)))
        else:
            if Smartphone.objects.filter(name__contains=product_company):
                return redirect(reverse('products:products_brand', args=(product_company,)))
            return render(request, 'product_not_found.html')
            
    smartphone_brand = Smartphone.objects.filter(name__exact = product_search)
    if not smartphone_brand:
        product_company = product_search.split(' ')[0]
        other_products = (Smartphone.objects.filter(name__startswith = product_company))
        not_found_error = "We could not find the Exact Product but there are other products from "
        return render(request, 'products.html', {'smartphone_brand': other_products, 'not_found_error': not_found_error, 'product_company': product_company})

    else:
        product_company = product_search.split(' ')[0]
        other_products = (Smartphone.objects.filter(name__startswith = product_company).exclude(name__exact = product_search))

        all_product_list = list(chain(smartphone_brand, other_products))
        return render(request, 'products.html', {'smartphone_brand': all_product_list})


class ProductNotFoundView(TemplateView):
    template_name = 'product_not_found.html'

    @login_required(login_url='login:login')
    def get(self, request):
        return render(request, self.template_name, {'user': request.user})


