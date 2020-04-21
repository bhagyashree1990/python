# try-except-else block
try:
   print(45/12)
except ValueError:
   print('caught ValueError')
except ZeroDivisionError:
   print('caught ZeroDivisionError')
else:
   print('Successfully divided')