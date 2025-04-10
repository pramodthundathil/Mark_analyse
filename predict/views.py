from django.shortcuts import render, redirect
from .models import Datamodel, Question
from .forms import QuestinForm
from django.contrib import messages
from .prediction import model
import numpy as np


# Create your views here.
def MarkInput(request):
    if Datamodel.objects.filter(user = request.user).exists():
        messages.info(request,"You Already Given the Basic Datas Please Attend the aptitude test")
        return redirect("Aptitudetest")
    else:
        if request.method == "POST":
            name = request.POST["name"]
            gender = request.POST["gender"]
            bbranch = request.POST["bbranch"]
            py_10 = request.POST['py10']
            ch10 = request.POST['ch10']
            ma10 = request.POST["ma10"]
            py_12 = request.POST['py12']
            ch12 = request.POST['ch12']
            ma12 = request.POST['ma12']
            bsem1 = request.POST['bsem1']
            bsem2 = request.POST['bsem2'] 
            bsem3 = request.POST['bsem3'] 
            bsem4 = request.POST['bsem4']
            tmode = request.POST['tmode']
            stime = request.POST['stime']   
            data = Datamodel.objects.create(
                name=name,
                gender = gender,
                btech_branch = bbranch,
                physics_10 = float(py_10),
                chemistry_10 = float(ch10),
                maths_10 = float(ma10),
                physics_12 = py_12,
                chemistry_12 = ch12,
                maths_12 = ma12,
                btech_sem1 = bsem1,
                btech_sem2 = bsem2,
                btech_sem3 = bsem3,
                btech_sem4 = bsem4,
                mode_study = tmode,
                study_time = stime,
                user = request.user
                )
            data.save()
            messages.info(request,"Your Datas are Recorded Please Attend the aptitude test")
            return redirect("Aptitudetest")

        return render(request,'markinput.html')

def AddQuestion(request):
    form = QuestinForm()
    if request.method == "POST":
        if Question.objects.all().count() < 20:
            form = QuestinForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("AdminHome")
        else:
            messages.info(request,"Already have Ten Question Please delete one and try agine")
            return redirect("AddQuestion")
    return render(request,"addquestion.html",{"form":form})

def DeleteQuestion(request,pk):
    Question.objects.get(id = pk).delete()
    messages.info(request,"Question Deleted Success")
    return redirect("AdminHome")

def Aptitudetest(request):
    questions = Question.objects.all()
    if request.method == "POST":
        val = []
        mark = 0
        for i in questions:
            name = str(i.id)
            x = request.POST[name]
            if i.answer == x:
                mark += 0.5
            val.append(x)
        print(mark)
        try:
            dmodel = Datamodel.objects.get(user = request.user)
            dmodel.iq_marks = mark
            dmodel.save()
            messages.info(request,"Your Mark In IQ Test is {}".format(mark))
            return redirect('MarkProfile')
        except:
            messages.info(request,"Please Fill The form And attend IQ test for Proper Calculations")
            return redirect("MarkInput")
    context = {
        "questions":questions
    }
    return render(request,"aptitudetest.html",context)

def MarkProfile(request):
    context = {}
    try:
        data = Datamodel.objects.get(user = request.user)
        dmodel = Datamodel.objects.get(user = request.user)
        # btechtotalvalue = ((dmodel.btech_sem1+dmodel.btech_sem2+dmodel.btech_sem3+dmodel.btech_sem4)/3100 * 100)/12.5
        iqscore = dmodel.iq_marks/5
        # totalscorein10 = btechtotalvalue + iqscore
        timestudy  = dmodel.study_time
        tenth = (dmodel.physics_10 + dmodel.chemistry_10 + dmodel.maths_10)/3
        twelth = (dmodel.physics_12 + dmodel.chemistry_12 + dmodel.maths_12)/3
        # features = np.array([[timestudy, iqscore,tenth,twelth,9.2,8.2,8.6,7.4]])
        features = np.array([[timestudy, iqscore,tenth,twelth,dmodel.btech_sem1,dmodel.btech_sem2,dmodel.btech_sem3,dmodel.btech_sem4]])

        # features = np.array([[timestudy, totalscorein10]])
        print(model.predict(features))
        predict_value = model.predict(features)
        dmodel.prediction_result = float(predict_value)
        dmodel.save()
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
        else:
            magrade = "E"
            
        context["data"] = data
        context["pres"] = float(predict_value)
        context["pygrade"] = pygrade
        context["magrade"] = magrade
        context["chgrade"] = chgrade
        
        return render(request,"markprofile.html",context)
        
    except:
        messages.info(request,"Please Fill the form and attend the IQ test to view this Page")
        return redirect("MarkInput")
    
def PredictScore(request):
    dmodel = Datamodel.objects.get(user = request.user)
    # btechtotalvalue = ((dmodel.btech_sem1+dmodel.btech_sem2+dmodel.btech_sem3+dmodel.btech_sem4)/3100 * 100)/12.5
    iqscore = dmodel.iq_marks/5
    # totalscorein10 = btechtotalvalue + iqscore
    timestudy  = dmodel.study_time
    # features = np.array([[timestudy, totalscorein10]])
    # features = np.array([[10, 7,97,99,9.2,8.2,8.6,7.4]])
    tenth = (dmodel.physics_10 + dmodel.chemistry_10 + dmodel.maths_10)/3
    twelth = (dmodel.physics_12 + dmodel.chemistry_12 + dmodel.maths_12)/3
    features = np.array([[timestudy, iqscore,tenth,twelth,dmodel.btech_sem1,dmodel.btech_sem2,dmodel.btech_sem3,dmodel.btech_sem4]])

    
    print(model.predict(features))
    predict_value = model.predict(features)
    dmodel.prediction_result = float(predict_value)
    dmodel.save()
    
    return redirect('MarkProfile')
    