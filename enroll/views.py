from django.shortcuts import render,HttpResponseRedirect
from .form import StudentRegistration
from .models import User
# Create your views here.

# this function will show and add data

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm,email = em,password = pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

# This function will delete data from the database

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This function will edit data from the database
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)


    return render(request,'enroll/updatestudent.html',{'form':fm})