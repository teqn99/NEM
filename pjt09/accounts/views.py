from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from wordcloud import WordCloud

from .forms import CustomUserChangeForm, CustomUserCreationForm
# 유저프로필
# movies앱에서 Review모델 (ScoreCalc)
from movies.models import Review
from django.db.models import F, Sum, FloatField, Avg    #score계산위한

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:main-view')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('movies:after_signup')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:main-view')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get('next') or 'movies:main-view')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:main-view')


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # for wordcloud
    if len(person.like_movies.all()) > 0:
        movies = person.like_movies.all()
        genres_list = ''
        for m in movies:
            genres = m.genres.all()
            for g in genres:
                genres_list += g.genre_name + ' '
        wc = WordCloud(font_path='accounts/fonts/NanumGothic-Bold.ttf', \
                    background_color='white',\
                    width=1000, height=500, max_font_size=300).generate(genres_list)
                    # width=700, height=500, max_font_size=300).generate(genres_list)
                    # width=300, height=200, max_font_size=100).generate(genres_list)
                    # width=100, height=80, max_font_size=50).generate(genres_list)
        wc.to_file(f'accounts/static/wc/wc_{person.username}.png')

    # print(person)   #admin
    # print(person.pk)    #1
    score_avg = 0
    # 프로필페이지에 띄울, 해당 유저가 남긴 모든 리뷰의 평균
    # X list에는 aggregate쓸 수 없다는 에러 / reviews = get_list_or_404(Review, user_id=person.pk).aggregate(average=Avg('score'))
    if len(Review.objects.filter(user_id=person.pk)) > 0:   #평점을 부여한 적이 없는 경우, NoneType에 대해서는 average계산불가하므로
        reviews_avg = Review.objects.filter(user_id=person.pk).aggregate(average=Avg('score'))
        # print(reviews_avg)  #{'average': 5.333333333333333}
        # print(round(reviews_avg['average'], 2)) #5.33
        score_avg = round(reviews_avg['average'], 2)
    # reactions 개수
    reactions_count = len(person.happy_reviews.all()) + len(person.sad_reviews.all()) + len(person.angry_reviews.all())
    # favorite movie figures
    figures_count = len(person.like_director.all()) + len(person.like_actor.all())
    context = {
        'person': person,
        'score_avg': score_avg,
        'reactions_count' : reactions_count,
        'figures_count': figures_count,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                followed = False
            else:
                person.followers.add(user)
                followed = True
        follow_status = {
            'followed': followed,
            'followersCount': person.followers.count(),
            'followingsCount': person.followings.count(),
        }
        return JsonResponse(follow_status)
    return HttpResponse(status=401)
    # return redirect('accounts:profile', person.username)


@login_required
@require_http_methods(['GET', 'POST'])
def profile_update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, files=request.FILES, instance=request.user)  #이미지도 같이 받음
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/profile_update.html', context)
