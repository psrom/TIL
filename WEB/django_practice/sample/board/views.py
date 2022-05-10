from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


# controller
def index(request):
    # index controller 생성

    user_list = ['설윤', '수지', '원영', '설아']

    role = "superuser"

    return render(request, 'index.html', {'name':'사용자1', 'user_list': user_list, "role": role})