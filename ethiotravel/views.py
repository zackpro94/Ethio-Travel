from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.
def index(request):
    
    dests = destination.objects.all()
    tips = best_tips.objects.all()
    intro = intros.objects.all()
    testimonial = testimony.objects.all()
    disc = discount.objects.all()
    return render(request, 'index.html', {"dests": dests, "tips": tips, 'intro': intro, 'testimonial': testimonial, 'disc': disc})

def dest_detail(request, post):
    
    post = get_object_or_404(destination, slug=post,)

    return render(request, 'destview.html', {'post' : post})

def about(request):

    return render(request, 'about.html')

def news(request):
    
    return render(request, 'news.html')


def contact(request):
    
    return render(request, 'contact.html')






    

