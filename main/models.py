from django.db import models

# Create your models here.

class ExperienceCategory(models.Model):
    Category = models.CharField(max_length=100,null=True, blank=True)
    Description = models.CharField(max_length=100,null=True, blank=True)
    Image = models.FileField(upload_to='ExperienceCategory',null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)

class ExperienceImages(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Image = models.FileField(upload_to='ExperienceImages',null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)

class ExperienceIncluded(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Types = models.CharField(max_length=100,null=True, blank=True)
    Lines = models.CharField(max_length=100,null=True, blank=True)

class Experience(models.Model):
    EC_id=models.IntegerField(default=0,null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    Name=models.CharField(max_length=100,null=True, blank=True)
    Image = models.FileField(upload_to='Experience',null=True, blank=True)
    SmallDescription = models.CharField(max_length=100,null=True, blank=True)
    Description = models.CharField(max_length=100,null=True, blank=True)
    Address = models.CharField(max_length=100,null=True, blank=True)
    Price = models.CharField(max_length=100,null=True, blank=True)
    Days = models.CharField(max_length=100,null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    EIm_id = models.IntegerField(default=0,null=True, blank=True)
    EIn_id = models.IntegerField(default=0,null=True, blank=True)
    EF_id = models.IntegerField(default=0,null=True, blank=True)
    View = models.CharField(max_length=100,null=True, blank=True)

    # def save(self, *args, **kwargs):
    #         Id = str(self.id)
    #         self.EIm_id=Id
    #         self.EIn_id=Id
    #         self.EF_id=Id
    #         super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)


class ExperienceFormsQ(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Name=models.CharField(max_length=100,null=True, blank=True)
    Q1 = models.TextField(default='',blank=True)
    Q2 = models.TextField(default='',blank=True)
    Q3 = models.TextField(default='',blank=True)
    Q4 = models.TextField(default='',blank=True)
    Q5 = models.TextField(default='',blank=True)
    Q6 = models.TextField(default='',blank=True)
    Q7 = models.TextField(default='',blank=True)
    Q8 = models.TextField(default='',blank=True)
    Q9 = models.TextField(default='',blank=True)
    Q10 = models.TextField(default='',blank=True)
    Q11 = models.TextField(default='',blank=True)
    Q12 = models.TextField(default='',blank=True)
    Q13 = models.TextField(default='',blank=True)
    Q14 = models.TextField(default='',blank=True)
    Q15 = models.TextField(default='',blank=True)
    Q16 = models.TextField(default='',blank=True)
    Q17 = models.TextField(default='',blank=True)


class ExperienceFormsA(models.Model):
    E_id = models.IntegerField(default=0,null=True, blank=True)
    Name=models.CharField(max_length=100,null=True, blank=True)
    FullName = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Email = models.CharField(max_length=100,null=True, blank=True)
    ContactNo = models.CharField(max_length=100,null=True, blank=True)
    State = models.CharField(max_length=100,null=True, blank=True)
    City = models.CharField(max_length=100,null=True, blank=True)
    SOP = models.TextField(null=True, blank=True)
    A1 = models.TextField(default='',blank=True)
    A2 = models.TextField(default='',blank=True)
    A3 = models.TextField(default='',blank=True)
    A4 = models.TextField(default='',blank=True)
    A5 = models.TextField(default='',blank=True)
    A6 = models.TextField(default='',blank=True)
    A7 = models.TextField(default='',blank=True)
    A8 = models.TextField(default='',blank=True)
    A9 = models.TextField(default='',blank=True)
    A10 = models.TextField(default='',blank=True)
    A11 = models.TextField(default='',blank=True)
    A12 = models.TextField(default='',blank=True)
    A13 = models.TextField(default='',blank=True)
    A14 = models.TextField(default='',blank=True)
    A15 = models.TextField(default='',blank=True)
    A16 = models.TextField(default='',blank=True)
    A17 = models.TextField(default='',blank=True)