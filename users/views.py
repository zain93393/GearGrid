from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userRegisterForm
from store.models import Ad
from django.views.generic import DetailView, ListView, CreateView
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! Login to continue')
            return redirect('login')
    else:
        form = userRegisterForm()
    return render(request, 'users/register.html',{'form':form})


class UserAdsListView(ListView):
    model = Ad
    template_name = 'users/profile.html'  # Create this template
    context_object_name = 'user_ads'
 

    def get_queryset(self):
        return Ad.objects.filter(seller=self.request.user)