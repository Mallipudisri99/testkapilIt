from django.shortcuts import render, get_object_or_404
from student.models import Contact,Profile,Video
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q

from django.conf import settings

def index(request):
    
    return render(request,'index.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")
        
        obj = Contact(name=name, email=em, subject=sub, message=msz)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"

    return render(request,'contact.html', context)

def about(request):
    return render(request,'about.html')


def register(request):
    context = {}
    if request.method == "POST":
        # Fetch data from html form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        contact = request.POST.get('number')
        check = User.objects.filter(username=email)
        
        if len(check) == 0:
            # Save data to both tables
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()

            profile = Profile(user=usr, contact_number=contact)
            profile.save()
            
            context['status'] = f"User {name} Registered Successfully!"
            return render(request, 'reg-success.html', context)
        else:
            context['error'] = f"A User with this email already exists"

    return render(request, 'register.html', context)

def check_user_exists(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Exist'})
    else:
        return JsonResponse({'status':1,'message':'A user with this email already exists!'})

def signin(request):
    context={}
    if request.method=="POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')

        check_user = authenticate(username=email, password=passw)
        if check_user:
            login(request, check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/dashboard2')
            return HttpResponseRedirect('/dashboard')
        else:
            context.update({'message':'Invalid Login Details!','class':'alert-danger'})

    return render(request,'login.html', context)

def dashboard(request):
    context={}
    login_user = get_object_or_404(User, id = request.user.id)
    #fetch login user's details
    profile = Profile.objects.get(user__id=request.user.id)
    context['profile'] = profile

    #update profile
    if "update_profile" in request.POST:
        print("file=",request.FILES)
        name = request.POST.get('name')
        contact = request.POST.get('contact_number')
        add = request.POST.get('address')
       

        profile.user.first_name = name 
        profile.user.save()
        profile.contact_number = contact 
        profile.address = add 

        if "profile_pic" in request.FILES:
            pic = request.FILES['profile_pic']
            profile.profile_pic = pic
        profile.save()
        context['status'] = 'Profile updated successfully!'
    
    #Change Password 
    if "change_pass" in request.POST:
        c_password = request.POST.get('current_password')
        n_password = request.POST.get('new_password')

        check = login_user.check_password(c_password)
        if check==True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context['status'] = 'Password Updated Successfully!' 
        else:
            context['status'] = 'Current Password Incorrect!'

    return render(request, 'dashboard.html', context)

def dashboard2(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
   
    
    return render(request, "dashboard2.html",context)

# def videoDetail(request, video_id):
#     # Get the video object or return a 404 error if not found
#     video = get_object_or_404(Video, id=video_id)

#     # Get similar videos (example: videos by the same user)
#     similar_videos = Video.objects.filter(
#         Q(user=video.user) & ~Q(id=video.id)
#     )[:3]  # Adjust this query based on your criteria for similarity

#     context = {
#         'video': video,
#         'similar_videos': similar_videos,
#     }

#     return render(request, 'videoplayer.html', context)

# def video_get(request):
#     if request.method=="GET":
#         uid = request.GET.get('uid')
#         print(uid)
#         if uid:
#             return uid
#     return render(request, 'dashboard2.html')


def videoDetail(request ):
    if request.method =="GET":
     uid=request.GET.get("uid")
     videos = Video.objects.get(id=uid)
     context = {
        'videos': videos,
    }
     return render(request, 'videoplayer.html', context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

