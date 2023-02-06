import re
from playwright.sync_api import Page, expect, sync_playwright


def test_client_autocomplete(page: Page, const=None):
    page.goto("https://qa02.therapbd.net/")

    page.locator('#loginName').type('rasha-cos')
    page.locator('#password').type('therap321#')
    page.locator('#providerCode').type('DDD-ND')
    page.get_by_role("button").click()

    ######################### client autocomplete ###############################
    page.goto("https://qa02.therapbd.net/ma/client/individualSearch?adminSearch=true")
    page.locator('#clientLookup').type('michael adkins')
    page.wait_for_timeout(3000)
    page.locator('#clientLookup').press('ArrowDown+Enter')
    page.locator('#clientLookup').press('Enter')


    page.wait_for_timeout(5000)