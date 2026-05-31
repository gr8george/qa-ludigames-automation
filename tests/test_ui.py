from playwright.sync_api import sync_playwright

BASE_URL = "https://play.ludigames.com"

def open_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    return playwright, browser, page

# Verifies that the homepage is accessible and loads successfully, ensuring users can reach the website.
def test_homepage_loads():
    playwright, browser, page = open_page()
    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        assert "Ludigames" in page.title()
    finally:
        browser.close()
        playwright.stop()

# Confirms that game links are displayed on the homepage, ensuring users can discover available games.
def test_homepage_has_game_links():
    playwright, browser, page = open_page()
    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        game_links = page.locator("a[href*='game']")
        assert game_links.count() > 0
    finally:    
        browser.close()
        playwright.stop()

# Checks that at least one game link points to a valid page, helping detect broken game URLs early.
def test_first_game_link_has_valid_url():
    playwright, browser, page = open_page()
    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        first_game = page.locator("a[href*='game']").first
        href = first_game.get_attribute("href")
        assert href is not None
        assert "game" in href or href.startswith("/")
    finally:
        browser.close()
        playwright.stop()

# Verifies that every category page is accessible and loads correctly, ensuring site navigation functions properly.
from urllib.parse import urljoin
def test_all_categories_work():
    playwright, browser, page = open_page()
    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        category_links = page.locator("a[href*='category']")
        category_count = category_links.count()
        assert category_count > 0, "No categories found"

        # Collect URLs first
        categories = []
        for i in range(category_count):
            link = category_links.nth(i)

            href = link.get_attribute("href")
            name = link.inner_text().strip()

            assert href, f"Category '{name}' has no href"

            categories.append(
                (name, urljoin(BASE_URL, href))
            )

        # Test each category
        for category_name, category_url in categories:
            print(f"\nTesting category: {category_name}")

            # Verify URL returns 200
            response = page.request.get(category_url)

            assert response.status == 200, (
                f"Category '{category_name}' returned "
                f"{response.status}"
            )

            # Open category page
            page.goto(category_url, wait_until="domcontentloaded")

            # Verify page loaded successfully
            assert page.title() != "", (
                f"Category '{category_name}' has no title"
            )
            # Verify category contains games
            game_links = page.locator("a[href*='game']")
            game_count = game_links.count()
            assert game_count > 0, (
                f"Category '{category_name}' contains no games"
            )
            print(
                f"✓ {category_name}: "
                f"{game_count} games found"
            )
    finally:
        browser.close()
        playwright.stop()

# Ensures that all game buttons direct users to valid game pages rather than broken or missing content.
from urllib.parse import urljoin
def test_all_game_buttons_lead_to_valid_pages():
    playwright, browser, page = open_page()
    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        game_links = page.locator("a[href*='game']")
        count = game_links.count()

        assert count > 0

        for i in range(count):
            href = game_links.nth(i).get_attribute("href")
            assert href is not None
            full_url = urljoin(BASE_URL, href)
            response = page.request.get(full_url)
            assert response.status == 200, f"Broken game link: {full_url}"
    finally:
        browser.close()
        playwright.stop()

# Confirms that every category contains games and that all game links within those categories are reachable and valid.
from urllib.parse import urljoin
def test_all_categories_and_their_game_links_are_valid():
    playwright, browser, page = open_page()
    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        # Find category buttons/links
        category_links = page.locator("a[href*='category.html?']")
        category_count = category_links.count()
        assert category_count > 0
        print(f"\nFound {category_count} categories")

        for category_index in range(category_count):
            category_link = category_links.nth(category_index)
            category_name = category_link.inner_text().strip()
            href = category_link.get_attribute("href")
            assert href is not None
            category_url = urljoin(BASE_URL, href)
            print(f"\nOpening category: {category_name}")
            print(f"URL: {category_url}")

            # Open category page
            category_response = page.request.get(category_url)
            assert category_response.status == 200, (
                f"Broken category page: {category_url}"
            )

            page.goto(category_url, wait_until="domcontentloaded")
      
            # Find game links inside category
            game_links = page.locator("a[href*='game']")
            game_count = game_links.count()

            assert game_count > 0, (
                f"No game links found in category: {category_name}"
            )
            print(f"Found {game_count} game links")

            # Validate each game link
            for game_index in range(game_count):
                game_link = game_links.nth(game_index)
                game_href = game_link.get_attribute("href")
                if not game_href:
                    continue
                game_url = urljoin(BASE_URL, game_href)
                print(f"Checking game URL: {game_url}")
                game_response = page.request.get(game_url)
                assert game_response.status == 200, (
                    f"Broken game link: {game_url}"
                )
    finally:
        browser.close()
        playwright.stop()

# Checks that the main links on the homepage do not return 404 errors, preventing users from encountering dead links.
from urllib.parse import urljoin
def test_homepage_links_do_not_return_404():
    playwright, browser, page = open_page()

    try:
        page.goto(BASE_URL, wait_until="domcontentloaded")
        links = page.locator("a[href]")
        link_count = links.count()
        assert link_count > 0, "No links found on homepage"

        checked_urls = set()
        for i in range(link_count):
            href = links.nth(i).get_attribute("href")
            if not href:
                continue

            # Skip anchors and javascript links
            if href.startswith("#") or href.startswith("javascript:"):
                continue

            url = urljoin(BASE_URL, href)
            # Avoid checking duplicates
            if url in checked_urls:
                continue

            checked_urls.add(url)
            response = page.request.get(url)

            assert response.status != 404, (
                f"Homepage link returns 404: {url}"
            )
            print(f"✓ {response.status} - {url}")
    finally:
        browser.close()
        playwright.stop()

