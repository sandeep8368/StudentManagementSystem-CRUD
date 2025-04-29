from django.shortcuts import redirect, render
from myapp.models import StudentModel



def display_all(request):
    display_data = StudentModel.objects.all()
    return render(request, 'html/display.html', {"data":display_data})



def add_record(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass')
        StudentModel.objects.create(
            name= name,
            email = email,
            phone = int(phone),
            password = int(password) 
        )
    return render(request, 'html/add.html')



def update_view(request,id):
    student = StudentModel.objects.get(id=id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.password = request.POST.get('pass')
        
        student.save()
        
        return redirect('dis')
    return render(request, 'html/update.html' ,{'student':student})





def delete_view(request,id):
    student = StudentModel.objects.get(id=id)
    student.delete()
    return redirect('dis')


