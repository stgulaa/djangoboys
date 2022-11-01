from django import forms
from .models import Post

#PostForm : 만들 폼의 이름(Post Model과 연결되는 폼)
#forms.ModelForm은 ModelForm이라는 것을 알려주는 구문
class PostForm(forms.ModelForm): #form 클래스를 상속받은 클래스
    #이 폼을 만들기 위해 어떤 model이 쓰여야하는지 장고에 알려주는 구문
    class Meta: #PostForm과 관련된 정보 설정
        model = Post #Post 모델과 연결
        fields = ('title', 'text',) # 이 폼에 나타낼 필드 지정