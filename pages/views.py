from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import AbstractUser, CustomUser
from .forms import View_bioForm

QUIZ_SIZE = 10

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def View_all(request):
    all = CustomUser.objects.all()
    return render(request, 'pages/view_all.html', locals())

def View_quiz(request):
    all = CustomUser.objects.all()
    quiz_size = QUIZ_SIZE
    return render(request, 'pages/view_quiz.html', locals())

def View_bio(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'pages/view_your_info.html', locals())

def Change_bio(request):
    if request.method == 'POST':
        form = View_bioForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

        print('clean, ',form['first_name'])
        print('clean, ',form['last_name'])
        print('clean, ',form['email'])
    else:
        form = View_bioForm()
    form = View_bioForm()
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'pages/view_your_info.html', locals())