from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Board, Comment
# Create your views here.


# controller
def index(request):
    # index controller 생성

    user_list = ['설윤', '수지', '원영', '설아']

    role = "superuser"

    return render(request, 'index.html', {'name':'사용자1', 'user_list': user_list, "role": role})

def board_list(request):
    board_list = Board.objects.all()
    return render(request, "board_list.html", {"board_list": board_list})

def board_write(request):
    if request.method == "POST":
        data = request.POST
        Board.objects.create(
            title=data['title'],
            contents=data['content']
        )

        return redirect('/board')
    else:
        pass
    return render(request, "board_write.html")

def board_detail(request, board_id):
    print(board_id)
    board = Board.objects.get(id=board_id)
    comments = board.comment_list.all()
    # comments = Comment.objects.filter(board_id = board).all()
    return render(request, "board_detail.html", {"board": board, "comments":comments})