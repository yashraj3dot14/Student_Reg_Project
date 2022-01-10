from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_form, name= 'student_form_render'),
    path('studlist/',views.student_list, name= 'student_list'),
    path('<int:id>/',views.student_form, name= 'student_update'),
    path('delete/<int:id>/',views.student_delete, name= 'student_delete'),
    path('search',views.search, name='student_search'),
]