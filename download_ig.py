import urllib.request
import re
import os

with open(r'C:\Users\flavi\.gemini\antigravity\brain\8d223c30-3a07-4136-b949-2f235091b408\.system_generated\steps\1234\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'property="og:image"\s+content="([^"]+)"', text)
if m:
    url = m.group(1).replace('&amp;', '&')
    print('Found Profile Image URL:', url[:120])
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        data = urllib.request.urlopen(req).read()
        os.makedirs('static/images', exist_ok=True)
        with open('static/images/vanshika_profile.jpg', 'wb') as out:
            out.write(data)
        print('Saved static/images/vanshika_profile.jpg, bytes:', len(data))
    except Exception as e:
        print('Error downloading:', e)
else:
    print('og:image not found')
