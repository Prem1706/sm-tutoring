import urllib.request
import urllib.parse
import json
import ssl

def get_image(query):
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=3&orientation=landscape"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        response = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        data = json.loads(response)
        if data.get('results'):
            for r in data['results']:
                desc = r.get('description') or r.get('alt_description')
                url = r['urls']['raw']
                print(f"[{query}] {desc}\n  -> {url}&q=80&w=1200&auto=format&fit=crop")
    except Exception as e:
        print(f"Error: {e}")

get_image("child doing homework")
get_image("tutor helping child")
get_image("school notebooks")
get_image("confident young student")
get_image("parent helping child homework")
