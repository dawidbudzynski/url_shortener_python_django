import random
import string

from shortener.models import Urls


def generate_short_code():
    length = 6
    valid_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        url_code = ''.join(random.choice(valid_characters) for _ in range(length))
        if not Urls.objects.filter(url_code=url_code).exists():
            return url_code
