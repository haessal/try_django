from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def hello(request):
    context = {'user':request.user}
    return render(request, 'hello.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')