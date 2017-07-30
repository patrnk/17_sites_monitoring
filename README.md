# Sites Monitoring Utility
Prints a warning if a website is unresponsive or its domain expires soon.

Requires Python 3. To install, run `pip install -r requirements.txt`.

URLs can be loaded from both stdin and a file:
```bash
$ python check_sites_health.py --url_file urls.txt
(*) http://devman.org domain expires soon
(!) http://devman1234.org appears to be unresponsive
(*) http://devman1234.org domain expires soon
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
