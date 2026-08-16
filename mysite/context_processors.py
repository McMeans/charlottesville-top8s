def gallery_nav(request):
    from .models import Graphic
    from .views import getUserID

    return {
        'num_submissions': Graphic.objects.filter(user=getUserID(request)).count(),
    }
