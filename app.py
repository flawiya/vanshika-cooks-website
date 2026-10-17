"""
Vanshika Swadisht Faral (वंशिका स्वादिष्ट फराळ 🪔)
Official E-Commerce Selling Platform for @vanshikacooks
Selling authentic homemade traditional Diwali snacks & pure desi ghee sweets.
Dual Language: English & हिन्दी / मराठी.
Delivery Area: Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India.
Delivery Pricing: ₹60 if cart total is below ₹700; FREE Delivery if ₹700 or above.
Payment Terms: Cash on Delivery with 50% initial advance payment.
Owner WhatsApp Inquiries: Routed securely through /order-whatsapp
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
import sqlite3
import json
import urllib.parse
import os
import random
import string

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "vanshika-faral-store-secret-2026")

DB_PATH = os.path.join(os.path.dirname(__file__), "vanshika_cooks.db")
SUPPORTED_LANGUAGES = ["en", "hi"]

# Official Owner WhatsApp Contact Numbers
WHATSAPP_NUMBER_1 = "918623865447"
WHATSAPP_NUMBER_2 = "918999585283"

# Delivery Pricing & Exact Location Definition
DELIVERY_FEE_BELOW_700 = 60
DELIVERY_FEE_ABOVE_700 = 0  # Free Delivery on orders ₹700 and above!
LOCAL_DELIVERY_CITY = "Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India."

def compute_delivery_fee(subtotal, is_outstation=False):
    """Calculates delivery charge: ₹60 if below ₹700, FREE (₹0) if ₹700 or above."""
    if is_outstation:
        return 0
    return DELIVERY_FEE_ABOVE_700 if subtotal >= 700 else DELIVERY_FEE_BELOW_700

TRANSLATIONS = {
    "en": {
        "lang_code": "en",
        "lang_name": "English",
        "brand_name": "Vanshika Swadisht Faral",
        "tagline": "Homemade Traditional Diwali Snacks & Sweets Made with Love",
        "sub_tagline": "Pure Desi Ghee • 100% Hygienic • Freshly Prepared Upon Order",
        "home": "Home",
        "faral_menu": "Faral Menu",
        "order_now": "Order Faral",
        "about": "Our Tradition",
        "contact": "Contact & Pre-Order",
        "cart": "My Faral Box",
        "filter_all": "All Faral Items",
        "filter_snacks": "Crispy Snacks",
        "filter_sweets": "Festive Sweets",
        "order_whatsapp": "Order on WhatsApp",
        "pre_order_now": "Pre-Order for Diwali",
        "quick_order": "Quick Order",
        "add_to_cart": "Add to Faral Box",
        "price_per_pack": "Pack Size & Price:",
        "shelf_life": "Shelf Life:",
        "taste_profile": "Taste Profile:",
        "pure_ingredients": "Key Ingredients:",
        "bestseller": "Bestseller",
        "customer_reviews": "Loved by Families Across Maharashtra & Beyond",
        "reviews_sub": "Authentic taste of home delivered to thousands of happy festival celebrations",
        "why_choose_us": "Why Families Trust Vanshika Swadisht Faral",
        "trust_1_title": "100% Pure Desi Ghee & Quality Grains",
        "trust_1_desc": "No cheap vanaspati or palm oil. Our sweets are slow-roasted in pure cow ghee and traditional grains.",
        "trust_2_title": "Freshly Fried Upon Order",
        "trust_2_desc": "Never stale or factory-mass-produced. Made in small hygienic kitchen batches right before delivery.",
        "trust_3_title": "Airtight Festive Packaging",
        "trust_3_desc": "Packed in food-grade airtight containers so your chaklis and karanjis arrive 100% crisp and unbroken.",
        "trust_4_title": "Doorstep Delivery",
        "trust_4_desc": "Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India. ₹60 fee below ₹700, and FREE Delivery above ₹700!",
        "booking_banner_title": "🪔 Diwali 2026 Pre-Orders Are Now Officially Open!",
        "booking_banner_sub": "Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India. ₹60 below ₹700, FREE Delivery above ₹700. COD with 50% advance.",
        "view_menu": "Explore Faral Menu",
        "switch_to_hindi": "मराठी / हिन्दी मध्ये पहा",
        "switch_to_english": "View in English",
        "pack_250g": "250g Pack",
        "pack_500g": "500g Pack",
        "pack_1kg": "1 kg Pack",
        "custom_inquiry": "Need Corporate or Bulk Gifting?",
        "custom_sub": "We deliver customized boxes with company branding and diwali cards for corporate teams.",
        "submit_inquiry": "Submit Booking Request",
        "inquiry_sent_success": "Thank you! Your pre-order request has been received. Vanshika will confirm your booking via WhatsApp shortly.",
        "delivery_notice_pill": "📍 Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India. (₹60 below ₹700 | FREE Delivery above ₹700) • Outside? Contact for courier",
        "cod_terms_notice": "💰 Cash on Delivery with 50% advance booking payment. 50% advance required via UPI to confirm fresh batch preparation.",
        "delivery_fee_label": "Delivery Charge (Aurangabad/Sambhaji Nagar):",
        "order_id_label": "Order ID",
        "customer_name_label": "Customer Full Name",
        "phone_label": "WhatsApp / Phone Number",
        "address_label": "Complete Delivery Address & Landmark",
        "date_needed_label": "Requested Delivery Date",
        "send_whatsapp_1": "📲 Send Order to WhatsApp (Channel 1)",
        "send_whatsapp_2": "📲 Send Order to WhatsApp (Channel 2)",
        "outstation_link_text": "Need delivery outside Aurangabad/Sambhaji Nagar? Click here for Outstation Inquiry"
    },
    "hi": {
        "lang_code": "hi",
        "lang_name": "मराठी / हिन्दी",
        "brand_name": "वंशिका स्वादिष्ट फराळ 🪔",
        "tagline": "घरगुती पारंपरिक दिवाळी फराळ व मिठाई | प्रेमाने तयार केलेले",
        "sub_tagline": "शुद्ध साजूक तूप • १००% हायजिनिक • ऑर्डरनुसार ताजे बनवलेले",
        "home": "होम",
        "faral_menu": "फराळ मेन्यू",
        "order_now": "फराळ ऑर्डर करा",
        "about": "आमची परंपरा",
        "contact": "ऑर्डर व चौकशी",
        "cart": "माझा फराळ बॉक्स",
        "filter_all": "सर्व फराळ",
        "filter_snacks": "खमंग नमकीन",
        "filter_sweets": "पारंपरिक मिठाई",
        "order_whatsapp": "व्हॉट्सॲपवर ऑर्डर करा",
        "pre_order_now": "दिवाळीसाठी प्री-ऑर्डर करा",
        "quick_order": "झटपट ऑर्डर",
        "add_to_cart": "बॉक्समध्ये जोडा",
        "price_per_pack": "वजन आणि किंमत:",
        "shelf_life": "टिकण्याची क्षमता:",
        "taste_profile": "चव आणि पोत:",
        "pure_ingredients": "वापरलेले शुद्ध साहित्य:",
        "bestseller": "सर्वाधिक पसंतीचे",
        "customer_reviews": "हजारो ग्राहकांची पसंती आणि विश्वास",
        "reviews_sub": "महाराष्ट्रातील घराघरात पोहोचलेली घरच्या हातची अस्सल दिवाळी चव",
        "why_choose_us": "वंशिका स्वादिष्ट फराळ का निवडावा?",
        "trust_1_title": "१००% शुद्ध साजूक तूप व दर्जेदार धान्य",
        "trust_1_desc": "वनस्पती किंवा पामतेलाचा शून्य वापर. सर्व मिठाई अस्सल गाईच्या साजूक तुपात मंद आचेवर भाजलेली.",
        "trust_2_title": "ऑर्डरनुसार ताजे तयार",
        "trust_2_desc": "फॅक्टरीचे जुने पॅकिंग नाही. तुमची ऑर्डर आल्यावर ताज्या बॅचमध्ये तयार करून पाठवले जाते.",
        "trust_3_title": "हवाबंद दर्जेदार पॅकिंग",
        "trust_3_desc": "चकली व करंजी न तुटता एकदम कुरकुरीत राहावी म्हणून खास हवाबंद बॉक्समध्ये सुरक्षित पॅकिंग.",
        "trust_4_title": "थेट घरपोच डिलिव्हरी",
        "trust_4_desc": "औरंगाबाद / छत्रपती संभाजीनगर, महाराष्ट्र, भारत मध्ये थेट घरपोच डिलिव्हरी. ₹७०० खाली ₹६०, आणि ₹७००+ वर मोफत डिलिव्हरी (FREE Delivery)!",
        "booking_banner_title": "🪔 दिवाळी २०२६ चे प्री-बुकिंग सुरू झाले आहे!",
        "booking_banner_sub": "Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India. ₹७०० खाली ₹६० शुल्क, ₹७००+ वर मोफत डिलिव्हरी. ५०% ॲडव्हान्ससह COD उपलब्ध.",
        "view_menu": "फराळ मेन्यू पहा",
        "switch_to_hindi": "मराठी / हिन्दी मध्ये पहा",
        "switch_to_english": "View in English",
        "pack_250g": "२५० ग्रॅम पॅक",
        "pack_500g": "५०० ग्रॅम पॅक",
        "pack_1kg": "१ किलो पॅक",
        "custom_inquiry": "कॉर्पोरेट किंवा मोठ्या प्रमाणावर गिफ्टिंग हवी आहे?",
        "custom_sub": "कंपनी भेटवस्तू, संस्था किंवा फॅमिलीसाठी खास कस्टमाईज्ड गिफ्ट बॉक्सेस उपलब्ध आहेत.",
        "submit_inquiry": "बुकिंग विनंती पाठवा",
        "inquiry_sent_success": "धन्यवाद! तुमची फराळ ऑर्डर चौकशी प्राप्त झाली आहे. वंशिका लवकरच व्हॉट्सॲपवर संपर्क करतील.",
        "delivery_notice_pill": "📍 Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India. (₹७०० खाली ₹६० | ₹७००+ वर मोफत डिलिव्हरी) • इतर शहरांसाठी कुरिअर चौकशी",
        "cod_terms_notice": "💰 कॅश ऑन डिलिव्हरी (५०% आगाऊ रक्कमेसह). साजूक तुपातील ताजी तयारी सुरू करण्यासाठी ५०% ॲडव्हान्स UPI द्वारे आवश्यक आहे.",
        "delivery_fee_label": "डिलिव्हरी शुल्क (औरंगाबाद / संभाजीनगर):",
        "order_id_label": "ऑर्डर क्रमांक (Order ID)",
        "customer_name_label": "ग्राहकाचे पूर्ण नाव",
        "phone_label": "व्हॉट्सॲप / संपर्क क्रमांक",
        "address_label": "घरपोच पत्ता व लँडमार्क",
        "date_needed_label": "हवी असलेली डिलिव्हरी तारीख",
        "send_whatsapp_1": "📲 व्हॉट्सॲप चॅनल १ वर पाठवा",
        "send_whatsapp_2": "📲 व्हॉट्सॲप चॅनल २ वर पाठवा",
        "outstation_link_text": "औरंगाबाद/संभाजीनगरबाहेरील इतर शहरांसाठी डिलिव्हरी हवी आहे? येथे क्लिक करा"
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
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
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

def generate_order_id(is_outstation=False):
    """Generates an unique human-readable Order ID e.g. #VSF-2026-8A4F or #VSF-OUT-9B2C."""
    prefix = "VSF-OUT" if is_outstation else "VSF-2026"
    chars = string.ascii_uppercase + string.digits
    conn = get_db_connection()
    while True:
        suffix = "".join(random.choices(chars, k=4))
        order_id = f"#{prefix}-{suffix}"
        row = conn.execute("SELECT id FROM orders WHERE order_id = ?", (order_id,)).fetchone()
        if not row:
            conn.close()
            return order_id

def build_order_whatsapp_message(order, items_list):
    """Formats complete WhatsApp order notification message for owners."""
    is_outstation = (order["order_type"] == "outstation")
    city_display = order["city"] if is_outstation else "Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India."

    if is_outstation:
        msg = f"🪔 *OUTSTATION DIWALI FARAL INQUIRY*\n"
        msg += f"==============================\n"
        msg += f"🆔 *Inquiry ID:* {order['order_id']}\n"
        msg += f"👤 *Customer Name:* {order['customer_name']}\n"
        msg += f"📞 *Contact Number:* {order['phone']}\n"
        msg += f"📍 *Delivery Address:* {order['address']}\n"
        msg += f"🏙️ *Destination City/Location:* {city_display}\n"
        msg += f"📅 *Requested Delivery Date:* {order['delivery_date']}\n\n"
        msg += f"📦 *REQUESTED ITEMS & QUANTITY:*\n"
        for item in items_list:
            msg += f"• {item.get('qty', 1)}x {item.get('name', '')} ({item.get('pack', '')}) - ₹{item.get('subtotal', item.get('price', 0))}\n"
        msg += f"\n💰 *ESTIMATED FARAL SUBTOTAL:* ₹{int(order['subtotal'])}\n"
        msg += f"📦 *Courier Shipping Charge:* (To be quoted on WhatsApp)\n"
        if order.get("special_notes"):
            msg += f"\n💬 *Customer Note:* {order['special_notes']}\n"
        msg += f"==============================\n"
        msg += f"🔔 *Action Needed:* Please contact customer, quote parcel courier charges, and confirm dispatch."
    else:
        msg = f"🪔 *NEW DIWALI FARAL ORDER PLACED!*\n"
        msg += f"==============================\n"
        msg += f"🆔 *Order ID:* {order['order_id']}\n"
        msg += f"👤 *Customer Name:* {order['customer_name']}\n"
        msg += f"📞 *Contact Number:* {order['phone']}\n"
        msg += f"📍 *Delivery Address:* {order['address']}\n"
        msg += f"🏙️ *Delivery Location:* Doorstep delivery across Aurangabad/Chhatrapati Sambhajinagar, Maharashtra, India.\n"
        msg += f"📅 *Order Needed Date:* {order['delivery_date']}\n\n"
        msg += f"📦 *ORDER QUANTITY & ITEMS:*\n"
        for item in items_list:
            msg += f"• {item.get('qty', 1)}x {item.get('name', '')} ({item.get('pack', '')}) - ₹{item.get('subtotal', item.get('price', 0))}\n"
        msg += f"\n💰 *BILL BREAKDOWN:*\n"
        msg += f"• Faral Subtotal: ₹{int(order['subtotal'])}\n"
        if int(order['delivery_fee']) == 0:
            msg += f"• Delivery Fee: ₹0 (FREE DELIVERY - Cart ₹700+)\n"
        else:
            msg += f"• Delivery Fee: ₹{int(order['delivery_fee'])} (Rate: ₹60 below ₹700, FREE above ₹700)\n"
        msg += f"• *Total Order Value:* ₹{int(order['total_amount'])}\n"
        msg += f"------------------------------\n"
        msg += f"💳 *PAYMENT TERMS (COD with 50% Advance):*\n"
        msg += f"• *50% Initial Advance to Pay:* ₹{int(order['advance_amount'])}\n"
        msg += f"• *50% Cash on Delivery (Balance):* ₹{int(order['cod_balance'])}\n"
        if order.get("special_notes"):
            msg += f"\n💬 *Customer Note:* {order['special_notes']}\n"
        msg += f"==============================\n"
        msg += f"🔔 *Action Needed:* Verify fresh preparation slot, confirm order with customer, and send UPI details for 50% initial advance payment."

    return msg

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

@app.context_processor
def inject_translations():
    lang = get_current_lang()
    t = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    return {
        "current_lang": lang,
        "t": t,
        "other_lang": "hi" if lang == "en" else "en",
        "other_lang_label": "मराठी / हिन्दी" if lang == "en" else "English",
        "delivery_fee_below_700": DELIVERY_FEE_BELOW_700,
        "delivery_fee_above_700": DELIVERY_FEE_ABOVE_700,
        "local_city": LOCAL_DELIVERY_CITY
    }

# ----------------- ROUTES -----------------

@app.route("/")
def home():
    lang = get_current_lang()
    conn = get_db_connection()

    products_rows = conn.execute("SELECT * FROM faral_products ORDER BY is_bestseller DESC, id ASC").fetchall()
    products = [FaralProduct(r, lang) for r in products_rows]

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
    return render_template("home.html", products=products, reviews=reviews)

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
    conn.close()

    return render_template("faral_menu.html", products=products, selected_category=category, search_query=query)

@app.route("/product/<slug>")
def product_detail(slug):
    lang = get_current_lang()
    conn = get_db_connection()

    row = conn.execute("SELECT * FROM faral_products WHERE slug = ?", (slug,)).fetchone()
    if row:
        product = FaralProduct(row, lang)
        related_rows = conn.execute("SELECT * FROM faral_products WHERE slug != ? ORDER BY RANDOM() LIMIT 3", (slug,)).fetchall()
        related = [FaralProduct(r, lang) for r in related_rows]
        conn.close()
        return render_template("product_detail.html", product=product, related_products=related)

    conn.close()
    return redirect(url_for("faral_menu"))

# ----------------- CHECKOUT & ORDERING -----------------

@app.route("/cart")
@app.route("/checkout")
@app.route("/order")
def checkout():
    lang = get_current_lang()
    conn = get_db_connection()
    products_rows = conn.execute("SELECT * FROM faral_products ORDER BY id ASC").fetchall()
    products = [FaralProduct(r, lang) for r in products_rows]
    conn.close()

    prefill_slug = request.args.get("item", "")
    prefill_pack = request.args.get("pack", "500g")
    prefill_qty = int(request.args.get("qty", 1))

    return render_template(
        "checkout.html",
        products=products,
        prefill_slug=prefill_slug,
        prefill_pack=prefill_pack,
        prefill_qty=prefill_qty
    )

@app.route("/place-order", methods=["POST"])
def place_order():
    """Processes customer order, calculates delivery fee (₹60 below ₹700, FREE above ₹700) + 50% advance."""
    is_json = request.is_json
    data = request.get_json() if is_json else request.form

    customer_name = (data.get("customer_name") or "").strip()
    phone = (data.get("phone") or "").strip()
    delivery_zone = (data.get("delivery_zone") or "aurangabad").strip()
    other_city = (data.get("other_city") or "").strip()
    address = (data.get("address") or "").strip()
    delivery_date = (data.get("delivery_date") or "").strip()
    special_notes = (data.get("special_notes") or "").strip()

    raw_items = data.get("items")
    items_list = []
    if isinstance(raw_items, str):
        try:
            items_list = json.loads(raw_items)
        except Exception:
            items_list = []
    elif isinstance(raw_items, list):
        items_list = raw_items

    if not items_list:
        single_item = data.get("item_name")
        single_pack = data.get("item_pack", "500g")
        single_price = float(data.get("item_price", 0))
        single_qty = int(data.get("item_qty", 1))
        if single_item and single_price > 0:
            items_list.append({
                "name": single_item,
                "pack": single_pack,
                "price": single_price,
                "qty": single_qty,
                "subtotal": single_price * single_qty
            })

    if not customer_name or not phone or not address or not delivery_date or not items_list:
        if is_json:
            return jsonify({"status": "error", "message": "Please fill in all required fields (Name, Phone, Address, Delivery Date, and at least one Faral item)."}), 400
        return redirect(url_for("checkout", error="missing_fields"))

    is_outstation = (delivery_zone == "outstation")
    city = other_city if is_outstation and other_city else LOCAL_DELIVERY_CITY

    # Calculate subtotal and delivery charge: ₹60 if below ₹700, FREE if ₹700 or above
    subtotal = sum(float(item.get("subtotal", float(item.get("price", 0)) * int(item.get("qty", 1)))) for item in items_list)
    delivery_fee = compute_delivery_fee(subtotal, is_outstation=is_outstation)
    total_amount = subtotal + delivery_fee
    advance_amount = round(total_amount / 2.0)
    cod_balance = total_amount - advance_amount

    order_id = generate_order_id(is_outstation=is_outstation)
    order_type = "outstation" if is_outstation else "local"

    items_summary_lines = []
    for it in items_list:
        items_summary_lines.append(f"{it.get('qty', 1)}x {it.get('name')} ({it.get('pack')})")
    items_summary = ", ".join(items_summary_lines)

    conn = get_db_connection()
    conn.execute("""
    INSERT INTO orders (
        order_id, order_type, customer_name, phone, address, city,
        delivery_date, items_json, items_summary, subtotal, delivery_fee,
        total_amount, advance_amount, cod_balance, payment_terms,
        status, special_notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id, order_type, customer_name, phone, address, city,
        delivery_date, json.dumps(items_list, ensure_ascii=False), items_summary,
        subtotal, delivery_fee, total_amount, advance_amount, cod_balance,
        "COD with 50% Advance", "Pending 50% Advance Confirmation", special_notes
    ))
    conn.commit()
    conn.close()

    if is_json:
        return jsonify({
            "status": "success",
            "order_id": order_id,
            "redirect_url": url_for("order_success", order_id=order_id)
        })

    return redirect(url_for("order_success", order_id=order_id))

@app.route("/order-success/<order_id>")
def order_success(order_id):
    """Displays order confirmation receipt, unique Order ID, and instant WhatsApp dispatch buttons to both owners."""
    lang = get_current_lang()
    conn = get_db_connection()
    order_row = conn.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,)).fetchone()
    conn.close()

    if not order_row:
        return redirect(url_for("home"))

    order = dict(order_row)
    try:
        items_list = json.loads(order["items_json"])
    except Exception:
        items_list = []

    wa_message = build_order_whatsapp_message(order, items_list)
    encoded_wa = urllib.parse.quote(wa_message)

    wa_url_1 = url_for("dispatch_order_whatsapp", order_id=order_id, channel=1)
    wa_url_2 = url_for("dispatch_order_whatsapp", order_id=order_id, channel=2)

    return render_template(
        "order_success.html",
        order=order,
        items=items_list,
        wa_url_1=wa_url_1,
        wa_url_2=wa_url_2,
        wa_message=wa_message
    )

@app.route("/outstation-inquiry", methods=["GET", "POST"])
def outstation_inquiry():
    """Dedicated page for customers outside Aurangabad/Chhatrapati Sambhajinagar to request parcel/courier Faral delivery."""
    lang = get_current_lang()
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        city = request.form.get("city", "").strip()
        address = request.form.get("address", "").strip()
        delivery_date = request.form.get("delivery_date", "").strip()
        items_text = request.form.get("items", "").strip()
        notes = request.form.get("notes", "").strip()

        if name and phone and city and items_text:
            items_list = [{"name": items_text, "pack": "Custom Quantity", "qty": 1, "price": 0, "subtotal": 0}]
            order_id = generate_order_id(is_outstation=True)

            conn = get_db_connection()
            conn.execute("""
            INSERT INTO orders (
                order_id, order_type, customer_name, phone, address, city,
                delivery_date, items_json, items_summary, subtotal, delivery_fee,
                total_amount, advance_amount, cod_balance, payment_terms,
                status, special_notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                order_id, "outstation", name, phone, address or city, city,
                delivery_date or "Flexible", json.dumps(items_list, ensure_ascii=False), items_text,
                0, 0, 0, 0, 0, "Custom Outstation Courier", "Awaiting Courier Quote", notes
            ))
            conn.commit()
            conn.close()
            return redirect(url_for("order_success", order_id=order_id))

    return render_template("outstation.html")

@app.route("/about")
def about():
    return render_template("about.html")

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

# ----------------- DIRECT WHATSAPP GATEWAY -----------------

@app.route("/order-whatsapp")
def order_whatsapp():
    """Universal WhatsApp order router directing inquiries to WhatsApp without exposing phone numbers in the HTML."""
    channel = request.args.get("channel", "1")
    target_phone = WHATSAPP_NUMBER_2 if str(channel) == "2" else WHATSAPP_NUMBER_1

    item = (request.args.get("item") or "").strip()

    generic_items = ["", "Diwali Faral Assorted Box", "Direct Diwali Faral Inquiry", "Diwali Faral Direct Order", "Outstation Diwali Faral Inquiry", "Diwali Faral"]
    if item and item not in generic_items:
        msg = f"🪔 *Namaste Vanshika!* I would like to order *{item}*."
    else:
        msg = "🪔 *Namaste Vanshika!* I would like to order Diwali Faral."

    encoded_msg = urllib.parse.quote(msg)
    wa_url = f"https://api.whatsapp.com/send?phone={target_phone}&text={encoded_msg}"
    return redirect(wa_url)

@app.route("/dispatch-order-whatsapp/<order_id>")
def dispatch_order_whatsapp(order_id):
    """Directs order confirmation receipt to WhatsApp channels securely without exposing phone numbers in frontend."""
    channel = request.args.get("channel", "1")
    target_phone = WHATSAPP_NUMBER_2 if str(channel) == "2" else WHATSAPP_NUMBER_1

    conn = get_db_connection()
    order_row = conn.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,)).fetchone()
    conn.close()

    if not order_row:
        return redirect(url_for("home"))

    order = dict(order_row)
    try:
        items_list = json.loads(order["items_json"])
    except Exception:
        items_list = []

    wa_message = build_order_whatsapp_message(order, items_list)
    encoded_wa = urllib.parse.quote(wa_message)
    wa_url = f"https://api.whatsapp.com/send?phone={target_phone}&text={encoded_wa}"
    return redirect(wa_url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Starting Vanshika Swadisht Faral Store on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
