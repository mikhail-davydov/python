def get_method_owner(cls, method):
    for klass in cls.mro():
        if method in klass.__dict__:
            return klass
    return None
