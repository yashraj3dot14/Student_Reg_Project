from django import forms
from .models import StudentInfo,StudentAcademic

class StudentInfoForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = '__all__'

class StudentAcademicForm(forms.ModelForm):

    class Meta:
        model = StudentAcademic
        fields = ['student','maths', 'physics', 'chemistry', 'biology', 'english']

    def __init__(self, *args, **kwargs):
        super(StudentAcademicForm, self).__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Select RollNo'