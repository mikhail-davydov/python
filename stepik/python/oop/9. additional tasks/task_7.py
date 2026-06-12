from dataclasses import dataclass, field


@dataclass
class Pagination:
    data: list
    page_size: int
    current_page: int = field(init=False, default=1)
    total_pages: int = field(init=False)

    def __post_init__(self):
        page_count = len(self.data) // self.page_size
        self.total_pages = (1 + page_count) if len(self.data) % self.page_size else page_count

    def get_visible_items(self):
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.data[start:end]

    def prev_page(self):
        self.current_page = max(1, self.current_page - 1)
        return self

    def next_page(self):
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages

    def go_to_page(self, page_num):
        page_num = min(max(1, page_num), self.total_pages)
        self.current_page = page_num


# alt

class Pagination:
    def __init__(self, data, size):
        self.pages = [data[i:i + size] for i in range(0, len(data), size)]
        self.total_pages = len(self.pages)
        self.current_page = 1

    def prev_page(self):
        self.current_page = max(1, self.current_page - 1)
        return self

    def next_page(self):
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages

    def go_to_page(self, page):
        self.current_page = max(1, min(page, self.total_pages))

    def get_visible_items(self):
        return self.pages[self.current_page - 1]
