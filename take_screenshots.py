from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        pages = ["index.html", "Aboutus.html", "alienware.html", "asus.html", "contact.html", "cookiepolicy.html", "lenovo.html", "login.html", "privacypolicy.html", "signup.html", "termsandcondition.html"]

        for p in pages:
            page.goto(f"file://{os.getcwd()}/{p}")
            page.screenshot(path=f"screenshots/{p.replace('.html', '.png')}")

        browser.close()

run()
