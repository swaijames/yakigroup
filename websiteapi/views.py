from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.views.generic.edit import DeleteView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView


# # Create your views here.
# class AuthView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class PackageView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Package.objects.all()
    serializer_class = PackageSerialiser


# class Package_Detail_View(
#     viewsets.GenericViewSet,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin
#
# ):
#     queryset = Package_Details.objects.all()
#     serializer_class = Package_Detail_Serialiser
#

class DestnationView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerialiser


# class Destination_Detail_View(
#     viewsets.GenericViewSet,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin
# ):
#     queryset = Destination_Detail.objects.all()
#     serializer_class = Destination_Detail_Serialiser


class GalleryView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class HeroView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class BookingView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@login_required
def index(request):
    return render(request, 'Tour/index.html')


# Create your views here.
def booking(request):
    return render(request, 'Tour/bookings.html')


def booking_add(request):
    return render(request, 'Tour/booking-add.html')


def booking_edit(request):
    return render(request, 'Tour/booking-edit.html')


def customer(request):
    return render(request, 'Tour/customers.html')


def room_list(request):
    dest = Destination.objects.all().order_by('-updated_at')
    context = {'dest': dest}
    return render(request, 'Tour/room-list.html', context)


class DestinationDelete(DeleteView):
    model = Destination
    success_url = "/room_list"
    template_name = 'Tour/room-delete.html'


def update(request, id):
    mydest = Destination.objects.get(id=id)
    template = loader.get_template('Tour/destination.update.html')
    context = {
        'mydest': mydest,
    }
    return HttpResponse(template.render(context, request))


def update_destination(request, id):
    title = request.POST['title']
    longitude = request.POST['longtude']
    latitude = request.POST['latitude']
    depaturetime = request.POST['depaturetime']
    return_time = request.POST['returntime']
    departure = request.POST['departure']
    image = request.POST['image']
    subimage1 = request.POST['image1']
    subimage2 = request.POST['image2']
    description = request.POST['description']
    dest = Destination.objects.get(id=id)
    dest.title = title
    dest.map_longtude = longitude
    dest.map_latitude = latitude
    dest.departureTime = depaturetime
    dest.return_time = return_time
    dest.departure = departure
    dest.image = image
    dest.sub_image1 = subimage1
    dest.sub_image2 = subimage2
    dest.description = description

    dest.save()
    return HttpResponseRedirect(reverse('room_list'))


def room_type(request):
    return render(request, 'Tour/room-type.html')


def destination_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        longitude = request.POST['longtude']
        latitude = request.POST['latitude']
        depaturetime = request.POST['depaturetime']
        return_time = request.POST['returntime']
        departure = request.POST['departure']
        image = request.POST['image']
        subimage1 = request.POST['image1']
        subimage2 = request.POST['image2']
        description = request.POST['description']
        destination = Destination.objects.create(title=title, map_latitude=latitude, map_longtude=longitude,
                                                 departureTime=depaturetime, return_time=return_time,
                                                 departure=departure, image=image, description=description,
                                                 sub_image1=subimage1, sub_image2=subimage2)
        messages.success(request, 'Data has been submitted')
        print(destination)
        # return redirect('/destination_add')
    return render(request, 'Tour/destination-add.html')


def package_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        duration = request.POST['duration']
        group_size = request.POST['groupsize']
        tour_guide = request.POST['tour_guide']
        tour_type = request.POST['tour_type']
        description = request.POST['description']
        price = request.POST['price']

        #     package details
        pd_description = request.POST['pd-description']
        pd_destination = request.POST['pd-destination']
        pd_included = request.POST['pd-include']
        pd_excluded = request.POST['pd-excluded']
        pd_departure_time = request.POST['pd-departureTime']
        pd_return_time = request.POST['pd-return-time']
        pd_departure = request.POST['pd-departure']
        pd_upload_photo = request.POST['pd-upload_photo']
        # pd_destination_picture = request.POST['pd-destination_picture']
        package_status = request.POST['pd-package_status']

        #     travel plan
        tp_description = request.POST['tp-description']
        tp_day_title = request.POST['tp-day_title']
        tp_from = request.POST['tp-from']
        tp_to = request.POST['tp-to']
        tp_day_feature = request.POST['tp-day_feature']
        #
        tp_description2 = request.POST['tp-description2']
        tp_day_title2 = request.POST['tp-day_title2']
        tp_from2 = request.POST['tp-from2']
        tp_to2 = request.POST['tp-to2']
        tp_day_feature2 = request.POST['tp-day_feature2']
        #
        tp_description3 = request.POST['tp-description3']
        tp_day_title3 = request.POST['tp-day_title3']
        tp_from3 = request.POST['tp-from3']
        tp_to3 = request.POST['tp-to3']
        tp_day_feature3 = request.POST['tp-day_feature3']
        #
        tp_description4 = request.POST['tp-description4']
        tp_day_title4 = request.POST['tp-day_title4']
        tp_from4 = request.POST['tp-from4']
        tp_to4 = request.POST['tp-to4']
        tp_day_feature4 = request.POST['tp-day_feature4']
        #
        tp_description5 = request.POST['tp-description5']
        tp_day_title5 = request.POST['tp-day_title5']
        tp_from5 = request.POST['tp-from5']
        tp_to5 = request.POST['tp-to5']
        tp_day_feature5 = request.POST['tp-day_feature5']

        #     tour gallery_image
        gallery1 = request.POST['gallery1']
        gallery2 = request.POST['gallery2']
        gallery3 = request.POST['gallery3']
        gallery4 = request.POST['gallery4']
        # gallery5 = request.POST['gallery5']

        package = Package.objects.create(package_duration=duration, package_price=price, package_tour_type=tour_type,
                                         package_tour_guide=tour_guide, package_people_group=group_size,
                                         package_title=title, info_detail=pd_description, description=description,
                                         info_destination=pd_destination,
                                         info_excluded1=pd_included, info_excluded2=pd_excluded,
                                         info_depature_time=pd_departure_time,
                                         info_return_time=pd_return_time, info_depature=pd_departure,
                                         info_image1=pd_upload_photo,
                                         # info_image2=pd_destination_picture,
                                         travel_plan_day_description_To=tp_description,
                                         travel_plan_day_title=tp_day_title,
                                         travel_plan_day_time_From=tp_from,
                                         travel_plan_day_time_To=tp_to,
                                         travel_plan_detail=tp_day_feature,
                                         travel_plan2_day_description_To=tp_description2,
                                         travel_plan2_day_title=tp_day_title2,
                                         travel_plan2_day_time_From=tp_from2,
                                         travel_plan2_day_time_To=tp_to2,
                                         travel_plan2_detail=tp_day_feature2,
                                         travel_plan3_day_description_To=tp_description3,
                                         travel_plan3_day_title=tp_day_title3,
                                         travel_plan3_day_time_From=tp_from3,
                                         travel_plan3_day_time_To=tp_to3,
                                         travel_plan3_detail=tp_day_feature3,
                                         travel_plan4_day_description_To=tp_description4,
                                         travel_plan4_day_title=tp_day_title4,
                                         travel_plan4_day_time_From=tp_from4,
                                         travel_plan4_day_time_To=tp_to4,
                                         travel_plan4_detail=tp_day_feature4,
                                         travel_plan5_day_description_To=tp_description5,
                                         travel_plan5_day_title=tp_day_title5,
                                         travel_plan5_day_time_From=tp_from5,
                                         travel_plan5_day_time_To=tp_to5,
                                         travel_plan5_detail=tp_day_feature,
                                         tour_gallery_image1=gallery1, tour_gallery_image2=gallery2,
                                         tour_gallery_image3=gallery3, tour_gallery_image4=gallery4,
                                         )

        messages.success(request, 'Data has been submitted')
        print(package)

    return render(request, 'Tour/package-add.html')


def package_list(request):
    return render(request, 'Tour/package-list.html')


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("/yaki_dashboard")
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('/yaki_dashboard')

            messages.info(request, ' Invalid password')
            return redirect('/login')
        return render(request, 'auths/login.html')
    except Exception as e:
        print(e)


def logout_view(request):
    logout(request)
    return redirect('/login')


def reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            uid = User.objects.get(email=email)
            url = f'http://127.0.0.1:9000/password_reset_confirm/{uid.profile.uuid}'
            send_mail('reset', url, settings.EMAIL_HOST_USER, [email], fail_silently=False, )
            return redirect('/password_reset_done')
        else:
            messages.error(request, "email address is not exists")
    return render(request, 'auths/reset.html')


def change_password(request, uid):
    try:
        if Profile.objects.filter(uuid=uid).exists():
            if request.method == 'POST':
                pass1 = 'password1' in request.POST and request.POST['password1']
                pass2 = 'password2' in request.POST and request.POST['password2']
                if pass1 == pass2:
                    p = Profile.objects.get(uuid=uid)
                    u = p.user
                    user = User.objects.get(username=u)
                    user.password = make_password(pass1)
                    user.save()
                    messages.success(request, "password has been reset successfully")
                    return redirect('login')
                else:
                    messages.error(request, "two password did not match")
        else:
            return HttpResponse('invalid url')
    except:
        return HttpResponse('invalid url')
    return render(request, 'auths/password_reset_confirm.html')


def password_reset_done(request):
    return render(request, 'auths/password_reset_done.html')


def user_profile(request):
    return render(request, 'User-profile/user-profile-regular.html')


def profile(request):
    if request.method == "POST":
        if request.POST.get('update_user') == "user_update":
            firstname = request.POST.get('firstname')
            email = request.POST.get('email')
            lastname = request.POST.get('lastname')
            print("first", firstname, " email ", email, " last ", lastname)
            User.objects.filter(id=request.user.id).update(first_name=firstname, email=email, last_name=lastname)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/logout/')
        else:
            if "old_password" in form.errors:
                messages.error(request, "Your old password was entered incorrectly")
                return redirect('/user_profile')
            elif "The two password fields didn’t match" in form.errors:
                messages.error(request, "The two password fields didn’t match")
                return redirect('/user_profile')
            else:
                messages.error(request, "The password is too similar to the last name")
                return redirect('/user_profile')
    form = PasswordChangeForm(request.user)
    print(form)

    context = {
        "form": form
    }
    return render(request, 'User-profile/user-profile-regular.html', context)
