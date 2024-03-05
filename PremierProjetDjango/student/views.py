
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
#Ajouter et afficher les infos d'un étudiant
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name = nm,email=em,password=pw)
            reg.save()
            fm= StudentRegistration()
    else:
        fm=StudentRegistration()
    stud= User.objects.all()
    return render(request,'student/addandshow.html',{'form':fm, 'stu':stud})


#Modifier les informations
def update_data(request, id):
    pi = User.objects.get(pk=id)  
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')  
    
    else:
        fm = StudentRegistration(instance=pi)
    return render(request, 'student/updatestudent.html', {'form': fm})


#Supprimer les données d'un étudiant 

def delete_data(request,id):
    if request.method== 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')