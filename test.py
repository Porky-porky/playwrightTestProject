import example_page


def test_example_is_working():
    page = example_page.ExamplePage()
    page.open()
    assert page.get_header() == "Example Domain"
