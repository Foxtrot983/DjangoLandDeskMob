from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ReportForm1, ReportForm2

from .models import Report

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def main(request): #Основной темплэйт тут лежит
    form = ReportForm1()
    context = {'form': form}
    if request.method == "POST" and is_ajax(request=request):
        form = ReportForm1(request.POST)
        form2 = ReportForm2(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']
            form.save()
            return JsonResponse({"name": name}, status=200)
        
        if form2.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            form.save()
            return JsonResponse({"name": name}, status=200)

        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    return render(request, 'main.html', context)
"""    if request.user_agent.is_mobile:
        return render(request, 'm_main.html', context)
    elif request.user_agent.is_tablet:
        return render(request, 't_main.html', context)
    else:
        return render(request, 'main.html', context)
"""


def ajax_posting1(request):
    form = ReportForm1()
    if request.method == "POST" and is_ajax(request=request):
        form = ReportForm1(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']
            form.save()
            return JsonResponse({"name": name}, status=200)

def ajax_posting2(request):
    if request.method == "POST" and is_ajax(request=request):
            form = ReportForm2(request.POST)
            
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                form.save()
                return JsonResponse({"name": name}, status=200)

@login_required
def looklogs(request):
    object = Report.objects.all().order_by('-date')
    return render(request,'looklogs.html', {'object': object})
