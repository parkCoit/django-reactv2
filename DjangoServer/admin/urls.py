"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('muser/', include('muser.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from admin.views import hello

urlpatterns = [
    path('', hello),
    path("blog/auth", include('blog.blog_users.urls')),
    path("blog/comments", include('blog.comments.urls')),
    path("blog/posts", include('blog.posts.urls')),
    path("blog/tags", include('blog.tags.urls')),
    path("blog/views", include('blog.views.urls')),

    path("mplx/cinemas", include('multiplex.cinemas.urls')),
    path("mplx/movie", include('multiplex.movies.urls')),
    path("mplx/showtimes", include('multiplex.showtimes.urls')),
    path("mplx/theater_tickets", include('multiplex.theater_tickets.urls')),
    path("mplx/theaters", include('multiplex.theaters.urls')),

    path("shop/carts", include('shop.carts.urls')),
    path("shop/categories", include('shop.categories.urls')),
    path("shop/deliveries", include('shop.deliveries.urls')),
    path("shop/orders", include('shop.orders.urls')),
    path("shop/products", include('shop.products.urls')),
    path("stroke", include('stroke.urls')),
    path("dlearn", include("dlearn.urls")),
    path("webcrawler", include("webcrawler.urls")),
    path("nlp", include("nlp.samsung_report.urls")),
    path("nlp", include("nlp.imdb.urls"))
]
