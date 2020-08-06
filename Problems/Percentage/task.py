def get_percentage(num, n=None):
    if n is None:
        return str(round(num * 100)) + "%"
    return str(round((num * 100), n)) + "%"
