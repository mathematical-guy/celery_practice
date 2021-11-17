from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from  .tasks import create_random_user_accounts
from .forms import GenerateRandomUserForm



def generate_users(request):
    if request.method == "GET":
        form = GenerateRandomUserForm()
    else:
        form = GenerateRandomUserForm(request.POST)
        if(form.is_valid()):
            total = form.cleaned_data['total']
            form = GenerateRandomUserForm()
            create_random_user_accounts.apply_async(args=(total,))
    
    context = {
        'form': form,
    }
    template_name = 'app/generate_users.html'
    return render(request, template_name, context)




def users(request):
    template_name = 'app/users.html'
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)