from django.utils.encoding import DjangoUnicodeDecodeError

class ForceUTF8Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Принудительно устанавливаем кодировку UTF-8
        if 'Content-Type' in response and 'charset' not in response['Content-Type']:
            response['Content-Type'] = response['Content-Type'] + '; charset=utf-8'
        elif 'Content-Type' not in response:
            response['Content-Type'] = 'text/html; charset=utf-8'
        return response