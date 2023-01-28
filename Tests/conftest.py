import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData

driver = None


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")    # This will return the Browser value to setup method
    if browser_name == "chrome":
        service_obj = Service(TestData.Chrome_driver_Path)
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == 'firefox':
        service_obj = Service(TestData.Firefox_driver_Path)
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "edge":
        service_obj = Service(TestData.Edge_driver_path)
        driver = webdriver.Edge(service=service_obj)

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


""" pytest HTML Report """

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'E Commerce SwagLabs'
    config._metadata['Module Name'] = 'Home Page'
    config._metadata['Tester'] = 'Ganesh'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


""" Below is another  method for setup or Initialize Browser """
# @pytest.fixture(params=["chrome"], scope="class")
# def init_driver(request):
#     """ Invoke browser by service object"""
#     if request.param == "chrome":
#         service_obj = Service(TestData.Chrome_driver_Path)
#         web_driver = webdriver.Chrome(service = service_obj)
#
#     if request.param == "firefox":
#         service_obj = Service(TestData.Firefox_driver_Path)
#         web_driver = webdriver.Firefox(service = service_obj)
#
#     """ Invoke browser by DriverManager class """
#     # if request.param == "chrome":
#     #     web_driver = webdriver.Chrome(ChromeDriverManager().install())    #
#     # if request.param == "firefox":
#     #     web_driver = webdriver.Firefox(GeckoDriverManager().install())
#
#     """ Invoke browser by Executable Path"""
#     # if request.param == "chrome":
#     #     web_driver = webdriver.Chrome(executable_path=TestData.Chrome_Executable_Path )
#
#     # if request.param == "firefox":
#     #     web_driver = webdriver.Firefox(executable_path = TestData.Firefox_Executable_Path)
#
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()
