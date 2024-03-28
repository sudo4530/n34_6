from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=50)
    total_course = models.PositiveIntegerField()
    image = models.ImageField(upload_to="course/speciality/")

    def __str__(self):
        return self.title

class CourseRole(models.TextChoices):
    DRAFT = ("Ko'rinmasin", "Ko'rinmasin")
    Publish = ("Ko'rinsin", "ko'rinsin")


class Courses(models.Model):
    title = models.CharField(max_length=100)
    speciality = models.ManyToManyField(Speciality)
    image = models.ImageField(upload_to="course/course/")
    active_students = models.PositiveIntegerField(default=0)
    durection = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    rayting = models.FloatField(default=0.0)
    status = models.CharField(max_length=20, choices=CourseRole.choices, default=CourseRole.Publish)
    create_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title

class TeacherPosition(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    speciality = models.ForeignKey(TeacherPosition, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="course/teacher/")
    link_twitter = models.URLField(null=True, blank=True)
    link_facebook = models.URLField(null=True, blank=True)
    link_ln = models.URLField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





