import psutil
print psutil.cpu_times()
print psutil.cpu_percent(interval=1)
for x in range(3):
	print psutil.cpu_percent(interval=1, percpu=True)
print 'cpus: ' + str(psutil.cpu_count())