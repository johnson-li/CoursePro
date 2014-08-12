import os


def save_to_file(content, filename, msg=None):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, 'wb') as f:
        f.write(content)
    if msg:
        print msg + ' [' + filename + ']'
