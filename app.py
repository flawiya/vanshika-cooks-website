"""
Vanshika Swadisht Faral (वंशिका स्वादिष्ट फराळ 🪔)
Official E-Commerce Selling Platform for @vanshikacooks
Selling authentic homemade traditional Diwali snacks, pure desi ghee sweets & gift hampers.
Dual Language: English & हिन्दी (with authentic Maharashtrian Marathi festive touch).
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
import sqlite3
import json
import urllib.parse
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "vanshika-faral-store-secret-2026")

DB_PATH = os.path.join(os.path.dirname(__file__), "vanshika_cooks.db")
SUPPORTED_LANGUAGES = ["en", "hi"]

# Secure contact number representation (WhatsApp inquiry gateway)
WHATSAPP_CONTACT = "919876543210"

TRANSLATIONS = {
    "en": {
        "lang_code": "en",
        "lang_name": "English",
        "brand_name": "Vanshika Swadisht Faral",
        "tagline": "Homemade Traditional Diwali Snacks & Sweets Made with Love",
        "sub_tagline": "Pure Desi Ghee • 100% Hygienic • Freshly Prepared Upon Order",
        "home": "Home",
        "faral_menu": "Faral Menu",
        "hampers": "Gift Hampers",
        "about": "Our Tradition",
        "reels": "Watch Making",
        "contact": "Pre-Order / Bulk",
        "cart": "My Faral Box",
        "filter_all": "All Faral Items",
        "filter_snacks": "Crispy Snacks",
        "filter_sweets": "Festive Sweets",
        "filter_hampers": "Gift Hampers",
        "order_whatsapp": "Order on WhatsApp",
        "pre_order_now": "Pre-Order for Diwali",
        "quick_order": "Quick Order",
        "add_to_cart": "Add to Faral Box",
        "price_per_pack": "Pack Size & Price:",
        "shelf_life": "Shelf Life:",
        "taste_profile": "Taste Profile:",
        "pure_ingredients": "Key Ingredients:",
        "bestseller": "Bestseller",
        "items_included": "What's Inside This Hamper:",
        "customer_reviews": "Loved by Families Across Maharashtra & Beyond",
        "reviews_sub": "Authentic taste of home delivered to thousands of happy festival celebrations",
        "why_choose_us": "Why Families Trust Vanshika Swadisht Faral",
        "trust_1_title": "100% Pure Desi Ghee & Quality Grains",
        "trust_1_desc": "No cheap vanaspati or palm oil. Our sweets are slow-roasted in pure cow ghee and traditional grains.",
        "trust_2_title": "Freshly Fried Upon Order",
        "trust_2_desc": "Never stale or factory-mass-produced. Made in small hygienic kitchen batches right before shipping.",
        "trust_3_title": "Airtight Festive Packaging",
        "trust_3_desc": "Packed in food-grade airtight containers so your chaklis and karanjis arrive 100% crisp and unbroken.",
        "trust_4_title": "Doorstep Delivery Before Diwali",
        "trust_4_desc": "Carefully dispatched to Mumbai, Pune, Nashik, across India and international UK orders on time.",
        "booking_banner_title": "🪔 Diwali 2026 Pre-Orders Are Now Officially Open!",
        "booking_banner_sub": "Avoid the last-minute festival rush! Book early to ensure guaranteed fresh delivery for your family.",
        "view_menu": "Explore Faral Menu",
        "view_hampers": "View Gift Hampers",
        "switch_to_hindi": "मराठी / हिन्दी मध्ये पहा",
        "switch_to_english": "View in English",
        "pack_250g": "250g Pack",
        "pack_500g": "500g Pack",
        "pack_1kg": "1 kg Pack",
        "custom_inquiry": "Need Corporate or Custom Gifting?",
        "custom_sub": "We deliver customized boxes with company branding and diwali cards for corporate teams.",
        "submit_inquiry": "Submit Booking Request",
        "inquiry_sent_success": "Thank you! Your pre-order request has been received. Vanshika will confirm your booking via WhatsApp shortly."
    },
    "hi": {
        "lang_code": "hi",
        "lang_name": "मराठी / हिन्दी",
        "brand_name": "वंशिका स्वादिष्ट फराळ 🪔",
        "tagline": "घरगुती पारंपरिक दिवाळी फराळ व मिठाई | प्रेमाने तयार केलेले",
        "sub_tagline": "शुद्ध साजूक तूप • १००% हायजिनिक • ऑर्डरनुसार ताजे बनवलेले",
        "home": "होम",
        "faral_menu": "फराळ मेन्यू",
        "hampers": "दिवाळी गिफ्ट बॉक्सेस",
        "about": "आमची परंपरा",
        "reels": "बनवताना पहा",
        "contact": "ऑर्डर व चौकशी",
        "cart": "माझा फराळ बॉक्स",
        "filter_all": "सर्व फराळ",
        "filter_snacks": "खमंग नमकीन",
        "filter_sweets": "पारंपरिक मिठाई",
        "filter_hampers": "गिफ्ट हॅम्पर्स",
        "order_whatsapp": "व्हॉट्सॲपवर ऑर्डर करा",
        "pre_order_now": "दिवाळीसाठी प्री-ऑर्डर करा",
        "quick_order": "झटपट ऑर्डर",
        "add_to_cart": "बॉक्समध्ये जोडा",
        "price_per_pack": "वजन आणि किंमत:",
        "shelf_life": "टिकण्याची क्षमता:",
        "taste_profile": "चव आणि पोत:",
        "pure_ingredients": "वापरलेले शुद्ध साहित्य:",
        "bestseller": "सर्वाधिक पसंतीचे",
        "items_included": "या बॉक्समध्ये काय आहे:",
        "customer_reviews": "हजारो ग्राहकांची पसंती आणि विश्वास",
        "reviews_sub": "महाराष्ट्रातील घराघरात पोहोचलेली घरच्या हातची अस्सल दिवाळी चव",
        "why_choose_us": "वंशिका स्वादिष्ट फराळ का निवडावा?",
        "trust_1_title": "१००% शुद्ध साजूक तूप व दर्जेदार धान्य",
        "trust_1_desc": "वनस्पती किंवा पामतेलाचा शून्य वापर. सर्व मिठाई अस्सल गाईच्या साजूक तुपात मंद आचेवर भाजलेली.",
        "trust_2_title": "ऑर्डरनुसार ताजे तयार",
        "trust_2_desc": "फॅक्टरीचे जुने पॅकिंग नाही. तुमची ऑर्डर आल्यावर ताज्या बॅचमध्ये तयार करून पाठवले जाते.",
        "trust_3_title": "हवाबंद दर्जेदार पॅकिंग",
        "trust_3_desc": "चकली व करंजी न तुटता एकदम कुरकुरीत राहावी म्हणून खास हवाबंद बॉक्समध्ये सुरक्षित पॅकिंग.",
        "trust_4_title": "दिवाळीपूर्वी वेळेवर घरपोच डिलिव्हरी",
        "trust_4_desc": "मुंबई, पुणे, नाशिक, संपूर्ण भारत तसेच आंतरराष्ट्रीय स्तरावर वेळेत घरपोच डिलिव्हरी.",
        "booking_banner_title": "🪔 दिवाळी २०२६ चे प्री-बुकिंग सुरू झाले आहे!",
        "booking_banner_sub": "सणासुदीच्या ऐनवेळच्या गर्दीपासून वाचा! आजच आपले बुकिंग निश्चित करा आणि ताजी चव मिळवा.",
        "view_menu": "फराळ मेन्यू पहा",
        "view_hampers": "गिफ्ट बॉक्सेस पहा",
        "switch_to_hindi": "मराठी / हिन्दी मध्ये पहा",
        "switch_to_english": "View in English",
        "pack_250g": "२५० ग्रॅम पॅक",
        "pack_500g": "५०० ग्रॅम पॅक",
        "pack_1kg": "१ किलो पॅक",
        "custom_inquiry": "कॉर्पोरेट किंवा मोठ्या प्रमाणावर गिफ्टिंग हवी आहे?",
        "custom_sub": "कंपनी भेटवस्तू, संस्था किंवा फॅमिलीसाठी खास कस्टमाईज्ड गिफ्ट बॉक्सेस उपलब्ध आहेत.",
        "submit_inquiry": "बुकिंग विनंती पाठवा",
        "inquiry_sent_success": "धन्यवाद! तुमची फराळ ऑर्डर चौकशी प्राप्त झाली आहे. वंशिका लवकरच व्हॉट्सॲपवर संपर्क करतील."
    }
}

def get_db_connection():
    needs_init = not os.path.exists(DB_PATH)
    if not needs_init:
        try:
            test_conn = sqlite3.connect(DB_PATH)
            cur = test_conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='faral_products'")
            if not cur.fetchone():
                needs_init = True
            test_conn.close()
        except Exception:
            needs_init = True

    if needs_init:
        try:
            from init_db import init_faral_db
            init_faral_db()
        except Exception as e:
            print(f"Error auto-initializing faral database: {e}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_current_lang():
    lang = request.args.get("lang")
    if lang in SUPPORTED_LANGUAGES:
        session["lang"] = lang
        return lang
    if "lang" in session and session["lang"] in SUPPORTED_LANGUAGES:
        return session["lang"]
    cookie_lang = request.cookies.get("vanshika_lang")
    if cookie_lang in SUPPORTED_LANGUAGES:
        session["lang"] = cookie_lang
        return cookie_lang
    return "en"

class FaralProduct:
    def __init__(self, row, lang="en"):
        self.id = row["id"]
        self.slug = row["slug"]
        self.lang = lang
        self.is_hi = (lang == "hi")

        self.name = row["name_hi"] if self.is_hi else row["name_en"]
        self.name_en = row["name_en"]
        self.name_hi = row["name_hi"]

        self.tagline = row["tagline_hi"] if self.is_hi else row["tagline_en"]
        self.description = row["description_hi"] if self.is_hi else row["description_en"]
        self.category = row["category"]
        self.category_name = row["category_hi"] if self.is_hi else row["category_en"]

        self.price_250g = row["price_250g"]
        self.price_500g = row["price_500g"]
        self.price_1kg = row["price_1kg"]
        self.price_gbp = row["price_gbp"]

        self.shelf_life = row["shelf_life_hi"] if self.is_hi else row["shelf_life_en"]
        self.taste_profile = row["taste_profile_hi"] if self.is_hi else row["taste_profile_en"]
        self.image = row["image"]
        self.is_bestseller = row["is_bestseller"]

        try:
            raw_ing = row["ingredients_hi"] if self.is_hi else row["ingredients_en"]
            self.ingredients = json.loads(raw_ing)
        except Exception:
            self.ingredients = []

class FaralHamper:
    def __init__(self, row, lang="en"):
        self.id = row["id"]
        self.slug = row["slug"]
        self.lang = lang
        self.is_hi = (lang == "hi")

        self.name = row["name_hi"] if self.is_hi else row["name_en"]
        self.tagline = row["tagline_hi"] if self.is_hi else row["tagline_en"]
        self.description = row["description_hi"] if self.is_hi else row["description_en"]
        self.weight = row["weight"]
        self.price_inr = row["price_inr"]
        self.price_gbp = row["price_gbp"]
        self.badge = row["badge_hi"] if self.is_hi else row["badge_en"]
        self.image = row["image"]

        try:
            raw_items = row["items_included_hi"] if self.is_hi else row["items_included_en"]
            self.items_included = json.loads(raw_items)
        except Exception:
            self.items_included = []

@app.context_processor
def inject_translations():
    lang = get_current_lang()
    t = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    return {
        "current_lang": lang,
        "t": t,
        "other_lang": "hi" if lang == "en" else "en",
        "other_lang_label": "मराठी / हिन्दी" if lang == "en" else "English"
    }

# ----------------- ROUTES -----------------

@app.route("/")
def home():
    lang = get_current_lang()
    conn = get_db_connection()

    products_rows = conn.execute("SELECT * FROM faral_products ORDER BY is_bestseller DESC, id ASC").fetchall()
    products = [FaralProduct(r, lang) for r in products_rows]

    hampers_rows = conn.execute("SELECT * FROM faral_hampers ORDER BY id ASC").fetchall()
    hampers = [FaralHamper(r, lang) for r in hampers_rows]

    reviews_rows = conn.execute("SELECT * FROM faral_reviews ORDER BY id ASC").fetchall()
    reviews = []
    for r in reviews_rows:
        reviews.append({
            "name": r["name"],
            "city": r["city_hi"] if lang == "hi" else r["city_en"],
            "rating": r["rating"],
            "item": r["item_hi"] if lang == "hi" else r["item_en"],
            "text": r["text_hi"] if lang == "hi" else r["text_en"]
        })

    conn.close()
    return render_template("home.html", products=products, hampers=hampers, reviews=reviews)

@app.route("/menu")
def faral_menu():
    lang = get_current_lang()
    category = request.args.get("category", "all")
    query = request.args.get("q", "").strip()

    conn = get_db_connection()
    sql = "SELECT * FROM faral_products WHERE 1=1"
    params = []

    if category and category != "all":
        sql += " AND category = ?"
        params.append(category)

    if query:
        sql += " AND (name_en LIKE ? OR name_hi LIKE ? OR description_en LIKE ? OR description_hi LIKE ? OR ingredients_en LIKE ? OR ingredients_hi LIKE ?)"
        like_q = f"%{query}%"
        params.extend([like_q, like_q, like_q, like_q, like_q, like_q])

    sql += " ORDER BY is_bestseller DESC, id ASC"
    rows = conn.execute(sql, params).fetchall()
    products = [FaralProduct(r, lang) for r in rows]

    hampers_rows = conn.execute("SELECT * FROM faral_hampers ORDER BY id ASC").fetchall()
    hampers = [FaralHamper(r, lang) for r in hampers_rows]
    conn.close()

    return render_template("faral_menu.html", products=products, hampers=hampers, selected_category=category, search_query=query)

@app.route("/product/<slug>")
def product_detail(slug):
    lang = get_current_lang()
    conn = get_db_connection()

    # Check products
    row = conn.execute("SELECT * FROM faral_products WHERE slug = ?", (slug,)).fetchone()
    if row:
        product = FaralProduct(row, lang)
        # Related items
        related_rows = conn.execute("SELECT * FROM faral_products WHERE slug != ? ORDER BY RANDOM() LIMIT 3", (slug,)).fetchall()
        related = [FaralProduct(r, lang) for r in related_rows]
        conn.close()
        return render_template("product_detail.html", product=product, related_products=related)

    # Check hampers
    h_row = conn.execute("SELECT * FROM faral_hampers WHERE slug = ?", (slug,)).fetchone()
    if h_row:
        hamper = FaralHamper(h_row, lang)
        conn.close()
        return render_template("hamper_detail.html", hamper=hamper)

    conn.close()
    return redirect(url_for("faral_menu"))

@app.route("/hampers")
def hampers_page():
    lang = get_current_lang()
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM faral_hampers ORDER BY id ASC").fetchall()
    hampers = [FaralHamper(r, lang) for r in rows]
    conn.close()
    return render_template("hampers.html", hampers=hampers)

@app.route("/cart")
def cart_page():
    return render_template("cart.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reels")
def reels():
    lang = get_current_lang()
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM faral_products ORDER BY id ASC").fetchall()
    products = [FaralProduct(r, lang) for r in rows]
    conn.close()
    return render_template("reels.html", products=products)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        city = request.form.get("city", "").strip()
        items = request.form.get("items", "").strip()
        instructions = request.form.get("instructions", "").strip()

        if name and phone:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO order_inquiries (customer_name, phone, email, delivery_city, items_ordered, total_estimate, special_instructions) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (name, phone, email, city, items, 0, instructions)
            )
            conn.commit()
            conn.close()
            return render_template("contact.html", success=True)

    return render_template("contact.html", success=False)

@app.route("/switch-language/<lang>")
def switch_language(lang):
    if lang not in SUPPORTED_LANGUAGES:
        lang = "en"
    session["lang"] = lang

    next_page = request.args.get("next")
    if not next_page or next_page.startswith("//") or "://" in next_page:
        next_page = url_for("home")

    resp = make_response(redirect(next_page))
    resp.set_cookie("vanshika_lang", lang, max_age=30*24*60*60)
    return resp

# ----------------- WHATSAPP ORDER GENERATOR -----------------

@app.route("/order-whatsapp")
def order_whatsapp():
    """Generates direct pre-filled WhatsApp link with ordered product, weight, and delivery inquiry."""
    item = request.args.get("item", "Diwali Faral Assorted Box")
    pack = request.args.get("pack", "500g")
    price = request.args.get("price", "")

    msg = f"🪔 *Namaste Vanshika!* I would like to order Diwali Faral:\n\n"
    msg += f"• *Item:* {item}\n"
    msg += f"• *Pack Size:* {pack}\n"
    if price:
        msg += f"• *Price:* ₹{price}\n"
    msg += f"\nPlease share availability and delivery timeframe. Thank you!"

    encoded_msg = urllib.parse.quote(msg)
    wa_url = f"https://api.whatsapp.com/send?text={encoded_msg}"
    return redirect(wa_url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Starting Vanshika Swadisht Faral Store on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
