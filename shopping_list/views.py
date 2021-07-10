# from django.http import HttpResponse
from django.shortcuts import render
from .models import ItemList
from .forms import PostForm
from django.http import HttpResponseRedirect 

#handling the post request, making sure we're saving data to database
# def addListView(request):
#     shopping_item = request.POST['content']
#     new_shopping_item = ItemList(item = shopping_item)
#     new_shopping_item.save()
#     #redirecting it to the main path 
    # return HttpResponseRedirect('/')

#adding method to delete item
def deleteItems(request, i):
    #deleting by the id, using i as a primary key to identify each item in shopping list
    item_lst = ItemList.objects.get(id = i)
    item_lst.delete()
    return HttpResponseRedirect('/') 
    
#deleting all items in list
def deleteAll(request):
    ItemList.objects.all().delete()
    return HttpResponseRedirect('/')

def list_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            total_items = ItemList.objects.all()
            form = PostForm()
            context = {
                'form': form,
                'total_items': total_items
            }
            return render(request, 'shopping_list.html', context)
    else:
        form = PostForm()

    total_items = ItemList.objects.all()
    context = {
        'form': form,
        'total_items': total_items
    }
    return render(request, 'shopping_list.html', context)
    # return render(request, 'shopping_list.html', {'form':form})
        # total_items = ItemList.objects.all
        # return render(request, 'shopping_list.html', {'total_items': total_items})
    #obtaining all items from ItemList and saving it in a variable called total_items
    # total_items = ItemList.objects.all()
    # if request.method == 'GET':
    #     form = PostForm()
    # else:
    #     form = PostForm(request.POST)

    # return render(request, 'shopping_list.html', context = {'total_items': total_items})

