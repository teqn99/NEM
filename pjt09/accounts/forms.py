from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user, get_user_model
# 회원정보/프로필수정
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

# 회원정보수정( => 프로필수정 / 인스타처럼) / 여긴 비밀번호변경폼은 빼기
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_photo', 'bio', )

