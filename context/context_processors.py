from homePageApp.models import blog
from homePageApp.models import category


def recentBlog(request):
    recent_blogs=blog.objects.all().order_by('-created_at')
    recent_blogs=recent_blogs[:3]
    return {'recent_blog':recent_blogs}
def categories(request):
    categorie=category.objects.all()
    return{'category':categorie}