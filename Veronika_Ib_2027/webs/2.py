def is_safe_url(url: str) -> bool:
    newurl = urlparse(url)
    if newurl.scheme == 'http' and newurl.hostname == 'public' and newurl.port == '5067':
        return True
    else:
        return False