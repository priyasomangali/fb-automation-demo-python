from tests.common.base import BaseClass
from tests.user_actions.locators.user_actions_locators import *

class HomePage(BaseClass):

    def share_post(self,post_data):
        self.click(home_btn_loc)
        self.set_value(write_post_txt_loc,post_data)
        self.click(share_post_btn_loc)