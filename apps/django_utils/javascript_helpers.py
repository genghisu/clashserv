def generate_thickbox_href(base_url, width, height, iframe):
    params = {}
    params['base_url'] = base_url
    params['width'] = str(width)
    params['height'] = str(height)
    params['TB_iframe'] = str(iframe).lower()
    
    if base_url.index('?'):
        final_url = """%(base_url)s&TB_iframe=%(TB_iframe)s&width=%(width)s&height=%(height)s""" % params
    else:
        final_url = """%(base_url)s?TB_iframe=%(TB_iframe)s&width=%(width)s&height=%(height)s""" % params
    return final_url