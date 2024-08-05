from django.shortcuts import render,redirect
from .models import Experience,ExperienceCategory,ExperienceImages,ExperienceIncluded,ExperienceFormsQ,ExperienceFormsA
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
# Create your views here.
# Pahado Se Front-Side
def home(request):
    dt=Experience.objects.all()[:2]
    dt2=Experience.objects.all()
    data= {'dt':dt,'dt2':dt2}
    return render(request,'index.html',data)

def Experiences(request):
    dt=ExperienceCategory.objects.all()
    data={'dt':dt}
    return render(request,'experiences.html',data)

def ECategory(request,name):
    EC=ExperienceCategory.objects.get(Category=name)
    dt=Experience.objects.filter(EC_id=EC.id)
    data={'dt':dt,'name':name}
    return render(request,'ec.html',data)

def ExperiencesDetails(request,Category,Name):
    ec=ExperienceCategory.objects.get(Category=Category)
    dt=Experience.objects.get(EC_id=ec.id,Name=Name)
    fm= ExperienceFormsQ.objects.filter(Name=Name).exists()
    EDI = ExperienceIncluded.objects.filter(E_id=dt.id)
    EIM = ExperienceImages.objects.filter(E_id=dt.id)
    data={'dt':dt,'ec':ec,'EDI':EDI,'EIM':EIM,'fm':fm}
    return render(request,'experiences-details.html',data)

def ExperiencesForm(request,name):
    fm= ExperienceFormsQ.objects.get(Name=name)
    dt=Experience.objects.get(id=fm.E_id)
    data={'fm':fm,'dt':dt}
    return render(request,'experiencesform.html',data)

def Stays(request):
    return render(request,'stays.html')

def About(request):
    return render(request,'about.html')

def Memories(request):
    return render(request,'memories.html')

def Blog(request):
    return redirect('/')
    # return render(request,'blog.html')

def Contact(request):
    return render(request,'contact.html')

def Login(request):
    return render(request,'login.html')

# Pahado Se Admin-Side
def Admin(request):
    return render(request,'admin/dashboard.html')

def AExperience(request):
    dt=Experience.objects.all()
    ec=ExperienceCategory.objects.all()
    data={'dt':dt,'ec':ec}
    return render(request,'admin/experiences.html',data)

def AddExperiences(request):
    dt=ExperienceCategory.objects.all()
    # ExperienceIncluded.objects.all().delete()
    data={'dt':dt}
    if request.method=="POST": 
        Categoryid=request.POST.get('Category')
        dt=ExperienceCategory.objects.get(id=Categoryid)
        Name=request.POST.get('Name')
        Image=request.FILES.get('Image')
        SmallDescription=request.POST.get('SmallDescription')
        Description=request.POST.get('Description')
        Address=request.POST.get('Address')
        Price=request.POST.get('Price')
        Days=request.POST.get('Days')
        Date=request.POST.get('Date')
        View=request.POST.get('View')
        dt=Experience.objects.create(EC_id=Categoryid,Category=dt.Category,Name=Name,Image=Image,SmallDescription=SmallDescription,Description=Description,Address=Address,Price=Price,Days=Days,Date=Date,View=View)
        dt.save()
        return redirect('/AExperience')
    return render(request,'admin/addexperiences.html',data)

@csrf_exempt
def IncludedCreate(request):
    if request.method == 'POST':
        E_id = request.POST.get('E_id')
        Types = request.POST.get('Types')
        Lines = request.POST.get('Lines')
        dt=ExperienceIncluded.objects.create(E_id=E_id,Types=Types,Lines=Lines)
        dt.save()
        return JsonResponse({'E_id':E_id,'Types':Types,'Lines':Lines})
    
def Category(request):
    dt=ExperienceCategory.objects.all()
    data={'dt':dt}
    return render(request,'admin/category.html',data)

def AddCategory(request):
    if request.method=="POST": 
        Category=request.POST.get('Category')
        Description=request.POST.get('Description')
        Image=request.FILES.get('Image')
        dt=ExperienceCategory.objects.create(Category=Category,Description=Description,Image=Image)
        dt.save()
        return redirect('/ExperienceCategory')
    return render(request,'admin/addcategory.html')

def CategoryDelete(request,id):
    dt=ExperienceCategory.objects.get(id=id)
    dt.delete()
    return redirect('/ExperienceCategory')


def ExperiencesDelete(request,id):
    dt=Experience.objects.get(id=id)
    dt.delete()
    return redirect('/AExperience')

def ExperiencesView(request,id):
    dt=Experience.objects.get(id=id)
    ec=ExperienceCategory.objects.get(id=dt.EC_id)
    ei=ExperienceImages.objects.filter(E_id=dt.id)
    EIN=ExperienceIncluded.objects.filter(E_id=dt.id)
    data={'dt':dt,'ec':ec,'ei':ei,'EIN':EIN}
    if request.method == 'POST':
        E_id = request.POST.get('E_id')
        Image=request.FILES.get('Image')
        df=ExperienceImages.objects.create(E_id=E_id,Image=Image)
        df.save()
        return redirect(f'/ExperiencesView/{E_id}#Images')
    return render(request,'admin/experiencesvie.html',data)

def FIncluded(request):
    if request.method == 'POST':
        E_id = request.POST.get('E_id')
        Lines = request.POST.get('Lines')
        df=ExperienceIncluded.objects.create(E_id=E_id,Types='Included',Lines=Lines)
        df.save()
        return redirect(f'/ExperiencesView/{E_id}#FIncluded')

def FNotIncluded(request):
    if request.method == 'POST':
        E_id = request.POST.get('E_id')
        Lines = request.POST.get('Lines')
        df=ExperienceIncluded.objects.create(E_id=E_id,Types='NotIncluded',Lines=Lines)
        df.save()
        return redirect(f'/ExperiencesView/{E_id}#FNotIncluded')
    
def ExImageDelete(request,id):
    dt=ExperienceImages.objects.get(id=id)
    E_id = dt.E_id
    dt=ExperienceImages.objects.get(id=id)
    dt.delete()
    return redirect(f'/ExperiencesView/{E_id}')

def DeleteIncluded(request,id):
    dt=ExperienceIncluded.objects.get(id=id)
    E_id = dt.E_id
    dt=ExperienceIncluded.objects.get(id=id)
    dt.delete()
    return redirect(f'/ExperiencesView/{E_id}')

def ExperienceForm(request):
    dt=Experience.objects.all()
    EQ = ExperienceFormsQ.objects.all()
    dt2 =[]
    for i in dt:
        dt2.append(i.Name)
    EQ2=[]
    for j in EQ:
        EQ2.append(j.Name)
    lsr = [i.Name for i in dt if i.Name not in EQ2]
    print(lsr)
    if lsr == []:
        ls = []
    elif lsr == dt2:
        ls = dt2
    else:   
        ls = lsr
    data={'dt':dt,'EQ':EQ,'ls':ls}
    if request.method == 'POST':
        Name = request.POST.get('Name')
        for i in dt:
            if i.Name == Name:
                E_id = i.id
        dt= ExperienceFormsQ.objects.create(E_id=E_id,Name=Name)
        dt.save()
        return redirect('/ExperienceForm')
    return render(request,'admin/experiencesform.html',data)

def ExperiencesFormDelete(request,id):
    dt=ExperienceFormsQ.objects.get(id=id)
    dt.delete()
    return redirect('/ExperienceForm')

def ExperienceFormView(request,id):
    EQ = ExperienceFormsQ.objects.get(id=id)
    dt=Experience.objects.filter(id=EQ.E_id,Name=EQ.Name)
    data={'EQ':EQ,'dt':dt}
    if request.method == 'POST':
        EQ.Q1 = request.POST.get('Q1')
        EQ.Q2 = request.POST.get('Q2')
        EQ.Q3 = request.POST.get('Q3')
        EQ.Q4 = request.POST.get('Q4')
        EQ.Q5 = request.POST.get('Q5')
        EQ.Q6 = request.POST.get('Q6')
        EQ.Q7 = request.POST.get('Q7')
        EQ.Q8 = request.POST.get('Q8')
        EQ.Q9 = request.POST.get('Q9')
        EQ.Q10 = request.POST.get('Q10')
        EQ.save()
        return redirect(f'/ExperiencesFormDataList/{id}')
    return render(request,'admin/experiencesformview.html',data)

def ExperiencesFormDataList(request,id):
    EQ = ExperienceFormsQ.objects.get(id=id)
    dt=Experience.objects.filter(id=EQ.E_id,Name=EQ.Name)
    data={'EQ':EQ,'dt':dt}
    return render(request,'admin/experiencesdatalist.html',data)