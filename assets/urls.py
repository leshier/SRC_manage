from django.urls import path
from assets import views

app_name = 'assets'

urlpatterns = [
    path('', views.index,name='index'),
    path('index/', views.index,name='index'),
    path('srclist/',views.srclist),
    path('add/',views.add),
    path('chksrcname/',views.chksrcname),
    path('chkcomname/',views.chkcomname),
    path('addsrc/',views.addsrc),
    path('addcom/',views.addcom),

    path('domain/',views.domain),
    path('ips/',views.ips),
    path('company/',views.company),
]