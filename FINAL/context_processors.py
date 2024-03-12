
def notification_context_processor(request):
    if request.user.is_authenticated:
        notifications = request.user.notifications.filter(opened=False)
        notifications_count = notifications.count()
        return {'notifications': notifications, 'notifications_count': notifications_count}       
    else:
        return {"notifications": []}
