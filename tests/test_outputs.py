import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    """Load and parse /app/report.json as a JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json is not a JSON object"
    return data


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and is a single valid JSON object."""
    load_report()


def test_total_requests():
    """Criterion 2: total_requests equals the number of non-empty request lines (6)."""
    data = load_report()
    assert data["total_requests"] == 6, data.get("total_requests")


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    data = load_report()
    assert data["unique_ips"] == 3, data.get("unique_ips")


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path (/index.html)."""
    data = load_report()
    assert data["top_path"] == "/index.html", data.get("top_path")
