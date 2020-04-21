try:
   print(45/0)
except ValueError:
   print('caught ValueError')
except ZeroDivisionError:
   print('caught ZeroDivisionError')
else:
   print('Successfully divided')
finally:
   print('Every block executed!')