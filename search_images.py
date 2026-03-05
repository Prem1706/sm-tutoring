import urllib.request
import re

def search_unsplash(query):
    url = f"https://unsplash.com/s/photos/{query.replace(' ', '-')}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        urls = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+', html)
        seen = set()
        res = []
        for u in urls:
            if u not in seen:
                seen.add(u)
                res.append(u)
        return res[:10]
    except Exception as e:
        print(f"Error: {e}")
        return []

print("Hero (close up child learning):")
for u in search_unsplash("close up child learning"): print(u)
print("\nAbout (tutor helping child):")
for u in search_unsplash("tutor helping child"): print(u)
print("\nServices (books studying):")
for u in search_unsplash("books studying close up"): print(u)
