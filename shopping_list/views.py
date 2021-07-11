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
            # form.save()
            fs= form.save()
            fs.user= request.user
            fs.save()
            # users = User.objects.all() 
            # current_user = request.user
            # print(f"printing current id {fs.user.id}")
            #Choices are: id, item, user, user_id
            total_items = ItemList.objects.all()
            print(total_items)
            form = PostForm()
            context = {
                'form': form,
                'total_items': total_items
            }
            return render(request, 'shopping_list.html', context)
    else:
        form = PostForm()
        total_items = ItemList.objects.all()
        current_user = request.user
        print(f"printing current id {current_user.id}")
        context = {
            'form': form,
            'total_items': total_items
        }
        return render(request, 'shopping_list.html', context)


def home(request):
    print('rendering to home now')
    return render(request, 'home.html')

