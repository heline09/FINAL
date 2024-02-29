def notification_context_processor(request):
    if request.user.is_authenticated:
        notifications = request.user.notifications 
        return {'notifications': notifications}
       
    else:
        return {"notifications": []}
