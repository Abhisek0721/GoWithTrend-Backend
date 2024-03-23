from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from app.jobs.getCompaniesPrice import getCompaniesPriceJob

# Create a scheduler
scheduler = BackgroundScheduler()

# Schedule the job to run every day at 9:30 AM
# scheduler.add_job(job, 'cron', hour=2, minute=16)
# scheduler.add_job(job, 'interval', minutes=1)
# scheduler.add_job(getCompaniesPriceJob, 'interval', seconds=1)
scheduler.add_job(getCompaniesPriceJob, CronTrigger(hour=23, minute=0, day_of_week='mon-fri'))

# Start the scheduler


def startJobs():
    scheduler.start()
