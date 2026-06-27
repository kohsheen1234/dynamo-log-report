An Apache-style access log is at `/app/access.log`. Each non-empty line is one
request and starts with the client IP address, followed by the usual common
log fields, including a quoted request line such as `"GET /index.html HTTP/1.1"`.

Parse the log and write a summary report to `/app/report.json`. The file must be
a single JSON object with exactly these three keys:

- `total_requests` (integer): the number of request lines in the log (non-empty
  lines only).
- `unique_ips` (integer): the count of distinct client IP addresses, where the
  IP is the first whitespace-separated field of each line.
- `top_path` (string): the request path (the second token inside the quoted
  request line, e.g. `/index.html`) that appears most often across all requests.

Success criteria:

1. `/app/report.json` exists and contains a single valid JSON object.
2. `total_requests` equals the number of non-empty request lines in the log.
3. `unique_ips` equals the number of distinct client IP addresses.
4. `top_path` is the most frequently requested path.
