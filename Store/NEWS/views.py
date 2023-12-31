from django.shortcuts import render, redirect
from .models import Articles
from .forms import Articlesform
from django.views.generic import DetailView

# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView (DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == 'POST':
        form = Articlesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = Articlesform()
    data = {
         'form': form,
         'error' : error
    }
    return render(request, 'news/create.html', data)