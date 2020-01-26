from contextlib import contextmanager
@contextmanager
def open_file(name):
    f = open("contextcheck.txt", 'w')
    yield f
    f.close()
