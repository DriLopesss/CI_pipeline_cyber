# Semgrep CI Demo Repo

This is a minimal example repository to test Semgrep integration via GitHub Actions.

Structure:
- .github/workflows/ci.yml  -> GitHub Actions workflow that runs Semgrep and uploads a JSON report artifact.
- arquivos_vulneraveis/example.py -> Python file with an intentional SQL injection vulnerability.
- arquivos_vulneraveis/example.js -> JS file with an intentional XSS vulnerability.
