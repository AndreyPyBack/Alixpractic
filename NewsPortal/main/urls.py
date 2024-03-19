from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [path('', views.index),
               path('setcookie/', views.setcookie, name='setcookie'),
               path('showcookie/', views.showcookie, name='showcookie'),
               path('del/',views.deletecookie,),
               path('setrrcookie/', views.set_cookie, name='cookier'),
               path('showcounter/', views.show_counter, name='show_counter'),
               path('products/', views.ProductListView.as_view(), name='product_list'),
               path('new/', views.main, name="mytest"),
               path('<int:pk>',
                    views.NewDetailView.as_view(), name='new'),
               path('create_form/', views.create, name='create_form'),
               path('signup/', views.register, name='signup'), ]
# path('login/', LoginView.as_view( template_name='registration/login.html'), name='login'),]
