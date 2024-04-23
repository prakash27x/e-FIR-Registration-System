from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import AuthenticationForm
from .models import FIR
from .forms import FirForm




from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]  # Note: It's 'username' for AuthenticationForm
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)

            if user is not None:
                print(f"Authenticated user: {user}")
                login(request, user)
                messages.success(request, f"Welcome, {email}!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    # If it's not a POST request or authentication fails, render the login page
    return render(request, "index.html")



    #if(request.method == "POST"):
     #   print(request.POST)
     #   form = AuthenticationForm(request, data=request.POST)
      #  print(form.is_valid())
       # if form.is_valid():
        #    username = form.cleaned_data["username"]
         #   password = form.cleaned_data["password"]
          #  user = authenticate(request, username=username, password=password)

           # if user is not None:
            #    login(request, user)
             #   messages.success(request, f"Welcome, {username}!")
              #  return redirect('home')
            #else:
             #   messages.error(request, "Invalid username or password.")

        #else:
         #   print(form.errors)
          #  messages.error(request, "Invalid username or password.")

    #else:
     #   form = AuthenticationForm()
   # return render(request, "index.html")

def home(request):
    return render(request, "home.html")



def register(request):
    if request.method == "POST":
        form_data = request.POST.get('full_name')
        print(form_data)
        form = ApplicationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            phone = form.cleaned_data["phone"]
            national_id = form.cleaned_data["national_id"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            register = Form(full_name=full_name, phone=phone,
                                national_id=national_id, email=email, password=password)
            register.save()
            print("HEHEHE")
            message_body = f"A new user have been submitted. Thank you, \n{full_name}"
            email_message = EmailMessage("User Registration Completed!", message_body, to=[email])
            email_message.send()

            messages.success(request, "User Registered Successfully!")
            return redirect("index")
    else:
        return render(request, "register.html")

def fir(request):
    if request.method == "POST":
        form_data = request.POST.get('full_name')
        print(form_data)
        form = FirForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            registrationDate = form.cleaned_data["registrationDate"]
            policeOffice = form.cleaned_data["policeOffice"]


            full_name = form.cleaned_data["full_name"]
            address = form.cleaned_data["address"]
            dob = form.cleaned_data["dob"]
            phone = form.cleaned_data["phone"]

            complaint_details = form.cleaned_data["type_law"]

            offender_full_name = form.cleaned_data["fullname"]
            address_off = form.cleaned_data["address_off"]
            off_f_m_name = form.cleaned_data["off_f/m_name"]
            offender_description = form.cleaned_data["description"]

            offence_place = form.cleaned_data["place"]
            related_detail = form.cleaned_data["related_detail"]
            nature = form.cleaned_data["nature"]
            evidence = form.cleaned_data["evidence"]
            others = form.cleaned_data["others"]

            con_name_sign = form.cleaned_data["sign"]
            sub_date = form.cleaned_data["sub_date"]

            fir_request = FIR(registrationDate=registrationDate, policeOffice=policeOffice, full_name=full_name,
                               address=address, dob=dob, phone=phone, complaint_details=complaint_details,
                               offender_full_name=offender_full_name, address_off=address_off, off_f_m_name=off_f_m_name,
                               offender_description=offender_description, offence_place=offence_place,
                               related_detail=related_detail, nature=nature, evidence=evidence, others=others,
                               con_name_sign=con_name_sign, sub_date=sub_date)


            fir_request.save()
            print("HEHEHE")
            #message_body = f"A new user have been submitted. Thank you, \n{full_name}"
            #email_message = EmailMessage("User Registration Completed!", message_body, to=[email])
            #email_message.send()

            messages.success(request, "FIR has been sent to administration!")
            return redirect("home")

        else:
            request
            messages.error(request, "Form submission is not valid. Please check the form and try again.")
    else:
        return render(request, "fir.html")

    #return render(request, "fir.html")
