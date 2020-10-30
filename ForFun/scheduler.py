import schedule

def job():
  print('Hello')

def hi():
  print('Hi')

schedule.every(2).seconds.do(job)
schedule.every(3).seconds.do(hi)

while True:
  schedule.run_pending()
