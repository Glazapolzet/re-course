from django.utils import translation

from django.utils.translation import get_language, activate, get_supported_language_variant, get_language_from_request


def set_lang_middleware(get_response):

    def middleware(request):
        print(get_language())
        lang_code = get_language_from_request(request, check_path=True)

        activate(get_supported_language_variant(lang_code.strip('/')))
            
        response = get_response(request)

        return response

    return middleware
