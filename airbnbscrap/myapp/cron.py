from django_cron import CronJobBase, Schedule
from myapp.service.scraper import Scraper


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0  # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 0
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'myapp.my_cron_job'  # a unique code

    def __init__(self):
        self.data = Scraper()

    def do(self):
        self.data.saveScrapData()

        