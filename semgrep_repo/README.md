# Semgrep CI Demo Repo

This is a minimal example repository to test Semgrep integration via GitHub Actions.

Structure:
- .github/workflows/ci.yml  -> GitHub Actions workflow that runs Semgrep and uploads a JSON report artifact.
- vulnerable_examples/example.py -> Python file with an intentional SQL injection vulnerability.
- vulnerable_examples/example.js -> JS file with an intentional XSS vulnerability.

How to use:
1. Clone this repository.
2. (Optional) Run Semgrep locally:
   - Install semgrep: `pip install semgrep`
   - Run: `semgrep --config auto --json --output semgrep-report.json .`
3. Or push to GitHub (branch `main`) and the workflow will run automatically.
4. Check Actions → latest run → download artifact `semgrep-report`.

Notes:
- The workflow is configured to run on pushes to `main`. If your default branch has a different name, update the workflow triggers.
- The "Fail if critical findings" step is optional and can be removed if you don't want the job to fail on critical findings.
