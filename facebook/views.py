from django.shortcuts import render, redirect

# Create your views here.

from facebook.models import Article
from facebook.models import Comment


def remove_feed (request, pk) :
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' :
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
    return render (request, 'remove_feed.html', {'feed':article})

def edit_feed (request, pk) :
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' :
        if article.password == request.POST['password']:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')

    return render (request, 'edit_feed.html',{'feed':article})

def new_feed (request) :
    if request.method == 'POST':
         new_article = Article.objects.create(
            author = request.POST['author'],
            title = request.POST['title'],
            text = request.POST['content'] +"감사합니다",
            password = request.POST['password'])

         return redirect (f'/feed/{ new_article.pk }')

    return render (request, 'new_feed.html')

def Newsfeed (request) :
    articles = Article.objects.all()
    return render(request, 'Newsfeed.html', {'articles':articles })

def detail_feed (request,pk) :
    article = Article.objects.get(pk=pk)

    # 코멘트 데이터를 받아서 등록
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password'],
        )

    return render (request,'detail_feed.html', {'feed':article})





def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    myname = '곽혜인'
    age = 23
    global count
    count = count + 1

    diary = ['10월 3일 -  스터디를 했다', '10얼 4일 - 학교 가기 싫다', '10월 5일 - 축제 힘들어','이건추가']

    if age > 19:
        status = '성인'
    else:
        status = '민짜'

    return render(request, 'play2.html', { 'name': myname, 'count': count, 'status' : status,
                                           'diary' : diary})

def HelenKwak(request):

    return render(request,'HelenKwak.html')

count=0
def event(request):
    global count
    count=count+1
    if count == 25:
        status = '당첨되셨습니다.'
    else:
        status = '넌 당첨 아니야!'

    name = '곽혜인'
    return render(request, 'event.html', {'name': name, 'count' : count, 'status' : status})