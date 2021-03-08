from django.apps import AppConfig


class ForcastConfig(AppConfig):
    name = 'forcast'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        # you must import your modules here
        # to avoid AppRegistryNotReady exception
        from .models import Current_Weather, Weekly
        from .extraction.scraping_IMS_current import scrape_IMS_current
        from .extraction.scraping_IMS_weekly import scrape_IMS_weekly
        scrape_IMS_current()
        # startup code here
