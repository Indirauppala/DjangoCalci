from django.shortcuts import render

# Create your views here.
def calculate(request):
    if request.method=="POST":
        value1=int(request.POST.get('num1'))
        value2=int(request.POST.get('num2'))
        operator=request.POST.get('oper')
        result=None
        if operator=="+":
            result=value1+value2
        elif operator=="-":
            result=value1-value2
        elif operator=="*":
            result=value1*value2
        elif operator=="/":
            result=value1//value2
        elif operator=="%":
            result=value1%value2
        else:
            result="operator not found"
        context={'result':result}
        return render(request,'calci.html',context)
    else:
        return render(request,'calci.html')
