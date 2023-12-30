from django.shortcuts import render,redirect
from predict.models import Datamodel
from .froms import BookAddForm, SuggestionForm
from .models import Recomendations, Books
from django.contrib import messages

# Create your views here.

def StudentDeatilsView(request,pk):
    data = Datamodel.objects.get(id = pk)
    if data.physics_10 <=20:
        pygrade = "E"
    elif data.physics_10 <= 29 and data.physics_10 >20:
        pygrade = "D"
    elif data.physics_10 <= 39 and data.physics_10 >=30:
        pygrade = "D+"
    elif data.physics_10 <= 49 and data.physics_10 >40:
        pygrade = "C"
    elif data.physics_10 <= 59 and data.physics_10 >50:
        pygrade = "C+"
    elif data.physics_10 <= 69 and data.physics_10 >60:
        pygrade = "B"
    elif data.physics_10 <= 79 and data.physics_10 >79:
        pygrade = "B+"
    elif data.physics_10 <= 89 and data.physics_10 >80:
        pygrade = "A"
    elif data.physics_10 <= 100 and data.physics_10 >90:
        pygrade = "A+"
        
    if data.chemistry_10 <=20:
        chgrade = "E"
    elif data.chemistry_10 <= 29 and data.chemistry_10 >20:
        chgrade = "D"
    elif data.chemistry_10 <= 39 and data.chemistry_10 >=30:
        chgrade = "D+"
    elif data.chemistry_10 <= 49 and data.chemistry_10 >40:
        chgrade = "C"
    elif data.chemistry_10 <= 59 and data.chemistry_10 >50:
        chgrade = "C+"
    elif data.chemistry_10 <= 69 and data.chemistry_10 >60:
        chgrade = "B"
    elif data.chemistry_10 <= 79 and data.chemistry_10 >70:
        chgrade = "B+"
    elif data.chemistry_10 <= 89 and data.chemistry_10 >80:
        chgrade = "A"
    elif data.chemistry_10 <= 100 and data.chemistry_10 >90:
        chgrade = "A+"
    else:
        chgrade = None
            
    if data.maths_10 <=20:
        magrade = "E"
    elif data.maths_10 <= 29 and data.maths_10 >20:
        magrade = "D"
    elif data.maths_10 <= 39 and data.maths_10 >=30:
        magrade = "D+"
    elif data.maths_10 <= 49 and data.maths_10 >40:
        magrade = "C"
    elif data.maths_10 <= 59 and data.maths_10 >50:
        magrade = "C+"
    elif data.maths_10 <= 69 and data.maths_10 >60:
        magrade = "B"
    elif data.maths_10 <= 79 and data.maths_10 >79:
        magrade = "B+"
    elif data.maths_10 <= 89 and data.maths_10 >80:
        magrade = "A"
    elif data.maths_10 <= 100 and data.maths_10 >90:
        magrade = "A+"
            
       
    
    context = {
        "data":data
    }
    
    context["pygrade"] = pygrade
    context["magrade"] = magrade
    context["chgrade"] = chgrade
    
    return render(request,"studentsingleview.html",context)

def GiveSuggestions(request,pk):
    data = Datamodel.objects.get(id = pk)
    Previreco = Recomendations.objects.filter(student = data.user).order_by("-id")
    form  = SuggestionForm()
        
        
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            formdata = form.save()
            formdata.save()
            formdata.student = data.user
            formdata.Teacher = request.user.first_name
            formdata.save()
            messages.info(request,"Instractions Reported")
            return redirect('GiveSuggestions',pk = pk)
            
    context = {
        "form":form,
        'data':data,
        "prevreco":Previreco
    }
    return render(request,"suggestionbox.html",context)

def DeleteRecommentation(request,pk):
    Recomendations.objects.get(id = pk).delete()
    return redirect("TeacherHome")
    

def Addbook(request):
    books = Books.objects.filter(creator = request.user)
    form = BookAddForm()
    if request.method == "POST":
        form = BookAddForm(request.POST,request.FILES)
        if form.is_valid():
            formdata = form.save()
            formdata.save()
            formdata.creator = request.user
            formdata.save()
            messages.info(request,"Book Added To list")
            return redirect("Addbook")
    context = {
        "form":form,
        "books":books
    }
    return render(request,"bookaddteacher.html",context)

def DeleteBook(request,pk):
    Books.objects.get(id = pk).delete()
    messages.info(request,"Book Deleted")
    return redirect('Addbook')
    
def RecommendationsStudentView(request):
    Previreco = Recomendations.objects.filter(student = request.user).order_by("-id")
    context = {
        "prerec":Previreco
    }
    return render(request,"recommendations.html",context)

def LeaveRepaly(request,pk):
    rec = Recomendations.objects.get(id = pk)
    if request.method == "POST":
        replay = request.POST["reaply"]
        rec.student_Repaly = replay 
        rec.save()
        messages.info(request,"Replay Sent To teacher")
        return redirect(RecommendationsStudentView)
    return redirect(RecommendationsStudentView)
    
