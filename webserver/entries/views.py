from django.shortcuts import render
from entries.forms import FirstPage
from entries.models import entry 
from django.db import connection
 
def one(request):
    if request.method == 'POST':
        form = FirstPage(request.POST)
        if form.is_valid():
            cur_entry = request.POST.get('entry', '')
        entry_object = entry(entry=cur_entry)
        entry_object.save()
        all_entry = entry.objects.all()
        current_entry_query = "SELECT * FROM entries_entry where entry=\'"+cur_entry+"\';"
        with connection.cursor() as cursor:
           cursor.executescript(current_entry_query)
           ans = cursor.fetchone()
        
        return render(request, 'entries/one.html', {'entry_object': entry_object,'is_registered':True, 'form':form, 'all_entry':all_entry, 'current_user':ans, })
 
    else:
        form = FirstPage()
        return render(request, 'entries/one.html', {'form': form})
