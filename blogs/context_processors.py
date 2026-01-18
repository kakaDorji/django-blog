from .models import Category
from assignments.models import SocialLink

def get_categories(req):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_social_links(req):
    socialLink=SocialLink.objects.all()
    return dict(socialLink=socialLink)