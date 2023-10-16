from django.shortcuts import render
from django.views.generic import TemplateView
# Створіть свої представлення тут.
class HomePageView(TemplateView):
 def get(self, request, **kwargs):
     return render(request, 'index.html', context=None)

from django.views.generic import DetailView
from .models import Article

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'  # Шлях до шаблону
    context_object_name = 'article'  # Ім'я змінної в контексті шаблону