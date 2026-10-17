import urllib.request
import re
import os

with open(r'C:\Users\flavi\.gemini\antigravity\brain\8d223c30-3a07-4136-b949-2f235091b408\.system_generated\steps\1234\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'property="og:image"\s+content="([^"]+)"', text)
if m:
    url = m.group(1).replace('&amp;', '&')
    high_res_url = re.sub(r's\d+x\d+_', '', url)
    print("Trying high-res URL:", high_res_url[:120])
    req = urllib.request.Request(high_res_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        data = urllib.request.urlopen(req).read()
        with open('static/images/vanshika_logo_highres.jpg', 'wb') as out:
            out.write(data)
        print('Saved high-res logo! Bytes:', len(data))
    except Exception as e:
        print('High res failed:', e)
