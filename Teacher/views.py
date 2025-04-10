from django.shortcuts import render,redirect
from predict.models import Datamodel
from .froms import BookAddForm, SuggestionForm
from .models import Recomendations, Books, ChatContent
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
    else:
        pygrade = "E"


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
        chgrade = "E"
            
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
    else:
        magrade = "E"
            
       
    
    context = {
        "data":data
    }
    
    context["pygrade"] = pygrade
    context["magrade"] = magrade
    context["chgrade"] = chgrade
    
    return render(request,"studentsingleview.html",context)




def StudentDeatilsViewParent(request,pk):
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
    else:
        pygrade = "E"


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
        chgrade = "E"
            
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
    else:
        magrade = "E"
            
       
    
    context = {
        "data":data
    }
    
    context["pygrade"] = pygrade
    context["magrade"] = magrade
    context["chgrade"] = chgrade
    
    return render(request,"studentsingleview_parent.html",context)



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


def ChatAdd(request):
    if request.method == "POST":
        chat = request.POST["chat"]
        chatdata = ChatContent.objects.create(message = chat, user = request.user)
        chatdata.save()
        return redirect("Index")
    return redirect("Index")



from predict.models import Examination, mark_exams
from predict.forms import ExaminationForm, MarkExamsForm
from django.contrib.auth.models import User
from Home.models import Parent_Student_Relation

def add_exam(request):
    exams = Examination.objects.all()
    form = ExaminationForm()
    if request.method == "POST":
        form = ExaminationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Exam Added")
            return redirect("add_exam")
    context = {
        "form":form,
        "exams":exams
    }
    return render(request,"add_exam.html",context)


def add_marks_to_students(request):
    students = User.objects.filter(groups__name=None)

    context = {
        "students":students
    }
    return render(request,"add_marks_to_students.html",context)

def add_marks(request, student_id):
    student = User.objects.get(id=student_id)
    marks = mark_exams.objects.filter(user=student)
    form = MarkExamsForm()
    if request.method == "POST":
        form = MarkExamsForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.user = student
            formdata.save()
            messages.info(request,"Marks Added")
            return redirect('add_marks', student_id=student_id)
        else:
            messages.error(request, "Error adding marks. Please check the form.")
            return redirect('add_marks', student_id=student_id)
    
    context = {
        "student": student,
        "form": form,
        "marks":marks
    }
    return render(request, "add_marks.html", context)


def view_marks_parent(request):
    relations = Parent_Student_Relation.objects.filter(parent=request.user)[0]
    students = relations.student
    marks = mark_exams.objects.filter(user=students)

    context = {
        "marks": marks,
        "students": students
    }

    return render(request,"view_marks_parent.html",context)


def Mymarks(request):
    marks = mark_exams.objects.filter(user=request.user)
    context = {
        "marks": marks
    }
    return render(request,"mymarks.html",context)