from homePageApp.models import blog

def recentBlog(request):
    recent_blogs=blog.objects.all().order_by('-created_at')
    recent_blogs=recent_blogs[:3]
    return {'recent_blog':recent_blogs}