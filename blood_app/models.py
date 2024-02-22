from django.db import models

class DonorDetails(models.Model):
    donor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    blood_group = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)

class PatientDetail(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    blood_group = models.CharField(max_length=10)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(PatientDetail, on_delete=models.CASCADE)
    blood_units = models.IntegerField()
    request_date = models.DateField()
    request_time = models.TimeField()
    remark = models.TextField()

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    blood_group = models.CharField(max_length=10)
    quantity = models.IntegerField()
    type = models.CharField(max_length=100)

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(PatientDetail, on_delete=models.CASCADE)
    feedback_data = models.TextField()
