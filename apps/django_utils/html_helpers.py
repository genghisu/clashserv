import re

def strip_all_tags(input):
    tag_expression = re.compile(r'<(.|\n)*?>')
    safe_input = tag_expression.sub('',  input)
    return safe_input
