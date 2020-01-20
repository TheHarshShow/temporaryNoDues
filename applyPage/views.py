from django.shortcuts import render
from django.http import HttpResponse
from applyPage.models import Department, Student, BTP, Other, Lab, LabRequestEntry, BTPRequestEntry, OthersRequestEntry

# Create your views here.

def index(request):

    lab_request_list = LabRequestEntry.objects.order_by('date_sent')
    other_request_list = OthersRequestEntry.objects.order_by('date_sent')
    request_dict = {"labRequests": lab_request_list, "otherRequests": other_request_list, "student_roll": 180101028}

    return render(request, 'applyPage.html', context=request_dict)
