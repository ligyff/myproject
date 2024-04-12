import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods


def hello(request):
    return HttpResponse("Hello, World!")


def hello1(request):
    return HttpResponse("Hello, World!111111111111111111111")


@require_http_methods(["GET"])
def my_view(request):
    param = request.GET.get('myparam', None)  # 获取名为'myparam'的GET参数
    if param:
        # 你的逻辑代码，比如从数据库获取数据
        data = {'message': f'你传递的参数是: {param}'}
    else:
        data = {'message': '没有提供参数'}

    return JsonResponse(data)



@require_http_methods(["POST"])
def my_view_post(request):

    # 获取POST请求的参数
    post_data = json.loads(request.body)
    myparam = post_data.get('myparam', None)

    if myparam:
        # 你的逻辑代码，比如处理数据、保存到数据库等
        data = {'message': f'你传递的参数是: {myparam}'}
    else:
        data = {'message': '没有提供参数'}

    return JsonResponse(data)
