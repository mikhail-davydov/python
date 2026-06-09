def sourcetemplate(url):
    def get_full_url(**kwargs):
        nonlocal url
        if not kwargs:
            return url
        return url + '?' + '&'.join([f'{key}={value}' for key, value in sorted(kwargs.items())])
    return get_full_url


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
