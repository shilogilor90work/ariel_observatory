# Create your tasks here

from celery.decorators import periodic_task
from celery.schedules import crontab
from .extraction.scraping_IMS_current import scrape_IMS_current
from .extraction.scraping_IMS_weekly import scrape_IMS_weekly


@periodic_task(run_every=crontab(minute='0,10,20,30,40,50'))
def current_scrape():
    print("starting current scrape")
    scrape_IMS_current()
    print("finished current scrape")


@periodic_task(run_every=crontab(minute=0, hour='6,18'))
def weekly_scrape():
    print("starting weekly scrape")
    scrape_IMS_weekly()
    print("finished weekly scrape")