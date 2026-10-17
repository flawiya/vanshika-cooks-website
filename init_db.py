"""
Vanshika Swadisht Faral (वंशिका स्वादिष्ट फराळ 🪔)
Database initialization for Diwali Food & Snacks E-Commerce Selling Website.
Dedicated artisanal catalog: Bhajani Chakli, Shahi Besan Ladoo, Coconut Karanji,
Poha Chivda, Shankarpali, Lasun Sev, Motichoor Ladoo, Anarse.
"""

import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "vanshika_cooks.db")

PRODUCTS = [
    {
        "slug": "bhajani-chakli",
        "name_en": "Authentic Crispy Bhajani Chakli",
        "name_hi": "खमंग व कुरकुरीत पारंपरिक भाजणी चकली",
        "tagline_en": "Traditional roasted multigrain spiral with sharp spikes & zero oiliness",
        "tagline_hi": "पारंपरिक भाजणीच्या पिठाची काटेरी, खमंग व तोंडात विरघळणारी चकली",
        "description_en": "Crafted from slow-roasted multigrain flour (chana dal, urad dal, rice, coriander seeds, and cumin), seasoned with organic white sesame, ajwain, and pure hing. Ultra-crispy, spiky, and light on the stomach without excess oil.",
        "description_hi": "पारंपरिक भाजणीच्या पिठापासून (डाळी, तांदूळ, धणे, जिरे भाजून) बनवलेली अस्सल चकली. पांढरे तीळ, ओवा आणि हिंगाची खमंग चव. अजिबात तेलकट नसलेली आणि जिभेवर विरघळणारी.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 175,
        "price_500g": 330,
        "price_1kg": 640,
        "price_gbp": 12.99,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Savory, Spiced, Crunchy with Sesame & Carom aroma",
        "taste_profile_hi": "खमंग, कुरकुरीत, तीळ व ओव्याचा सुवास",
        "image": "/static/images/products/bhajani_chakli.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Traditional Roasted Bhajani Flour", "Pure White Sesame (Til)", "Carom Seeds (Ajwain)", "Kashmiri Chilli", "Asafoetida (Hing)", "Refined Groundnut Oil", "Rock Salt"],
        "ingredients_hi": ["पारंपरिक भाजणी पीठ", "पांढरे तीळ", "ओवा", "कश्मीरी लाल मिरची", "हिंग", "शुद्ध शेंगदाणा तेल", "सेंधा मीठ"]
    },
    {
        "slug": "shahi-besan-ladoo",
        "name_en": "Shahi Pure Desi Ghee Danedar Besan Ladoo",
        "name_hi": "शुद्ध साजूक तुपातील दाणेदार बेसन लाडू",
        "tagline_en": "Slow-roasted coarse gram flour in pure cow ghee with cardamom & pistachios",
        "tagline_hi": "घरच्या साजूक तुपात खमंग भाजलेले, वेलची आणि पिस्त्यांचे दाणेदार लाडू",
        "description_en": "Patiently roasted for 45 minutes on low flame in pure country cow ghee. Made with coarse gram flour and traditional bura crystalline sugar to give that irresistible grainy (danedar) halwai texture. Studded with roasted pistachios and fragrant green cardamom.",
        "description_hi": "शुद्ध साजूक तुपात मंद आचेवर खमंग भाजलेले दाणेदार बेसन लाडू. पिठीसाखरेऐवजी पारंपरिक तगार (बुरा) वापरल्याने लाडू जिभेला चिकटत नाहीत आणि तोंडात विरघळतात. वेलची व पिस्त्याची मनसोक्त उधळण.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 210,
        "price_500g": 390,
        "price_1kg": 760,
        "price_gbp": 15.99,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Melt-in-mouth, Rich Pure Ghee, Cardamom & Nutty",
        "taste_profile_hi": "तोंडात विरघळणारे, साजूक तुपाचा घमघमाट, वेलची स्वाद",
        "image": "/static/images/products/shahi_besan_ladoo.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Coarse Chana Dal Besan", "100% Pure Desi Cow Ghee", "Traditional Bura Sugar", "Green Cardamom (Elaichi)", "Nutmeg (Jaiphal)", "California Pistachios"],
        "ingredients_hi": ["जाडसर डाळीचे बेसन", "१००% शुद्ध साजूक तूप", "पारंपरिक बुरा साखर", "हिरवी वेलची", "जायफळ", "पिस्ता"]
    },
    {
        "slug": "khuskhushit-karanji",
        "name_en": "Crispy Flaky Coconut & Mawa Karanji",
        "name_hi": "खुसखुशीत नारळ-खव्याची पारंपरिक करंजी",
        "tagline_en": "Delicate flaky pastry shell stuffed with roasted dry coconut, mawa & dry fruits",
        "tagline_hi": "पदराची खुसखुशीत करंजी, सुकं खोबरं, खवा, खसखस व सुकामेव्याच्या सारणाने भरलेली",
        "description_en": "Our signature crescent-shaped festive pastry. Made with a layered, blistering-crisp outer crust kneaded with hot ghee, stuffed generously with roasted dry grated coconut, pink-roasted khoya, poppy seeds (khas khas), charoli, and aromatic nutmeg.",
        "description_hi": "दिवाळीच्या ताटाची खरी शान! कडकडीत तुपाचे मोहन घालून मळलेली पदर सुटलेली खुसखुशीत पारी, आत गुलाबी भाजलेले सुके खोबरे, खवा, खसखस, चारोळी आणि जायफळाचे समृद्ध गोड सारण.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 200,
        "price_500g": 380,
        "price_1kg": 740,
        "price_gbp": 14.99,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Crisp flaky crust, aromatic sweet coconut & nutty mawa",
        "taste_profile_hi": "खुसखुशीत बिस्किटासारखी पारी, खोबरे व खव्याचा गोडवा",
        "image": "/static/images/products/karanji.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Refined Wheat Flour", "Chiroti Rava", "Pure Desi Ghee", "Dry Roasted Coconut", "Fresh Mawa", "Poppy Seeds (Khas Khas)", "Charoli & Almonds", "Cardamom & Nutmeg"],
        "ingredients_hi": ["मैदा", "चिरोटी रवा", "साजूक तूप", "भाजलेले सुके खोबरे", "ताजा खवा", "खसखस", "चारोळी व बदाम", "वेलची-जायफळ"]
    },
    {
        "slug": "patla-poha-chivda",
        "name_en": "Crunchy Roasted Patla Poha Chivda",
        "name_hi": "खमंग भाजलेला पातळ पोहा चिवडा",
        "tagline_en": "Low-oil roasted thin flattened rice with fried peanuts, dalia & curry leaves",
        "tagline_hi": "अतिशय कमी तेलात भाजलेला खमंग पातळ पोह्यांचा चिवडा, शेंगदाणे व खोबऱ्याच्या फोडणीसह",
        "description_en": "A guilt-free festival favorite! Thin paper poha is gently roasted dry until featherlight and crunchy, then tossed in an aromatic tempering of crisp green chillies, curry leaves, golden roasted peanuts, pandharpuri dalia, and dry coconut chips.",
        "description_hi": "कमी तेलाचा, पचायला हलका आणि खमंग चिवडा. पातळ पोहे मंद आचेवर भाजून त्यावर हिरवी मिरची, कढीपत्ता, शेंगदाणे, खोबऱ्याचे पातळ काप आणि डाळ्यांची खमंग फोडणी दिलेली. थोडीशी गोड-तिखट चव.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 150,
        "price_500g": 280,
        "price_1kg": 540,
        "price_gbp": 10.99,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Light, Crunchy, Sweet-Savory-Tangy tempered flavor",
        "taste_profile_hi": "हलका, कुरकुरीत, आंबट-गोड-तिखट खमंग चव",
        "image": "/static/images/products/poha_chivda.jpg",
        "is_bestseller": 0,
        "ingredients_en": ["Paper Thin Poha", "Roasted Peanuts", "Dalia (Futana Dal)", "Dry Coconut Slivers", "Crispy Curry Leaves", "Green Chillies", "Mustard & Cumin", "Turmeric, Hing, Rock Salt, Sugar"],
        "ingredients_hi": ["पातळ पोहे", "शेंगदाणे", "पंढरपुरी डाळे", "सुक्या खोबऱ्याचे काप", "कढीपत्ता", "हिरवी मिरची", "मोहरी-जिरे", "हळद, हिंग, मीठ, साखर"]
    },
    {
        "slug": "god-shankarpali",
        "name_en": "Melt-in-Mouth Flaky Sweet Shankarpali",
        "name_hi": "पदराची खुसखुशीत बिस्किटासारखी गोड शंकरपाळी",
        "tagline_en": "Crispy golden diamond biscuits kneaded with whole milk & pure ghee",
        "tagline_hi": "दूध, साखर आणि साजूक तुपाच्या अचूक प्रमाणातील पदर सुटलेली शंकरपाळी",
        "description_en": "Crafted using the golden 1:1:1 ratio (pure ghee, whole milk, and sugar). Rolled thick and slowly fried on low flame to create multi-layered, buttery, bite-sized diamond biscuits that melt like shortbread.",
        "description_hi": "तूप, दूध आणि साखरेच्या अचूक प्रमाणात बनवलेली शंकरपाळी. मंद आचेवर सावकाश तळल्यामुळे आत छान पदर सुटतात आणि ती बिस्किटासारखी खुसखुशीत होते. लहानांपासून मोठ्यांपर्यंत सर्वांची आवडती.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 160,
        "price_500g": 300,
        "price_1kg": 580,
        "price_gbp": 11.99,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Delicately sweet, Flaky layers, Mild cardamom undertone",
        "taste_profile_hi": "खमंग गोडवा, बिस्किटासारखे पदर, वेलचीचा सुवास",
        "image": "/static/images/products/shankarpali.jpg",
        "is_bestseller": 0,
        "ingredients_en": ["Refined Wheat Flour", "Whole Cow Milk", "Pure Desi Ghee", "Granulated Sugar", "Cardamom Powder", "Pinch of Sea Salt"],
        "ingredients_hi": ["मैदा", "गाईचे दूध", "शुद्ध साजूक तूप", "साखर", "वेलची पूड", "चिमूटभर मीठ"]
    },
    {
        "slug": "tikha-lasun-sev",
        "name_en": "Crispy Spicy Garlic Besan Sev (Lasun Shev)",
        "name_hi": "चमचमीत तिखट लसूण बारीक शेव",
        "tagline_en": "Golden crisp chickpea noodles infused with freshly pounded garlic & spices",
        "tagline_hi": "ताजा लसूण, हिंग आणि कश्मीरी मिरचीच्या खमंग चवीची कुरकुरीत शेव",
        "description_en": "Finely pressed crispy chickpea flour sev seasoned with freshly crushed garlic paste, carom seeds, red chilli, and a pinch of asafoetida. Fried to golden perfection with zero greasiness.",
        "description_hi": "ताज्या लसणाची खमंग पेस्ट, ओवा आणि तिखट मसाल्यांनी समृद्ध बेसन शेव. चहाच्या वेळी किंवा चिवड्यासोबत खाण्यासाठी एकदम चविष्ट आणि अतिशय कुरकुरीत.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 150,
        "price_500g": 280,
        "price_1kg": 540,
        "price_gbp": 10.99,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Zesty garlic punch, Mildly spicy, Extra crunchy",
        "taste_profile_hi": "लसणाची खमंग चव, झणझणीत तिखट, मस्त कुरकुरीत",
        "image": "/static/images/products/lasun_sev.jpg",
        "is_bestseller": 0,
        "ingredients_en": ["Gram Flour (Besan)", "Fresh Garlic Cloves", "Red Kashmiri Chilli", "Carom Seeds (Ajwain)", "Asafoetida", "Refined Groundnut Oil", "Rock Salt"],
        "ingredients_hi": ["चना डाळीचे पीठ", "गावरान लसूण", "कश्मीरी लाल तिखट", "ओवा", "हिंग", "शेंगदाणा तेल", "मीठ"]
    },
    {
        "slug": "shahi-motichoor-ladoo",
        "name_en": "Shahi Pure Ghee Motichoor Ladoo",
        "name_hi": "शुद्ध साजूक तुपातील मोतीचूर लाडू",
        "tagline_en": "Melt-in-mouth tiny golden pearls in desi ghee with saffron & melon seeds",
        "tagline_hi": "बारीक मण्यांसारखे तोंडात विरघळणारे साजूक तुपातील केशर मोतीचूर लाडू",
        "description_en": "Authentic halwai-style tiny gram flour boondi pearls slowly fried in 100% pure desi ghee, soaked in fragrant saffron and cardamom sugar syrup, studded with magajtari (watermelon seeds).",
        "description_hi": "दिवाळीच्या पूजेसाठी आणि पाहुण्यांच्या आदरातिथ्यासाठी खास! अस्सल साजूक तुपात तळलेले बारीक बुंदीचे दाणे, काश्मिरी केशर, वेलची आणि मगज बी (खरबुजाच्या बिया) घालून वळलेले मऊ लाडू.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 220,
        "price_500g": 410,
        "price_1kg": 790,
        "price_gbp": 16.50,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Juicy pearls, Saffron-cardamom warmth, Pure ghee aroma",
        "taste_profile_hi": "रसरशीत, केशरी सुवास, साजूक तुपाचा समृद्ध स्वाद",
        "image": "/static/images/products/motichoor_ladoo.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Besan (Gram Flour)", "100% Pure Desi Cow Ghee", "Sugar Syrup", "Kashmiri Saffron", "Green Cardamom", "Melon Seeds (Magajtari)"],
        "ingredients_hi": ["बेसन", "शुद्ध साजूक तूप", "साखरेचा पाक", "केशर", "हिरवी वेलची", "मगज बी"]
    },
    {
        "slug": "paramparik-anarse",
        "name_en": "Traditional Ghee Anarse with Poppy Seeds",
        "name_hi": "पारंपरिक खसखस लावलेले जाळीदार अनारसे",
        "tagline_en": "Fermented aged rice & jaggery delicacies fried in pure cow ghee with white poppy crust",
        "tagline_hi": "साजूक तुपात तळलेले, खसखशीचे आवरण असलेले पारंपरिक जाळीदार अनारसे",
        "description_en": "An ancient Maharashtrian festival art. Premium aged Wada Kolam rice is soaked for 3 days with daily water changes, shade-dried, hand-pounded with organic Kolhapur jaggery, and naturally fermented before slow frying in pure cow ghee.",
        "description_hi": "अतिशय कौशल्याने बनवले जाणारे पारंपरिक जाळीदार अनारसे. ३ दिवस रोज पाणी बदलून भिजवलेले तांदूळ, सेंद्रिय गूळ आणि साजूक तुपात तळलेले. वरून खसखशीचा कुरकुरीत लेप आणि आतून मऊ-खुसखुशीत जाळी.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 220,
        "price_500g": 410,
        "price_1kg": 790,
        "price_gbp": 16.50,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Delicate Caramelized Jaggery, Nutty Poppy seeds, Crispy lace",
        "taste_profile_hi": "गुळाचा खमंग गोडवा, खसखशीचा क्रंच, जाळीदार टेक्सचर",
        "image": "/static/images/products/anarse.jpg",
        "is_bestseller": 0,
        "ingredients_en": ["Aged Wada Kolam Rice", "Organic Kolhapur Jaggery", "Pure Desi Ghee", "White Poppy Seeds (Khas Khas)", "Nutmeg"],
        "ingredients_hi": ["जुना वाडा कोलम तांदूळ", "कोल्हापुरी सेंद्रिय गूळ", "साजूक तूप", "पांढरी खसखस", "जायफळ"]
    }
]

REVIEWS = [
    {
        "name": "Smita Kulkarni",
        "city_en": "Samarth Nagar, Chhatrapati Sambhajinagar",
        "city_hi": "समर्थ नगर, छत्रपती संभाजीनगर",
        "rating": 5,
        "item_en": "Bhajani Chakli (500g)",
        "item_hi": "खमंग भाजणी चकली",
        "text_en": "Vanshika's Chakli is hands down the best in Sambhajinagar! Crispy, zero oil on fingers, and authentic bhajani aroma. Delivered fresh to my doorstep in 1 day!",
        "text_hi": "वंशिकाची चकली संभाजीनगरमधील सर्वात भारी आहे! अजिबात तेलकट नाही आणि मस्त काटेरी. दुसऱ्याच दिवशी घरी गरम ताजी मिळाली!"
    },
    {
        "name": "Rajesh Deshmukh",
        "city_en": "CIDCO N-4, Chhatrapati Sambhajinagar",
        "city_hi": "सिडको एन-४, छत्रपती संभाजीनगर",
        "rating": 5,
        "item_en": "Shahi Besan Ladoo (1kg)",
        "item_hi": "साजूक तूप बेसन लाडू",
        "text_en": "Pure cow ghee taste took me back to my grandmother's home. Perfect danedar texture that doesn't stick to palate. 50% advance booking was very smooth.",
        "text_hi": "शुद्ध साजूक तुपाचा घमघमाट अगदी आजीच्या हातच्या लाडवांसारखा होता. तोंडात विरघळतात आणि टाळ्याला चिकटत नाहीत. उत्कृष्ट सेवा!"
    },
    {
        "name": "Ananya Joshi",
        "city_en": "Garkheda, Chhatrapati Sambhajinagar",
        "city_hi": "गारखेडा, छत्रपती संभाजीनगर",
        "rating": 5,
        "item_en": "Coconut Mawa Karanji & Poha Chivda",
        "item_hi": "नारळ करंजी व पोहा चिवडा",
        "text_en": "The karanji pastry was so flaky and stuffed generously with dry coconut & mawa. Loved the FREE delivery for my ₹800 order!",
        "text_hi": "करंजी एकदम खुसखुशीत आणि आतलं खोबरं-खव्याचं सारण अप्रतिम होतं! ₹७०० पेक्षा जास्त ऑर्डरवर मोफत डिलिव्हरी (FREE Delivery) मिळाल्यामुळे खूप आनंद झाला."
    }
]

def init_faral_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Recreate tables cleanly
    cursor.execute("DROP TABLE IF EXISTS faral_products")
    cursor.execute("DROP TABLE IF EXISTS faral_hampers")
    cursor.execute("DROP TABLE IF EXISTS faral_reviews")
    cursor.execute("DROP TABLE IF EXISTS order_inquiries")

    cursor.execute("""
    CREATE TABLE faral_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        name_en TEXT NOT NULL,
        name_hi TEXT NOT NULL,
        tagline_en TEXT NOT NULL,
        tagline_hi TEXT NOT NULL,
        description_en TEXT NOT NULL,
        description_hi TEXT NOT NULL,
        category TEXT NOT NULL,
        category_en TEXT NOT NULL,
        category_hi TEXT NOT NULL,
        price_250g INTEGER NOT NULL,
        price_500g INTEGER NOT NULL,
        price_1kg INTEGER NOT NULL,
        price_gbp REAL NOT NULL,
        shelf_life_en TEXT NOT NULL,
        shelf_life_hi TEXT NOT NULL,
        taste_profile_en TEXT NOT NULL,
        taste_profile_hi TEXT NOT NULL,
        image TEXT NOT NULL,
        is_bestseller INTEGER DEFAULT 0,
        ingredients_en TEXT NOT NULL,
        ingredients_hi TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE faral_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city_en TEXT NOT NULL,
        city_hi TEXT NOT NULL,
        rating INTEGER NOT NULL,
        item_en TEXT NOT NULL,
        item_hi TEXT NOT NULL,
        text_en TEXT NOT NULL,
        text_hi TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE order_inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT,
        delivery_city TEXT NOT NULL,
        items_ordered TEXT NOT NULL,
        total_estimate INTEGER NOT NULL,
        special_instructions TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT UNIQUE NOT NULL,
        order_type TEXT NOT NULL DEFAULT 'local',
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        delivery_date TEXT NOT NULL,
        items_json TEXT NOT NULL,
        items_summary TEXT NOT NULL,
        subtotal REAL NOT NULL,
        delivery_fee REAL NOT NULL,
        total_amount REAL NOT NULL,
        advance_amount REAL NOT NULL,
        cod_balance REAL NOT NULL,
        payment_terms TEXT DEFAULT 'COD with 50% Advance',
        status TEXT DEFAULT 'Pending 50% Advance Confirmation',
        special_notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Populate products
    for p in PRODUCTS:
        cursor.execute("""
        INSERT INTO faral_products (
            slug, name_en, name_hi, tagline_en, tagline_hi,
            description_en, description_hi, category, category_en, category_hi,
            price_250g, price_500g, price_1kg, price_gbp,
            shelf_life_en, shelf_life_hi, taste_profile_en, taste_profile_hi,
            image, is_bestseller, ingredients_en, ingredients_hi
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["slug"], p["name_en"], p["name_hi"], p["tagline_en"], p["tagline_hi"],
            p["description_en"], p["description_hi"], p["category"], p["category_en"], p["category_hi"],
            p["price_250g"], p["price_500g"], p["price_1kg"], p["price_gbp"],
            p["shelf_life_en"], p["shelf_life_hi"], p["taste_profile_en"], p["taste_profile_hi"],
            p["image"], p["is_bestseller"],
            json.dumps(p["ingredients_en"], ensure_ascii=False),
            json.dumps(p["ingredients_hi"], ensure_ascii=False)
        ))

    # Populate reviews
    for rev in REVIEWS:
        cursor.execute("""
        INSERT INTO faral_reviews (name, city_en, city_hi, rating, item_en, item_hi, text_en, text_hi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (rev["name"], rev["city_en"], rev["city_hi"], rev["rating"], rev["item_en"], rev["item_hi"], rev["text_en"], rev["text_hi"]))

    conn.commit()
    conn.close()
    print("Vanshika Swadisht Faral Database successfully initialized with local product images!")

if __name__ == "__main__":
    init_faral_db()
