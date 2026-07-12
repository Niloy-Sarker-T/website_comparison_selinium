from website_comparison import WebsiteComparer


def test_validate_url_accepts_https_url():
    comparer = WebsiteComparer()

    assert comparer.validate_url("https://example.com")


def test_validate_url_rejects_plain_text():
    comparer = WebsiteComparer()

    assert not comparer.validate_url("not a url")


def test_normalize_url_adds_https():
    comparer = WebsiteComparer()

    assert comparer.normalize_url("example.com") == "https://example.com"


def test_default_browser_is_firefox():
    comparer = WebsiteComparer()

    assert comparer.browser == "firefox"


def test_browser_can_be_chrome():
    comparer = WebsiteComparer(browser="chrome")

    assert comparer.browser == "chrome"


def test_invalid_browser_raises_error():
    try:
        WebsiteComparer(browser="safari")
    except ValueError as error:
        assert "Unsupported browser" in str(error)
    else:
        raise AssertionError("Expected ValueError for unsupported browser")
