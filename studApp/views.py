from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentInfoForm,StudentAcademicForm
from .models import StudentInfo, StudentAcademic
from django.contrib import messages

# Create your views here.
def student_form(request, id= 0):
    if request.method == 'GET':
        if id == 0:
            form1 = StudentInfoForm()
            form2 = StudentAcademicForm()
        else:
            studentinfo = StudentInfo.objects.get(pk= id)
            studentacademic = StudentAcademic.objects.get(student_id= id) #student_id is foreign key
            form1 = StudentInfoForm(instance= studentinfo)
            form2 = StudentAcademicForm(instance= studentacademic)
        return render(request, 'studApp/student_form.html', {'form1': form1, 'form2': form2})
    else:
        if id == 0:
            #here we are distinguished two forms based on their butto name through if condition
            #studentInfo form
            if 'studentInfo' in request.POST: #name of button
                roll = request.POST['roll_no']
                #print('Roll from DB: ',StudentInfo.objects.filter(roll_no= roll))
                if StudentInfo.objects.filter(roll_no= roll):
                    #print('inside repeating roll no')
                    messages.error(request, 'Roll number already exist')
                    return redirect('student_form_render')

                form1 = StudentInfoForm(request.POST)
                #print('form: ',form1.is_valid())
                if form1.is_valid():
                    print('form is valid')
                    form1.save()
                return redirect('student_form_render')
            #return render(request, 'studApp/student_form.html')

            #studentAcademic form
            if 'studentAcademic' in request.POST:
                print('Request content:  ',request.POST)
                student_id = request.POST['student']
                if StudentAcademic.objects.filter(student_id= int(student_id)):
                    messages.error(request, 'Student marks is already inserted')
                    return redirect('student_form_render')

                form2 = StudentAcademicForm(request.POST)
                if form2.is_valid():
                    form2.save()
                return redirect('/students/studlist/')
        else:
            studentinfo = StudentInfo.objects.get(pk= id)
            studentacademic = StudentAcademic.objects.get(student_id= id)
            print('inside edit')
            if 'studentInfo' in request.POST:
                form1 = StudentInfoForm(request.POST, instance= studentinfo)
                #print('inside edit form1',form1.is_valid())
                if form1.is_valid():
                    form1.save()

            if 'studentAcademic' in request.POST:
                form2 = StudentAcademicForm(request.POST, instance=studentacademic)
                #print('inside edit form2', form2)
                if form2.is_valid():
                    print('inside edit form2')
                    form2.save()
        return redirect('/students/studlist/')



def student_list(request):
    students = StudentInfo.objects.all()
    academic = StudentAcademic.objects.all()
    return render(request, 'studApp/student_list.html',{'students':students, 'academic': academic})

def student_delete(request, id):
    studentinfo = StudentInfo.objects.get(pk= id)
    studentinfo.delete()
    return redirect('/students/studlist/')


def search(request):
    query = request.GET['student']
    students = StudentInfo.objects.filter(name__icontains= query)
    return render(request,'studApp/search.html',{'students': students})