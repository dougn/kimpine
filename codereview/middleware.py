class DisableCSRFMiddleware(object):
    """This is a BAD middleware. It disables CSRF protection.

    If someone comes up with a smart approach to make upload.py work
    with Django's CSRF protection, please submit a patch!
    """

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
