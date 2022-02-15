from datetime import datetime, timedelta

x = datetime(1931, 10, 12) 
y = x + timedelta(days=7)

print(x.strftime('%Y-%m-%d'))
print()
print(y.strftime('%Y-%m-%d'))