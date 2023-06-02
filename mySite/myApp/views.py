from django.core.exceptions import ObjectDoesNotExist;
from django.forms.models import model_to_dict;
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound;
from django.views.decorators.csrf import csrf_exempt;
from myApp import models;
import json



def hello_world(request):
    return HttpResponse("hello world vinco")

def school(request):
    return HttpResponse("welcome to school app")

@csrf_exempt
def subject_link(request):
    if request.method == "GET":
        subjects = list(models.Subject.objects.values())
        return JsonResponse(subjects, safe=False, status=200)
    elif request.method == "POST":
        subj = request.body        
        subject = json.loads(subj)
        new_subject = models.Subject(**subject)       
        new_subject.save()            
        return JsonResponse(subject, status=200)
    else:
        return HttpResponseNotFound("Response not found")
    
@csrf_exempt
def subject_detail(request, pk):
    
    try: 
        subject = models.Subject.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"There is no subject with id {pk}"}, status=404)
    if request.method == "GET":

        return JsonResponse(model_to_dict(subject))
    elif request.method == "PUT":
        subject_bytes = request.body
        new_subject = json.loads(subject_bytes)
        subject.__dict__.update(new_subject)
        subject.save()
        return JsonResponse(new_subject, status=200)

    elif request.method == "DELETE":
        subject.delete()
        return HttpResponse(status=204)
        

@csrf_exempt
def teacher(request):
    if request.method == "GET":
        teacher = list(models.Teacher.objects.values())
        return JsonResponse(teacher, safe=False, status=200)
    elif request.method == "POST":
        teacher = request.body
        teach = json.loads(teacher)
        new_teach = models.Teacher(**teach)
        new_teach.save()
        return JsonResponse(teach, status=201)
    else:
        return HttpResponseNotFound("Response not found")   


@csrf_exempt
def teacher_detail(request, pk):
    try:
        teacher = models.Teacher.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"There is no teacher with id {pk}"}, status=404)
    if request.method == "GET":
        return JsonResponse(model_to_dict(teacher))
    elif request.method == "PUT":
        teach_byte = request.body
        new_teach = json.loads(teach_byte)
        new_teacher = models.Teacher(**new_teach)
        new_teacher.save()
        return JsonResponse(new_teach, status=200)
    elif request.method == "DELETE":
        teacher.delete()
        return HttpResponse(status=204)
        

