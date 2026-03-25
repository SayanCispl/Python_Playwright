import logging

class BasePage:
    def __init__(self, page, test_name="base_test"):
        self.page = page
        self.test_name = test_name
        # Configure a logger per test
        self.logger = logging.getLogger(test_name)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def wait(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)
