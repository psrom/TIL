from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board', views.board_list, name='board_list'),
    path('board/write', views.board_write, name="board_write"),
    path('board/detail/<board_id>', views.board_detail, name="board_detail")
]