from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.



def registeruser(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            # user=form.save(commit=False)
            # user.role=2
            # user.set_password(form.cleaned_data['password']) #one way to save password in hash  encrypted form
            # user.save()
            # form.save()

            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            # print("User Created")
            messages.success(request,'User Created Successfully')
            return redirect('registeruser')
        else:
            print('invalid form')
            print(form.errors)

    else:
        form=UserForm()

    context={
        'form':form

    }
    return render(request,'accounts/registeruser.html',context)
