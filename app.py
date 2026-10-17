"""
Vanshika Cooks - Bilingual (English / हिन्दी) Food & Recipe Web Application
Official Web Platform for @vanshikacooks Instagram Creator
Full dual-language support for UI, recipes, ingredients, steps, and tips.
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
import sqlite3
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "vanshika-cooks-secret-key-2026-bilingual")

DB_PATH = os.path.join(os.path.dirname(__file__), "vanshika_cooks.db")

# Supported languages
SUPPORTED_LANGUAGES = ["en", "hi"]

# Comprehensive Bilingual UI Translations
TRANSLATIONS = {
    "en": {
        "lang_code": "en",
        "lang_name": "English",
        "brand_name": "Vanshika Cooks",
        "tagline": "Authentic Recipes, Kitchen Secrets & Modern Flavour",
        "home": "Home",
        "recipes": "Recipes",
        "categories": "Categories",
        "kitchen_tips": "Kitchen Tips",
        "about": "About Vanshika",
        "reels": "Watch Reels",
        "contact": "Contact & Collab",
        "search_placeholder": "Search recipes, ingredients (e.g. paneer, dosa, chai)...",
        "filter_all": "All Recipes",
        "filter_breakfast": "Breakfast",
        "filter_main": "Main Course",
        "filter_snack": "Snacks & Chaat",
        "filter_dessert": "Desserts",
        "filter_quick": "Quick 15-Min",
        "filter_drinks": "Beverages",
        "prep_time": "Prep Time",
        "cook_time": "Cook Time",
        "total_time": "Total Time",
        "servings": "Servings",
        "difficulty": "Difficulty",
        "calories": "Calories",
        "ingredients": "Ingredients",
        "instructions": "Step-by-Step Instructions",
        "chef_tips": "Vanshika's Pro Secrets",
        "cook_mode": "Cook Mode",
        "scale_servings": "Adjust Servings:",
        "print_recipe": "Print Recipe",
        "share_recipe": "Share Recipe",
        "copied": "Recipe link copied to clipboard!",
        "view_recipe": "View Recipe",
        "explore_more": "Explore All Recipes",
        "featured_recipes": "Signature Recipes",
        "featured_sub": "Tried, tested, and loved by millions of home cooks",
        "trending_now": "Trending on @vanshikacooks",
        "latest_tips": "Kitchen Secrets & Hacks",
        "tips_sub": "Simple culinary science to level up your everyday cooking",
        "community_reviews": "Loved by Home Cooks",
        "reviews_sub": "Real feedback from readers cooking our recipes across the globe",
        "about_heading": "Hi, I'm Vanshika!",
        "about_sub": "Home Chef, Food Creator & Culinary Storyteller",
        "about_bio_short": "Welcome to my kitchen! I'm the creator behind @vanshikacooks. My goal is to make authentic Indian cooking approachable, deeply flavorful, and joyful for modern kitchens.",
        "newsletter_title": "Get Vanshika's Weekly Tadka",
        "newsletter_sub": "Handpicked weekly recipes, seasonal menus, and kitchen secrets delivered straight to your inbox.",
        "subscribe": "Subscribe Free",
        "subscribe_success": "Welcome to the family! Check your inbox this Sunday for delicious recipes.",
        "follow_instagram": "Follow @vanshikacooks on Instagram",
        "follow_sub": "Catch daily recipe reels, quick cooking stories, and behind-the-scenes!",
        "min": "mins",
        "step": "Step",
        "note": "Note",
        "no_recipes_found": "No recipes found matching your search. Try searching for 'paneer', 'dosa', or 'chai'!",
        "read_more": "Read More",
        "back_to_recipes": "← Back to Recipes",
        "contact_title": "Work with Vanshika",
        "contact_sub": "For brand collaborations, sponsored recipe reels, cooking masterclasses, or media inquiries.",
        "send_message": "Send Message",
        "message_sent_success": "Thank you! Your message has been sent successfully. Vanshika will get back to you shortly.",
        "name_label": "Your Full Name",
        "email_label": "Email Address",
        "phone_label": "Phone / WhatsApp (Optional)",
        "subject_label": "Subject / Purpose",
        "message_label": "Your Message",
        "brand_collab": "Brand Partnership / Sponsorship",
        "recipe_query": "Recipe Question / Feedback",
        "event_inquiry": "Workshop / Event Inquiry",
        "other": "Other",
        "diet_tag": "Diet",
        "switch_to_hindi": "हिन्दी में पढ़ें",
        "switch_to_english": "Read in English",
        "cook_mode_title": "Cook Mode Active",
        "cook_mode_sub": "Screen will stay awake. Check off each step as you cook!",
        "exit_cook_mode": "Exit Cook Mode",
        "completed": "Done"
    },
    "hi": {
        "lang_code": "hi",
        "lang_name": "हिन्दी",
        "brand_name": "वंशिका कुक्स",
        "tagline": "घर का असली स्वाद, रसोई के राज़ और नई रेसिपीज़",
        "home": "होम",
        "recipes": "रेसिपीज़",
        "categories": "श्रेणियाँ",
        "kitchen_tips": "किचन टिप्स",
        "about": "वंशिका के बारे में",
        "reels": "रील्स देखें",
        "contact": "संपर्क एवं सहयोग",
        "search_placeholder": "रेसिपी या सामग्री खोजें (जैसे पनीर, डोसा, चाय)...",
        "filter_all": "सभी रेसिपीज़",
        "filter_breakfast": "नाश्ता",
        "filter_main": "मुख्य व्यंजन",
        "filter_snack": "नाश्ता व चाट",
        "filter_dessert": "मिठाइयाँ",
        "filter_quick": "झटपट 15 मिनट",
        "filter_drinks": "पेय पदार्थ",
        "prep_time": "तैयारी का समय",
        "cook_time": "पकाने का समय",
        "total_time": "कुल समय",
        "servings": "सर्विंग्स (लोग)",
        "difficulty": "कठिनाई",
        "calories": "कैलोरी",
        "ingredients": "आवश्यक सामग्री",
        "instructions": "विधि (कदम दर कदम)",
        "chef_tips": "वंशिका के सीक्रेट टिप्स",
        "cook_mode": "कुक मोड",
        "scale_servings": "सर्विंग्स बदलें:",
        "print_recipe": "रेसिपी प्रिंट करें",
        "share_recipe": "रेसिपी शेयर करें",
        "copied": "रेसिपी लिंक कॉपी हो गया!",
        "view_recipe": "रेसिपी देखें",
        "explore_more": "सभी रेसिपीज़ देखें",
        "featured_recipes": "खास पसंदीदा रेसिपीज़",
        "featured_sub": "लाखों होम कुक्स द्वारा बनाई और सराही गई रेसिपीज़",
        "trending_now": "इंस्टाग्राम पर ट्रेंडिंग (@vanshikacooks)",
        "latest_tips": "रसोई के राज़ व नुस्खे",
        "tips_sub": "रोजाना के खाने को आसान और स्वादिष्ट बनाने के वैज्ञानिक तरीके",
        "community_reviews": "दर्शकों और कुक्स का प्यार",
        "reviews_sub": "हमारी रेसिपीज बनाकर खुश हुए परिवारों की सच्ची राय",
        "about_heading": "नमस्ते, मैं हूँ वंशिका!",
        "about_sub": "होम शेफ, फूड क्रिएटर एवं स्टोरीटेलर",
        "about_bio_short": "मेरी रसोई में आपका स्वागत है! मैं @vanshikacooks की फाउंडर हूँ। मेरा उद्देश्य है हर घर में भारतीय कुकिंग को आसान, मजेदार और रेस्टोरेंट जैसा लाजवाब बनाना।",
        "newsletter_title": "वंशिका का साप्ताहिक तड़का सब्सक्राइब करें",
        "newsletter_sub": "हर रविवार ताज़ा रेसिपीज़, मौसमी मेन्यू और किचन टिप्स सीधे अपने ईमेल पर पाएं।",
        "subscribe": "मुफ्त सब्सक्राइब करें",
        "subscribe_success": "हमारे परिवार में स्वागत है! इस रविवार अपने इनबॉक्स में स्वादिष्ट रेसिपीज़ देखें।",
        "follow_instagram": "इंस्टाग्राम पर @vanshikacooks को फॉलो करें",
        "follow_sub": "रोजाना नई रेसिपी रील्स, स्टोरीज और कुकिंग हैक्स देखने के लिए जुड़ें!",
        "min": "मिनट",
        "step": "कदम",
        "note": "नोट",
        "no_recipes_found": "आपकी खोज के अनुसार कोई रेसिपी नहीं मिली। 'पनीर', 'डोसा' या 'चाय' खोज कर देखें!",
        "read_more": "विस्तार से पढ़ें",
        "back_to_recipes": "← सभी रेसिपीज़ पर वापस जाएं",
        "contact_title": "वंशिका के साथ काम करें / संपर्क करें",
        "contact_sub": "ब्रांड साझेदारी, स्पॉन्सर्ड रील्स, कुकिंग मास्टरक्लास या मीडिया पूछताछ के लिए।",
        "send_message": "संदेश भेजें",
        "message_sent_success": "धन्यवाद! आपका संदेश सफलतापूर्वक भेज दिया गया है। वंशिका जल्द ही आपसे संपर्क करेंगी।",
        "name_label": "आपका पूरा नाम",
        "email_label": "ईमेल पता",
        "phone_label": "फ़ोन / व्हाट्सएप (वैकल्पिक)",
        "subject_label": "विषय / उद्देश्य",
        "message_label": "आपका संदेश",
        "brand_collab": "ब्रांड पार्टनरशिप / स्पॉन्सरशिप",
        "recipe_query": "रेसिपी से जुड़ा सवाल / सुझाव",
        "event_inquiry": "वर्कशॉप / इवेंट पूछताछ",
        "other": "अन्य",
        "diet_tag": "खानपान प्रकार",
        "switch_to_hindi": "हिन्दी में पढ़ें",
        "switch_to_english": "Read in English",
        "cook_mode_title": "कुक मोड एक्टिव",
        "cook_mode_sub": "स्क्रीन बंद नहीं होगी। खाना बनाते समय हर कदम पर टिक लगाते जाएं!",
        "exit_cook_mode": "कुक मोड से बाहर निकलें",
        "completed": "पूरा हुआ"
    }
}

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_current_lang():
    """Determine language from query parameter, session, or cookie. Defaults to 'en'."""
    # 1. Query parameter override (e.g. ?lang=hi)
    lang = request.args.get("lang")
    if lang in SUPPORTED_LANGUAGES:
        session["lang"] = lang
        return lang

    # 2. Session
    if "lang" in session and session["lang"] in SUPPORTED_LANGUAGES:
        return session["lang"]

    # 3. Cookie
    cookie_lang = request.cookies.get("vanshika_lang")
    if cookie_lang in SUPPORTED_LANGUAGES:
        session["lang"] = cookie_lang
        return cookie_lang

    return "en"

class RecipeItem:
    """Helper wrapper to expose language-specific attributes smoothly to templates."""
    def __init__(self, row, lang="en"):
        self.id = row["id"]
        self.slug = row["slug"]
        self.lang = lang
        self.is_hi = (lang == "hi")

        self.title = row["title_hi"] if self.is_hi else row["title_en"]
        self.title_en = row["title_en"]
        self.title_hi = row["title_hi"]

        self.summary = row["summary_hi"] if self.is_hi else row["summary_en"]
        self.category = row["category"]
        self.category_name = row["category_hi"] if self.is_hi else row["category_en"]

        self.prep_time = row["prep_time"]
        self.cook_time = row["cook_time"]
        self.total_time = row["total_time"]
        self.servings = row["servings"]
        self.difficulty = row["difficulty_hi"] if self.is_hi else row["difficulty_en"]
        self.diet_tag = row["diet_tag_hi"] if self.is_hi else row["diet_tag_en"]
        self.calories = row["calories"]
        self.image = row["image"]
        self.instagram_reel = row["instagram_reel"]
        self.is_featured = row["is_featured"]

        # Parse JSON fields based on language
        try:
            raw_ing = row["ingredients_hi"] if self.is_hi else row["ingredients_en"]
            self.ingredients = json.loads(raw_ing)
        except Exception:
            self.ingredients = []

        try:
            raw_steps = row["steps_hi"] if self.is_hi else row["steps_en"]
            self.steps = json.loads(raw_steps)
        except Exception:
            self.steps = []

        try:
            raw_tips = row["pro_tips_hi"] if self.is_hi else row["pro_tips_en"]
            self.pro_tips = json.loads(raw_tips)
        except Exception:
            self.pro_tips = []

@app.context_processor
def inject_translations():
    lang = get_current_lang()
    t = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    return {
        "current_lang": lang,
        "t": t,
        "other_lang": "hi" if lang == "en" else "en",
        "other_lang_label": "हिन्दी" if lang == "en" else "English"
    }

# ----------------- ROUTES -----------------

@app.route("/")
def home():
    lang = get_current_lang()
    conn = get_db_connection()

    # Featured recipes
    featured_rows = conn.execute("SELECT * FROM recipes WHERE is_featured = 1 ORDER BY id ASC LIMIT 4").fetchall()
    featured_recipes = [RecipeItem(r, lang) for r in featured_rows]

    # Latest / all recipes preview
    all_rows = conn.execute("SELECT * FROM recipes ORDER BY id ASC").fetchall()
    all_recipes = [RecipeItem(r, lang) for r in all_rows]

    # Kitchen tips
    tips_rows = conn.execute("SELECT * FROM kitchen_tips ORDER BY id ASC LIMIT 4").fetchall()
    tips = []
    for row in tips_rows:
        tips.append({
            "icon": row["icon"],
            "category": row["category_hi"] if lang == "hi" else row["category_en"],
            "title": row["title_hi"] if lang == "hi" else row["title_en"],
            "content": row["content_hi"] if lang == "hi" else row["content_en"]
        })

    # Testimonials
    test_rows = conn.execute("SELECT * FROM testimonials ORDER BY id ASC").fetchall()
    testimonials = []
    for row in test_rows:
        testimonials.append({
            "name": row["name"],
            "city": row["city_hi"] if lang == "hi" else row["city_en"],
            "rating": row["rating"],
            "recipe_tried": row["recipe_tried_hi"] if lang == "hi" else row["recipe_tried_en"],
            "text": row["text_hi"] if lang == "hi" else row["text_en"]
        })

    conn.close()
    return render_template(
        "home.html",
        featured_recipes=featured_recipes,
        all_recipes=all_recipes,
        tips=tips,
        testimonials=testimonials
    )

@app.route("/recipes")
def recipes_list():
    lang = get_current_lang()
    category = request.args.get("category", "all")
    query = request.args.get("q", "").strip()

    conn = get_db_connection()
    sql = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if category and category != "all":
        sql += " AND category = ?"
        params.append(category)

    if query:
        sql += " AND (title_en LIKE ? OR title_hi LIKE ? OR summary_en LIKE ? OR summary_hi LIKE ? OR ingredients_en LIKE ? OR ingredients_hi LIKE ?)"
        like_q = f"%{query}%"
        params.extend([like_q, like_q, like_q, like_q, like_q, like_q])

    sql += " ORDER BY is_featured DESC, id ASC"
    rows = conn.execute(sql, params).fetchall()
    recipes = [RecipeItem(r, lang) for r in rows]
    conn.close()

    return render_template("recipes_list.html", recipes=recipes, selected_category=category, search_query=query)

@app.route("/recipe/<slug>")
def recipe_detail(slug):
    lang = get_current_lang()
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM recipes WHERE slug = ?", (slug,)).fetchone()
    if not row:
        conn.close()
        return redirect(url_for("recipes_list"))

    recipe = RecipeItem(row, lang)

    # Get 3 related recipes
    related_rows = conn.execute("SELECT * FROM recipes WHERE slug != ? AND category = ? LIMIT 3", (slug, recipe.category)).fetchall()
    if len(related_rows) < 3:
        needed = 3 - len(related_rows)
        extra = conn.execute("SELECT * FROM recipes WHERE slug != ? ORDER BY RANDOM() LIMIT ?", (slug, needed)).fetchall()
        related_rows = list(related_rows) + list(extra)

    related = [RecipeItem(r, lang) for r in related_rows]
    conn.close()

    return render_template("recipe_detail.html", recipe=recipe, related_recipes=related)

@app.route("/recipe/<slug>/cook")
def recipe_cook_mode(slug):
    lang = get_current_lang()
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM recipes WHERE slug = ?", (slug,)).fetchone()
    conn.close()
    if not row:
        return redirect(url_for("recipes_list"))

    recipe = RecipeItem(row, lang)
    return render_template("cook_mode.html", recipe=recipe)

@app.route("/tips")
def kitchen_tips():
    lang = get_current_lang()
    conn = get_db_connection()
    tips_rows = conn.execute("SELECT * FROM kitchen_tips ORDER BY id ASC").fetchall()
    tips = []
    for row in tips_rows:
        tips.append({
            "icon": row["icon"],
            "category": row["category_hi"] if lang == "hi" else row["category_en"],
            "title": row["title_hi"] if lang == "hi" else row["title_en"],
            "content": row["content_hi"] if lang == "hi" else row["content_en"]
        })
    conn.close()
    return render_template("tips.html", tips=tips)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reels")
def reels():
    lang = get_current_lang()
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM recipes ORDER BY id ASC").fetchall()
    recipes = [RecipeItem(r, lang) for r in rows]
    conn.close()
    return render_template("reels.html", recipes=recipes)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if name and email and message:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO contact_inquiries (name, email, phone, subject, message) VALUES (?, ?, ?, ?, ?)",
                (name, email, phone, subject, message)
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

    # Determine redirect destination
    next_page = request.args.get("next")
    if not next_page or next_page.startswith("//") or "://" in next_page:
        next_page = url_for("home")

    resp = make_response(redirect(next_page))
    resp.set_cookie("vanshika_lang", lang, max_age=30*24*60*60)  # 30 days
    return resp

# ----------------- API ENDPOINTS -----------------

@app.route("/api/subscribe", methods=["POST"])
def api_subscribe():
    data = request.get_json(silent=True) or request.form
    email = data.get("email", "").strip().lower()
    lang = get_current_lang()

    if not email or "@" not in email:
        return jsonify({"status": "error", "message": "Invalid email address"}), 400

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO newsletter_subscribers (email, preferred_lang) VALUES (?, ?)", (email, lang))
        conn.commit()
        msg = TRANSLATIONS[lang]["subscribe_success"]
    except sqlite3.IntegrityError:
        msg = TRANSLATIONS[lang]["subscribe_success"]
    finally:
        conn.close()

    return jsonify({"status": "success", "message": msg})

@app.route("/api/recipes/search")
def api_search():
    lang = get_current_lang()
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "")

    conn = get_db_connection()
    sql = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if category and category != "all":
        sql += " AND category = ?"
        params.append(category)

    if q:
        sql += " AND (title_en LIKE ? OR title_hi LIKE ? OR summary_en LIKE ? OR summary_hi LIKE ? OR ingredients_en LIKE ? OR ingredients_hi LIKE ?)"
        like_q = f"%{q}%"
        params.extend([like_q, like_q, like_q, like_q, like_q, like_q])

    rows = conn.execute(sql, params).fetchall()
    results = []
    for r in rows:
        item = RecipeItem(r, lang)
        results.append({
            "slug": item.slug,
            "title": item.title,
            "summary": item.summary,
            "category": item.category_name,
            "prep_time": item.prep_time,
            "cook_time": item.cook_time,
            "total_time": item.total_time,
            "difficulty": item.difficulty,
            "diet_tag": item.diet_tag,
            "image": item.image,
            "url": url_for("recipe_detail", slug=item.slug)
        })
    conn.close()
    return jsonify({"count": len(results), "recipes": results})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Starting Vanshika Cooks bilingual server on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
