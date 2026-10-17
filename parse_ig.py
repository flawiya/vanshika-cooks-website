import re
import json

with open(r'C:\Users\flavi\.gemini\antigravity\brain\8d223c30-3a07-4136-b949-2f235091b408\.system_generated\steps\1234\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find cdninstagram urls
urls = re.findall(r'https://[^"\'\s]+\.cdninstagram\.com/[^"\'\s<>&]+', text)
clean_urls = list(set([u.replace('&amp;', '&') for u in urls]))
print(f"Total CDN URLs found: {len(clean_urls)}")
for i, u in enumerate(clean_urls):
    print(f"[{i}] {u[:150]}")

# Look for faral keywords
for word in ['चकली', 'करंजी', 'लाडू', 'शेव', 'चिवडा', 'शंकरपाळी', 'अनारसे', 'chakli', 'karanji', 'laddu', 'ladoo', 'chivda', 'shankarpali', 'sev', 'faral', 'फराळ', 'besan', 'poha']:
    m = len(re.findall(word, text, re.IGNORECASE))
    if m:
        print(f"Keyword match '{word}': {m}")

# Search for any post text/captions
with open("scratch_ig_urls.txt", "w", encoding="utf-8") as out:
    for u in clean_urls:
        out.write(u + "\n")
