from unicodedata import category
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from category.models import category
from post.models import post
from users.models import users
from comment.models import comment
# home page function1
def HomePage(request):
    postData=post.objects.all()[:4]
    usersData=users.objects.all()
    categorydata=category.objects.all()
    # postData=post.objects.all()[:4]
    data={
        'four_news_post':postData,
        'categorydata':categorydata,
        'usersData':usersData,
    }
    return render (request,"index.html",data)
# about us page function
# def AboutPage(request):
#     return render (request,"aboutus.html")
# world page function
def categoryNews(request,pageId):
    categorydata=category.objects.all()

    name_news_post=category.objects.filter(id=pageId)
    postData=post.objects.filter(p_category=pageId)[:2]
    all_news_post=post.objects.filter(p_category=pageId)

    usersData=users.objects.all()
    data={
        'four_news_post':postData,
        'all_news_post':all_news_post,
        'categorydata':categorydata,
        'name_news_post':name_news_post,
        'usersData':usersData,
        'pageId':pageId,
    }
    return render (request,"world.html",data)
# travel page function
# def TravelPage(request):
#     return render (request,"travel.html")
# # politice page function
# def PoliticsPage(request):
#     return render (request,"politics.html")
# # fashion page function
# def FashionPage(request):
#     return render (request,"fashion.html")
# # busniess page function
# def BusniessPage(request):
#     return render (request,"business.html")
# # art page function
# def ArtPage(request):
#     return render (request,"art.html")
# # sports page function
# def SportPage(request):
#     return render (request,"sports.html")
# # real-eastet page function
# def RealPage(request):
#     return render (request,"real-estate.html")
# news-post page function
def Login(request):
    return render (request,"Login.html")
# SignUp page function
def SignUp(request):
    return render (request,"SignUp.html")
# # contact page function
def ContactPage(request):
    # if request.method=='post':
    #     username=request.POST.get("username")
    #     email=request.POST.get("email")
    #     Details=request.POST.get("Details")
    #     comment_insert=comments(cmnt_name=username,cmnt_email=email,cmnt_details=Details)
    #     comment_insert.save()
    #     print(username)
    postData=post.objects.all()[:4]
    usersData=users.objects.all()
    categorydata=category.objects.all()
    # postData=post.objects.all()[:4]
    data={
        'four_news_post':postData,
        'categorydata':categorydata,
        'usersData':usersData,
    }
    return render (request,"contactus.html",data)
# # author page function
# def AuthorPage(request):
#     return render (request,"author.html")

def date(request):
    postDate=post.objects.all();
    data={
        'postData':postDate,
    }
    return render("header.html",data);

def singlePage(request,singleID):
    postData=post.objects.filter(id=singleID)[:1]
    usersData=users.objects.all()
    categorydata=category.objects.all()
    # postData=post.objects.all()[:4]
    data={
        'single_news_post':postData,
        'categorydata':categorydata,
        'usersData':usersData,
    }

    if request.method=='post':
        username=request.post.get("username")
        email=request.post.get("email")
        Details=request.post.get("Details")
        comment_insert=comment(cmnt_name=username,cmnt_email=email,cmnt_details=Details)
        # comment_insert.save()
        print(username)
    return render(request,"single.html",data)

# top menu function
def NavigationMenu(request):
    categoryData=category.objects.all();
    Data={
        'category':categoryData,
    }
    return render(request,"index.html",categoryData[0].c_name)
