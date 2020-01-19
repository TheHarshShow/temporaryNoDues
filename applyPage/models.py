from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=264, unique=True)
    hod_name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.department_name

class Student(models.Model):
    student_name = models.CharField(max_length=264,unique=False)
    roll_number = models.IntegerField(unique=True)
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=264, unique=True)
    student_type = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.student_name

class BTP(models.Model):
    professor_name = models.CharField(max_length=264,unique=True)
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.professor_name

class Other(models.Model):
    name = models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.name


class Lab(models.Model):
	department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
	course_id = models.CharField(max_length=264,unique=True)
	lab_name = models.CharField(max_length=264,unique=True)

	def __str__(self):
		return self.course_id



class LabRequestEntry(models.Model):
    name = models.ForeignKey(Lab,on_delete=models.DO_NOTHING)
    student_name = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    date_sent = models.DateField()
    #the applied field indicates whether the entry has been applied
    applied = models.BooleanField()
    #The approved field is 0 when waiting, 1 when approved, -1 when disapproved
    approved = models.PositiveSmallIntegerField()
    remark = models.CharField(max_length = 1000,blank=True)
    
    def __str__(self):
        return str(self.name)

class BTPRequestEntry(models.Model):
    name = models.ForeignKey(BTP,on_delete=models.DO_NOTHING)
    student_name = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    date_sent = models.DateField()
    applied = models.BooleanField(default=False)
    approved = models.PositiveSmallIntegerField(default=0)
    remark = models.CharField(max_length = 1000,blank=True)

    def __str__(self):
        return str(self.name)


class OthersRequestEntry(models.Model):
    name = models.ForeignKey(Other ,on_delete=models.DO_NOTHING)
    student_name = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    date_sent = models.DateField()
    applied = models.BooleanField(default=False)
    approved = models.PositiveSmallIntegerField(default=0)
    remark = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return str(self.name)
