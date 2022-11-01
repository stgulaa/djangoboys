from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# from 다음에 있는 마침표(.)는 현재 디렉토리 또는 애플리케이션
from .models import Post
from django.utils import timezone
from .forms import PostForm

# post_index 뷰(view)
def post_index(request):
    return render(request, 'blog/post_index.html', {})


# post_list 뷰(view)
def post_list(request):
    # posts 라는 쿼리셋 선언하면서 결과 받아옴
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# 게시물 상세 페이지 처리 핸들러(뷰)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# 게시물 작성 폼을 보여주는 핸들러(뷰 메소드) 추가
# 폼을 불러올때, submit할때, 둘다 이 뷰를 사용함.
# 이때 request에는 우리가 입력했던 데이터들이 들어있음.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)  # POST 메시지 바디에 입력되는 값을 가는 객체 생성
        if form.is_valid():  # 폼이 유효하다면
            post = form.save(commit=False)  # 임시 저장하여 post 객체를 리턴받는다.
            post.author = request.user
            post.published_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            post.save()  # 데이터를 실제로 저장한다.
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    # return 문은 else: 와 같은 레벨이어야 함!!
    return render(request, 'blog/post_edit.html', {'form': form})


# 게시물 수정 뷰
# url로 부터 추가로 pk 매개변수를 받아서 처리
# get_object_or_404(Post, pk=pk)를 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)를 가져옵니다.
# 즉, pk 로 원하는 글을 찾는다.
# 이렇게 가져온 데이터를 수정 폼을 띄울때 보여주고 또 저장할 때도 이 메소드(뷰)를 사용해서 처리한다.
def post_edit(request, pk):
    # 수정하고자 하는 글의 게시물에 해당하는 Post 모델 인스턴스(instance)를 데이터베이스에서 가져옴
    post = get_object_or_404(Post, pk=pk)

    # 수정 화면의 내용을 저장할 때 처리
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)  # POST 메시지 바디에 입력되는 값을 갖는 객체 생성
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:   # 처음 수정폼을 띄워줄 때 처리
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})