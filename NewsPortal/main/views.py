from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import New
from django.views.generic import DetailView


def index(request):
    users = New.objects.all()
    paginator = Paginator(users, 2)  # показывать 25 объектов на странице
    page = request.GET.get('page')  # получить текущую страницу из параметров URL
    products = paginator.get_page(page)

    return render(request, 'index.html', context={'users': products, 'title': 'Мой сайт'})


def main(request):
    users = New.objects.all()
    return render(request, 'layout.html', {'users': users})


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class NewDetailView(DetailView):
    model = New
    template_name = 'detail.html'
    context_object_name = 'new'


from .forms import NewForms


def create(request):
    if request.method == 'POST':
        form = NewForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mytest')
    else:
        form = NewForms()

    return render(request, 'create_form.html', {'form': form})


from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


from django.views.generic import ListView
from django.views.generic.base import TemplateResponseMixin


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = New
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        return context


from django.http import HttpResponse

from django.http import HttpResponse

from django.http import HttpResponse
from django.http import HttpResponse


def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName', 'is your Cookies', max_age=None)
    return html


def showcookie(request):
    show = request.COOKIES.get('CookieName')
    if show:
        html = "Hello! {0}".format(show)
    else:
        html = "Cookie 'cookieName' is not set."
    return HttpResponse(html)


def deletecookie(request):
    html = HttpResponse("<h1>Cookies Deleted</h1>")
    html.delete_cookie('CookieName')
    return html


















def set_cookie(request):
    html = HttpResponse("<h1>Мой сайт</h1>")
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    html.set_cookie('visit_count', str(visit_count))
    return html

def show_counter(request):
    visit_count = request.COOKIES.get('visit_count', '0')
    return render(request, 'counter.html', {'visit_count': visit_count})