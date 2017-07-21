from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.


# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=255)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=255)


# class Page(models.Model):
#     # Fields
#     id = models.AutoField()
#     title = models.CharField(max_length=255)
#
#     # Metadata
#     class Meta:
#         ordering = ('title',)
#
#     # Methods
#     def __str__(self):
#         return self.title

class Teacher(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # courses = models.ManyToManyField(Course)

    # Metadata
    class Meta:
        ordering = ('user',)

    # Methods
    def __str__(self):
        return self.user.get_full_name()


class Course(models.Model):
    # Fields
    # id = models.AutoField()
    course_name = models.CharField(max_length=200)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=0)
    location = models.CharField(max_length=200)

    # Metadata
    class Meta:
        ordering = ('course_name',)

    # Methods
    def __str__(self):
        return self.course_name


class Student(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    # Metadata
    class Meta:
        ordering = ('user',)

    # Methods
    def __str__(self):
        return self.user.get_full_name()


class Assignment(models.Model):
    # Fields
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Date Assigned')
    score = models.IntegerField()
    max_score = models.IntegerField()

    # Metadata
    class Meta:
        ordering = ('title',)

    # Methods
    def __str__(self):
        return self.title


class Parent(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    # Metadata
    class Meta:
        ordering = ('user',)

    # Methods
    def __str__(self):
        return self.user.get_full_name()


