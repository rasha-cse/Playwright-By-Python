import re
from playwright.sync_api import Page, expect, sync_playwright


def test_iframe_with_locator(page: Page, const=None):
    page.goto("https://qa02.therapbd.net/")

    page.locator('#loginName').type('rasha-cos')
    page.locator('#password').type('therap321#')
    page.locator('#providerCode').type('DDD-ND')
    page.get_by_role("button").click()

    #page.locator('"Agree"').click()

    ################################### iframe(with locator) ###############################
    page.goto("https://qa02.therapbd.net/ma/nd/osp/osp?_flowId=nd-osp-flow&formId=OSP-DDDND-LDB2JVSBDWXUW")
    frame_three = page.wait_for_selector("#mce_0_ifr").content_frame()
    frame_three.locator('#tinymce').type('DDD-ND')

    page.wait_for_timeout(8000)

    ################################### iframe(with id) working ###############################
    page.goto('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
    frame_one = page.wait_for_selector("#iframeResult").content_frame()
    frame_one.wait_for_selector("#cars").select_option(value = "saab")
    ################################### iframe working ###############################


    page.wait_for_timeout(5000)