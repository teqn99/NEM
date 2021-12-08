from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_GET, require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from .models import Movie, Review, Actor, Director
from .forms import ReviewForm
from .recommend import recommendation, df_new, recommended_movie_info
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# 검색기능을 위한 추가
from django.views.generic import ListView
import json
import random
# 부트스트랩 메시지
from django.contrib import messages
import datetime

class FilteringMovies(ListView):
    model = Movie
    template_name = 'movies/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["qs_json"] = json.dumps(list(Movie.objects.values('id', 'title', 'popularity')))
        # context["qs_json"] = json.dumps(list(Movie.objects.values('id', 'title', 'popularity', 'poster_path')))
        context["qs_json"] = json.dumps(list(Movie.objects.values('id', 'title', 'popularity', 'original_title', 'trailer', 'poster_path')))
        # context["qs_json"] = json.dumps(list(Movie.objects.values('id', 'title', 'popularity', 'poster_path', 'overview')))
        # print(Movie.objects.values('title'))
        # print(context["qs_json"])
        # print(context)

        movies = Movie.objects.all()
        popularity = Movie.objects.all().order_by('-popularity')
        vote_average = Movie.objects.all().order_by('-vote_average')
        release_date = Movie.objects.all().order_by('-release_date')
        context['movies'] = movies
        context['popularity'] = popularity[:50]
        context['vote_average'] = vote_average[:50]
        context['release_date'] = release_date[:50]
        # print(context)
        return context


@require_GET
def index(request):
    movies = Movie.objects.order_by('-pk')
    # movies = Movie.objects.all()
    # print(len(movies))
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    recommend = recommendation(df_new, movie.title)
    info_list = recommended_movie_info(recommend)
    # print(info_list)
    actors = movie.actors_info.all()
    director = movie.director_info.all()
    reviews = Review.objects.all().filter(movie=movie).order_by('pk')

    popularity = list(Movie.objects.all().order_by('-popularity'))
    for idx, val in enumerate(popularity):
        if val.title == movie.title:
            rank = idx + 1
            break
    score = movie.vote_average * 10

    context = {
        'movie': movie,
        'info_list': info_list,
        'actors': actors,
        'director': director,
        'reviews': reviews,
        'rank': rank,
        'score': score,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
@login_required
def first_recommend(request):
    movies = request.user.like_movies.all()
    movies_list = list(movies.values('title'))

    recommend_list = []
    for i in range(len(movies_list)):
        recommend = recommendation(df_new, movies_list[i]['title'])
        info_list = recommended_movie_info(recommend)
        recommend_list.extend(info_list[:3])

    final = []
    s = set()
    for movie in recommend_list:
        if movie['title'] not in s:
            final.append(movie)
        s.add(movie['title'])

    context = {
        'recommend_list': final,
    }
    return render(request, 'movies/first_recommend.html', context)


@require_POST
def wish(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.wish_users.filter(pk=user.pk).exists():
            movie.wish_users.remove(user)
            wished = False
        else:
            movie.wish_users.add(user)
            wished = True
        wish_status = {
            'wished' : wished,
        }
        return JsonResponse(wish_status)
    return HttpResponse(status=401)

# wish 삭제 (해당유저만)/ profile페이지에서 / 좋아요삭제처럼
@require_POST
def delete_wish(request, movie_pk):
    # wish_movies = request.user.wish_movies.all()
    # wish_movie = request.user.wish_movies.filter(pk=movie_pk)
    # 위 쿼리셋으로 말고 get_object_or_404로 받기
    # wish_movie.wish_users.remove(request.user)    #AttributeError: 'QuerySet' object has no attribute 'wish_users'
    wishmovie = get_object_or_404(Movie, pk=movie_pk)
    # print(wishmovie)
    if wishmovie.wish_users.filter(pk=request.user.pk).exists():
        # print('TRUE')   #TRUE
        wishmovie.wish_users.remove(request.user)
        # print('REMOVED')   #REMOVED
    # print(request.user) #ch1
    # print(type(request.user))   #<class 'django.utils.functional.SimpleLazyObject'>
    # print(request.user.username) #ch1
    # print(request.user.pk)  #5
    messages.warning(request, 'wish movie가 삭제되었습니다.')
    return redirect('accounts:profile', request.user.username)



@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            liked = False
        else:
            movie.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)


@require_POST
def director_like(request, director_pk):
    if request.user.is_authenticated:
        director = get_object_or_404(Director, pk=director_pk)
        user = request.user

        if director.like_users.filter(pk=user.pk).exists():
            director.like_users.remove(user)
            liked = False
        else:
            director.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)


@require_POST
def actor_like(request, actor_pk):
    if request.user.is_authenticated:
        actor = get_object_or_404(Actor, pk=actor_pk)
        user = request.user

        if actor.like_users.filter(pk=user.pk).exists():
            actor.like_users.remove(user)
            liked = False
        else:
            actor.like_users.add(user)
            liked = True
        like_status = {
            'liked' : liked,
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)

# Review ---------------------------------------------------------------------------------

@login_required
@require_http_methods(['GET', 'POST'])
def review_create(request, movie_pk):
    # 추가
    this_movie = get_object_or_404(Movie, pk=movie_pk)
    movie_title = this_movie.title
    release_date = this_movie.release_date
    release_year = release_date.year
    # print(release_date.year)    #2021
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            movie = get_object_or_404(Movie, pk=movie_pk)
            review.movie = movie
            review.save()
            messages.info(request, '리뷰가 작성되었습니다.')
            return redirect('movies:detail', movie_pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
        'movie_title':movie_title,
        'release_year': release_year,
        'movie_pk':movie_pk,
    }
    return render(request, 'movies/review_create.html', context)

# 리뷰수정(작성자만)
@login_required
@require_http_methods(['GET', 'POST'])
def update_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # ??? 오류 movie = get_object_or_404(Movie, pk=movie_pk)
    this_movie = get_object_or_404(Movie, pk=movie_pk)
    movie_title = this_movie.title
    # print(this_movie.title)   #더 하더 데이 폴
    release_date = this_movie.release_date
    release_year = release_date.year
    # #POST
    if request.method == 'POST':
        form = ReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            movie = get_object_or_404(Movie, pk=movie_pk)   
            review.movie = movie    #movie에는 instance 하나 전체가 들어가야(pk x)
            review.save()
            messages.warning(request, '리뷰가 수정되었습니다.')
            return redirect('movies:detail', movie_pk)  #여기 movie_pk같이 넘겨주기위해 variable routing으로 같이 받아줌

    # #GET
    if request.method == 'GET':
        form = ReviewForm(instance=review)

    context = {
        # ??? 오류 'movie' : movie,
        'form' : form,
        'movie_pk':movie_pk, #리뷰업데이트 html에서 movie_pk를 쓰기 위해
        'review':review,
        'movie_title':movie_title,
        'release_year': release_year,
    }
    return render(request, 'movies/review_update.html', context)


# 리뷰삭제(작성자만)
@require_POST
def delete_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    messages.warning(request, '리뷰가 삭제되었습니다.')
    return redirect('movies:detail', movie_pk)



@require_GET
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # comments = review.comment_set.all()
    # comment_form = CommentForm()
    context = {
        'review': review,
        # 'comment_form': comment_form,
        # 'comments': comments,
    }
    return render(request, 'movies/review_detail.html', context)

@require_POST
def happy_review(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.happy_users.filter(pk=request.user.pk).exists():
            # 이모지 취소
            review.happy_users.remove(request.user)
            # 이모지 클릭 여부
            happy = False
        else:
            # 이모지 클릭
            review.happy_users.add(request.user)
            # 이모지 클릭 여부
            happy = True
        happy_status = {
            'is_happy' : happy,
            'count': review.happy_users.count(),
        }
        return JsonResponse(happy_status)
    return HttpResponse(status=401) #401은 로그인(인증)이 안 됨

def sad_review(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.sad_users.filter(pk=request.user.pk).exists():
            # 이모지 취소
            review.sad_users.remove(request.user)
            # 이모지 클릭 여부
            sad = False
        else:
            # 이모지 클릭
            review.sad_users.add(request.user)
            # 이모지 클릭 여부
            sad = True
        sad_status = {
            'is_sad' : sad,
            'count': review.sad_users.count(),
        }
        return JsonResponse(sad_status)
    return HttpResponse(status=401) #401은 로그인(인증)이 안 됨

def angry_review(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.angry_users.filter(pk=request.user.pk).exists():
            # 이모지 취소
            review.angry_users.remove(request.user)
            # 이모지 클릭 여부
            angry = False
        else:
            # 이모지 클릭
            review.angry_users.add(request.user)
            # 이모지 클릭 여부
            angry = True
        angry_status = {
            'is_angry' : angry,
            'count': review.angry_users.count(),
        }
        return JsonResponse(angry_status)
    return HttpResponse(status=401) #401은 로그인(인증)이 안 됨


# after signup --------------------------------------------------------------------
@require_GET
def after_signup(request):
    movies = list(Movie.objects.all())
    random_movies = random.sample(movies, 10)
    context = {
        'random_movies': random_movies,
    }
    return render(request, 'movies/after_signup.html', context)


    