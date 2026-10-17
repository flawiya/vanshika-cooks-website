# Vanshika Cooks — Official Bilingual Recipe Platform 🍳
**The official website for [@vanshikacooks](https://www.instagram.com/vanshikacooks/)**

An artisanal, modern culinary web platform featuring authentic homemade Indian recipes, kitchen secrets, video reels, and a seamless **English / हिन्दी** bilingual switch for all pages, recipe ingredients, instructions, and pro tips.

---

## 🌟 Key Features

1. **Full English / Hindi (हिन्दी) Bilingual Toggle:**
   - One-click language switcher in the header and mobile drawer.
   - Switch language on any page or individual recipe without losing your place.
   - Dual-language recipe titles, descriptions, categories, exact ingredient names/measurements, step-by-step instructions, and pro secrets.
   - Persistent language choice stored in session and cookies.

2. **Interactive Recipe Experience:**
   - **Dynamic Servings Scaler:** Adjust portions with `+` / `-` buttons; ingredient amounts recalculate automatically in real time!
   - **Interactive Ingredient Checklist:** Check off ingredients as you prepare them in the kitchen.
   - **Cook Mode (Distraction-Free):** Fullscreen view with oversized kitchen-friendly text, collapsible ingredients, step checkmarks, and **Screen Wake Lock API** (keeps your phone screen from dimming while cooking).
   - **Print Recipe:** Clean, ink-friendly CSS print stylesheet.
   - **Share Recipe:** Native Web Share API + clipboard fallback with feedback toasts.

3. **Instagram Reels & Social Integration:**
   - Dedicated Reels spotlight showcasing [@vanshikacooks](https://www.instagram.com/vanshikacooks/) content.
   - Direct Instagram links on every recipe card.
   - Community tag instructions (`#VanshikaCooks`).

4. **Kitchen Tips & Secrets (किचन टिप्स):**
   - Practical culinary science hacks (cotton-soft rotis, preventing burnt spices, keeping paneer tender, preserving fresh herbs).
   - One-click copy/share tip feature.

5. **Tested Home Cook Reviews:**
   - Authentic community testimonials from Delhi, Mumbai, Chandigarh, and Pune.

6. **Brand Collaboration & Inquiries:**
   - Professional contact form for brand sponsorships, workshops, and cooking inquiries.
   - Direct WhatsApp quick-chat routing.

---

## 🚀 Running Locally

```bash
# 1. Navigate to the project directory
cd C:\Users\flavi\.gemini\antigravity\scratch\vanshika-cooks-website

# 2. Initialize the SQLite database (already initialized)
python init_db.py

# 3. Start the Flask application
python app.py
```
Open your browser and visit:  
👉 **`http://localhost:5001`** (or `http://127.0.0.1:5001`)

---

## ☁️ 24/7 Cloud Deployment (Render.com)

1. Push this directory to your GitHub account (e.g. `https://github.com/flawiya/vanshika-cooks-website`).
2. Go to [Render.com](https://render.com) and click **New +** > **Web Service**.
3. Select your repository.
4. Set:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**. Your site will be live on a free `.onrender.com` domain 24/7!
