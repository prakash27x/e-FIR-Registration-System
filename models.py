from datetime import datetime

from django.db import models

class Form(models.Model):
    full_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    national_id = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name}"


class FIR(models.Model):
    registrationDate = models.DateField()
    policeOffice = models.CharField(max_length=255)

    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    phone = models.CharField(max_length=20)

    complaint_details = models.TextField()

    offender_full_name = models.CharField(max_length=255, blank=True, null=True)
    address_off = models.CharField(max_length=255, blank=True, null=True)
    off_f_m_name = models.CharField(max_length=255, blank=True, null=True)
    offender_description = models.TextField(blank=True, null=True)

    offence_place = models.TextField()
    related_detail = models.TextField()
    nature = models.TextField(blank=True, null=True)
    evidence = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)

    con_name_sign = models.CharField(max_length=255, default='')
    sub_date = models.DateField(default=datetime.now)


    def __str__(self):
        return f"FIR #{self.id} - {self.full_name}"
