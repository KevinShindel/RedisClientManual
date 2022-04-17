
DEFAULT_KEY_PREFIX = "ru102py-app"


def prefixed_key(f):
    def prefixed_method(self, *args, **kwargs):
        key = f(self, *args, **kwargs)
        return '%s:%s' % (self.prefix, key)
    return prefixed_method


class KeySchema:

    def __init__(self, prefix: str = DEFAULT_KEY_PREFIX):
        self.prefix = prefix

    def __str__(self):
        return "KeySchema class"

    @prefixed_key
    def site_hash_key(self, site_id):
        return 'sites:info:%s' % site_id

    @prefixed_key
    def startswith_hash_key(self, pattern):
        return 'sites:info:%s*' % pattern

    @prefixed_key
    def endswith_hash_key(self, pattern):
        return 'sites:info:*%s' % pattern

    @prefixed_key
    def site_ids_key(self):
        return "sites:ids"
