from django.shortcuts import redirect

def login_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')  # Redirect to the login page if not logged in
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func