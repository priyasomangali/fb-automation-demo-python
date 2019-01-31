from tests.common.base import BaseClass
from tests.user_actions.locators.user_actions_locators import *

class HomePage(BaseClass):

    def share_post(self,post_data):
        self.click(home_btn_loc)
        import time
        time.sleep(4)
        self.click("//*[@data-referrer='pagelet_composer']//*[contains(@class,'clearfix')]")
        self.set_value("//*[@data-testid='status-attachment-mentions-input']","priya")
        self.click(share_post_btn_loc)
        posted_data = self.get_text("//*[contains(@class,'userContent')]//p")
        return post_data