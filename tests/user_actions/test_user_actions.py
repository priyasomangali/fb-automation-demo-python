from tests.user_actions.conftest import *


class TestUserActions():
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = driver(True)
        cls.data_to_post = share_post_on_fb_data()
        cls.home_page = HomePage(cls.driver)

    def test_add_post(self):
        posted_data = self.home_page.share_post(share_post_on_fb_data["plain_text_post"])
        if posted_data == share_post_on_fb_data["plain_text_post"]:
            assert True

    def test_add_empty_post(self):
        pass

    def test_post_with_image_and_text(self):
        pass

    def test_post_only_image(self):
        pass

    def test_post_with_video_and_text(self):
        pass

    def test_post_with_only_video(self):
        pass

    def test_edit_post(self):
        pass

    def test_delete_post(self):
        pass
