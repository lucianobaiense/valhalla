#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from .models import News, System, Profile
from django.db.models import Q
from django.contrib.auth.models import User

#---------------------------------------------------------
#    Custom Processors
#---------------------------------------------------------

def profile(request):
    if request.user.is_authenticated:
        # Get display name
        try:
            display_name = request.user.profile.nickname
            if display_name == '':
                display_name = request.user.first_name
        except:
            display_name = request.user.first_name

        # Get display photo
        try:
            display_photo = request.user.profile.photo
        except:
            display_photo = ""

        # Get notifications
        user_id = request.user.id
        news_count = News.objects.exclude(Q(author_id=user_id) | Q(readers=user_id)).count()
        system_count = System.objects.filter(reader_id=user_id, read=False).count()
        system_data = System.objects.filter(reader_id=user_id, read=False).values().order_by('-created')
        notifications_count = news_count + system_count
        notifications = False
        if news_count > 0 or system_count > 0:
            notifications = True

        return {
            'display_name'  : display_name,
            'display_photo' : display_photo,
            'notifications_check' : notifications,
            'notifications_count' : notifications_count,
            'news_count': news_count,
            'system_data' : system_data,
        }
    else:
        return {}
