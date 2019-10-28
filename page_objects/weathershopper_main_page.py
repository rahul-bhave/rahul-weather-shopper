"""
This class models the main Temperature page.
"""
from .Base_Page import Base_Page
from page_objects.weathershopper_Object import weathershopper_Object
from utils.Wrapit import Wrapit


class weathershopper_main_page(Base_Page,weathershopper_Object):
    "Page Object for the temperature main page"
    
    def start(self):    
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)
