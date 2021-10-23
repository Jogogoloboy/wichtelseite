from django.utils import timezone
from wishes.models import Phase

def time_now(request):
    return {'time_now': timezone.now()}

def wishing_phase(request):
    if Phase.objects.filter(name='Wishtime').exists():
        if Phase.objects.get(name='Wishtime').start_date <= timezone.now() <=  Phase.objects.get(name='Wishtime').end_date:
            return {'wishing_phase': 'Wishing on'}
        else: 
            return {'wishing_phase': ''}
    else: return {'wishing_phase': 'Wishing on'}

def selection_phase(request):
    if Phase.objects.filter(name='Selectiontime').exists():
        if Phase.objects.get(name='Selectiontime').start_date <= timezone.now() <=  Phase.objects.get(name='Selectiontime').end_date:
            return {'selection_phase': 'Selection on'}
        else: 
            return {'selection_phase': ''}
    else: return {'selection_phase': 'Selection on'}

def shipping_phase(request):
    if Phase.objects.filter(name='Shippingtime').exists():
        if Phase.objects.get(name='Shippingtime').start_date <= timezone.now() <=  Phase.objects.get(name='Shippingtime').end_date:
            return {'shipping_phase': 'Shipping on'}
        else: 
            return {'shipping_phase': ''}
    else: return {'shipping_phase': 'Shipping on'}