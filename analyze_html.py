import re
import json

with open(r'C:\Users\flavi\.gemini\antigravity\brain\8d223c30-3a07-4136-b949-2f235091b408\.system_generated\steps\1234\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Look for script tags or JSON payloads
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print(f"Total script tags: {len(scripts)}")

# Search for shortcodes or display_url
shortcodes = re.findall(r'"shortcode":\s*"([^"]+)"', text)
print("Shortcodes:", shortcodes)

# Search for display_url or thumbnail_src
display_urls = re.findall(r'"display_url":\s*"([^"]+)"', text)
print("Display URLs:", len(display_urls))

# Search for any jpg or webp urls
all_imgs = re.findall(r'https://[^"\'\s<>]+\.(?:jpg|jpeg|png|webp)[^"\'\s<>]*', text)
unique_imgs = list(set([u.replace('\\u0026', '&').replace('&amp;', '&') for u in all_imgs]))
print(f"Total image URLs found: {len(unique_imgs)}")

with open("found_images.txt", "w", encoding="utf-8") as out:
    for u in unique_imgs:
        out.write(u + "\n")
        print("IMG URL:", u[:120])

# Search for any faral or post descriptions
texts = re.findall(r'"text":\s*"([^"]+)"', text)
print("Texts found:", len(texts))
for t in texts[:10]:
    try:
        print("T:", t.encode('ascii', 'ignore').decode())
    except:
        pass
