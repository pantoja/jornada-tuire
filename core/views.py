from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from tuites.models import Tuite

def index(request):
    context = {
        'now': datetime.now(),
        'tuites': Tuite.objects.all(),
    }

    return render(request, 'home.html', context)








"""
    from django.shortcuts import render
    from django.http import HttpResponse
    from core.helpers import get_character_name, ip_info

    def index(request):
    country = ip_info('country_name')
    flag = ip_info('flag')
    flag_image = f'<img src="{flag}" />'

    context = {
    'my_name': 'banesa',
    'country': country,
    'flag': flag,
    }

    return render(request, 'index.html', context)
"""



"""
    from django.shortcuts import render
    from django.http import HttpResponse
    from core.helpers import get_character_name, ip_info
    from datetime import datetime

    def index(request):

        context = {
            'now': datetime.now(),
        }

        return render(request, 'index.html', context)
"""