def seconds_to_text(secs):
    if secs < 0:
        return "0 seconds ago"
    years = secs // 31536000
    months = secs // 2592000
    weeks = secs//604800
    days = secs//86400
    hours = secs//3600
    minutes = secs//60
    seconds = secs
    if years > 0:
        return f'{years} years ago'
    elif months > 0:
        return f'{months} months ago'
    elif weeks > 0:
        return f'{weeks} weeks ago'
    elif days > 0:
        return f'{days} days ago'
    elif hours > 0:
        return f'{hours} hours ago'
    elif minutes > 0:
        return f'{minutes} minutes ago'
    else:
        return f'{seconds} seconds ago'