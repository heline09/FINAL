def notification_context_processor(request):
    if request.user.is_authenticated:
        try:
            return {'notifications': request.user.notifications }
        except Exception as e:
            n = [e.args[0], 'Notification 1', 'Notification 2', 'Notification 3']
            return {'notifications': n}
    else:
        return {"notifications": []}

