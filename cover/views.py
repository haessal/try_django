from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {'user':'hoge'}
    return render(request, 'hello.html', context)
