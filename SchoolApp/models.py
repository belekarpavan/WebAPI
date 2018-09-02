from django.db import models

# Create your models here.
class department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=40)

    class Meta:
        db_table="department"

    def __str__(self):
        return self.dept_name


class course(models.Model):
    course_id=models.CharField(primary_key=True, max_length=40)
    course_name=models.CharField(unique= True, max_length=40)
    dept=models.ForeignKey(department, on_delete=models.CASCADE)
    class Meta:
        db_table="course"

    def __str__(self):
        return self.course_name

class subject(models.Model):
    subject_id=models.CharField(primary_key=True, max_length=40)
    subject_name=models.CharField(max_length=40)
    course=models.ForeignKey(course, on_delete=models.CASCADE)
    class Meta:
        db_table="subject"

    def __str__(self):
        return self.subject_name


class register(models.Model):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    pin = models.CharField(max_length=6)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return (self.first_name + " " + self.last_name+" "+str(type(self)))


class parent(register):
    occupation = models.CharField(max_length=40)

    def __str__(self):
        return (self.first_name+" "+self.last_name)
    class Meta:
        db_table="parent"

class student(register):
    roll_no=models.CharField(max_length=6)
    guardian = models.ForeignKey(parent,null=True, on_delete=models.CASCADE)
    dept = models.ForeignKey(department, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    class Meta:
        db_table = "student"


class teacher(register):
    isadmin = models.CharField(max_length=5)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    class Meta:
        db_table = "teacher"
