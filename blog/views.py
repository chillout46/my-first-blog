from django.shortcuts import render
from django.utils import timezone # Post를 불러와서 정렬(filter)하는 데 사용되는 timezone.now() 함수를 쓰기 위해 불러옴
from .models import Post # /my-first-blog/blog/models.py 에서 Post 를 불러 옴

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #게시일(published_date) 기준으로 데이터베이스로부터 Post 글을 불러옴
    return render(request, 'blog/post_list.html', {'posts': posts}) # 매개변수 posts를 html에서 사용할 수 있게 추가: 이제부터 html에서 post 를 로드 가능 {{ post }}
