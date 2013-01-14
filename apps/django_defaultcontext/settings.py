from django.conf import settings
from django_comments.models import Comment
from tagging.models import Tag
from django_qa.models import Question, Answer
from code.models import Code
from projects.models import DjangoProject
from applications.models import App
from tutorials.models import Tutorial

ENABLE_STATIC_PATHS = getattr(settings, 'ENABLE_STATIC_PATHS', True)
MODEL_CONTENT_TYPES = getattr(settings, 'MODEL_CONTENT_TYPES', [Comment, Tag, Question, Answer, App, Code, DjangoProject, Tutorial])