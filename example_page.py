from playwright.sync_api import sync_playwright


class ExamplePage:
    def __init__(self):
        self.p = sync_playwright().start()
        self.browser = self.p.webkit.launch()
        self.page = self.browser.new_page()
        self.url = 'https://example.com'
        self.header = 'h1'

    def open(self):
        self.page.goto("https://example.com")

    def get_header(self):
        return self.page.inner_text(self.header)
