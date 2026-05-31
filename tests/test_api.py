import requests

BASE_URL = "https://play.ludigames.com"

# Ensures the homepage is reachable and responding successfully to users.
def test_homepage_returns_200():
    response = requests.get(BASE_URL, timeout=10)
    assert response.status_code == 200

# Verifies that the homepage loads quickly and provides a good user experience.
def test_homepage_response_time_under_3_seconds():
    response = requests.get(BASE_URL, timeout=10)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3

# Confirms that the server returns a valid HTML page instead of broken or empty content.
def test_homepage_contains_html():
    response = requests.get(BASE_URL, timeout=10)
    content = response.text.lower()
    assert response.status_code == 200
    assert "<html" in content or "<!doctype html" in content

# Ensures the homepage returns the correct content type for proper browser rendering.
def test_homepage_has_security_headers_or_content_type():
    response = requests.get(BASE_URL, timeout=10)
    content_type = response.headers.get("content-type", "").lower()
    assert response.status_code == 200
    assert "text/html" in content_type

#Verifies that invalid URLs are handled safely without crashing the server.
def test_invalid_page_does_not_return_server_error():
    response = requests.get(f"{BASE_URL}/this-page-should-not-exist-qa-test", timeout=10)
    assert response.status_code < 500