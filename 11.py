def url_check(urlable: str):
    return urlable.startswith("https") and urlable.endswith(".com")

str1 = "https://google.com"

print(f"Is valid URL: {url_check(str1)}")