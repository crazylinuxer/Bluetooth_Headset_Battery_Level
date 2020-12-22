import os

dev_info = os.environ.get('dev_info', '').split()[1]
print(dev_info if dev_info.count(':') >= 5 else '')
