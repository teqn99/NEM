# FINAL PROJECT

## 1. 팀 정보

### (1) 팀원 정보

- 팀장: 김태균
- 팀원: 안채현

### (2) 세부 일정

| 일자      |                                                              |
| --------- | ------------------------------------------------------------ |
| 11/17(수) | - ERD 작성(ErdCloud) <br/>- 프로토타이핑 (JustinMind)<br/>- API 선정(TMDB) <br/>- TMDB API를 이용하여 데이터 수집 및 DB 저장<br/>- 특정 영화와 유사한 장르의 영화들을 추천<br/> |
| 11/18(목) | - TMDB API를 이용하여 데이터 수집 및 DB 저장<br/>- 특정 영화와 유사한 장르의 영화들을 추천<br/>- Movie Index/Detail페이지 기능 구현<br/>- django + javascript를 이용한 영화 검색<br/> |
| 11/19(금) | - 랜덤 영화 추천페이지(after_signup)<br/>- 유사장르 영화 추천페이지(first_recommend)<br/>- 좋아요한 영화 장르 워드클라우드 기능<br/>- 리뷰 기능 및 반응 구현<br/>- 프로필 페이지에서 유저와 관련된 정보 활용<br/>- 프로필 사진<br/> |
| 11/22(월) | - detail.html 함께 작업<br/>- index.html 디자인<br/>- 소셜로그인 기능 구현<br/>- profile.html 디자인<br/> |
| 11/23(화) | - login, signup.html 디자인<br/>- after_signup.html 디자인<br/>- first_recommend.html 디자인<br/> |
| 11/24(수) | - index.html 애니메이션 <br/>- main 페이지 함께 작업<br/>- review.html 디자인 <br/> |
| 11/25(목) | - Readme, ppt 발표자료 정리                                  |



### (3) 업무 분담 내역

| 김태균                                                       | 안채현                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - TMDB API를 이용하여 데이터 수집 및 DB 저장<br/>- 특정 영화와 유사한 장르의 영화들을 추천<br/>- index/detail페이지 기능<br/>- 랜덤 영화 추천페이지(after_signup)<br/>- 유사장르 영화 추천페이지(first_recommend)<br/>- 좋아요한 영화 장르 워드클라우드 기능<br/>- detail.html 함께 작업<br/>- index.html 디자인<br/>- login, signup.html 디자인<br/>- after_signup.html 디자인<br/>- index.html 애니메이션<br/>- main 페이지 함께 작업 <br/> | - ERD 작성<br/>- 모델링<br/>- 영화 검색<br/>- 리뷰 기능 및 반응 구현<br/>- 프로필 페이지에서 유저와 관련된 정보 활용<br/>- 프로필 사진<br/>- 소셜로그인 기능<br/>- detail, profile.html 디자인<br/>- signup.html 디자인<br/>- first_recommend.html 디자인<br/>- review.html 디자인 <br/>- main 페이지 함께 작업 <br/> |



## 2. 목표

### (1) 프로젝트 목표

- 영화 정보 기반 추천 서비스 구성
- 커뮤니티 서비스 구성
- HTML, CSS, JavaScript, (Vue.js), Django, (REST API), DataBase 등을 활용한 실제 서비스 설계
- (서비스 관리 및 유지보수)



### (2) 목표 서비스 구현 및 실제 구현 정도

#### (2)-1 기본 구현 기능

|                  | 목표 서비스                                                  | 구현 여부 |
| ---------------- | ------------------------------------------------------------ | --------- |
| A. 관리자 뷰     | i. 관리자 권한의 유저만 영화 등록/수정/삭제 권한을 가집니다.<br/>ii. 관리자 권한의 유저만 유저 관리 권한을 가집니다.<br/>iii. 장고에서 기본적으로 제공하는 admin 기능을 이용하여 구현합니다.<br/>iv. Vue.js를 활용하는 경우에도 Django admin기능을 이용하여 구현할 수 있습니다. | V         |
| B. 영화 정보     | i. 영화 정보는 Database Seeding을 활용하여 최소 50개 이상의 데이터가<br/>존재하도록 구성해야 합니다.<br/>ii. 모든 로그인 된 유저는 영화에 대한 평점 등록/수정/삭제 등을 할 수 있어야 합니다. | V         |
| C. 추천 알고리즘 | i. 평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 합니다.<br/>ii. 추천 알고리즘의 지정된 형식은 없으나, 사용자는 반드시 최소 1개 이상의 방식으로<br/>영화를 추천 받을 수 있어야 합니다.<br/>iii. 추천 방식은 각 팀별로 자유롭게 선택할 수 있으며 어떠한 방식으로 추천 시스템을<br/>구성했는지 설명할 수 있어야 합니다. | V         |
| D. 커뮤니티      | i. 영화 정보와 관련된 대화를 할 수 있는 커뮤니티 기능을 구현해야 합니다.<br/>ii. 로그인한 사용자만 글을 조회/생성할 수 있으며 작성자 본인만 글을 수정/삭제<br/>할 수 있습니다.<br/>iii. 사용자는 작성된 게시 글에 댓글을 작성할 수 있어야 하며, 작성자 본인만 댓글을<br/>삭제할 수 있습니다.<br/>iv. 각 게시글 및 댓글은 생성 및 수정 시각 정보가 포함되어야 합니다. | V         |
| E. 기타          | i. 최소한 5개 이상의 URL 및 페이지를 구성해야 합니다.<br/>ii. HTTP Method와 상태 코드는 상황에 맞게 적절하게 반환되어야 하며,<br/>필요에 따라 메시지 프레임워크 등을 사용하여 에러 페이지를 구성해야 합니다.<br/>iii. 필요한 경우 Ajax를 활용한 비동기 요청을 통해 사용자 경험을 향상 시켜야 합니다. | V         |

#### (2)-2 추가적인 목표 기능

| 추가 목표 서비스         | 실제 구현 정도                                               |
| ------------------------ | ------------------------------------------------------------ |
| 장르별 워드클라우드 구현 | 사용자가 좋아요한 영화들의 장르를 분석하여 워드클라우드 시각화 |
| 영화 추천                | 컨텐츠 필터링 기반 연관 장르별 추천 기능                     |
| 유튜브 트레일러 기능     | TMDB의 API를 통해 movie id를 이용하여 유튜브 트레일러 경로 수집 |
| 프로필 사진              | STATIC, MEDIA 경로를 생성하여 기본 이미지 및 사용자가 등록한 프로필 사진을 저장 |
| 소셜 로그인              | Google 및 Github 로그인 기능 구현                            |
| 리뷰 감정 반응           | 리뷰에 감정 이모지를 통해 반응                               |
| 영화 검색                | Ajax를 활용한 비동기 요청을 통해 검색어 입력 시 실시간 검색 결과 출력 |
| 메인 페이지              | CSS를 활용하여 NEM 메인 페이지 디자인                        |



## 3. 데이터베이스 모델링 (ERD)



<img src="final_pjt_README.assets/image-20211125130746009.png" alt="image-20211125130746009"  />



## 4. 개발 환경

> A. 언어
> 	i. Python 3.8+
> 	ii. Django 3.x
> 	(iii. Node.js LTS)
> 	(iv. Vue.js 2.x)
>
> B. 도구
> 	i. VSCode
> 	ii. Chrome Browser
>
> C. 아키텍처 (택 1)
> 	i. Django & Vanila JS
> 	(ii. Django REST API 서버 & Vue.js)
>
> D. 사용한 Tools
> 	i. Git
> 	ii. Just in mind
> 	iii. Kakao Oven
> 	iv. ERD Cloud
> 	v. Google Drive
> 	vi. Chrome Browser

### 4-1. 초기 세팅

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata movies/fixtures/genre_data.json
python manage.py loaddata movies/fixtures/director_data.json
python manage.py loaddata movies/fixtures/actor_data.json
python manage.py loaddata movies/fixtures/movie_data.json
python manage.py runserver
```



## 5. 기능에 대한 설명 (jpg, gif)

1. NEM 시작 페이지(main_page/mainpage.html)

   ![처음페이지](final_pjt_README.assets/처음페이지.jpg)

2. 로그인(accounts/login.html)

   ![로그인](final_pjt_README.assets/로그인.jpg)

3. 회원가입(accounts/signup.html)

   ![사인업](final_pjt_README.assets/사인업.jpg)

4. 취향분석(movies/after_signup.html)

   ![랜덤추천](final_pjt_README.assets/랜덤추천.jpg)

5. 추천영화(movies/first_recommend.html)

   ![추천](final_pjt_README.assets/추천.jpg)

6. 영화 메인(movies/index.html)

   ![인덱스](final_pjt_README.assets/인덱스.jpg)
   
   ![검색](final_pjt_README.assets/검색.jpg)



7. 영화 상세(movies/detail.html)

   ![디테일1](final_pjt_README.assets/디테일1.jpg)

   ![디테일2](final_pjt_README.assets/디테일2.jpg)

   ![리뷰감정](final_pjt_README.assets/리뷰감정.jpg)

   ![디테일3](final_pjt_README.assets/디테일3.jpg)

8. 리뷰작성(movies/review_create.html)

   ![리뷰작성](final_pjt_README.assets/리뷰작성.jpg)

9. 리뷰수정(movies/review_update.html)

   ![리뷰수정](final_pjt_README.assets/리뷰수정.jpg)

10. 프로필(accounts/profile.html)

    ![프로필1](final_pjt_README.assets/프로필1.jpg)

    ![프로필2](final_pjt_README.assets/프로필2.jpg)

    ![프로필3](final_pjt_README.assets/프로필3.jpg)

    ![프로필4](final_pjt_README.assets/프로필4.jpg)

    ![프로필5](final_pjt_README.assets/프로필5.jpg)

    ![프로필6](final_pjt_README.assets/프로필6.jpg)

11. 프로필 수정(accounts/profile_update.html)

    ![프로필 수정](final_pjt_README.assets/프로필 수정.jpg)

    ![프로필 수정오나료](final_pjt_README.assets/프로필 수정오나료.jpg)



## 6. 배포 서버 URL

보류



## 7. 느낀 점

- DB
- 
- 장고의 기본 authentication form만 사용하거나 부트스트랩에서 제공하는 기본 디자인만 사용해왔는데, 처음으로 회원가입을 위한 UserCreationForm과  로그인을 위한 AuthenticationForm을 장고 깃허브에 들어가서 구성 필드들을 확인해보면서 화면을 커스터마이징할 수 있었다. 



---

# 프로젝트 과정



## 1. 2021.11.17 (수)

### TODAY 목표

- 김태균

  * TMDB API를 이용하여 데이터 수집 및 DB 저장
  * 비슷한 장르의 영화들을 추천

- 안채현

  - ERD 작성, 모델링

### TODAY 오류 해결 과정

- 오류:

  ```
  OperationalError at /
  no such table: django_session
  ```

  - 해결:

    ```
    서버에서 위 에러 발생 시, db초기화(db.sqlite 삭제 및 init 제외 migration삭제) 후
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser 
    $ python manage.py loaddata
    $ python manage.py loaddata movies/fixtures/movies/cast.json
    $ python manage.py loaddata movies/fixtures/movies/genre.json
    $ python manage.py loaddata movies/fixtures/movies/movies.json
    $ python manage.py loaddata movies/fixtures/movies/users.json
    $ python manage.py runserver
    ```
  
    

- 오류:

  ```
  TypeError at /movies/
  Object of type date is not JSON serializable
  ```

  - 해결

    ```
    movies/models.py에 Movie 클래스의 fields 중, release_date 의 타입이 DateField인데,  Movie의 모든 필드를 가져오는 values()메서드를 사용하니, 이 date필드가 JSON으로 serialize 되지 않는 것 같다. 그래서 이 release_date 필드가 포함되지 않게, 가져올 필드(title, poster_path)만 values()안에 지정하니 위 서버에러가 해결되었다.
    
    # context["qs_json"] = json.dumps(list(Movie.objects.values()))
    context["qs_json"] = json.dumps(list(Movie.objects.values('title')))
    ```

    

- 오류:

  ```
  NOT NULL constraint failed
  ```

  - 해결

    ```
    API를 가져올 때 예를 들어 감독이 없는 경우는 movie-loader.py에서 제외했더라도, 빈 리스트로 들어오는 경우가 있는 듯했다. 그래서 models.py의 모든 필드에 null = True를 지정해주었다.
    ```

    

- 오류:

  ```
  json파일을 DB로 불러오는 과정에서 형식이 맞지 않아 에러가 발생하였다. 
  ```

  - 해결

    ```
    json파일을 구성할 때 한 딕셔너리 안에 "model", "pk", "fields" 형식으로 구성해야 함
    ```

    

### TODAY 결과사진

- 프로토타이핑

  ```
  - Just in Mind를 이용해서 대략적인 화면 구성을 해 보고, 왓챠피디아, 넷플릭스, 네이버 영화, TMDB사이트의 화면 구성을 보며 API요청시 어떤 필드들이 필요할 지 조합할 수 있는 계기가 되었다.
  ```

  

  - ![image-20211119025248188](final_pjt_README.assets/image-20211119025248188.png)
  - ![image-20211119025330822](final_pjt_README.assets/image-20211119025330822.png)

- cast, director, trailer 정보를 포함하여 602개의 영화 데이터를 fixture 폴더에 저장

  - movies/fixtures/actor_data2.json

    ![image-20211125220545272](final_pjt_README.assets/image-20211125220545272.png)

  - movies/fixtures/director_data2.json

    ![image-20211125220627360](final_pjt_README.assets/image-20211125220627360.png)

  - movies/fixtures/genre_data2.json

    ![image-20211125220701642](final_pjt_README.assets/image-20211125220701642.png)

  - movies/fixtures/movie_date2.json

    ![image-20211125220737493](final_pjt_README.assets/image-20211125220737493.png)

---



## 2. 2021.11.18(목)

### TODAY 목표

- 김태균

  * Movie Index/Detail페이지 기능 구현
  
- 안채현

  - django + javascript를 이용한 영화 라이브 필터검색 
  
    

### TODAY 오류 해결 과정

- 오류: next parameter

  - 해결 

    ```
    최종 리다이렉트하는 주소와 연결된 뷰함수에 @login_required 데코레이션
    원래 쓰려던 기능/버튼의 urㅣ태그에 최종 리다이렉트 주소로 적어주어야 한다. (accounts:login X )
    ```

    


### TODAY 결과사진

- movies/index.html

  ![image-20211125222516385](final_pjt_README.assets/image-20211125222516385.png)

- movies/detail.html

  ![image-20211125222541195](final_pjt_README.assets/image-20211125222541195.png)

- movies/index.html

  ![image-20211125222646653](final_pjt_README.assets/image-20211125222646653.png)



----



## 3. 2021.11.19(금)

### TODAY 목표

- 김태균

  * after_signup 10개 랜덤 영화 추천페이지
  * first_recommend에서 after_signup에서 선택한 영화를 기반으로 한 영화당 3개의 유사장르 영화 추천
  * 워드클라우드 

- 안채현

  - 리뷰 기능 및 반응 구현
  
  - 프로필 페이지에서 유저와 관련된 정보 활용
  
  - 프로필 사진
  
    

### TODAY 오류 해결 과정

- 오류: 

  ```
  AllAuth에러 해결방법
  
  $ source venv/Scripts/activate
  (venv) 
  $ pip install -r requirementx.txt
  $ python manage.py migrate
  $ python manage.py runserver
  
  auth_login(request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
  ```
  
  - 해결:
  
    ```
    - venv환경에서 requirements.txt 해두면, 다음 vs코드 닫았다가 열 때는 source venv/S/a만 해주면 다시 install 안 해도 되었다.
    - admin페이지에서 key 과 secret 등록해주었다.
    ```
    
    

### TODAY 결과사진

- movies/after_signup.html

  ![image-20211125222322758](final_pjt_README.assets/image-20211125222322758.png)

  ![image-20211125222345175](final_pjt_README.assets/image-20211125222345175.png)

- movies/first_recommend.html

  ![image-20211125222418678](final_pjt_README.assets/image-20211125222418678.png)

- accounts/profile.html

  ![image-20211125223011072](final_pjt_README.assets/image-20211125223011072.png)

  ![image-20211125223031685](final_pjt_README.assets/image-20211125223031685.png)

- movies/detail.html

  ![image-20211125222903692](final_pjt_README.assets/image-20211125222903692.png)

------



## 4. 2021.11.22(월)

### TODAY 목표

- 김태균

  * detail.html 함께 작업
  * index.html 디자인
  
- 안채현

  - 소셜로그인
  
  - detail, profile.html 디자인
  
    

### TODAY 오류 해결 과정

- 오류:

  ```
  include 태그를 이용해서 같은 태그명/JS변수명을 사용하는 carousel html을 accounts/profile.html이나 movies/detail.html에서 중복 사용할 때, 기존 profile, detail.html에서 구성된 변수와 태그의 스타일과 carousel html의 변수명 혹은 태그명이 동일할 때, css스타일 등이 의도치 않게 함께 적용되었다. 
  ```

  - 해결:

    ```
     충돌하지 않도록 태그명과 변수명이 겹치면 모두 변경해 줘야 했다.
    ```
  
    

- 오류:

  ```
  Carousel 4개 이하일 때 뒤로가지 않거나, 마지막 페이지에서 잘렸던 것
  ```

  - 해결

    ```
    한 움직임의 길이와 총 길이를 조정해주고 1페이지일 때 설정을 달리해주었다.
    ```
  
    



### TODAY 결과사진

- movies/index.html

  <img src="final_pjt_README.assets/image-20211123085403758.png" alt="image-20211123085403758" style="zoom:50%;" />

  <img src="final_pjt_README.assets/image-20211123085443144.png" alt="image-20211123085443144" style="zoom:33%;" />

- accounts/profile.html

  <img src="final_pjt_README.assets/image-20211123085254370.png" alt="image-20211123085254370" style="zoom:33%;" />

  <img src="final_pjt_README.assets/image-20211123084455625.png" alt="image-20211123084455625" style="zoom:33%;" />

- movies/detail.html

  <img src="final_pjt_README.assets/image-20211123084606954.png" alt="image-20211123084606954" style="zoom:33%;" />

  <img src="final_pjt_README.assets/image-20211123090007842.png" alt="image-20211123090007842" style="zoom:33%;" />



---



## 5. 2021.11.23(화)

### TODAY 목표

- 김태균

  * login, signup.html 디자인
  * after_signup.html 디자인

  

- 안채현

  - signup.html 디자인
  - first_recommend.html 디자인
  
    

### TODAY 오류 해결 과정

- 오류:

  ```
  overview같은 경우 json 파싱이 잘 되지 않아 다른 필드들을 불러오는 데에도 영향을 미쳤다. 
  ```

  - 해결:

    ```
    # context["qs_json"] = json.dumps(list(Movie.objects.values('title')))
    context["qs_json"] = json.dumps(list(Movie.objects.values()))
    
    위와 같이 value() 안에 문제없이 가져올 수 있는 필드명만 지정해주었다.
    ```

    

- 오류:

  ```
  innerHtml에 a태그를 넣는 형식이 달라 오류가 발생했다.
  ```

  - 해결:

    ```
    box.innerHTML += `<a href="{% url 'movies:detail' ${movie['id']} %}"><b>${movie['title']}</b></a><br>`
    ```

    



### TODAY 결과사진

- movies/after_signup.html

  ![image-20211125215449574](final_pjt_README.assets/image-20211125215449574.png)

- movies/first_recommend.html

  ![image-20211125215601708](final_pjt_README.assets/image-20211125215601708.png)

- signup.html

  ![image-20211124231710190](final_pjt_README.assets/image-20211124231710190.png)

- login.html

  ![image-20211124231750084](final_pjt_README.assets/image-20211124231750084.png)



------



## 6. 2021.11.24(수)

### TODAY 목표

- 김태균

  * index.html 애니메이션
  * main 페이지 함께 작업

- 안채현

  - review.html
  
  - main 페이지 함께 작업
  
    

### TODAY 오류 해결 과정

- 오류: 

  ```
  - Profile화면을 구성하면서 좋아요한 배우와 감독을 나열하기 위해 carousel을 사용했는데, 화면을 확대하거나 축소할 때 프로필 이미지의 비율이 변동되었다. 
  ```

  - 해결:

    ```
    css에서 min-width나 min-height가 적용된 부분을 지워주었다.
    ```
    




### TODAY 결과사진

- movies/index.html

  - 카드에 마우스 호버 시 앞으로 튀어나오는 효과 

- review_create.html

  ![image-20211125215228152](final_pjt_README.assets/image-20211125215228152.png)

- review_update.html

  ![image-20211125215332296](final_pjt_README.assets/image-20211125215332296.png)

- main_page/mainpage.index

  ![image-20211125214611448](final_pjt_README.assets/image-20211125214611448.png)

  
