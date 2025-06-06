import re
from playwright.sync_api import Page, expect, sync_playwright


def test_multi_tab(page: Page, const=None):
    page.goto("https://sample.test.net/")

    page.locator('#loginName').type('rasha')
    page.locator('#password').type('sample.test#')
    page.get_by_role("button").click()

    page.locator('"Agree"').click()

    ################################### multi/new tab ###############################

    page.goto("https://sample.test.net/ma/ger/preview?formId=JDX2PV3GU5RNP")
    page.locator("id=clientInfo").click()
    #page.wait_for_timeout(5000)
    with page.context.expect_page() as tab:
        page.click('"Individual Home Page"')
    new_tab = tab.value
    new_tab.locator("id=dashboard-link").click()


    page.wait_for_timeout(5000)
