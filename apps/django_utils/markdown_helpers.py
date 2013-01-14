from BeautifulSoup import BeautifulStoneSoup

def fix_markdown(x):
    return unicode(BeautifulStoneSoup(x, convertEntities=BeautifulStoneSoup.HTML_ENTITIES))