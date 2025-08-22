import pytest
import time
from selenium.common.exceptions import TimeoutException
from pages.auth_page import AuthPage
from pages.video_page import VideoPage

@pytest.mark.parametrize("driver_fixture", ["driver_chrome", "driver_firefox", "driver_edge"])
def test_auth(driver_fixture, request):
    driver = request.getfixturevalue(driver_fixture)

    driver.get("https://my.proweb.uz/log-in?q=/home")

    auth_page = AuthPage(driver)
    auth_page.enter_phone_number("998933965750")
    auth_page.click_btn_next()
    auth_page.enter_password("Nadejniyparol123#")
    auth_page.click_btn_submit()

    try:
        auth_page.click_btn_session()
        auth_page.click_btn_finish()
    except:
        pass

    video_page = VideoPage(driver)
    video_page.click_course_button()
    time.sleep(2)
    video_page.click_lessons_button()
    time.sleep(2)
    video_page.click_last_lesson_btn()
    time.sleep(2)

    try:
        video_page.click_star_btn()
        time.sleep(2)
        video_page.click_real_star_btn()
        time.sleep(2)
        video_page.click_send_btn()
        time.sleep(2)
    except:
        pass

    video_page.click_appropriate_maximize_btn()
    time.sleep(2)
    video_page.click_play_btn()
    time.sleep(10)
