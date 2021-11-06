from django.shortcuts import render
from .models import Questions as Question
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
def connect(request):
    res = {
        "message" : "",
        "payload" : {}
    }

    if request.method == "GET":
        res["message"] = "Success"

    else:
        res["message"] = "Fail"
    
    res = json.dumps(res)
    res = json.loads(res)

    return JsonResponse(res,safe=False)

@csrf_exempt
def start(request):
    res = {
        "message" : "",
        "payload" : {}
    }

    if request.method == "GET":
        question = Question.objects.all().values("qn", "question")

        if len(question) != 0:
            res["payload"] = question[0]
            res["message"] = "Success"
        else:
            res["message"] = "Fail"
    else:
        res["message"] = "Fail"
    
    res = json.dumps(res)
    res = json.loads(res)

    return JsonResponse(res,safe=False)

@csrf_exempt
def questions(request):
    res = {
        "message" : "",
        "payload" : {}
    }

    if request.method == "POST":
        content = json.loads(request.body.decode('utf-8')) # required
        question = Question(question=content["question"],answer = content["answer"])
        question.save()
        res["message"] = "SUCCESS"

    else:
        res["message"] = "Fail"
    
    res = json.dumps(res)
    res = json.loads(res)

    return JsonResponse(res,safe=False)