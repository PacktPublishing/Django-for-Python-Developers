from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(ListView):
    model = Student
    #default template_name is student_list.html
    #default context_object_name is student_list

class StudentDetailView(DetailView):
    model = Student
    #default template_name is student_detail.html
    #default context_object_name is student

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName','lastName','testScore')

class StudentUpdateView(UpdateView):
    model = Student
    fields=('testScore',)

class StudentDeleteView(DeleteView):
    model = Student
    success_url=reverse_lazy('students')
