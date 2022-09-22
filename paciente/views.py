from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from paciente.forms import pacienteForm  
from paciente.models import paciente  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = pacienteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = pacienteForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    pacientes = paciente.objects.all()  
    return render(request,"show.html",{'pacientes':pacientes})  
def edit(request, id):  
    paciente = paciente.objects.get(id=id)  
    return render(request,'edit.html', {'paciente':paciente})  
def update(request, id):  
    paciente = paciente.objects.get(id=id)  
    form = pacienteForm(request.POST, instance = paciente)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'paciente': paciente})  
def destroy(request, id):  
    paciente = paciente.objects.get(id=id)  
    paciente.delete()  
    return redirect("/show")  