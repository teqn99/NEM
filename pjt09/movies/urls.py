from django.urls import path
from . import views
# 이거추가
from movies.views import FilteringMovies
# from movies.views import FilteredMovies

app_name = 'movies'

urlpatterns = [
    # 틀린이유: url적는 순서. 리뷰수정&삭제보다 아래 높으면 디테일하게 못 잡음
    path('<int:movie_pk>/', views.detail, name='detail'),
    # 리뷰수정 & 리뷰삭제 / 틀린이유: url적는 순서. 맨 아래 놓으면 디테일하게 못 잡음
    path('<int:movie_pk>/update_review/<int:review_pk>/', views.update_review, name = 'update_review'),    #Form 표시 및 기존 리뷰 수정 / GET & POST
    path('<int:movie_pk>/delete_review/<int:review_pk>/', views.delete_review, name = 'delete_review'),    #단일 리뷰 삭제 / GET or POST
    # path('', views.index, name='index'),
    
    # wish영화 삭제(문제시 url 배치고려)
    path('delete_wish/<int:movie_pk>/', views.delete_wish, name='delete_wish'),

    path('<int:movie_pk>/wish/', views.wish, name='wish'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('<int:director_pk>/director_like/', views.director_like, name='director_like'),
    path('<int:actor_pk>/actor_like/', views.actor_like, name='actor_like'),

    path('<int:movie_pk>/review/<int:review_pk>', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/review/create/', views.review_create, name='review_create'),
    # 리뷰 반응 이모지
    path('<int:review_pk>/happy_review/', views.happy_review, name='happy_review'),
    path('<int:review_pk>/sad_review/', views.sad_review, name='sad_review'),
    path('<int:review_pk>/angry_review/', views.angry_review, name='angry_review'),


    # 추가
    path('', FilteringMovies.as_view(), name='main-view'),
    path('after_signup/', views.after_signup, name='after_signup'),
    path('first_recommend/', views.first_recommend, name='first_recommend'),


]
