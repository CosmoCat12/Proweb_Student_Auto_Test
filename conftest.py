import pytest
from selenium import webdriver


@pytest.fixture
def driver_chrome():
    driver_c = webdriver.Chrome()
    driver_c.maximize_window()
    driver_c.implicitly_wait(10)
    yield driver_c
    driver_c.quit()

@pytest.fixture
def driver_firefox():
    driver_f = webdriver.Firefox()
    driver_f.maximize_window()
    driver_f.implicitly_wait(10)
    yield driver_f
    driver_f.quit()

@pytest.fixture
def driver_edge():
    driver_e = webdriver.Edge()
    driver_e.maximize_window()
    driver_e.implicitly_wait(10)
    yield driver_e
    driver_e.quit()
