from apscheduler.schedulers.background import BackgroundScheduler

def sendNotifications():
  pass

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sendNotifications)
    scheduler.start()
