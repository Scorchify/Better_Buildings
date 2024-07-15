from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReportingForm
from django.utils import timezone


#page requests
def home(request):
    return render(request,"index.html")

def reporting(request):
    return render(request, "reporting.html")

def display(request):
    return render(request, "display.html")

#form requests 
def reportPosted(request):
    q1_response = None
    q2_response = None
    report_time: None
    form = ReportingForm()

    if request.method == "POST":
        form = ReportingForm(request.POST)
        if form.is_valid():
            # Retrieve cleaned data
            q1_response = form.cleaned_data['q1']
            q2_response = form.cleaned_data['q2']
            report_time = timezone.now()
            return render(request, "reportPosted.html", {"q1_response": q1_response, "q2_response": q2_response, "report_time": report_time})
        
    else:
        form = ReportingForm()
        
    return render(request, "reporting.html", {"form": form, "q1_response": q1_response, "q2_response": q2_response})