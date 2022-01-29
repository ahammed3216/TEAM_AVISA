from django.contrib.auth import authenticate, login,logout
from .models import Bussiness, Jobs, Notification, Profile
from django.shortcuts import redirect, render
from .forms import NotificationForm, ProfileForm,LoginForm, RegisterForm,JobForm, User,BussinessForm
# Create your views here.


def profileFormView(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        form=ProfileForm(request.POST ,request.FILES)
        profile=Profile()
        if form.is_valid():
            
            print(form.cleaned_data)
            first_name=form.cleaned_data.get('first_name')
            second_name=form.cleaned_data.get('second_name')
            address=form.cleaned_data.get('address')
            phone_no=form.cleaned_data.get('phonenumber')
            ward=form.cleaned_data.get('ward')
            panchayath=form.cleaned_data.get('panchayath')
            email=form.cleaned_data.get('email')
            house_no=form.cleaned_data.get('house_no')
            image=form.cleaned_data.get('image')


        
            profile.first_name=first_name
            profile.second_name=second_name
            profile.address=address
            profile.phonenumber=phone_no
            profile.ward=ward
            profile.panchayath=panchayath
            profile.email=email
            profile.house_no=house_no
            profile.image=image
            profile.user=request.user
            profile.save()

            return redirect('/')
        
        print(form.errors)
        context={
            'form':form,
        }
        return render(request,"profileform.html",context)


    else:
        return redirect('/login')

def home(request):
    return render(request,"home1.html")


def Register(request):
    form=RegisterForm(request.POST or None)
    print(form.errors)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password1=form.cleaned_data.get('password1')
        password2=form.cleaned_data.get('password2')

        user=User.objects.create_user(username,email,password2)

        user.save()

        return redirect('/login')
    

    return render(request,'register.html',context={'form':form})


def LoginView(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        
        user=authenticate(username=username,password=password)
        login(request,user)
        user=User.objects.get(username=username)
        email=user.email
        print(user.is_authenticated)   
        print(email)

        return redirect('/profileform')

    return render (request,"login.html",context={'form':form})



def logoutview(request):
    
    logout(request)
    print(request.user.is_authenticated)
    print("h")
    return redirect('/')


def profileView(request):
    profiles=Profile.objects.all()
    context={
        'profiles':profiles,
    }
    return render(request,"profile_views.html",context)

def JobFormView(request):
    form=JobForm(request.POST ,request.FILES)
    print("hau")
    if form.is_valid():
        
        print(form.cleaned_data)
        jobname=form.cleaned_data.get('jobname')
        location=form.cleaned_data.get('location')
        phonenumber=form.cleaned_data.get('phonenumber')
        employee_name=form.cleaned_data.get('employee_name')
        email=form.cleaned_data.get('email')
        image=form.cleaned_data.get('image')
        description=form.cleaned_data.get('description')


        job=Jobs(
            jobname=jobname,
            location=location,
            phonenumber=phonenumber,
            employee_name=employee_name,
            email=email,
            image=image,
            description=description

        )
        job.user=request.user

        job.save()

        return redirect('/')

    print(form.errors)
       

    return render(request,"jobform.html",{'form':form})


def JobView(request):
    jobs=Jobs.objects.all()
    return render(request,"jobview.html",{'jobs':jobs})


def BussinessFormView(request):
    form=BussinessForm(request.POST,request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        owner_name=form.cleaned_data.get('owner_name')
        bussiness_name=form.cleaned_data.get('bussiness_name')
        description=form.cleaned_data.get('description')
        image=form.cleaned_data.get('image')
        location=form.cleaned_data.get('location')
        type=form.cleaned_data.get('sector')
        phonenumber=form.cleaned_data.get('phonenumber')

        bussiness=Bussiness(
            owner_name=owner_name,
            bussiness_name=bussiness_name,
            description=description,
            image=image,
            location=location,
            type=type,
            phonenumber=phonenumber
        )


        
        bussiness.user=request.user
        bussiness.save()

        return redirect('/')
    print(form.errors)

    return render(request,"bussiness_form.html",{'form':form})



def BussinessView(request):
    bs_q=Bussiness.objects.all()
    return render(request,"bussiness_view.html",{'items':bs_q})




def NotificationFormView(request):
    form=NotificationForm(request.POST ,request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        text=form.cleaned_data.get('text')
        subject=form.cleaned_data.get('subject')
        image=form.cleaned_data.get('image')

        notification=Notification(
            text=text,
            subject=subject,
            image=image
        )
        notification.user=request.user

        notification.save()

        return redirect('/')
    
    return render(request,"notification.html",{'form':form})





def NotificationView(request):
    not_qs=Notification.objects.all()
    context={
        'items':not_qs
    }
    return render(request,"notification_view.html",context)



def profile_single(request):
    profile=Profile.objects.get(user=request.user)
    jobs=Jobs.objects.filter(user=request.user)
    items=Bussiness.objects.filter(user=request.user)
    context={
        'jobs':jobs,
        'profile':profile,
        'items':items
    }
    return render(request,"profile_new.html",context)