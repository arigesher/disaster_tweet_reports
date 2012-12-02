MISSING_VALUE = '!__MISSING_VALUE__!'


def trim_tweet(tweet):
    fields = (
        u'user',
        u'place',
        u'text',
        u'created_at',
        u'coordinates'
    )
    trimmed_tweet = trim_map(tweet, fields)
    trimmed_tweet[u'user'] = trim_user(trimmed_tweet[u'user'])
    return trimmed_tweet


def trim_user(user):
    fields = (
        u'id',
        u'screen_name',
        u'name',
    )
    return trim_map(user, fields)


def trim_map(src, fields, dst=None):
    #fields = map(lambda x: unicode(x, 'utf-8'), fields)
    if not dst:
        dst = {}

    for field in fields:
        if(field in src):
            dst[field] = src[field]
        else:
            dst[field] = MISSING_VALUE
    return dst
