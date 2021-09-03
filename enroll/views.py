from django.forms.widgets import PasswordInput
from enroll.models import User
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.


#this Function will add new item and show all items.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # after fm.is_valid() and fm.save() our form will start submitting our data into our data base
        # if fm.is_valid(): 
        #     fm.save()

                #or

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()

            #if we want to show the blank field after submitting 
            #after running the above code and submitting then this fm will be passed in the form into the dictionary {'form':fm}
            #then this fm will be shown in the templates
            # fm = StudentRegistration()
        
    else:
        # else part generate then blank form
        fm = StudentRegistration()
        
    #this User.object.all() function contain all the data of our model or table
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm ,'stu':stud})


#This Function Will Update/Edit
def update_data(request,id):
    # return render(request,'enroll/updatestudent.html',{'id':id}) just for checking that what happen when we click to edit button

    #after triggering this function it will first show the udpatestudent.html templates
    #This all will run when we click update button under the updatestudent.html
    if request.method == 'POST':
        # it will give us all the data of the provided primary key.
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    
    return render(request, 'enroll/updatestudent.html',{'form':fm})


#This Function Will Delete
def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id) #it will give us all the data of the provided primary key.
        pi.delete()
        return HttpResponseRedirect('/')

