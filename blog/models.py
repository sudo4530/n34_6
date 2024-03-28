from django.db import models
from users.models import CustomUser
from course.models import Teacher

class Tags(models.Model):
    name = models.CharField(max_length=100)

class BlogPostRole(models.TextChoices):
    PUBLISH = ("p", "Publish")
    DRAFT = ("d", "Draft")

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/blog/")
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    status = models.CharField(max_length=10, choices=BlogPostRole.choices, default=BlogPostRole.PUBLISH)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.text[:10]}"

# from mdeditor.fields import MDTextField
#
# class BlogTest(models.Model):
#     text = MDTextField(null=True, blank=True)