from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

import random
import string
import re

def slugify(name,  rank = 10):
    """
    Generates a database friendly slug with a random hash attached
    """
    
    slug = name.strip()[0:47]
    slug = slug.replace(' ',  '_').replace(':',  '_')
    hash_list = [random.choice(string.letters) for x in range(0,  rank)]
    slug_hash = ''.join(hash_list)
    slug = slug + '-' + slug_hash
    return slug

def slugify_name(name):
    cleaned_name = name.strip().lower()
    final_name = slugify(re.sub(r'[^\w^\s]',  '',  cleaned_name).replace(' ',  '-'), 3)
    return final_name
