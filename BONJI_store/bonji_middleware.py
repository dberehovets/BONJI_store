from django.http import Http404
from django.urls import reverse


def hide_django_admin_middleware(get_response):

    def middleware(request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_staff:
                raise Http404()

        return get_response(request)

    return middleware