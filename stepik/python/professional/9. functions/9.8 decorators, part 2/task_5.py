import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)!s}</{tag}>'

        return wrapper

    return decorator


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))
