from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def home_page(request):
    return render(request, 'home.html')
def new_list(request):
    return redirect('/lists/the-only-list-in-the-world/')