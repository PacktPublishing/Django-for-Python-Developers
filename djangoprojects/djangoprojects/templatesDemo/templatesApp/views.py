from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict={"name":"Bharath"}
    return render(request,'templatesApp/firstTemplate.html',context=myDict)

def renderEmployee(request):
    myDict={"id":123,"name":"John","sal":10000}
    return render(request,'templatesApp/employeeTemplate.html',myDict)
