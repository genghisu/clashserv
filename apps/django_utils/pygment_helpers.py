import re

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def highlight_markdown_helper(x):
    if x.group('target'):
        return "<code>" + highlight(x.group('target'), PythonLexer(), HtmlFormatter()).replace("<pre>", "").replace("</pre>", "") + "</code>"
    
def highlight_markdown(markdown):
    exp = re.compile(r'<code>(?P<target>.+?)</code>', re.S)
    return exp.sub(highlight_markdown_helper, markdown, 100)