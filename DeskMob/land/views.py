from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Report

def main(request): #Основной темплэйт тут лежит
    agent = request.META['HTTP_USER_AGENT'].lower()
    print(agent)
    if ('android' in agent or 'iphone' in agent):
        return render(request, 'm_main.html')
    else:
        return render(request, 'main.html')

@login_required
def looklogs(request):
    object = Report.objects.all().order_by('-date')
    return render(request,'looklogs.html', {'object': object})
