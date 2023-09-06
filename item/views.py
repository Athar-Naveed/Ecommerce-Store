from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Item,Category
from .forms import NewItemForm,EditItemForm
# Create your views here.

def browse_item(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    item = Item.objects.filter(is_sold=False)
    category = Category.objects.all()
    if category_id:
        item = item.filter(category_id=category_id)
    if query:
        item = item.filter(Q(name__icontains=query)|Q(description__icontains=query))

    return render(request,'item.html',{'items':item,'query':query,'category':category,'category_id':int(category_id)})

def detail(request,pk):
    item = get_object_or_404(Item,id=pk)
    related_item = Item.objects.filter(category=item.category,is_sold=False).exclude(id=pk)[0:5]
    return render(request,'detail.html',{'item':item,'related_items':related_item})

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request,'form.html',{'form':form,'title':'New Item'})

@login_required
def delete_item(request,pk):
    item = get_object_or_404(Item,id=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit_item(request,pk):
    item = get_object_or_404(Item,id=pk,created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request,'form.html',{'form':form,'title':'Edit Item'})