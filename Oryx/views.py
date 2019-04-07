from django.views.generic import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.shortcuts import render
import os, re
from productapi.models import Smartphone, Rated
from productapi.models import Smartphone

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        # smartphones = Smartphone.objects.all().order_by('-total_ratings')
        # top_smartphones = []
        # for i in range(0, 6):
        #     top_smartphones.append(smartphones[i])
        if request.session.get('user_id') is not None:
            return redirect(reverse('home:home',))
        else:
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

def PrivacyPolicyView(request):
    return render(request, 'privacy_policy.html')


def UploadView(request):

    smartphones_list = []

    total_smartphones_list = ['Asus PadFone 2.jpeg', 'Asus PadFone E.jpeg', 'Asus PadFone Infinity Lite .jpeg', 'Asus PadFone Infinity.jpeg', 'Asus PadFone Mini 4.3.jpeg', 'Asus PadFone Mini.jpeg', 'Asus PadFone S.jpeg', 'Asus PadFone X Mini.jpeg', 'Asus PadFone X.jpeg', 'Asus PadFone.jpeg', 'Asus ROG Phone.jpeg', 'Asus ZenFone 2 Laser.jpeg', 'Asus ZenFone 2.jpeg', 'Asus ZenFone 2E.jpeg', 'Asus Zenfone 3 Deluxe.jpeg', 'Asus Zenfone 3 Laser.jpeg', 'Asus Zenfone 3 Max.jpeg', 'Asus Zenfone 3 Ultra.jpeg', 'Asus Zenfone 3 Zoom.jpeg', 'Asus Zenfone 3.jpeg', 'Asus Zenfone 3s Max.jpeg', 'Asus Zenfone 4 Max Plus.jpeg', 'Asus Zenfone 4 Max Pro.jpeg', 'Asus Zenfone 4 Max.jpeg', 'Asus Zenfone 4 Pro.jpeg', 'Asus ZenFone 4 Selfie Lite.jpeg', 'Asus Zenfone 4 Selfie Pro .jpeg', 'Asus Zenfone 4 Selfie.jpeg', 'Asus ZenFone 4.jpeg', 'Asus Zenfone 5 Lite.jpeg', 'Asus ZenFone 5.jpeg', 'Asus Zenfone 5Z.jpeg', 'Asus ZenFone 6.jpeg', 'Asus ZenFone AR.jpeg', 'Asus ZenFone C.jpeg', 'Asus ZenFone Go.jpeg', 'Asus Zenfone Live.jpeg', 'Asus Zenfone Max M1.jpeg', 'Asus Zenfone Max M2.jpeg', 'Asus Zenfone Max Plus.jpeg', 'Asus Zenfone Max Pro M1.jpeg', 'Asus Zenfone Max Pro M2.jpeg', 'Asus ZenFone Max.jpeg', 'Asus ZenFone Selfie.jpeg', 'Asus Zenfone V.jpeg', 'Asus ZenFone Zoom.jpeg', 'iPhone 3G.jpeg', 'iPhone 3GS.jpeg', 'iPhone 4.jpeg', 'iPhone 5.jpeg', 'iPhone 5S.jpeg', 'iPhone 6.jpeg', 'iPhone 6S.jpeg', 'iPhone 7.jpeg', 'iPhone 8.jpeg', 'iPhone S.jpeg', 'iPhone XS .jpeg', 'Mi 1.jpeg', 'Mi 1S.jpeg', 'Mi 2.jpeg', 'Mi 2A.jpeg', 'Mi 2s .jpeg', 'Mi 3.jpeg', 'Mi 4.jpeg', 'Mi 4c.jpeg', 'Mi 4i.jpeg', 'Mi 4s.jpeg', 'Mi 5.jpeg', 'Mi 5c.jpeg', 'Mi 5s.jpeg', 'Mi 5X.jpeg', 'Mi 6.jpeg', 'Mi 8 EE.jpeg', 'Mi 8 Lite.jpeg', 'Mi 8 SE.jpeg', 'Mi A2 Lite.jpeg', 'Mi A2.jpeg', 'Mi Max 2.jpeg', 'Mi Max 3.jpeg', 'Mi Max Prime.jpeg', 'Mi Max.jpg', 'Mi Mix 2.jpeg', 'Mi Mix 2s.jpeg', 'Mi Mix 3.jpeg', 'Mi Mix.jpeg', 'Mi Note 2.jpeg', 'Mi Note 3.jpeg', 'Mi Note Pro.jpeg', 'Mi Note.jpeg', 'Mi Pad 2.jpeg', 'Mi Pad 3.jpeg', 'Mi Pad 4 Plus.jpeg', 'Mi Pad 4.jpeg', 'Mi Pad.jpeg', 'Moto C Plus .jpeg', 'Moto C.jpeg', 'Moto E.jpeg', 'Moto E3 Power .jpeg', 'Moto E3.jpeg', 'Moto E4 Plus .jpeg', 'Moto E4.jpeg', 'Moto E5 Play .jpeg', 'Moto E5 Plus.jpeg', 'Moto E5.jpeg', 'Moto G.jpeg', 'Moto G4 .jpeg', 'Moto G4 Play .jpeg', 'Moto G4 Plus.jpeg', 'Moto G5 Plus.jpeg', 'Moto G5.jpeg', 'Moto G6 Play .jpeg', 'Moto G6 Plus.jpeg', 'Moto G6.jpeg', 'Moto M.jpeg', 'Moto Maxx.jpeg', 'Moto Turbo .jpeg', 'Moto X Force.jpeg', 'Moto X Play.jpeg', 'Moto X Pro.jpeg', 'Moto X Style.jpeg', 'Moto X4.jpeg', 'Moto Z Droid.jpeg', 'Moto Z Force Droid .jpeg', 'Moto Z Force.jpeg', 'Moto Z Play.jpeg', 'Moto Z.jpeg', 'Moto Z2 Force Edition .jpeg', 'Moto Z2 Play .jpeg', 'Moto Z3 Play.jpeg', 'Moto.jpeg', 'Nokia 1.jpeg', 'Nokia 105.jpeg', 'Nokia 106.jpeg', 'Nokia 1100.jpeg', 'Nokia 130.jpeg', 'Nokia 150.jpeg', 'Nokia 2.1.jpeg', 'Nokia 2.jpeg', 'Nokia 216.jpeg', 'Nokia 230.jpeg', 'Nokia 3.1 Plus.jpeg', 'Nokia 3.1.jpeg', 'Nokia 3.jpeg', 'Nokia 3310.jpeg', 'Nokia 5.1 Plus.jpeg', 'Nokia 5.1.jpeg', 'Nokia 5.jpeg', 'Nokia 6.1 Plus.jpeg', 'Nokia 6.1.jpeg', 'Nokia 6.jpeg', 'Nokia 7 Plus.jpeg', 'Nokia 7.1.jpeg', 'Nokia 7.jpeg', 'Nokia 8 Sirocco.jpeg', 'Nokia 8.1.jpeg', 'Nokia 8.jpeg', 'Nokia 8110 4G.jpeg', 'Nokia Asha 202.jpeg', 'Nokia Asha 203.jpeg', 'Nokia Asha 205.jpeg', 'Nokia Asha 210.jpeg', 'Nokia Asha 230.jpeg', 'Nokia Asha 300.jpeg', 'Nokia Asha 302.jpeg', 'Nokia Asha 305.jpeg', 'Nokia Asha 306.jpeg', 'Nokia Asha 308.jpeg', 'Nokia Asha 309.jpeg', 'Nokia Asha 310.jpeg', 'Nokia Asha 311.jpeg', 'Nokia Asha 500.jpeg', 'Nokia Asha 501.jpeg', 'Nokia Asha 502.jpeg', 'Nokia Asha 503.jpeg', 'Nokia N70 Music Edition.jpeg', 'Nokia N70.jpeg', 'Nokia N71.jpeg', 'Nokia N72.jpeg', 'Nokia N73 Music Edition.jpeg', 'Nokia N73.jpeg', 'Nokia N75.jpeg', 'Nokia N76.jpeg', 'Nokia N77.jpeg', 'Nokia N78.jpeg', 'Nokia N79.jpeg', 'Nokia N8.jpeg', 'Nokia N80.jpeg', 'Nokia N81.jpeg', 'Nokia N82.jpeg', 'Nokia N85.jpeg', 'Nokia N86.jpeg', 'Nokia N9.jpeg', 'Nokia N90.jpeg', 'Nokia N900.jpeg', 'Nokia N91.jpeg', 'Nokia N92.jpeg', 'Nokia N93.jpeg', 'Nokia N93i.jpeg', 'Nokia N95.jpeg', 'Nokia N950.jpeg', 'Nokia N96 .jpeg', 'Nokia N97 mini.jpeg', 'Nokia N97.jpeg', 'Nokia X+.jpeg', 'Nokia X.jpeg', 'Nokia X2.jpeg', 'Nokia XL 4G.jpeg', 'Nokia XL.jpeg', 'Oppo A3.jpeg', 'Oppo A37.jpeg', 'Oppo A3s.jpeg', 'Oppo A57.jpeg', 'Oppo A71.jpeg', 'Oppo A73.jpeg', 'Oppo A73s.jpeg', 'Oppo A75.jpeg', 'Oppo A77.jpeg', 'Oppo A79.jpeg', 'Oppo A83.jpeg', 'Oppo F1s.jpeg', 'Oppo F3 plus.jpeg', 'Oppo F3.jpeg', 'Oppo F5 Youth.jpeg', 'Oppo F5.jpeg', 'Oppo F7 Youth.jpeg', 'Oppo F7.jpeg', 'Oppo F9 Pro.jpg', 'Oppo F9.jpeg', 'Oppo Find 5.jpeg', 'Oppo Find X.jpeg', 'Oppo K1.jpg', 'Oppo N1.jpeg', 'Oppo N3.jpeg', 'Oppo Oppo K1.jpeg', 'Oppo R11 Plus.jpeg', 'Oppo R11.jpeg', 'Oppo R11s Plus.jpeg', 'Oppo R11s.jpeg', 'Oppo R13.jpeg', 'Oppo R15 Pro.jpeg', 'Oppo R15.jpeg', 'Oppo R15x.jpeg', 'Oppo R17 Pro.jpeg', 'Oppo R17.jpeg', 'Oppo R1S.jpeg', 'Oppo R3.jpeg', 'Oppo R5.jpeg', 'Oppo R7 Plus.jpeg', 'Oppo R7.jpeg', 'Oppo R7s.jpeg', 'Oppo R9 Plus.jpeg', 'Oppo R9.jpeg', 'Oppo R9s Plus.jpeg', 'Oppo R9s.jpeg', 'Redmi 1.jpeg', 'Redmi 1S 4G.jpeg', 'Redmi 1s.jpeg', 'Redmi 2.jpeg', 'Redmi 2A.jpeg', 'Redmi 3S.jpeg', 'Redmi 3X.jpeg', 'Redmi 4 Prime.jpeg', 'Redmi 4.jpeg', 'Redmi 4A.jpeg', 'Redmi 4X.jpeg', 'Redmi 5.jpeg', 'Redmi 5A.jpeg', 'Redmi 6 Pro.jpeg', 'Redmi 6.jpeg', 'Redmi 6A.jpeg', 'Redmi Note 2 .jpeg', 'Redmi Note 3.jpeg', 'Redmi Note 3G.jpeg', 'Redmi Note 4.jpeg', 'Redmi Note 4G  .jpeg', 'Redmi Note 4X.jpeg', 'Redmi Note 5 Pro.jpeg', 'Redmi Note 5.jpeg', 'Redmi Note 6 Pro.jpeg', 'Redmi Note Prime.jpeg', 'Redmi Pro.jpeg', 'Redmi Y1 lite.jpeg', 'Redmi Y1.jpeg', 'Redmi Y2.jpeg', 'Samsung Galaxy A3.jpeg', 'Samsung Galaxy A5.jpeg', 'Samsung Galaxy A6+.jpeg', 'Samsung Galaxy A6.jpeg', 'Samsung Galaxy A6s.jpeg', 'Samsung Galaxy A7.jpeg', 'Samsung Galaxy A8+.jpeg', 'Samsung Galaxy A8.jpeg', 'Samsung Galaxy A8s.jpeg', 'Samsung Galaxy A9 Pro.jpeg', 'Samsung Galaxy A9.jpeg', 'Samsung Galaxy A9s.jpeg', 'Samsung Galaxy Ace 2.jpeg', 'Samsung Galaxy Ace 3.jpeg', 'Samsung Galaxy Ace 4.jpeg', 'Samsung Galaxy Ace Plus.jpeg', 'Samsung Galaxy Ace Style.jpeg', 'Samsung Galaxy Ace.jpeg', 'Samsung Galaxy C5 Pro.jpeg', 'Samsung Galaxy C5.jpeg', 'Samsung Galaxy C7 Pro.jpeg', 'Samsung Galaxy C7.jpeg', 'Samsung Galaxy C8.jpeg', 'Samsung Galaxy C9 Pro.jpeg', 'Samsung Galaxy C9.jpeg', 'Samsung Galaxy Core II.jpeg', 'Samsung Galaxy Core Plus.jpeg', 'Samsung Galaxy Core Prime.jpeg', 'Samsung Galaxy Core.jpeg', 'Samsung Galaxy Grand 2.jpeg', 'Samsung Galaxy Grand Neo Plus.jpeg', 'Samsung Galaxy Grand Neo.jpeg', 'Samsung Galaxy Grand Prime Plus.jpeg', 'Samsung Galaxy Grand Prime Pro.jpeg', 'Samsung Galaxy Grand Prime.jpeg', 'Samsung Galaxy Grand.jpeg', 'Samsung Galaxy J Max.jpeg', 'Samsung Galaxy J1 Ace Neo.jpeg', 'Samsung Galaxy J1 Ace.jpeg', 'Samsung Galaxy J1 Mini Prime.jpeg', 'Samsung Galaxy J1 Mini.jpeg', 'Samsung Galaxy J1 Nxt.jpeg', 'Samsung Galaxy J1.jpeg', 'Samsung Galaxy J2 Core.jpeg', 'Samsung Galaxy J2 Prime.jpeg', 'Samsung Galaxy J2 Pro.jpeg', 'Samsung Galaxy J2.jpeg', 'Samsung Galaxy J3 Emerge.jpeg', 'Samsung Galaxy J3 Prime.jpeg', 'Samsung Galaxy J3 Pro.jpeg', 'Samsung Galaxy J3.jpeg', 'Samsung Galaxy J4 Core.jpeg', 'Samsung Galaxy J4.jpeg', 'Samsung Galaxy J5 Prime.jpeg', 'Samsung Galaxy J5.jpeg', 'Samsung Galaxy J6.jpeg', 'Samsung Galaxy J7 Duo.jpeg', 'Samsung Galaxy J7 Max.jpeg', 'Samsung Galaxy J7 Nxt.jpeg', 'Samsung Galaxy J7 Prime 2.jpeg', 'Samsung Galaxy J7 Prime.jpeg', 'Samsung Galaxy J7 Pro.jpeg', 'Samsung Galaxy J7 Sky Pro.jpeg', 'Samsung Galaxy J7 V.jpeg', 'Samsung Galaxy J7+.jpeg', 'Samsung Galaxy J7.jpeg', 'Samsung Galaxy J8.jpeg', 'Samsung Galaxy Note 10.1.jpeg', 'Samsung Galaxy Note 3 Neo.jpeg', 'Samsung Galaxy Note 3.jpeg', 'Samsung Galaxy Note 4.jpeg', 'Samsung Galaxy Note 5.jpeg', 'Samsung Galaxy Note 7.jpeg', 'Samsung Galaxy Note 8.jpeg', 'Samsung Galaxy Note 9.jpeg', 'Samsung Galaxy Note Edge.jpeg', 'Samsung Galaxy Note II.jpeg', 'Samsung Galaxy Note Pro 12.2.jpeg', 'Samsung Galaxy Note Pro.jpeg', 'Samsung Galaxy Note.jpeg', 'Samsung Galaxy On Max.jpeg', 'Samsung Galaxy On Nxt.jpeg', 'Samsung Galaxy On5 Pro.jpeg', 'Samsung Galaxy On5.jpeg', 'Samsung Galaxy On6.jpeg', 'Samsung Galaxy On7 Pro.jpeg', 'Samsung Galaxy On7.jpeg', 'Samsung Galaxy On8.jpeg', 'Samsung Galaxy S Advance.jpeg', 'Samsung Galaxy S Duos .jpeg', 'Samsung Galaxy S Duos 2.jpeg', 'Samsung Galaxy S Duos 3.jpeg', 'Samsung Galaxy S II Plus.jpeg', 'Samsung Galaxy S III Mini.jpeg', 'Samsung Galaxy S III Neo.jpeg', 'Samsung Galaxy S III Slim.jpeg', 'Samsung Galaxy S III.jpeg', 'Samsung Galaxy S4 Active.jpeg', 'Samsung Galaxy S4 Mini.jpeg', 'Samsung Galaxy S4 Zoom.jpeg', 'Samsung Galaxy S4.jpeg', 'Samsung Galaxy S5 Active.jpeg', 'Samsung Galaxy S5 Mini.jpeg', 'Samsung Galaxy S5 Neo.jpeg', 'Samsung Galaxy S5 Plus.jpeg', 'Samsung Galaxy S5.jpeg', 'Samsung Galaxy S6 Active.jpeg', 'Samsung Galaxy S6 Edge+.jpeg', 'Samsung Galaxy S6 Edge.jpeg', 'Samsung Galaxy S6.jpeg', 'Samsung Galaxy S7 Active.jpeg', 'Samsung Galaxy S7 Edge.jpeg', 'Samsung Galaxy S7.jpeg', 'Samsung Galaxy S8 Active.jpeg', 'Samsung Galaxy S8+.jpeg', 'Samsung Galaxy S8.jpeg', 'Samsung Galaxy S9+.jpeg', 'Samsung Galaxy S9.jpeg', 'Samsung Galaxy Tab 10.1.jpeg', 'Samsung Galaxy Tab 2.jpeg', 'Samsung Galaxy Tab 3 Lite.jpeg', 'Samsung Galaxy Tab 3.jpeg', 'Samsung Galaxy Tab 4.jpeg', 'Samsung Galaxy Tab 7.0 Plus.jpeg', 'Samsung Galaxy Tab 7.7.jpeg', 'Samsung Galaxy Tab 8.9.jpeg', 'Samsung Galaxy Tab A 10.1 .jpeg', 'Samsung Galaxy Tab A 7.0 .jpeg', 'Samsung Galaxy Tab A 8.0.jpeg', 'Samsung Galaxy Tab A 9.7.jpeg', 'Samsung Galaxy Tab A.jpeg', 'Samsung Galaxy Tab E.jpeg', 'Samsung Galaxy Tab Pro.jpeg', 'Samsung Galaxy Tab S.jpeg', 'Samsung Galaxy Tab S2.jpeg', 'Samsung Galaxy Tab S3.jpeg', 'Samsung Galaxy Tab S4.jpeg', 'Samsung Galaxy Tab.jpeg', 'Samsung Galaxy TabPro S.jpeg', 'Vivo Nex A.jpeg', 'Vivo Nex S.jpeg', 'Vivo Nex.jpeg', 'Vivo V1.jpeg', 'Vivo V11 Pro.jpeg', 'Vivo V11.jpeg', 'Vivo V11i.jpeg', 'Vivo V1Max.jpeg', 'Vivo V3 Max.jpeg', 'Vivo V3.jpeg', 'Vivo V5 Lite.jpeg', 'Vivo V5 Plus.jpeg', 'Vivo V5.jpeg', 'Vivo V5s.jpeg', 'Vivo V7+.jpeg', 'Vivo V7.jpeg', 'Vivo V9 Pro.jpeg', 'Vivo V9 Youth.jpeg', 'Vivo V9.jpeg', 'Vivo X Shot.jpeg', 'Vivo X20 Plus UD.jpeg', 'Vivo X20 Plus.jpeg', 'Vivo X20.jpeg', 'Vivo X21 UD.jpeg', 'Vivo X21i.jpeg', 'Vivo X21s.jpeg', 'Vivo X23 Symphony Edition.jpeg', 'Vivo X23.jpeg', 'Vivo X3S.jpeg', 'Vivo X5Max+.jpeg', 'Vivo X5Max.jpeg', 'Vivo X5Pro.jpeg', 'Vivo X5S L.jpeg', 'Vivo X6 Plus.jpeg', 'Vivo X6.jpeg', 'Vivo X6S Plus.jpeg', 'Vivo X6S.jpeg', 'Vivo X7 Plus.jpeg', 'Vivo X7.jpeg', 'Vivo X9 Plus.jpeg', 'Vivo X9.jpeg', 'Vivo X9S Plus.jpeg', 'Vivo X9s.jpeg', 'Vivo Xplay 5.jpeg', 'Vivo Xplay 6.jpeg', 'Vivo Xplay5 Elite.jpeg', 'Vivo Y15.jpeg', 'Vivo Y15S.jpeg', 'Vivo Y21L.jpeg', 'Vivo Y22.jpeg', 'Vivo Y25.jpeg', 'Vivo Y27L.jpeg', 'Vivo Y31A.jpeg', 'Vivo Y31L.jpeg', 'Vivo Y51.jpeg', 'Vivo Y51L.jpeg', 'Vivo Y53.jpeg', 'Vivo Y53i.jpeg', 'Vivo Y55L.jpeg', 'Vivo Y55s.jpeg', 'Vivo Y66.jpeg', 'Vivo Y69.jpeg', 'Vivo Y71.jpeg', 'Vivo Y71i.jpeg', 'Vivo Y75.jpeg', 'Vivo Y79.jpeg', 'Vivo Y81.jpeg', 'Vivo Y83 Pro.jpeg', 'Vivo Y83.jpeg', 'Vivo Y93.jpeg', 'Vivo Y93s.jpeg', 'Vivo Y95.jpeg', 'Vivo Y97.jpeg', 'Vivo Z1 Lite.jpeg', 'Vivo Z1.jpeg', 'Vivo Z10.jpeg', 'Vivo Z1i.jpeg', 'Vivo Z3.jpeg', 'Vivo Z3i.jpeg']



    for i in smartphones_list:
        obj = Smartphone()
        obj.name = re.sub('.jpeg' or '.jpg', '', i).lower()
        j = re.sub(' ', '+', i)
        obj.save()

    return render(request, 'upload.html')
        


