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
        return f'{int(years)} years ago'
    elif months > 0:
        return f'{int(months)} months ago'
    elif weeks > 0:
        return f'{int(weeks)} weeks ago'
    elif days > 0:
        return f'{int(days)} days ago'
    elif hours > 0:
        return f'{int(hours)} hours ago'
    elif minutes > 0:
        return f'{int(minutes)} minutes ago'
    else:
        return f'{int(seconds)} seconds ago'

def validate_and_format_coordinates(lat, lon):
    if not lat or not lon:
        return None, None
    if lat > 90 or lat < -90:
        return None, None
    if lon > 180 or lon < -180:
        return None, None
    lat = float("{0:.4f}".format(lat))
    lon = float("{0:.4f}".format(lon))

    return (lat, lon)