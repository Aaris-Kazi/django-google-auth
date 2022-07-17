from datetime import datetime

dt = str(datetime.now())
dt = dt.replace(' ', '')
dt = dt.replace('-', '')
dt = dt.replace(':', '')
dt = dt.replace('.', '')

print(int(dt))