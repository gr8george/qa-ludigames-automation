# QA Ludigames Automation

This project contains automated UI and API tests for the Ludigames website:  
`https://play.ludigames.com`

The goal of the project is to verify that the homepage, game links, category pages, and basic server responses work correctly.

---

## Project Structure

```text
qa-ludigames-automation/
│
├── pytest.ini
├── requirements.txt
├── README.md
│
└── tests/
    ├── test_api.py
    └── test_ui.py
```

### File description

- `pytest.ini` — pytest configuration file.
- `requirements.txt` — list of Python libraries needed to run the project.
- `tests/test_api.py` — API/server-level tests using `requests`.
- `tests/test_ui.py` — browser UI tests using Playwright.

---

## Requirements

You need to have installed:

- Python 3.10 or newer
- Git
- pip
- Playwright browsers

---

## How to Get the Project from Git

Clone the repository:

```bash
git clone <your-repository-url>
```

Enter the project folder:

```bash
cd qa-ludigames-automation
```

---

## Create and Activate a Python Virtual Environment

### Windows PowerShell

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again:

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

When the environment is active, you should see something like this in the terminal:

```text
(venv)
```

---

## Install Required Libraries

After activating the virtual environment, install the dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not already include them, the main libraries needed are:

```bash
pip install pytest requests playwright
```

Then install the Playwright browser binaries:

```bash
playwright install
```

---

## How to Run the Tests

Run all tests:

```bash
pytest
```

Run only API tests:

```bash
pytest tests/test_api.py
```

Run only UI tests:

```bash
pytest tests/test_ui.py
```

Run tests with more detailed output:

```bash
pytest -v
```

---

## API Test Scenarios

The API tests check the basic server responses of the Ludigames homepage.

| Test | Description |
|---|---|
| `test_homepage_returns_200` | Ensures the homepage is reachable and returns a successful `200` response. |
| `test_homepage_response_time_under_3_seconds` | Verifies that the homepage responds in under 3 seconds. |
| `test_homepage_contains_html` | Confirms that the homepage response contains valid HTML content. |
| `test_homepage_has_security_headers_or_content_type` | Checks that the homepage returns the correct `text/html` content type. |
| `test_invalid_page_does_not_return_server_error` | Ensures invalid pages do not cause a server crash or `500` error. |

These tests are useful because they confirm that the website server is stable, fast, and returning proper web content.

---

## UI Test Scenarios

The UI tests use Playwright to open the Ludigames website in a real browser and validate user-facing functionality.

| Test | Description |
|---|---|
| `test_homepage_loads` | Verifies that the homepage opens successfully and the page title contains `Ludigames`. |
| `test_homepage_has_game_links` | Confirms that game links are visible on the homepage. |
| `test_first_game_link_has_valid_url` | Checks that the first game link has a valid URL. |
| `test_all_categories_work` | Verifies that category pages are accessible and contain games. |
| `test_all_game_buttons_lead_to_valid_pages` | Ensures all game links from the homepage lead to valid pages. |
| `test_all_categories_and_their_game_links_are_valid` | Checks that every category contains games and that every game link inside each category works. |
| `test_homepage_links_do_not_return_404` | Validates that homepage links do not return `404` errors. |

These tests are useful because they verify the main user journey: opening the website, browsing categories, finding games, and clicking valid links.

---

## Notes

- The UI tests currently launch Chromium with `headless=False`, so the browser window will be visible during test execution.
- If you want to run tests without opening the browser window, change this line in `tests/test_ui.py`:

```python
browser = playwright.chromium.launch(headless=False)
```

to:

```python
browser = playwright.chromium.launch(headless=True)
```

---

## Deactivate the Virtual Environment

When finished, deactivate the virtual environment:

```bash
deactivate
```


## Test run results
================================================ test session starts ================================================
platform darwin -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0 -- /Users/georgealx/qa-ludigames-automation/venv/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/georgealx/qa-ludigames-automation
configfile: pytest.ini
testpaths: tests
plugins: base-url-2.1.0, playwright-0.8.0
collected 12 items                                                                                                  

tests/test_api.py::test_homepage_returns_200 PASSED                                                           [  8%]
tests/test_api.py::test_homepage_response_time_under_3_seconds PASSED                                         [ 16%]
tests/test_api.py::test_homepage_contains_html PASSED                                                         [ 25%]
tests/test_api.py::test_homepage_has_security_headers_or_content_type PASSED                                  [ 33%]
tests/test_api.py::test_invalid_page_does_not_return_server_error PASSED                                      [ 41%]
tests/test_ui.py::test_homepage_loads PASSED                                                                  [ 50%]
tests/test_ui.py::test_homepage_has_game_links PASSED                                                         [ 58%]
tests/test_ui.py::test_first_game_link_has_valid_url PASSED                                                   [ 66%]
tests/test_ui.py::test_all_categories_work PASSED                                                             [ 75%]
tests/test_ui.py::test_all_game_buttons_lead_to_valid_pages PASSED                                            [ 83%]
tests/test_ui.py::test_all_categories_and_their_game_links_are_valid PASSED                                   [ 91%]
tests/test_ui.py::test_homepage_links_do_not_return_404 PASSED  
