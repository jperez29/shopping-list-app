# from django.http import HttpResponse
from collections import UserDict
from django.shortcuts import render
from .models import ItemList
from .forms import PostForm
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User

#adding method to delete item
def deleteItems(request, i):
    #deleting by the id, using i as a primary key to identify each item in shopping list
    item_lst = ItemList.objects.get(id = i)
    item_lst.delete()
    return HttpResponseRedirect('/items/') 
    
#deleting all items in list
def deleteAll(request):
    ItemList.objects.all().delete()
    return HttpResponseRedirect('/items/')

def list_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            total_items = ItemList.objects.all()
            #rendering a form so that the user can submit new items to list
            form = PostForm()
            context = {
                'form': form,
                'total_items': total_items
            }
            return render(request, 'shopping_list.html', context)
    else:
        '''if request is "GET", then sending a form to user along with previous 
        submitted items in shopping list'''
        form = PostForm()
        total_items = ItemList.objects.all()
        context = {
            'form': form,
            'total_items': total_items
        }
        return render(request, 'shopping_list.html', context)


def home(request):
    #showing users the homepage 
    return render(request, 'home.html')

