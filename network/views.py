from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt 

def index(request):
    followes = False
    profil = False
    indice = True
    if request.method == "POST":
        content = request.POST["Newpost"]
        Post.objects.create(user=request.user,content=content,date=datetime.datetime.now())

        return HttpResponseRedirect(reverse("index"))

    else:
        allPosts = Post.objects.all()
        allPosts = allPosts.order_by("-date")
        post_paginator = Paginator(allPosts, 10)
        page_number = request.GET.get('page')
        posts = post_paginator.get_page(page_number)
        likees = []
        likeposts = LikedPosts.objects.filter(user=request.user.username)

        for post in likeposts:
            likees.append(post.post)


        return render(request,"network/index.html",{
            "allPosts" : allPosts,
            "page":posts,
            "profil":profil,
            "indice": indice,
            "likees": likees
            })    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, name):
    followes = False
    likees = []
    likeposts = LikedPosts.objects.filter(user=request.user.username)

    for post in likeposts:
        likees.append(post.post)
    profil = True
    indice = False
    user = User.objects.get(username=name)
    ID = User.objects.get(username=name).id
    allPosts = Post.objects.filter(user=ID)
    allPosts = allPosts.order_by("-date")
    post_paginator = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    posts = post_paginator.get_page(page_number)
    followings = UserFollowing.objects.filter(user=name).all().count()
    followers = UserFollowing.objects.filter(following=name).all().count()
    owner = False
    if str(request.user) != name:
        owner = True

    

    alreadyFollow = True 
    try:
        UserFollowing.objects.get(user=request.user.username, following=name)
    except UserFollowing.DoesNotExist:
        alreadyFollow = False
    
           
    return render(request,"network/index.html",{
        "allPosts":allPosts, "following":followings, "owner":owner,"followers":followers, "name":name,"alreadyFollow":alreadyFollow,
        "page":posts,
        "profil":True,
        "indice":False,
        "likees": likees
    })    

    

def follow(request, name):
    UserFollowing.objects.create(user=request.user.username, following=name)

    return HttpResponseRedirect(reverse('profile',args=[name]))

def unfollow(request, name):
    user = UserFollowing.objects.get(user=request.user.username, following=name)
    user.delete()

    return HttpResponseRedirect(reverse('profile',args=[name]))


def following(request):
    likees = []
    likeposts = LikedPosts.objects.filter(user=request.user.username)

    for post in likeposts:
        likees.append(post.post)
    followes = True
    indice = False
    profil = False
    names = []
    users = UserFollowing.objects.filter(user=request.user.username).all()
    for user in users:
        names.append(user.following)

    allPosts = Post.objects.none()
    for name in names:
        allPosts |= Post.objects.filter(user=User.objects.get(username=name))

    post_paginator = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    posts = post_paginator.get_page(page_number)
    return render(request, "network/index.html",{
        "allPosts":allPosts,
        "page":posts,
        "indice":indice,
        "profil":profil,
        "followes":followes,
        "likees": likees
        })  

          
@csrf_exempt
def edit(request,id):
    if request.method == "POST":

        id = int(id)
        print(id)
        data = json.loads(request.body)
        content = data.get("content","")
        post = Post.objects.get(id=id)
        post.content = content
        post.save()

        return JsonResponse({"message":"Edited the post"},status=201)

    
def like(request, id):
    id = int(id)
    likedposts = LikedPosts.objects.create(user=request.user.username,post=id)
    liked = Post.objects.get(id=id) 
    liked.likes = liked.likes + 1
    liked.save()

    return HttpResponse("liked")


def unlike(request, id):
    id = int(id)
    unliked = LikedPosts.objects.get(user=request.user.username, post=id)
    unliked.delete()
    unlikes = Post.objects.get(id=id) 
    unlikes.likes = unlikes.likes - 1
    unlikes.save()

    return HttpResponse("unliked")    