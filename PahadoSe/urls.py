"""
URL configuration for PahadoSe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('Experiences',views.Experiences),
    path('Experiences/<str:name>',views.ECategory),
    path('Experiences/<str:Category>/<str:Name>',views.ExperiencesDetails),
    path('Stays',views.Stays),
    path('About',views.About),
    path('Memories',views.Memories),
    path('Blog',views.Blog),
    path('Contact',views.Contact),
    path('Login',views.Login_in,name='Login'),
    path('login',views.Login_in,name='Login'),
    path('Logout',views.Logout,name='Logout'),
    path('logout',views.Logout,name='Logout'),
    path('SignUp',views.SignUp),
    path('Admin',views.Admin),
    path('AExperience',views.AExperience),
    path('ExperienceForm',views.ExperienceForm),
    path('ExperiencesFormView/<int:id>',views.ExperienceFormView),
    path('ExperiencesFormDataList/<int:id>',views.ExperiencesFormDataList),
    path('ExperiencesForm/<str:name>',views.ExperiencesForm),
    path('AddExperiences',views.AddExperiences),
    path('ExperiencesView/<int:id>',views.ExperiencesView),
    path('ExperiencesEdit/<int:id>',views.ExperiencesEdit),
    path('ExperiencesFormDelete/<int:id>',views.ExperiencesFormDelete),
    path('FIncluded',views.FIncluded),
    path('FNotIncluded',views.FNotIncluded),
    path('ExImageDelete/<int:id>',views.ExImageDelete),
    path('DeleteIncluded/<int:id>',views.DeleteIncluded),
    path('ExperiencesDelete/<int:id>',views.ExperiencesDelete),
    path('IncludedCreate',views.IncludedCreate),
    path('ExperienceCategory',views.Category),
    path('AddCategory',views.AddCategory),
    path('EditCategory/<int:id>',views.EditCategory),
    path('DeleteCategory/<int:id>',views.CategoryDelete),
    path('AMemories',views.AMemories),
    path('MemoriesIDelete/<int:id>',views.MemoriesIDelete),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
