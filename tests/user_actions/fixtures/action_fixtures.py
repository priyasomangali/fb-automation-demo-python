import pytest


@pytest.fixture(scope="session")
def share_post_on_fb_data():
    return{
        "plain_text_post" : "This is a plain text",
        "post_with_link" : "post data with link - https://www.accuweather.com/en/in/chennai/206671/current-weather/206671"
    }