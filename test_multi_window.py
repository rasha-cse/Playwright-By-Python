import re
from playwright.sync_api import Page, expect, sync_playwright


def test_multi_window(page: Page, const=None):
    page.goto("https://sample.test.net/")

    page.locator('#loginName').type('rasha-da')
    page.locator('#password').type('sample.test#')
    page.get_by_role("button").click()

    ################################### multi/new window ###############################
    page.goto("https://sample.test.net/ma/admin2/userForm?userId=2366033")
    with page.context.expect_page() as window:
        page.locator("text=Set State Specific User Information").click()
    new_window = window.value
    new_window.locator("text=Update").click()

    page.wait_for_timeout(5000)

    page.goto("https://sample.test.net/ma/nd/osp/osp?_flowId=flow&formId=K5Y4QLSZL5RPM")
    with page.context.expect_page() as window:
        page.locator('"Attach"').click()
    new_window = window.value
    new_window.locator('"Attach"').click()

    page.wait_for_timeout(5000)
