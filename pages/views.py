from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    return HttpResponseRedirect("/listings/")

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_enabled': False,
        'show_garage': False,
        'show_bathrooms': False,
        'show_realtor': False,
        'show_featured': False,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)