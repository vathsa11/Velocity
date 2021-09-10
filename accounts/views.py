from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User, UserBusmapping,Busdetails,Conductor,Driver,Payment
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout
# Create your views here.
def studentregistration(request):
   if request.method == 'POST':
      username=request.POST['username']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      user_phone = request.POST['user_phone']
      Parent_Phone = request.POST['Parent_Phone']
      email=request.POST['email']
      Address_line=request.POST['Address_line']
      City=request.POST['City']
      State = request.POST['State']
      Branch=request.POST['Branch']
      password1= request.POST['password1']
      password2 = request.POST['password2']
      Pincode=request.POST['Pincode']


      if password1 == password2:
         if User.objects.filter(username=username).exists():
            messages.info(request,'username exists')
            return redirect('studentregistration')
         elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('studentregistration')
         else:
            user = User(username=username,first_name=first_name,last_name=last_name,user_phone=user_phone,Parent_Phone=Parent_Phone,email=email,Address_line=Address_line,City=City,State=State,Branch=Branch,password=password1,Pincode=Pincode)
            user.save()
            print('user created')
            return redirect('studentlogin')
      else:
         messages.info(request,"password not matching")
         return redirect('studentregistration')
      return redirect('/')

   else:
      return render(request,'studentregistration.html')


def studentlogin(request):
   if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
   
      user = authenticate(request, username=username , password=password)
      # user = student.objects.get_user(username)
      if user is not None:
         login(request, user)
         return redirect("/")
      else:
         messages.info(request,'invalid creditials')
         return redirect('studentlogin')

   else:
      return render(request,'studentlogin.html')


def profile(request):
   #person = {'firstname': 'pavan', 'lastname': 'kumar'}
   try:
      user = User.objects.filter(username=request.user)
      for u in user:
         bus_mapping = Payment.objects.filter(user_id=u.id)
         for bm in bus_mapping:
            print(bm.bus_number, bm.due_amount)
            bus_details = Payment.objects.filter(bus_number=bm.bus_number)
      profile = [
      {
            
      }]
      
      result = {
            'bus_number':bm.bus_number,
            'due_amount': bm.due_amount
         }
   
      return render(request,'profile.html',{'result':result})
   except Exception:
      redirect('/')
   return render(request,'profile.html')


def busfaculty(request):
   u = Driver.objects.all()
   c = Conductor.objects.all()
   return render(request,'busfaculty.html',{'data': u, 'result': c})


def busdetails(request):
   b = Busdetails.objects.all()
   return render(request,'busdetails.html',{'data': b})

def logout(request):
   django_logout(request)
   return redirect('/')

# Create your views here.
def index(request):
   return render(request,'index.html')

def announcements(request):
   return render(request,'announcements.html')

def about(request):
   return render(request,'about.html')


def simplecheckout(request):
   return render(request,'simplecheckout.html')


def passwordreset(request):
   return render(request,'passwordreset.html')


def passwordresetdone(request):
   return render(request,'passwordresetdone.html')

def passwordresetconfirm(request):
   return render(request,'passwordresetconfirm.html')

def passwordresetcomplete(request):
   return render(request,'passwordresetcomplete.html')

#def adminpage(request):
   #user = Busdetails.object.filter(bus_number=request.user)
   #for u in user:
      #bus_mapping = UserBusmapping.objects.filter(user_number=u.bus_number)
      #print(u.bus_mapping)

  