from django.db import models



def image_upload_path(instance, filename):
    # Generate upload path based on location
    return f'images/{instance.__class__.__name__}/{filename}'


# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=40)
    img = models.ImageField(upload_to = image_upload_path)
    desc = models.TextField()
    
    
    def __str__(self):
        return self.skill_name
    
    
class Course(models.Model):
    course_name = models.CharField(max_length=40)
    desc = models.TextField()
    img = models.ImageField(upload_to = image_upload_path, blank=True)
    price = models.BigIntegerField()
    
    
    def __str__(self):
        return self.course_name
    
    
class Project(models.Model):
    prj_name = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)
    demo_video_url = models.CharField(max_length=200)
    prj_screenshot = models.ImageField(upload_to = image_upload_path, blank=True)
    
    
    def __str__(self):
        return self.prj_name

    