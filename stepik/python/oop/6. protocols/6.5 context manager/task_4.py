class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, encoding='u8')
        return (line.strip() for line in self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.file.closed:
            self.file.close()
        return False
