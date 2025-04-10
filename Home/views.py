from django.shortcuts import render,redirect
from .forms import UserAddForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .decorators import admin_only
from predict.models import Question,Datamodel
from Teacher.models import ChatContent
from .models import Parent_Student_Relation


@admin_only
def Index(request):
    chat = ChatContent.objects.all()
    print(len(chat), "......................")
    context = {
        "chat":chat
    }
    return render(request,"index.html",context)

def AdminHome(request):
    question = Question.objects.all()
    users = User.objects.all()
    context = {
        "question":question,
        "users":users,
    }
    return render(request,"adminhome.html",context)

def TeacherHome(request):
    data = Datamodel.objects.all()
    chat = ChatContent.objects.all()
    context = {
        "data":data,
        "chat":chat
    }
    return render(request,"teacherindex.html",context)

def ParentHome(request):
    relation = Parent_Student_Relation.objects.filter(parent = request.user)[0]
    student = relation.student

    data = Datamodel.objects.filter(user = student)
    print(data)
    
    context = {
        "data":data,
       
    }
    return render(request,"parenthome.html",context)

def TeacherDelete(request,pk):
    User.objects.get(id= pk).delete()
    messages.info(request,"teacher deleted success")
    return redirect('AdminHome')






def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                # group = Group.objects.get(name='user')
                # new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('SignIn')
            
    return render(request,"register.html",{"form":form})


def Parent_signup(request):
    form = UserAddForm()
    options = User.objects.filter(groups__name=None)
    if request.method == "POST":
        form = UserAddForm(request.POST)
        student = request.POST.get('student')

        try:
            student = User.objects.get(id = student)
        except:
            messages.info(request,"Student Not Found")
            return redirect('Parent_signup')

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('Parent_signup')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('Parent_signup')
            else:
                new_user = form.save()
                new_user.save()
                
                group = Group.objects.get(name='parent')
                new_user.groups.add(group) 

                try:
                    relation = Parent_Student_Relation.objects.create(parent = new_user,student = student)
                    relation.save()
                except:
                    new_user.delete()
                    messages.info(request,"Relation Not Created. This Student Already Has A Parent")
                    return redirect('Parent_signup')

                
                messages.success(request,"Parent Created")
                return redirect('SignIn')
            
    return render(request,"register_parent.html",{"form":form,"options":options})

def AddTeacher(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('AdminHome')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('AdminHome')
            else:
                new_user = form.save()
                new_user.save()
                
                group = Group.objects.get(name='teacher')
                new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('AdminHome')
            
    return render(request,"adminaddeacher.html",{"form":form})
    

def SignOut(request):
    logout(request)
    return redirect('Index')




