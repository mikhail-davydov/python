class SortKey:

    def __init__(self, *args):
        self._sort_fields = args

    def __call__(self, obj):
        return [getattr(obj, attr) for attr in self._sort_fields]
