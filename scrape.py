import sys
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.facebook.com/profile.php?id=61579601194967")
        print("FACEBOOK_READY_FOR_LOGIN", flush=True)
        # Wait for the AI/user to send input unblocking this
        input()
        
        print("Scraping started...", flush=True)
        
        # Scroll to load a few posts
        for _ in range(5):
            page.mouse.wheel(0, 15000)
            page.wait_for_timeout(2000)
            
        # Try to find elements that look like posts
        with open("facebook_content.txt", "w", encoding="utf-8") as f:
            content = page.locator("body").inner_text()
            f.write(content)
            
        print("Scraping finished. Closing browser.", flush=True)
        browser.close()

if __name__ == "__main__":
    run()
