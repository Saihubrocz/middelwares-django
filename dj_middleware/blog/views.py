from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from datetime import datetime
current_time = datetime.now()
milliseconds = current_time.strftime("%H:%M:%S.%f")[:-3]

def v_resp(request):
    current_time = datetime.now()
    milliseconds = current_time.strftime("%H:%M:%S.%f")[:-3]
    print("I amview")

    return HttpResponse('its views functionality',milliseconds)

