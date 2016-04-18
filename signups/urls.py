from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^designers',views.designers, name='designers'),
    url(r'shopfront', views.shopfront, name='shopfront'),
    url(r'^signup', views.signup, name='signup')

]

