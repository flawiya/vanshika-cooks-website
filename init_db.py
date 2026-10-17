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
        "description_en": "Crafted from slow-roasted multigrain flour, seasoned with organic white sesame, ajwain, and pure hing. Ultra-crispy, spiky, and light on the stomach without excess oil.",
        "description_hi": "पारंपरिक भाजणीच्या पिठापासून बनवलेली अस्सल चकली. पांढरे तीळ, ओवा आणि हिंगाची खमंग चव. अजिबात तेलकट नसलेली आणि जिभेवर विरघळणारी.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 100,
        "price_500g": 200,
        "price_1kg": 400,
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
        "slug": "god-shankarpali",
        "name_en": "Melt-in-Mouth Sweet Shankar Pale",
        "name_hi": "पदराची खुसखुशीत गोड शंकरपाळी (Shankar Pale)",
        "tagline_en": "Crispy golden diamond biscuits kneaded with pure ghee & milk",
        "tagline_hi": "दूध, साखर आणि साजूक तुपाच्या अचूक प्रमाणातील पदर सुटलेली शंकरपाळी",
        "description_en": "Crafted using the golden ratio of pure ghee, milk, and sugar. Rolled thick and slowly fried on low flame to create multi-layered, buttery diamond biscuits that melt like shortbread.",
        "description_hi": "तूप, दूध आणि साखरेच्या अचूक प्रमाणात बनवलेली शंकरपाळी. मंद आचेवर सावकाश तळल्यामुळे आत छान पदर सुटतात आणि ती बिस्किटासारखी खुसखुशीत होते.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 115,
        "price_500g": 230,
        "price_1kg": 450,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Delicately sweet, Flaky layers, Mild cardamom undertone",
        "taste_profile_hi": "खमंग गोडवा, बिस्किटासारखे पदर, वेलचीचा सुवास",
        "image": "/static/images/products/shankarpali.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Refined Wheat Flour", "Whole Cow Milk", "Pure Desi Ghee", "Granulated Sugar", "Cardamom Powder", "Pinch of Sea Salt"],
        "ingredients_hi": ["मैदा", "गाईचे दूध", "शुद्ध साजूक तूप", "साखर", "वेलची पूड", "चिमूटभर मीठ"]
    },
    {
        "slug": "rava-ladoo",
        "name_en": "Pure Desi Ghee Danedar Rava Ladoo",
        "name_hi": "शुद्ध साजूक तुपातील दाणेदार रवा लाडू (Rava Ladoo)",
        "tagline_en": "Slow-roasted fine semolina in pure cow ghee with cardamom & dry fruits",
        "tagline_hi": "घरच्या साजूक तुपात खमंग भाजलेला, वेलची आणि सुकामेव्याचा दाणेदार रवा लाडू",
        "description_en": "Slow roasted in pure cow ghee. Made with fine semolina, golden raisins, cashews, and fragrant green cardamom to melt right in your mouth.",
        "description_hi": "शुद्ध साजूक तुपात मंद आचेवर खमंग भाजलेला दाणेदार रवा लाडू. वेलचीचा दरवळणारा सुवास आणि तोंडात विरघळणारी अप्रतिम चव.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 115,
        "price_500g": 230,
        "price_1kg": 450,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Melt-in-mouth, Rich Pure Ghee, Cardamom & Nutty",
        "taste_profile_hi": "तोंडात विरघळणारे, साजूक तुपाचा घमघमाट, वेलची स्वाद",
        "image": "/static/images/products/rava_ladoo.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Chiroti Fine Rava", "100% Pure Desi Cow Ghee", "Traditional Sugar", "Green Cardamom", "Nutmeg", "Cashews & Raisins"],
        "ingredients_hi": ["चिरोटी रवा", "१००% शुद्ध साजूक तूप", "साखर", "हिरवी वेलची", "जायफळ", "काजू व बेदाणे"]
    },
    {
        "slug": "murmura-chivda",
        "name_en": "Crunchy Spiced Murmura Chweda (Chivda)",
        "name_hi": "खमंग व कुरकुरीत मुरमुरा चिवडा (Murmura Chweda)",
        "tagline_en": "Crispy puffed rice chivda with golden peanuts, roasted coconut & curry leaves",
        "tagline_hi": "अतिशय हलका, कुरकुरीत आणि खमंग फोडणीचा मुरमुरा चिवडा",
        "description_en": "Super light and crunchy spiced puffed rice (Murmura Chweda) tossed with golden roasted peanuts, dry coconut slivers, and fragrant fresh curry leaves.",
        "description_hi": "कमी तेलाचा, पचायला अत्यंत हलका आणि कुरकुरीत चिवडा. शेंगदाणे, खोबऱ्याचे काप आणि कढीपत्त्याची खमंग फोडणी.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 90,
        "price_500g": 180,
        "price_1kg": 350,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Crispy, Light, Zesty & Aromatic",
        "taste_profile_hi": "हलका, मस्त कुरकुरीत, खमंग चव",
        "image": "/static/images/products/murmura_chivda.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Crisp Puffed Rice (Murmura)", "Roasted Peanuts", "Dry Coconut Slivers", "Fresh Curry Leaves", "Turmeric & Spices", "Rock Salt"],
        "ingredients_hi": ["कुरकुरीत मुरमुरे", "शेंगदाणे", "सुक्या खोबऱ्याचे काप", "कढीपत्ता", "हळद, हिंग व मसाले", "मीठ"]
    },
    {
        "slug": "kaju-katli",
        "name_en": "Royal Pure Cashew Kaju Katli",
        "name_hi": "अस्सल काजू कतली (Kaju Katli)",
        "tagline_en": "Diamond-cut artisanal sweet crafted from 100% premium Goa cashews",
        "tagline_hi": "१००% शुद्ध काजूपासून बनवलेली तोंडात विरघळणारी अस्सल काजू कतली",
        "description_en": "Premium melt-in-mouth Kaju Katli made from pure cashews and refined sugar. Smooth diamond cuts, delicate sweetness, zero artificial essence.",
        "description_hi": "उत्कृष्ट दर्जाच्या काजूपासून पारंपरिक पद्धतीने बनवलेली काजू कतली. तोंडात अलगद विरघळणारी आणि अजिबात जास्त गोड नसलेली.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 300,
        "price_500g": 600,
        "price_1kg": 1200,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Rich cashew velvet, subtle sweetness, melt-in-mouth",
        "taste_profile_hi": "काजूचा समृद्ध स्वाद, मऊ आणि तोंडात विरघळणारी",
        "image": "/static/images/products/kaju_katli.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["100% Premium Cashews (Kaju)", "Refined Sugar", "Pure Ghee for greasing"],
        "ingredients_hi": ["१००% शुद्ध काजू", "साखर", "साजूक तूप"]
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
        "price_250g": 90,
        "price_500g": 180,
        "price_1kg": 350,
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
        "slug": "patla-poha-chivda",
        "name_en": "Crunchy Roasted Patla Poha Chivda",
        "name_hi": "खमंग भाजलेला पातळ पोहा चिवडा",
        "tagline_en": "Low-oil roasted thin flattened rice with fried peanuts, dalia & curry leaves",
        "tagline_hi": "अतिशय कमी तेलात भाजलेला खमंग पातळ पोह्यांचा चिवडा, शेंगदाणे व खोबऱ्याच्या फोडणीसह",
        "description_en": "A guilt-free festival favorite! Thin paper poha is gently roasted dry until featherlight and crunchy, then tossed in an aromatic tempering of crisp green chillies, curry leaves, golden roasted peanuts, and dry coconut chips.",
        "description_hi": "कमी तेलाचा, पचायला हलका आणि खमंग चिवडा. पातळ पोहे मंद आचेवर भाजून त्यावर हिरवी मिरची, कढीपत्ता, शेंगदाणे, खोबऱ्याचे पातळ काप आणि डाळ्यांची खमंग फोडणी दिलेली.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 90,
        "price_500g": 180,
        "price_1kg": 350,
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
        "slug": "khuskhushit-karanji",
        "name_en": "Crispy Flaky Coconut & Mawa Karanji",
        "name_hi": "खुसखुशीत नारळ-खव्याची पारंपरिक करंजी",
        "tagline_en": "Delicate flaky pastry shell stuffed with roasted dry coconut, mawa & dry fruits",
        "tagline_hi": "पदराची खुसखुशीत करंजी, सुकं खोबरं, खवा, खसखस व सुकामेव्याच्या सारणाने भरलेली",
        "description_en": "Our signature crescent-shaped festive pastry. Made with a layered, blistering-crisp outer crust kneaded with hot ghee, stuffed generously with roasted dry grated coconut, pink-roasted khoya, and poppy seeds.",
        "description_hi": "दिवाळीच्या ताटाची खरी शान! कडकडीत तुपाचे मोहन घालून मळलेली पदर सुटलेली खुसखुशीत पारी, आत गुलाबी भाजलेले सुके खोबरे, खवा आणि खसखस.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 115,
        "price_500g": 230,
        "price_1kg": 450,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Crisp flaky crust, aromatic sweet coconut & nutty mawa",
        "taste_profile_hi": "खुसखुशीत बिस्किटासारखी पारी, खोबरे व खव्याचा गोडवा",
        "image": "/static/images/products/karanji.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Refined Wheat Flour", "Chiroti Rava", "Pure Desi Ghee", "Dry Roasted Coconut", "Fresh Mawa", "Poppy Seeds (Khas Khas)", "Cardamom & Nutmeg"],
        "ingredients_hi": ["मैदा", "चिरोटी रवा", "साजूक तूप", "भाजलेले सुके खोबरे", "ताजा खवा", "खसखस", "वेलची-जायफळ"]
    },
    {
        "slug": "diwali-faral-box",
        "name_en": "Diwali Faral Assorted Festive Box",
        "name_hi": "दिवाळी फराळ असॉर्टेड गिफ्ट बॉक्स",
        "tagline_en": "Festive combo box of fresh Chakli, Shankar Pale, Ladoo, Chivda & Sev",
        "tagline_hi": "चकली, शंकरपाळी, लाडू, चिवडा आणि शेव यांचा परिपूर्ण पारंपरिक सण बॉक्स",
        "description_en": "The complete festive indulgence! Packed with fresh homemade Chakli, Shankar Pale, Pure Ghee Ladoo, crunchy Poha/Murmura Chivda, and Garlic Sev in airtight festive packaging.",
        "description_hi": "संपूर्ण कुटुंबासाठी किंवा भेट देण्यासाठी परिपूर्ण फराळ पेटी. चकली, शंकरपाळी, साजूक तुपातील लाडू, पोहा/मुरमुरा चिवडा आणि बारीक शेव एकाच सुंदर बॉक्समध्ये.",
        "category": "combo",
        "category_en": "Festive Combos",
        "category_hi": "फराळ कॉम्बो",
        "price_250g": 150,
        "price_500g": 280,
        "price_1kg": 500,
        "shelf_life_en": "Max 10-12 Days",
        "shelf_life_hi": "कमाल १०-१२ दिवस",
        "taste_profile_en": "Complete Maharashtrian festive sweetness and crunch",
        "taste_profile_hi": "गोड आणि खमंग चवींचा परिपूर्ण पारंपरिक मेळ",
        "image": "/static/images/products/diwali_faral_box.jpg",
        "is_bestseller": 1,
        "ingredients_en": ["Pure Desi Cow Ghee", "Bhajani Flour", "Besan & Rava", "Whole Milk", "Puffed Rice & Poha", "Dry Fruits & Spices"],
        "ingredients_hi": ["शुद्ध साजूक तूप", "भाजणी पीठ", "बेसन व रवा", "गाईचे दूध", "मुरमुरे व पोहे", "सुकामेवा व मसाले"]
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
            p["price_250g"], p["price_500g"], p["price_1kg"], p.get("price_gbp", 0.0),
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
