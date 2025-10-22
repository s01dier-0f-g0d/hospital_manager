# Create your views here.
from .models import Patient
from .forms import PatientForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q

def home(request):
    # form=PatientForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request,'Patient data Created')
    #     return redirect('display')
    return render(request, 'home.html')


def create(request):
    form=PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Patient data created successfully')
        return redirect('display')
    return render(request,'create.html',{'form':form})

def display(request):
    search = request.GET.get('q')
    if search:
        data=Patient.objects.filter(
            Q(name__icontains=search) |
            Q(doctor_assigned__icontains=search) |
            Q(room_number__icontains=search) |
            Q(age__icontains=search) |
            Q(disease__icontains=search)
        )
    else:
        data = Patient.objects.all()
    return render(request,'display.html',{'data':data})

def update(request,key):
    data = get_object_or_404(Patient, id=key)
    form = PatientForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,'Patient data has been Modified')
        return redirect('display')
    return render(request,'update.html',{'form':form})

def deletePatient(request,key):
    data=get_object_or_404(Patient, id=key)
    if request.method =='POST':
        data.delete()
        messages.success(request,'Patient data Deleted')
        return redirect('display')
    return render(request,'remove.html',{'data':data})

