
from django.urls import path
from .views import AdDetailView, AdListView, AdCreateView, AdUpdateView, AdDeleteView
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    # path('ads/',views.ads, name='store-ads'),
    path('<int:pk>/',login_required(AdDetailView.as_view()), name='store-detail'),
   
    path('ads/new', login_required(AdCreateView.as_view()), name="store-create"),
    path('ads/<int:pk>/update', login_required(AdUpdateView.as_view()), name='ad-update'),
    path('ad/<int:pk>/delete/', login_required(AdDeleteView.as_view()), name='ad-delete'),
    path('ads/', AdListView.as_view(), name="store-ads"),
    path('about/',views.about, name="store-about"),
    path('faq/',views.faq, name="store-faq"),
    path('contact/',views.contact, name="store-contact"),
    path('',views.home, name='store-home'),
    
]
