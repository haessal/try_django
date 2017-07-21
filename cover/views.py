from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def hello(request):
    context = {'user':'hoge'}
    return render(request, 'hello.html', context)
