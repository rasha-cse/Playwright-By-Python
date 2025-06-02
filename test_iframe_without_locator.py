import re
from playwright.sync_api import Page, expect, sync_playwright


def test_iframe_without_locator(page: Page, const=None):
    page.goto("https://sample.test.net/")

    page.locator('#loginName').type('rasha-cos')
    page.locator('#password').type('therap321#')
    page.locator('#providerCode').type('DDD-ND')
    page.get_by_role("button").click()

    ################################### iframe(without locator) ###############################
    page.goto("https://sample.test.net//ma/admin2/userForm")
    page.locator('#new-title-add').click()
    page.wait_for_timeout(300)
    page.frames[1].locator('#title').type('DDD-ND')

    #page.wait_for_timeout(5000)

    page.goto("https://sample.test.net/ma/ifsp/plan/ifspInfo?ifspId=2122")
    page.locator("text=Add New").click()
    page.wait_for_timeout(300)
    page.frames[1].locator("text=Add").click()


    page.wait_for_timeout(5000)
