import shutil, psutil
du = shutil.disk_usage("/")
print(du)
print("Total amount of free space on disk is: {:.2f}%".format( (du.free / du.total) * 100 ))

print("CPU percentage used is: {}%".format(psutil.cpu_percent(0.1)))
print("CPU percentage used is: {}%".format(psutil.cpu_percent(0.5)))