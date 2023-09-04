from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    """ A view to return the index page"""
    return render (request, 'home/index.html')




# @login_required
# def admin_dashboard(request):
# # Check if the user is an admin (superuser)
#     if not request.user.is_superuser:
#         return HttpResponseForbidden("You are not authorized to access this page.")

#     # Your admin-only dashboard logic here
#     # This is where you can retrieve data, perform operations, and render the dashboard template

#     # Example: Get a list of all users (for demonstration purposes)
#     all_users = User.objects.all()

#     # Example: Render the admin dashboard template with user data
#     return render(request, 'admin_dashboard.html', {'users': all_users})
 