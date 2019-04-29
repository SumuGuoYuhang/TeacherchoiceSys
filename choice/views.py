from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, 'choice/login.html')

def loginSuccess(request):
    username = request.POST.get('username')
    userpassword = request.POST.get('userpassword')
    print(username)
    print(userpassword)
    if username == 'admin' and userpassword == 'admin':
        return render(request, 'choice/choose.html')

    else:
        return render(request, 'choice/login.html')

def choice(reqeust):
    pass