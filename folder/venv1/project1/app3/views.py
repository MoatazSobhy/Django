from django.shortcuts import render
from .models import *
from .forms import *
# # Create your views here.
# def index3(request):
#     # print(request.POST.get('username'))
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     # data = Login(user_name=username, user_password=password)
#     # data.save()
    
#     # Ensure both username and password are provided
#     if username and password:
#         # data = Login(user_name=username, user_password=password)
#         data.save()
#     else:
#         # Optionally handle the case where data is missing
#         return render(request, 'app3/index3.html', {'error': 'Both fields are required'})
    
#     return render(request, 'app3/index3.html', {'lf':LoginForm})

# CHAT Solution
def index3(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['user_name']
            # password = form.cleaned_data['user_password']

            # Assuming you have a model named Login to save the data
            data = Login(user_name=username, user_password=password)
            data.save()

            return render(request, 'app3/index3.html', {'form': form, 'message': 'Login successful'})
        else:
            return render(request, 'app3/index3.html', {'form': form, 'error': 'Both fields are required'})
    else:
        form = LoginForm()

    return render(request, 'app3/index3.html', {'form': form})