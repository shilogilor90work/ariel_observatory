from django.apps import AppConfig


class ForcastConfig(AppConfig):
    name = 'forcast'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        # you must import your modules here
        # to avoid AppRegistryNotReady exception
        # import schedule
        # import time
        from .models import Current_Weather, Weekly
        from .extraction.scraping_IMS_current import scrape_IMS_current
        from .extraction.scraping_IMS_weekly import scrape_IMS_weekly
        scrape_IMS_current()
        scrape_IMS_weekly()
        #
        # schedule.every(10).minutes.do(scrape_IMS_current())
        # schedule.every().day.at("10:30").do(scrape_IMS_weekly())
        # schedule.every().day.at("10:30").do(delete_old())
        #
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)
