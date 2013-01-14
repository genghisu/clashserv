from django.core.urlresolvers import reverse

def get_ip(request):
    """
    Returns ip address or None if the address is in an unexpected format
    """
    
    ip_address = request.META['REMOTE_ADDR']
    return ip_address

def get_page(request):
    """Returns the page parameter from the request.GET dictionary if it exists else default to page = 1"""

    if 'page' in request.GET.keys():
        page = request.GET['page']
    else:
        page = 1
    return page

def get_sort(request,  default):
    """Returns the @sort parameter from the request.GET dictionary if it exists else default to @default"""
    
    if 'sort' in request.GET.keys():
        sort = request.GET['sort']
    else:
        sort = default
    return sort

def append_redirect_path(path,  request):
    # handle requests that already contain a query string
    redirect = get_redirect_path(request)
    if path.strip().replace('/',  ''):
        return "%s?redirect=%s" % (path,  redirect)

def join_redirect_path(path,  redirect_path):
    return "%s?redirect=%s" % (path,  redirect_path)
    
def get_redirect_path(request):
    if 'redirect' in request.GET.keys():
        path = request.GET['redirect']
    else:
        path = reverse('main')
    return path

def get_protocol(request):
    if request.is_secure():
        protocol = 'https'
    else:
        protocol = 'http'
    return protocol

def get_domain(request):
    return "%s://%s" % (get_protocol(request),  request.get_host())
    
def get_full_url(request):
    return "%s%s" % (get_domain(request),  request.get_full_path())
    
