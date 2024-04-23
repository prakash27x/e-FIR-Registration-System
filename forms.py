from django import forms

class ApplicationForm(forms.Form):
    full_name = forms.CharField(max_length=80)
    phone = forms.CharField(max_length=80)
    national_id = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)


class FirForm(forms.Form)
    registrationDate = forms.DateField()
    policeOffice = forms.CharField(max_length=255)

    full_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    dob = forms.DateField()
    phone = forms.CharField(max_length=20)

    complaint_details = forms.TextField()

    offender_full_name = forms.CharField(max_length=255, blank=True, null=True)
    address_off = forms.CharField(max_length=255, blank=True, null=True)
    off_f_m_name = forms.CharField(max_length=255, blank=True, null=True)
    offender_description = forms.TextField(blank=True, null=True)

    offence_place = forms.TextField()
    related_detail = forms.TextField()
    nature = forms.TextField(blank=True, null=True)
    evidence = forms.TextField(blank=True, null=True)
    others = forms.TextField(blank=True, null=True)