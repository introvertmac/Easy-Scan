# Easy Scan

 A minimal scanner to test your web application for security issues


# Dependencies

- [Requests](http://docs.python-requests.org/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


# Results Include

1. Shows Response header
2. [Clickjacking](https://www.owasp.org/index.php/Clickjacking) 
3. [Same Site Scripting](https://www.acunetix.com/vulnerabilities/web/same-site-scripting)
4. [SPF records](https://support.google.com/a/answer/33786?hl=en)
5. [DMARC records](https://support.google.com/a/answer/2466563?hl=en)
6. Public Admin Page
7. Directory listing
8. [Validate Content Security Policy for known bypasses](https://en.wikipedia.org/wiki/Content_Security_Policy)


# How to use
- Install the dependencies
- run easy_test.py
- enter website's name like facebook.com (without http://, https:// or www) 


# Known Issue:
Following code makes multiple requests through different function, can be optimized for better results.

# License

[The MIT License Copyright](https://opensource.org/licenses/MIT) (c) 2017 Manish Bhattacharya

#Contact
If you have any queries, feel free to reach out at my Twitter [Manish Bhattacharya](https://twitter.com/introvertmac007)

// This is a Test for the code



