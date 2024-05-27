from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate,login

# Create your views here.
#def homeindex(request):
 #   if request.user.is_authenticated:
 #       return render(request, 'htmlfile/index.html')
  #  else:
  #      return render(request, 'htmlfile/login.html')  

#def login_view(request):
 #   user = ''
 #   if request.method == "POST":
   #     username = request.POST['username']
   #     pwd = request.POST['password']
    #    print("hi::")
     #   user = authenticate(username=username, password=pwd)
     #   print(user)
      #  if user is not None:
      #      login(request,user)
      #      return redirect('home')
      #  else:
      #      return render(request, 'htmlfile/login.html', {'error': 'Invalid'})
        
   #if user is not None:
   #     return redirect('home')    
   # else:
    #    return render(request, 'htmlfile/login.html')  
    
def resetpwd(request):
    if request.method == "POST":    
        nepassword = request.POST['npassword']
        conpassword= request.POST['copassword']
        reset = authenticate(npassword=nepassword, copassword=conpassword)
        print(reset)
        if reset is not None:
            resetpwd(request,reset)
            return redirect('login')
        else:
            return render(request, 'htmlfile/resetpwd.html', {'error': 'Invalid'})
    return render(request, 'htmlfile/resetpwd.html')    

def register(request):
    return render(request, 'htmlfile/registration.html')
 