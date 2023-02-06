import re
from playwright.sync_api import Page, expect, sync_playwright


def test_ifsp_popup(page: Page, const=None):
    page.goto("https://qa03.therapbd.net/")

    page.locator('#loginName').type('rasha-cos')
    page.locator('#password').type('therap321#')
    page.locator('#providerCode').type('DDD-ND')
    page.get_by_role("button").click()

    ######################### ifsp popup ###############################
    page.goto("https://qa03.therapbd.net/ma/ifsp/plan/familyConcerns?ifspId=2242")
    page.wait_for_timeout(3000)
    page.locator('#openBtn').click()


    page.wait_for_timeout(5000)