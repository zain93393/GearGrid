from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# Create your views here.

posts = [
    {
        'model':'Toyota Hilux Nano',
        'price':4000000,
        'year':2021,
        'transmission':'Manual',
        'city':'Islamabad'
    },
    {
        'model':'Suzuki cultus',
        'price':4000000,
        'year':2021,
        'transmission':'Manual',
        'city':'Islamabad'
    },
     {
        'model':'Suzuki ferari',
        'price':4000000,
        'year':2021,
        'transmission':'Manual',
        'city':'Islamabad'
    },
     {
        'model':'Suzuki ferari',
        'price':4000000,
        'year':2021,
        'transmission':'Manual',
        'city':'Islamabad'
    },
    
    
]


def home(request):
    context = {
        'posts':Ad.objects.all()
    }
    return render(request,'store/home.html',context)

def about(request):
    return render(request,'store/about_us.html')

def faq(request):
    return render(request,'store/FAQ.html')

def contact(request):
    return render(request,'store/contact_us.html')
# def ads(request):
#     context = {
#         'posts':Ad.objects.all()
#     }
#     return render(request,'store/ads.html',context)


class AdListView(ListView):
    model = Ad
    template_name = 'store/ads.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the location parameter from the URL
        location = self.request.GET.get('location')

        # If a location is provided, filter ads based on the location (case-insensitive)
        if location:
            queryset = queryset.filter(car_city__iexact=location)

        return queryset


    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the parameters from the URL
        car_company = self.request.GET.get('car_company')
        car_city = self.request.GET.get('car_city')
        transmission_type = self.request.GET.get('transmission_type')

        # Apply filters based on the selected parameters
        if car_company:
            queryset = queryset.filter(car_company=car_company)
        if car_city:
            queryset = queryset.filter(car_city=car_city)
        if transmission_type:
            queryset = queryset.filter(transmission_type=transmission_type)

        return queryset
   
class AdDetailView(DetailView):
    model = Ad
    template_name = 'store/product_description.html'
    context_object_name = 'posts'



class AdCreateView(CreateView):
    model = Ad
    template_name = 'store/ad_form.html'  # Replace 'your_app' with the actual app name
    fields = ['car_company', 'car_model', 'car_year', 'transmission_type', 'car_city', 'car_price', 'car_description', 'seller_number', 'image']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('store-ads')  # Redirect to the ads list view



class AdUpdateView(UpdateView):
    model = Ad
    template_name = 'store/ad_form.html'  # Replace 'your_app' with the actual app name
    fields = ['car_company', 'car_model', 'car_year', 'transmission_type', 'car_city', 'car_price', 'car_description', 'seller_number', 'image']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('store-ads')  # Redirect to the ads list view

class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'store/ad_confirm_delete.html'  # Create this template

    def get_success_url(self):
        return reverse_lazy('profile')