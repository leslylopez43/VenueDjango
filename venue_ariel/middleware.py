from django.http import HttpResponseForbidden

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check user's permissions or roles here
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized to access this page.")
        
        response = self.get_response(request)
        return response
