from urllib.parse import urlparse

MAX_OUTPUT = 5000
CHECKER_URL = os.environ.get("CHECKER_URL", "http://checker:9090/get_flag")
PUBLIC_HOST_ALLOWLIST = {"public"}

import html
def is_safe_url(url: str) -> bool:
    #  ^q ^{ ^~ ^z  ^t ^{      ^u ^t ^p ^z   ^x   ^~ ^r ^p ^} ^x  :
    try:
        parsed = urlparse(url)
        if parsed.scheme == 'http' and parsed.hostname == 'public' and parsed.port == '5067':
                return True
        else:
                return False
    except:
        return False
#       return True
    #  ^z ^~ ^} ^u    ^q ^{ ^~ ^z ^p  ^t ^{      ^u ^t ^p ^z   ^x   ^~ ^r ^p ^} ^x

