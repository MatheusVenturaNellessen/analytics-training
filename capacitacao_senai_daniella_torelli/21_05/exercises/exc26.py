from datetime import datetime

start = datetime(2025, 5, 22, 9, 0)
end = datetime(2025, 5, 22, 16, 0)

duration = end - start

print(duration)
print(f'{round(duration.seconds / 3600)} horas')
