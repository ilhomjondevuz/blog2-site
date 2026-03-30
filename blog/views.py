from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blogs/home.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blogs/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'author', 'summary', 'content', 'photo', ]
    success_url = reverse_lazy('home')
    template_name = 'blogs/article_create.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_create'] = False
        return context

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blogs/article_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_delete'] = False
        return context

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'author', 'summary', 'content', 'photo', ]
    success_url = reverse_lazy('home')
    template_name = 'blogs/article_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context