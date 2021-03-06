from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Prayer
from .forms import AddPrayerForm, AddCommentForm
from datetime import datetime
from django.views.generic import DeleteView

class DeletePrayerView(DeleteView):
    model = Prayer
    success_url = '/'
    template_name = 'prayers/delete_prayer.html'


def prayer_list(request):    
    prayers = Prayer.objects.order_by('publicatio')    
    context = {
            'prayers':prayers,
            'amenned_prayers':[],
        }    
    
    if request.user.is_authenticated:
        user_id = request.user.id        
        for prayer in prayers:
            if prayer.amens.filter(id=user_id).exists():
                context['amenned_prayers'].append(prayer.id)    
    
    return render(request,'prayers/prayers.html', context)

def add_prayer(request):
    if request.method == "POST":
        form = AddPrayerForm(request.POST)
        if form.is_valid:
            prayer = form.save(commit=False)
            prayer.poster = request.user
            prayer.publicatio = datetime.now()
            prayer.save()
            return redirect('home')
    else:
        form = AddPrayerForm()
        return render(request, 'prayers/edit_prayer.html', {'form': form})

def prayer_edit(request, pk):    
    prayer = get_object_or_404(Prayer, pk=pk)
    if prayer.poster == request.user:
        if request.method == "POST":
            form = AddPrayerForm(request.POST, instance=prayer)
            if form.is_valid:
                prayer = form.save(commit=False)
                prayer.poster = request.user
                prayer.publicatio = datetime.now()
                prayer.save()
                return redirect('home')
        else:
            form = AddPrayerForm(instance=prayer)
            return render(request, 'prayers/edit_prayer.html', {'form': form})
    else:
        return HttpResponse('Thou hast no right to edit this here prayer! Sinner!')

def handle_amen(request, pk):
    prayer = get_object_or_404(Prayer, pk=pk)    
    
    if prayer.amens.filter(id=request.user.id).exists():
        prayer.amens.remove(request.user)        
    else:
        prayer.amens.add(request.user)        
    
    return redirect('home')

def add_comment(request, pk):
    prayer = get_object_or_404(Prayer, pk=pk)
    form = AddCommentForm    
    if request.method == "POST":                        
        form = AddCommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)            
            comment.prayer = prayer
            comment.publicatio = datetime.now()
            comment.save()
            return redirect('home')        
    else:
        return render(request, 'prayers/add_comment.html', {'form': form, 'prayer':prayer})