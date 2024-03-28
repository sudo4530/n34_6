from django.contrib import admin
from .models import Courses, Speciality, TeacherPosition, Teacher

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("title", "total_course")


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "active_students", "durection", "price", "rayting", "status", "create_date")


@admin.register(TeacherPosition)
class TeacherPositionAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "speciality", "link_twitter", "link_facebook", "link_ln", "create_date")
