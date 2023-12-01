from django.utils import translation


def set_lang_middleware(get_response):

    def middleware(request):
        
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']
            
        response = get_response(request)

        return response

    return middleware
