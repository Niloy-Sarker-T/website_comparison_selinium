# Website Comparison Tool

The Website Comparison Tool is a Python-based QA automation project for comparing two websites and generating professional SQA reports. It checks website availability, rendered HTML differences, visual screenshot differences, broken links, page load time, optional API endpoints, and exports defect/test execution reports.

## Features

- URL validation and accessibility checks
- Selenium-based website loading
- HTML comparison with `content_diff.html`
- Screenshot comparison with highlighted visual differences
- Broken-link checking
- Page URL extraction
- Automatic severity classification
- Professional bug report export
- QA dashboard report
- Test execution report
- Excel QA workbook
- Optional API test report
- UAT sign-off PDF
- Starter Page Object Model structure
- Starter pytest tests
- GitHub Actions workflow

## Prerequisites

- Python 3.9+
- Firefox browser or Chrome browser
- Required Python packages

Firefox is the default browser. Chrome is also supported from the startup prompt.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the upgraded tool:

```bash
python website_comparison.py
```

For backward compatibility, this also works:

```bash
python test.py
```

The script asks for:

- Browser: `firefox` or `chrome`
- Website A URL
- Website B URL
- Optional API base URL

If the API base URL is provided, the tool runs sample checks for:

- `GET /products`
- `GET /users`
- `POST /login`

## Generated Reports

The tool writes reports in the project root and in the `reports/` folder.

| Report | Purpose |
| --- | --- |
| `results.html` | QA dashboard with summary, status, test execution, defects, and artifact links. |
| `bug_report.csv` | Defect report for tracking issues. |
| `bug_report.xlsx` | Excel version of the defect report. |
| `test_execution_report.csv` | Pass/fail test case execution report. |
| `qa_report.xlsx` | Multi-sheet QA workbook with Summary, Broken Links, Visual Differences, Performance, and Defects. |
| `api_test_report.html` | API test execution report. |
| `UAT_Report.pdf` | UAT sign-off style report with recommendation. |
| `content_diff.html` | HTML difference report. |
| `visual_diff.png` | Raw visual difference image. |
| `visual_diff_highlighted.png` | Screenshot difference highlighted with a red box. |
| `website1_page_urls.txt` | Extracted URLs from Website A. |
| `website2_page_urls.txt` | Extracted URLs from Website B. |

## Severity Classification

Findings are classified automatically:

| Finding Type | Severity |
| --- | --- |
| Website unreachable | Critical |
| Broken checkout/payment/cart/login/order link | High |
| Other broken links | Medium |
| Visual regression | Medium |
| Large HTML difference set | Medium |
| Small HTML difference set | Low |
| API server error or unreachable endpoint | High |

## Project Structure

```text
website_comparison.py
test.py
requirements.txt
pages/
    base_page.py
    home_page.py
    login_page.py
tests/
    test_website_comparison.py
.github/
    workflows/
        qa.yml
reports/
```

## Run Tests

```bash
pytest
```

## License

This project is released under the MIT License.
