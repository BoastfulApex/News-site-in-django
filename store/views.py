from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView


class ProfileLogin(LoginView):
    template_name = 'store/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('store')


def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def store(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    # return render(request, 'newsfeed/main.html', context)
    return render(request, 'store/store.html', context)


def cart(request, new_name):
    news = News.objects.filter(name=new_name)
    context = {
        'news': news
    }
    return render(request, 'store/cart.html', context)


def tags(request, new_tag, new_name):
    print('new_tag')
    news = News.objects.filter(tag=new_tag)
    context = {
        'news': news
    }
    return render(request, 'store/tags.html', context)


class NewsCreate(CreateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('add')


class NewsUpdate(UpdateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('store')


class NewsDelete(DeleteView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('store')


def news(request):
    context = {}

    # return render(request, 'newsfeed/main.html', context
    return render(request, 'newsfeed/newssss.html', context)

