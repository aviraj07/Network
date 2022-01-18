# Network
It is a webapp that lets people connect with each other.

<br>
<a href="https://avigram.herokuapp.com/">See it in action.</a>

## Installation
- You need to have **Django** installed on your local machine.
- Download this zip code.
- Go into this project's directory and run `python(or python3) manage.py runserver`.
- You'll be able to run the application.
- To install django on your machine, [click here](https://docs.djangoproject.com/en/3.2/topics/install/).
- To link database to your webapp run `python(or python3) manage.py makemigrations auctions` and then `python(or python3) manage.py migrate`.

## Usage
- After running the application, you need to register (if you're new a user) to use the webapp but you can view all posts without registering.
- Then the index page will load which contains all the posts and the likes each got. If you log in you'll see the **New Post** field where you can type the thing you want to post.
- You have the option to like each other's post and you can edit you post's content whenever you want.
- You can follow/unfollow people by visiting their profile (by clicking on their name).
- Their is a **Following** section where you can view the posts made by the people you're following.

## Structure/Design of program
This is a real time chat app. It is coded in Django and Javascript. HTML and CSS are used for styling and layout purposes.
<br>
Main files:
<br>
* *manage.py* - It contains all the required configurations to run your webapp.
* *network/static* - It includes the required styling css page and javascript to help user to have a good experience of the webapp.
* *network/templates* - These include all the html pages of the webapp from a basic layout file to each and every html page of the webapp.
* *network/models.py* - It contains all the database tables that django will handle to store information in it. The **Post**, **LikedPosts**, **UserFollowing** tables are included in this. **Post** will contain all the posts that people create, **LikedPosts** it contains the liked a certain post has, and **UserFollowing** contains the relation between users to know which user has how many followers/following.
* *network/views.py* - It contains all the logic behind rendering the required pages upon request and acting as a mediator between databse and user. 
* *network/urls.py* - It has all the urls that a user can request to visit the pages of the webapp.

There are other supporting files as well.


![Preview](./ezgif.com-gif-maker(1).gif)


