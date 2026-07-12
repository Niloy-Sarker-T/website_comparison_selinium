# Website Comparison Tool - Modification Summary

## What Has Been Done

### 1. Professional Bug Reports

The project now generates structured defect reports with fields that match real SQA workflows:

- `bug_id`
- `severity`
- `module`
- `description`
- `expected`
- `actual`
- `status`

Generated files:

- `bug_report.csv`
- `bug_report.xlsx`

This supports defect identification, documentation, and tracking.

### 2. QA Dashboard Report

The empty `results.html` placeholder has been turned into a professional QA dashboard.

The dashboard includes:

- Total links checked
- Broken links
- Visual differences
- HTML differences
- Site A load time
- Site B load time
- Overall status
- Test execution table
- Defect table
- Links to generated artifacts

Generated file:

- `results.html`

### 3. Severity Classification

The tool now classifies issues automatically.

Implemented severity rules:

| Issue Type | Severity |
| --- | --- |
| Website unreachable | Critical |
| Broken checkout/payment/cart/login/order link | High |
| Other broken links | Medium |
| Visual regression | Medium |
| Large HTML difference set | Medium |
| Small HTML difference set | Low |
| API server error or unreachable endpoint | High |

### 4. Test Case Execution Report

The project now records QA-style test case execution results.

Example test cases:

- URL Format Validation
- Website A Accessible
- Website B Accessible
- HTML Match
- Broken Links
- Visual Match
- Performance

Generated file:

- `test_execution_report.csv`

### 5. Screenshot Difference Highlighting

The old raw screenshot diff has been upgraded.

The tool now:

- Captures screenshots for both websites.
- Generates a raw difference image.
- Draws a red bounding box around the detected changed area.

Generated files:

- `screenshot1.png`
- `screenshot2.png`
- `visual_diff.png`
- `visual_diff_highlighted.png`

### 6. Excel QA Reports

The project now exports Excel reports for recruiters, QA leads, and non-technical stakeholders.

Generated files:

- `bug_report.xlsx`
- `qa_report.xlsx`

The `qa_report.xlsx` workbook contains:

- Summary
- Broken Links
- Visual Differences
- Performance
- Defects

### 7. API Testing Module

An optional API testing section has been added.

When the user provides an API base URL, the tool runs:

- `GET /products`
- `GET /users`
- `POST /login`

Generated file:

- `api_test_report.html`

If no API base URL is provided, the API report is still generated and marks the API tests as skipped.

### 8. Page Object Model Starter Structure

A starter Page Object Model structure has been added to show automation testing knowledge.

Added files:

- `pages/base_page.py`
- `pages/home_page.py`
- `pages/login_page.py`

This creates a clean base for future Selenium test expansion.

### 9. GitHub Actions CI/CD

A GitHub Actions workflow has been added.

Added file:

- `.github/workflows/qa.yml`

The workflow:

- Installs dependencies.
- Runs pytest.
- Uploads generated QA artifacts when available.

### 10. UAT Sign-off Report

The project now generates a UAT-style sign-off report.

Generated file:

- `UAT_Report.pdf`

The PDF includes:

- Application name
- Version label
- Test cases executed
- Passed count
- Failed count
- Open defects
- Overall status
- Release recommendation
- Defect summary

### 11. Dependency Management

A `requirements.txt` file has been added so the project can be installed consistently.

Added file:

- `requirements.txt`

### 12. Backward Compatibility

The old runnable file name `test.py` has been preserved as a wrapper.

Current entry points:

- `python website_comparison.py`
- `python test.py`

The main implementation now lives in:

- `website_comparison.py`

### 13. Starter Automated Tests

Basic pytest tests have been added for core URL helper behavior.

Added file:

- `tests/test_website_comparison.py`

### 14. Firefox and Chrome Browser Support

The Selenium driver setup now supports both Firefox and Chrome.

Implemented behavior:

- Firefox remains the default browser.
- Chrome can be selected from the startup prompt.
- Firefox uses `GeckoDriverManager`.
- Chrome uses `ChromeDriverManager`.
- Invalid browser names raise a clear error.

## What Has Been Avoided

### 1. Full Framework Migration

The project was not converted into a large pytest-only automation framework. That would be useful later, but it would make the current tool harder to run and review quickly.

### 2. Hardcoded Real API Credentials

The API testing module does not include real login credentials, tokens, or private endpoints. It uses a configurable API base URL and safe sample request data.

### 3. Fake Defects

The tool does not create fake defects just to make reports look full. Defects are generated from actual comparison results such as broken links, HTML differences, visual differences, inaccessible websites, and API failures.

### 4. Forced API Testing

API testing is optional. If no API base URL is provided, the API report marks those checks as skipped instead of failing the whole run.

### 5. Removing Existing Generated Files

Existing output artifacts such as `content_diff.html` and `full_differences.html` were not deleted. The upgraded tool writes fresh reports when it runs.

### 6. Hard Browser Switch

The project was not changed to Chrome-only. Instead, it now supports both Firefox and Chrome, with Firefox kept as the default so existing behavior does not break.

### 7. Overly Complex Visual Diff Algorithms

The screenshot comparison highlights the main changed area with a red bounding box. It avoids a heavy image-processing dependency or complex multi-region algorithm, keeping the project easy to install and explain.

## Final Status

The project has been upgraded from a simple website comparison prototype into a more complete SQA portfolio project. It now demonstrates web testing, visual regression testing, defect documentation, severity classification, test execution reporting, Excel reporting, optional API testing, UAT reporting, Page Object Model structure, and CI/CD readiness.
