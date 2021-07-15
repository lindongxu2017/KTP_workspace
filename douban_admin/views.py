from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from book.models import detail, all_list
import json

def get_list(request):
  # params = json.loads(request)
  print(request.get_raw_uri())
  # print(dir(request))
  if request.method == 'POST':
    return JsonResponse({
      "status": 400,
      "msg": 'error request method'
    })
  else:
    _type = str(request.GET.get('type'))
    _page = int(request.GET.get('page'))
    offset = 10*(_page-1)
    pagenum = offset + 10
    if _type == '1':
      _list = all_list.objects.order_by('-click')[offset:pagenum]
    else:
      _list = all_list.objects.order_by('id')[offset:pagenum]
    re_list = []
    length = all_list.objects.all().count()
    for item in _list:
      re_item = {
        "title": item.title,
        "bookfaceimg": item.bookfaceimg,
        "panelimg": item.panelimg,
        "price": item.price,
        "desc": item.desc,
        "click": item.click,
        "link": item.link
      }
      re_list.append(re_item)
    return JsonResponse({
      "status": 200,
      "total":length,
      "data": re_list,
      "msg": "OK"
    })

def get_detail(request):
  if request.method == 'GET':
    return JsonResponse({
      "status": 400,
      "msg": 'error request method'
    })
  else:
    params = json.loads(request.body)
    name = params['name']
    item = detail.objects.filter(bookname__contains=name)[0]
    num = all_list.objects.filter(title__contains=name)[0].click
    num = num + 1
    all_list.objects.filter(title__contains=name).update(click=num)
    re_item = {
      "bookname": item.bookname,
      "sample": item.sample,
      "dt": item.dt,
      "dd": item.dd,
      "link": item.link
    }
  return JsonResponse({
    "data": re_item,
    "status": 200,
    "msg": 'OK'
  })
  # return JsonResponse({"a": 1})

def get_banner(request):
  # params = json.loads(request)
  # print(request.get_raw_uri())
  # print(dir(request))
  if request.method == 'POST':
    return JsonResponse({
      "status": 400,
      "msg": 'error request method'
    })
  else:
    _list = all_list.objects.all()[0:5]
    re_list = []
    for item in _list:
      re_item = {
        "title": item.title,
        "bookfaceimg": item.bookfaceimg,
        "panelimg": item.panelimg,
        "price": item.price,
        "desc": item.desc,
        "click": item.click,
        "link": item.link
      }
      re_list.append(re_item)
    return JsonResponse({
      "status": 200,
      "data": re_list,
      "msg": "OK"
    })