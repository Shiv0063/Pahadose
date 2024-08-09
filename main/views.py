from django.shortcuts import render,redirect
from .models import Experience,ExperienceCategory,ExperienceImages,ExperienceIncluded,ExperienceFormsQ,ExperienceFormsA,MemoriesModel,UserDetails,ContactModel
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,Group
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
import os
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse, parse_qs
# Create your views here.
# non
# Pahado Se Front-Side
def Login_in(request):
    if request.method=="POST":
        email=request.POST.get('Email')
        try:
            userd = User.objects.get(email=email)
        except User.DoesNotExist:
            return redirect('/Login')
        username = userd.username
        password=request.POST.get('Password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user) 
            parsed_url = urlparse(request.META.get('HTTP_REFERER'))
            if 'next' in parsed_url:
                next_url = parse_qs(parsed_url.query)['next'][0]
            else:
                next_url=''
            if next_url != '':
                return redirect(next_url)
            else:
                return redirect('/')
        return redirect('/')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('/')

def SignUp(request):
    if request.method=="POST":
        Fullname = request.POST.get('Fullname')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        password = request.POST.get('Password')
        username = Fullname
        emailaddress = Email
        dt=User.objects.filter(username=Fullname).exists()
        if dt == True:
            return redirect('/SignUp')
        dt=User.objects.filter(email=Email).exists()
        if dt == True:
            return redirect('/SignUp')
        new_user= User.objects.create_user(username,emailaddress,password)
        new_user.save()
        dg=User.objects.get(email=Email)
        userd=UserDetails.objects.create(user_id=dg.id,FullName=Fullname,phone=Phone)
        userd.save()
        # messages.success(request,'New User Create Successfully.')
        return redirect('/Login')
    return render(request,'signup.html')

def home(request):
    dt=Experience.objects.all()[:2]
    dt2=Experience.objects.all()
    EQ=ExperienceCategory.objects.all()
    data= {'dt':dt,'dt2':dt2,'EQ':EQ}
    return render(request,'index.html',data)

@csrf_exempt
def ExperiencesAPI(request):
    PN = request.POST.get('value')
    Cy = ExperienceCategory.objects.get(Category=PN)
    Ex = Experience.objects.filter(EC_id=Cy.id).values()
    Ex = list(Ex)
    return JsonResponse({'Ex':Ex})

def ExperiencesSearch(request):
    if request.method == 'POST':
        Experiences = request.POST.get('Experiences')
        ExperiencesList = request.POST.get('ExperiencesList')
        return redirect(f'/Experiences/{Experiences}/{ExperiencesList}')

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
    if dt.View == 'ComingSoon':
        return redirect(f'/Experiences/{Category}')
    fm= ExperienceFormsQ.objects.filter(Name=Name).exists()
    EDI = ExperienceIncluded.objects.filter(E_id=dt.id)
    EIM = ExperienceImages.objects.filter(E_id=dt.id)
    data={'dt':dt,'ec':ec,'EDI':EDI,'EIM':EIM,'fm':fm}
    return render(request,'experiences-details.html',data)

@login_required(login_url='Login')
def ExperiencesForm(request,name):
    fm= ExperienceFormsQ.objects.get(Name=name)
    dt=Experience.objects.get(id=fm.E_id)
    dg= ExperienceCategory.objects.get(id=dt.EC_id)
    data={'fm':fm,'dt':dt}
    if request.method == 'POST':
        FullName = request.POST.get('FullName')
        DOB = request.POST.get('DOB')
        Email = request.POST.get('email')
        Countrycode = request.POST.get('Countrycode')
        ContactNo = request.POST.get('phone')        
        WPNo = request.POST.get('WPNo')
        Country = request.POST.get('Country')
        Pincode = request.POST.get('Pincode')
        SOP = request.POST.get('SOP')
        A1 = request.POST.get('A1') or ''
        A2 = request.POST.get('A2') or ''
        A3 = request.POST.get('A3') or ''
        A4 = request.POST.get('A4') or ''
        A5 = request.POST.get('A5') or ''
        A6 = request.POST.get('A6') or ''
        A7 = request.POST.get('A7') or ''
        A8 = request.POST.get('A8') or ''
        A9 = request.POST.get('A9') or ''
        A10 = request.POST.get('A10') or ''
        dt2= ExperienceFormsA.objects.create(E_id=dt.id,Name=dt.Name,FullName=FullName,DOB=DOB,Email=Email,Countrycode=Countrycode,ContactNo=ContactNo,Country=Country,WPNo=WPNo,Pincode=Pincode,SOP=SOP,A1=A1,A2=A2,A3=A3,A4=A4,A5=A5,A6=A6,A7=A7,A8=A8,A9=A9,A10=A10)
        dt2.save()
        return redirect(f'/Experiences/{dg.Category}/{dt.Name}')
    return render(request,'experiencesform.html',data)

def Stays(request):
    return render(request,'stays.html')

def About(request):
    return render(request,'about.html')

def Memories(request):
    dt=MemoriesModel.objects.all()
    data = {'dt':dt}
    return render(request,'memories.html',data)

def Blog(request):
    return redirect('/')
    # return render(request,'blog.html')

def Contact(request):
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        ContactNo=request.POST.get('ContactNo')
        WPNo=request.POST.get('WPNo')
        Email=request.POST.get('Email')
        Msg=request.POST.get('Msg')
        dt= ContactModel.objects.create(FullName=FullName,ContactNo=ContactNo,WPNo=WPNo,Email=Email,Msg=Msg)
        dt.save()
        return redirect('/')
    return render(request,'contact.html')
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

def ExperiencesEdit(request,id):
    dt=Experience.objects.get(id=id)
    eq=ExperienceCategory.objects.all()
    # ExperienceIncluded.objects.all().delete()
    data={'dt':dt,'eq':eq}
    if request.method=="POST": 
        Categoryid=request.POST.get('Category')
        dt=ExperienceCategory.objects.get(id=Categoryid)
        gh=Experience.objects.get(id=id)
        gh.Name=request.POST.get('Name')
        if request.FILES.get('Image'):
            os.remove(gh.Image.path)
            gh.Image = request.FILES.get('Image')
        gh.SmallDescription=request.POST.get('SmallDescription')
        gh.Description=request.POST.get('Description')
        gh.Address=request.POST.get('Address')
        gh.Price=request.POST.get('Price')
        gh.Days=request.POST.get('Days')
        gh.Date=request.POST.get('Date')
        gh.View=request.POST.get('View')
        gh.save()
        return redirect('/AExperience')
    return render(request,'admin/editexperiences.html',data)

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

def EditCategory(request,id):
    dt=ExperienceCategory.objects.get(id=id)
    data={'dt':dt}
    if request.method=="POST": 
        dt.Category=request.POST.get('Category')
        dt.Description=request.POST.get('Description')
        if request.FILES.get('Image'):
            os.remove(dt.Image.path)
            dt.Image = request.FILES.get('Image')
        dt.save()
        return redirect('/ExperienceCategory')
    return render(request,'admin/editcategory.html',data)

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
    EA = ExperienceFormsA.objects.filter(E_id=EQ.E_id)
    data={'EQ':EQ,'dt':dt,'EA':EA}
    return render(request,'admin/experiencesdatalist.html',data)

def AMemories(request):
    dt=MemoriesModel.objects.all()
    data={'dt':dt}
    if request.method == 'POST':
        Image = request.FILES.get('Image')
        df= MemoriesModel.objects.create(Image=Image)
        df.save()
        return redirect('/AMemories')
    return render(request,'admin/memories.html',data)

def MemoriesIDelete(request,id):
    dt=MemoriesModel.objects.get(id=id)
    dt.delete()
    return redirect('/AMemories')

def AStays(request):
    return render(request,'admin/stays.html')

def AddStays(request):
    return render(request,'admin/stays.html')

def ContactList(request):
    dt=ContactModel.objects.all()
    data={'dt':dt}
    return render(request,'admin/contact.html',data)

def ExperienceFormlist(request):
    EQ=ExperienceFormsQ.objects.all()
    EA=ExperienceFormsA.objects.all()
    data={'EQ':EQ,'EA':EA}
    return render(request,'admin/experienceformlist.html',data)


def DeleteQ():
    Experience.objects.all().delete()
    ExperienceCategory.objects.all().delete()
    ExperienceImages.objects.all().delete()
    ExperienceFormsA.objects.all().delete()
    ExperienceFormsQ.objects.all().delete()
    ExperienceIncluded.objects.all().delete()

