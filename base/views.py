# Create your views here.
from .models import Patient, Disease
from .forms import PatientForm , DiseaseForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

def home(request):
    return render(request, 'home.html')


def create(request):
    form=PatientForm(request.POST , request.FILES)
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
        data = Patient.objects.filter(is_deleted = False)
    return render(request,'display.html',{'data':data})

def update(request,key):
    data = get_object_or_404(Patient, id=key)
    if request.method =='POST':
        form = PatientForm(request.POST , request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Patient data has been Modified')
            return redirect('display')
    else:
        form = PatientForm(instance=data)
    return render(request,'update.html',{'form':form})

def deletePatient(request,key):
    data=get_object_or_404(Patient, id=key)
    if request.method == 'POST':
        data.is_deleted=True #data.delete() deletes data permanently
        data.deleted_at=timezone.now()
        data.save()
        messages.success(request,'Patient data Deleted')
        return redirect('display')
    return render(request,'remove.html',{'data':data})

#Create Disease
def create_disease(request):
    form= DiseaseForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Disease Created Successfully')
        return redirect('read_disease')
    return render(request, 'create_disease.html', {'form': form})

#Read Disease
def read_disease(request):
    search=request.GET.get('q')
    if search:
        data=Disease.objects.filter(
            Q(name__icontains=search)|
            Q(symptoms__icontains=search)|
            Q(treatment__icontains=search)
        )
    else:
        data=Disease.objects.all()
    return render(request, 'read_disease.html',{'data':data, 'search':search})

#Update Disease
def update_disease(request, key):
    data = get_object_or_404(Disease, id=key)
    if request.method=='POST':  
        form = DiseaseForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Disease Updated Successfully')
            return redirect('read_disease')
    else:
        form=DiseaseForm(instance=data)
    return render(request,'update_disease.html',{'form': form})

#Delete Disease
def delete_disease(request, key):
    data = get_object_or_404(Disease, id=key)
    if request.method == 'POST':
        data.delete()
        messages.success(request,'Disease Deleted Successfully')
        return redirect('read_disease')
    return render(request, 'delete_disease.html', {'data': data})

#History
def history(request):
    search=request.GET.get('q')
    if search:
        data= Patient.objects.filter(
            Q(title__icontains=search)|
            Q(desc__icontains=search)|
            Q(genre__icontains=search) 
        )
    else:
        data=Patient.objects.filter(is_deleted=True)
    return render(request,'history.html',{'data':data})

#Restore
def restore(request, key):
    data=get_object_or_404(Patient, id=key, is_deleted=True)
    if request.method=='POST':
        data.is_deleted=False
        data.deleted_at=None
        data.save()
        messages.success(request, "Patient Restored Successfully")
        return redirect('history')
    return render(request, 'restore.html', {'data':data})