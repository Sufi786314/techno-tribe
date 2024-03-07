from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from app.models import Employee,MaterialIn,MaterialOut
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib  import messages
import geocoder
import folium

latitude = 19.0537315
longitude = 72.9106087
college_address = [latitude,longitude]
# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        # --
        if not user.exists():
            messages.error(request,'Username Does not exists')
            return redirect('login')
        # if user.exists():
        #     messages.error(request,'Username Already exists')
        #     return redirect('login')
        user=authenticate(username=username,password=password)
        
        if user is None:
            messages.error(request,'Wrong Password')
            return redirect('login')
        else:
            login(request ,user)
            return redirect("home")

    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'Username Already exists')
            return redirect('register')
        user = User.objects.create(
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.success(request,'Account created successfully')
        return redirect('register')

    return render(request,'register.html')


# @login_required(login_url='login')
def index(request):
    if request.GET.get('search_materials'):
        # print(request.GET.get('search_materials'))
        queryset = queryset.filter(part_name__icontains = request.GET.get('search'))
    return render(request,'index.html')


# @login_required(login_url='login')
def about(request):
    if request.GET.get('search_materials'):
        # print(request.GET.get('search_materials'))
        queryset = queryset.filter(part_name__icontains = request.GET.get('search'))
    return render(request,'about.html')


# @login_required(login_url='login')
def services(request):
    if request.GET.get('search_materials'):
        # print(request.GET.get('search_materials'))
        queryset = queryset.filter(part_name__icontains = request.GET.get('search'))
    return render(request,'services.html')


# @login_required(login_url='login')
def contact(request):
    if request.GET.get('search_materials'):
        # print(request.GET.get('search_materials'))
        queryset = queryset.filter(part_name__icontains = request.GET.get('search'))
    return render(request,'contact.html')


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
# def materialin(request):
#     if request.method=="POST":
#         data = request.POST
#         part_name = request.POST.get('part_name')
#         date_of_receiving = request.POST.get('date_of_receiving')
#         quantity = request.POST.get('quantity')
#         w_o_n_o = request.POST.get('w_o_n_o')
#         challan = request.FILES.get('challan')

#         MaterialIn.objects.create(
#         part_name = part_name,
#         date_of_receiving = date_of_receiving,
#         quantity = quantity,
#         w_o_n_o = w_o_n_o,
#         challan = challan,
#         )
#         return redirect('materialin')
#     queryset = MaterialIn.objects.all()
#     if request.GET.get('search_materials'):
#         # print(request.GET.get('search_materials'))
#         queryset = queryset.filter(part_name__icontains = request.GET.get('search_materials'))
 

#     context = {'materialIn':queryset}
#     return render(request,'materialin.html',context)


# @login_required(login_url='login')
# def delete_materials(request,id):
#     queryset = MaterialIn.objects.get(id=id)
#     queryset.delete()
#     # print(id)
#     return redirect('/materialin/')
#     # return HttpResponse('a')

# @login_required(login_url='login')
# def update_materials(request,id):
#     queryset = MaterialIn.objects.get(id=id)
#     if request.method=="POST":
#         data = request.POST
#         part_name = request.POST.get('part_name')
#         date_of_receiving = request.POST.get('date_of_receiving')
#         quantity = request.POST.get('quantity')
#         w_o_n_o = request.POST.get('w_o_n_o')
#         challan = request.FILES.get('challan')

#         queryset.part_name = part_name
#         queryset.date_of_receiving = date_of_receiving
#         queryset.w_o_n_o = w_o_n_o
#         queryset.quantity = quantity

#         if challan:
#             queryset.challan = challan  
#         queryset.save()
#         return redirect('/materialin/')
#     context = {'materials':queryset}
#     return render(request,'update_materials.html',context)

# # ------------------------------------------------------------------------
# @login_required(login_url='login')
# def materialout(request):
#     if request.method=="POST":
#         data = request.POST
#         part_name = request.POST.get('part_name')
#         date_of_receiving = request.POST.get('date_of_receiving')
#         quantity = request.POST.get('quantity')
#         w_o_n_o = request.POST.get('w_o_n_o')
#         challan = request.FILES.get('challan')

#         MaterialOut.objects.create(
#         part_name = part_name,
#         date_of_receiving = date_of_receiving,
#         quantity = quantity,
#         w_o_n_o = w_o_n_o,
#         challan = challan,
#         )
#         return redirect('materialout')
#     queryset = MaterialOut.objects.all()

#     if request.GET.get('search_materials'):
#         # print(request.GET.get('search_materials'))
#         queryset = queryset.filter(part_name__icontains = request.GET.get('search_materials'))
 

#     context = {'materialOut':queryset}
#     return render(request,'materialout.html',context)

# # ------------------------------------------------------------------
# @login_required(login_url='login')
# def update_materials(request,id):
#     queryset = MaterialOut.objects.get(id=id)
#     if request.method=="POST":
#         data = request.POST
#         part_name = request.POST.get('part_name')
#         date_of_receiving = request.POST.get('date_of_receiving')
#         quantity = request.POST.get('quantity')
#         w_o_n_o = request.POST.get('w_o_n_o')
#         challan = request.FILES.get('challan')

#         queryset.part_name = part_name
#         queryset.date_of_receiving = date_of_receiving
#         queryset.w_o_n_o = w_o_n_o
#         queryset.quantity = quantity

#         if challan:
#             queryset.challan = challan  
#         queryset.save()
#         return redirect('/materialout/')
#     context = {'materials':queryset}
#     return render(request,'update_materialsout.html',context)

def teacher(request):
    return render(request,'teacher.html')

def stats(request):
    return render(request,'report1.html')

# views.py

from django.shortcuts import render
import geocoder
import folium
from django.http import HttpResponse

from django.shortcuts import render

def map_view(request):
    g=geocoder.ip("me")
    myaddress = g.latlng
    markers = [
        {myaddress},  # Example marker 1 (New York City)
        {'latitude': 34.0522, 'longitude': -118.2437},  # Example marker 2 (Los Angeles)
        # Add more markers as needed
    ]
    return render(request, 'map.html', {'markers':markers})

def student(request):
    return render(request,'studentprofile.html')

from django.shortcuts import render
from django.http import JsonResponse
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def attendance(request):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("")
    student_address= location.latitude,location.longitude
    # print(student_address)
    # Get college location from the database
    college_location = college_address
    # CollegeLocation.objects.first()  # Assuming there's only one college location stored
    
    # Calculate distance between student's location and college location
    student_location = (student_address)
    college_location = (college_location[0] ,college_location[1])
    distance = geodesic(student_location, college_location).kilometers
    # print(distance)
    # Define threshold (in kilometers)
    threshold = 0.5  # Adjust as needed
    
    # Check if student is within college premises
    if distance <= threshold:
        # Mark student's attendance as present
        # Add your attendance marking logic here
        attendance_status = "Present"
        print("Present")
    else:
        # Mark student's attendance as absent
        # Add your attendance marking logic here
        attendance_status = "Absent"
        print("Absent")
    
    # Return JSON response with attendance status
    return JsonResponse({'status': attendance_status})
