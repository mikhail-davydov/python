import logging


class ExcludeFilter(logging.Filter):

    def __init__(self, exclude_name=''):
        super().__init__(exclude_name)

    def filter(self, record):
        return not super().filter(record) if self.name else super().filter(record)


test_filter = ExcludeFilter(exclude_name='app.audit')
