"""
Vanshika Swadisht Faral (वंशिका स्वादिष्ट फराळ 🪔)
Database initialization for Diwali Food & Snacks E-Commerce Selling Website.
Full English & Hindi/Marathi bilingual product catalog with pricing (250g, 500g, 1kg),
assorted gift hampers, shelf life, pure desi ghee ingredients, and customer reviews.
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
        "shelf_life_en": "35 Days in an airtight container",
        "shelf_life_hi": "हवाबंद डब्यात ३५ दिवस ताजी राहते",
        "taste_profile_en": "Savory, Spiced, Crunchy with Sesame & Carom aroma",
        "taste_profile_hi": "खमंग, कुरकुरीत, तीळ व ओव्याचा सुवास",
        "image": "https://images.unsplash.com/photo-1605197150495-a2267b2d2f70?auto=format&fit=crop&w=1200&q=80",
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
        "shelf_life_en": "30 Days at room temperature",
        "shelf_life_hi": "३० दिवस ताजे राहतात",
        "taste_profile_en": "Melt-in-mouth, Rich Pure Ghee, Cardamom & Nutty",
        "taste_profile_hi": "तोंडात विरघळणारे, साजूक तुपाचा घमघमाट, वेलची स्वाद",
        "image": "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=1200&q=80",
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
        "shelf_life_en": "20 Days in an airtight container",
        "shelf_life_hi": "हवाबंद डब्यात २० दिवस",
        "taste_profile_en": "Crisp flaky crust, aromatic sweet coconut & nutty mawa",
        "taste_profile_hi": "खुसखुशीत बिस्किटासारखी पारी, खोबरे व खव्याचा गोडवा",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
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
        "shelf_life_en": "45 Days in an airtight tin",
        "shelf_life_hi": "४५ दिवस कुरकुरीत राहतो",
        "taste_profile_en": "Light, Crunchy, Sweet-Savory-Tangy tempered flavor",
        "taste_profile_hi": "हलका, कुरकुरीत, आंबट-गोड-तिखट खमंग चव",
        "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=1200&q=80",
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
        "shelf_life_en": "40 Days in an airtight box",
        "shelf_life_hi": "४० दिवस खुसखुशीत राहते",
        "taste_profile_en": "Delicately sweet, Flaky layers, Mild cardamom undertone",
        "taste_profile_hi": "खमंग गोडवा, बिस्किटासारखे पदर, वेलचीचा सुवास",
        "image": "https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?auto=format&fit=crop&w=1200&q=80",
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
        "description_en": "For those who crave savory Diwali crunch! Made from pure chana dal flour seasoned with freshly pounded whole garlic juice, ajwain, and fiery spices. Crisp, non-greasy, and utterly addictive.",
        "description_hi": "खमंग तिखटाची आवड असणाऱ्यांसाठी खास लसूण शेव. ताज्या लसणाचा रस, हिंग, ओवा आणि तिखट मसाल्यात मळलेल्या बेसनाची कुरकुरीत शेव. चहाच्या वेळेसाठी किंवा चिवड्यात मिसळण्यासाठी सर्वोत्तम.",
        "category": "snack",
        "category_en": "Crispy Snacks",
        "category_hi": "खमंग नमकीन",
        "price_250g": 160,
        "price_500g": 300,
        "price_1kg": 580,
        "price_gbp": 11.99,
        "shelf_life_en": "35 Days in an airtight container",
        "shelf_life_hi": "३५ दिवस कुरकुरीत राहते",
        "taste_profile_en": "Zesty, Pungent Garlic aroma, Medium Spicy, Crisp",
        "taste_profile_hi": "चमचमीत, लसणाचा खमंग वास, मध्यम तिखट, कुरकुरीत",
        "image": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=1200&q=80",
        "is_bestseller": 0,
        "ingredients_en": ["Pure Chana Dal Flour (Besan)", "Fresh Country Garlic Paste", "Red Chilli Powder", "Carom Seeds (Ajwain)", "Asafoetida (Hing)", "Pure Groundnut Oil", "Salt"],
        "ingredients_hi": ["शुद्ध चणा डाळ बेसन", "ताजा गावठी लसूण", "लाल तिखट", "ओवा", "हिंग", "शेंगदाणा तेल", "मीठ"]
    },
    {
        "slug": "royal-motichoor-ladoo",
        "name_en": "Royal Saffron Motichoor Ladoo in Desi Ghee",
        "name_hi": "शाही केशर मोतीचूर लाडू (साजूक तुपातील)",
        "tagline_en": "Fine micro boondi pearls soaked in fragrant saffron-cardamom sugar syrup",
        "tagline_hi": "अतिशय बारीक मोत्यांसारख्या बुंदीचे रसाळ लाडू, केशर, पिस्ता आणि मगज बियांसह",
        "description_en": "Artisanal tiny boondi pearls fried in pure desi ghee and soaked in warm saffron-infused cardamom syrup. Finished with roasted melon seeds (magaz) and slivered almonds. The crown jewel of Indian festivities.",
        "description_hi": "साजूक तुपात तळलेल्या अतिशय बारीक बुंदीचे रसाळ मोतीचूर लाडू. काश्मिरी केशर, वेलची, मगज बिया आणि पिस्त्याचे तुकडे. तोंडात टाकताच विरघळणारा शाही गोडवा.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 225,
        "price_500g": 420,
        "price_1kg": 820,
        "price_gbp": 16.99,
        "shelf_life_en": "12 Days (Keep refrigerated for longer freshness)",
        "shelf_life_hi": "१२ दिवस (फ्रिजमध्ये ठेवल्यास जास्त दिवस टिकतात)",
        "taste_profile_en": "Juicy, Aromatic Saffron, Rich Pure Ghee, Melt-in-mouth",
        "taste_profile_hi": "रसाळ, केशर-वेलचीचा सुवास, शुद्ध तुपाची श्रीमंती",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
        "is_bestseller": 1,
        "ingredients_en": ["Besan (Gram Flour)", "Pure Desi Ghee", "Sugar", "Pure Kashmiri Saffron (Kesar)", "Green Cardamom", "Magaj Seeds (Melon Seeds)", "Pistachios"],
        "ingredients_hi": ["बेसन", "शुद्ध साजूक तूप", "साखर", "काश्मिरी केशर", "वेलची", "मगज बी", "पिस्ता"]
    },
    {
        "slug": "traditional-anarse",
        "name_en": "Crispy Flaky Traditional Anarse (जाळीदार अनारसे)",
        "name_hi": "पारंपरिक जाळीदार व खुसखुशीत गुळाचे अनारसे",
        "tagline_en": "Heritage 3-day fermented rice & organic jaggery delicacy coated with poppy seeds",
        "tagline_hi": "३ दिवस भिजवलेल्या तांदळाचे व सेंद्रिय गुळाचे जाळीदार पारंपरिक अनारसे, खसखशीत घोळवलेले",
        "description_en": "A rare heritage Maharashtrian delicacy requiring master craftsmanship. Made from aged rice soaked for 3 days, shade-dried, pounded with organic Kolhapur jaggery, and fried in pure ghee until lace-like honeycombs (jalidaar) emerge, coated in white poppy seeds.",
        "description_hi": "अतिशय कौशल्याने बनवले जाणारे पारंपरिक जाळीदार अनारसे. ३ दिवस रोज पाणी बदलून भिजवलेले तांदूळ, सेंद्रिय गूळ आणि साजूक तुपात तळलेले. वरून खसखशीचा कुरकुरीत लेप आणि आतून मऊ-खुसखुशीत जाळी.",
        "category": "sweet",
        "category_en": "Festive Sweets",
        "category_hi": "पारंपरिक मिठाई",
        "price_250g": 220,
        "price_500g": 410,
        "price_1kg": 790,
        "price_gbp": 16.50,
        "shelf_life_en": "25 Days in an airtight container",
        "shelf_life_hi": "२५ दिवस उत्तम राहतात",
        "taste_profile_en": "Delicate Caramelized Jaggery, Nutty Poppy seeds, Crispy lace",
        "taste_profile_hi": "गुळाचा खमंग गोडवा, खसखशीचा क्रंच, जाळीदार टेक्सचर",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=1200&q=80",
        "is_bestseller": 0,
        "ingredients_en": ["Aged Wada Kolam Rice", "Organic Kolhapur Jaggery", "Pure Desi Ghee", "White Poppy Seeds (Khas Khas)", "Nutmeg"],
        "ingredients_hi": ["जुना वाडा कोलम तांदूळ", "कोल्हापुरी सेंद्रिय गूळ", "साजूक तूप", "पांढरी खसखस", "जायफळ"]
    }
]

HAMPERS = [
    {
        "slug": "royal-diwali-faral-box",
        "name_en": "Shahi Diwali Sampoorna Faral Hamper (1.5 kg)",
        "name_hi": "शाही दिवाळी संपूर्ण फराळ हॅम्पर (१.५ किलो)",
        "tagline_en": "All 5 signature Faral delicacies packed in an artisanal festive gift box",
        "tagline_hi": "दिवाळीच्या ५ मुख्य पदार्थांचा परिपूर्ण शाही फराळ बॉक्स",
        "description_en": "The ultimate festive gift box containing 300g Bhajani Chakli, 300g Pure Ghee Besan Ladoo, 300g Flaky Coconut Karanji, 300g Patla Poha Chivda, and 300g Sweet Shankarpali. Packed in a luxury gold-embossed box with a festive greeting card.",
        "description_hi": "दिवाळीसाठी परिपूर्ण भेटवस्तू! ३०० ग्रॅम भाजणी चकली, ३०० ग्रॅम साजूक तूप बेसन लाडू, ३०० ग्रॅम खुसखुशीत करंजी, ३०० ग्रॅम पातळ पोहा चिवडा आणि ३०० ग्रॅम गोड शंकरपाळी. सुंदर शाही गिफ्ट बॉक्समध्ये सुरक्षित पॅकिंग.",
        "weight": "1.5 kg Assorted",
        "price_inr": 1150,
        "price_gbp": 27.99,
        "badge_en": "Most Popular Gift Box",
        "badge_hi": "सर्वाधिक पसंतीचा गिफ्ट बॉक्स",
        "image": "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=1200&q=80",
        "items_included_en": ["300g Crispy Bhajani Chakli", "300g Pure Ghee Besan Ladoo", "300g Flaky Coconut Karanji", "300g Roasted Patla Poha Chivda", "300g Flaky Sweet Shankarpali", "Festive Diya & Greeting Card"],
        "items_included_hi": ["३०० ग्रॅम खमंग भाजणी चकली", "३०० ग्रॅम साजूक तूप बेसन लाडू", "३०० ग्रॅम खुसखुशीत करंजी", "३०० ग्रॅम पातळ पोहा चिवडा", "३०० ग्रॅम गोड शंकरपाळी", "शुभदिवाळी ग्रीटिंग कार्ड व पणती"]
    },
    {
        "slug": "executive-faral-box",
        "name_en": "Corporate & Family Faral Box (1.0 kg)",
        "name_hi": "कौटुंबिक फराळ गिफ्ट बॉक्स (१.० किलो)",
        "tagline_en": "Ideal corporate & family festive box with 4 bestsellers",
        "tagline_hi": "कुटुंब आणि ऑफिस सहकाऱ्यांना भेट देण्यासाठी १ किलोचा खास बॉक्स",
        "description_en": "Includes 250g Bhajani Chakli, 250g Besan Ladoo, 250g Poha Chivda, and 250g Spicy Garlic Sev in an elegant airtight gift carton.",
        "description_hi": "२५० ग्रॅम भाजणी चकली, २५० ग्रॅम बेसन लाडू, २५० ग्रॅम पोहा चिवडा आणि २५० ग्रॅम लसूण शेव. आकर्षक आणि हवाबंद गिफ्ट बॉक्स.",
        "weight": "1.0 kg Assorted",
        "price_inr": 790,
        "price_gbp": 19.99,
        "badge_en": "Best Value Hamper",
        "badge_hi": "किफायतशीर व उत्तम",
        "image": "https://images.unsplash.com/photo-1605197150495-a2267b2d2f70?auto=format&fit=crop&w=1200&q=80",
        "items_included_en": ["250g Bhajani Chakli", "250g Besan Ladoo", "250g Poha Chivda", "250g Tikha Garlic Sev", "Diwali Greetings"],
        "items_included_hi": ["२५० ग्रॅम भाजणी चकली", "२५० ग्रॅम बेसन लाडू", "२५० ग्रॅम पातळ पोहा चिवडा", "२५० ग्रॅम तिखट लसूण शेव", "दिवाळी शुभेच्छा"]
    }
]

REVIEWS = [
    {
        "name": "Smita Kulkarni",
        "city_en": "Dadar, Mumbai",
        "city_hi": "दादर, मुंबई",
        "rating": 5,
        "item_en": "Bhajani Chakli & Besan Ladoo",
        "item_hi": "भाजणी चकली आणि बेसन लाडू",
        "text_en": "The Chakli was out of this world! Not a single drop of extra oil, crisp spiky texture that stayed fresh for 3 weeks. The Besan Ladoos had that authentic pure ghee taste my grandmother used to make. Ordered 3kg more for Bhaubeej!",
        "text_hi": "चकली एकदम अप्रतिम! अजिबात तेलकट नाही, छान काटेरी आणि ३ आठवडे तशीच कुरकुरीत राहिली. बेसन लाडूत साजूक तुपाचा अस्सल सुवास होता. भाऊबीजेसाठी अजून ३ किलो मागवले आहेत!"
    },
    {
        "name": "Pranav Deshpande",
        "city_en": "Kothrud, Pune",
        "city_hi": "कोथरूड, पुणे",
        "rating": 5,
        "item_en": "Sampoorna Faral Hamper (1.5kg)",
        "item_hi": "संपूर्ण फराळ हॅम्पर (१.५ किलो)",
        "text_en": "Delivered to Pune right before Dhanteras! The Karanji crust was blistered and flaky without getting soggy. Packaging was airtight and totally intact. Supporting authentic home cooks like Vanshika is pure joy.",
        "text_hi": "धनत्रयोदशीच्या आधी पुण्यात वेळेवर डिलिव्हरी मिळाली! करंजीची पारी एकदम खुसखुशीत आणि सारण समृद्ध होते. पॅकिंग अतिशय दर्जेदार. वंशिकाच्या हातच्या फराळाला तोड नाही!"
    },
    {
        "name": "Rajeshwari Joshi",
        "city_en": "Nashik, Maharashtra",
        "city_hi": "नाशिक, महाराष्ट्र",
        "rating": 5,
        "item_en": "Sweet Shankarpali & Poha Chivda",
        "item_hi": "गोड शंकरपाळी आणि पोहा चिवडा",
        "text_en": "The Shankarpali had clear flaky biscuit layers and melted straight away on the tongue. Poha Chivda was crisp and not greasy at all. Clean, hygienic, and authentic Maharashtrian taste!",
        "text_hi": "शंकरपाळीला बिस्किटासारखे छान पदर सुटले होते आणि पोहा चिवडा अगदी कमी तेलात खमंग भाजलेला होता. नाशिकमध्ये घरपोच ताजी डिलिव्हरी मिळाली. खूप खूप धन्यवाद!"
    },
    {
        "name": "Mihir Patel",
        "city_en": "Thane (W), Mumbai",
        "city_hi": "ठाणे, मुंबई",
        "rating": 5,
        "item_en": "Corporate Faral Boxes (15 Hampers)",
        "item_hi": "कॉर्पोरेट फराळ बॉक्सेस (१५ हॅम्पर)",
        "text_en": "We ordered 15 executive Faral boxes for our office team Diwali gifting. Every single colleague praised the taste and homemade purity. Zero factory preservatives, 100% genuine warmth.",
        "text_hi": "आमच्या ऑफिसच्या कर्मचाऱ्यांना दिवाळी भेट म्हणून १५ बॉक्सेस मागवले होते. सर्वांना चव खूप आवडली. फॅक्टरीच्या भेसळयुक्त मिठाईपेक्षा हा घरचा फराळ हजार पटीने उत्तम आहे!"
    }
]

def init_faral_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop legacy tables and create dedicated store tables
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
    CREATE TABLE faral_hampers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        name_en TEXT NOT NULL,
        name_hi TEXT NOT NULL,
        tagline_en TEXT NOT NULL,
        tagline_hi TEXT NOT NULL,
        description_en TEXT NOT NULL,
        description_hi TEXT NOT NULL,
        weight TEXT NOT NULL,
        price_inr INTEGER NOT NULL,
        price_gbp REAL NOT NULL,
        badge_en TEXT,
        badge_hi TEXT,
        image TEXT NOT NULL,
        items_included_en TEXT NOT NULL,
        items_included_hi TEXT NOT NULL
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

    # Populate hampers
    for h in HAMPERS:
        cursor.execute("""
        INSERT INTO faral_hampers (
            slug, name_en, name_hi, tagline_en, tagline_hi, description_en, description_hi,
            weight, price_inr, price_gbp, badge_en, badge_hi, image,
            items_included_en, items_included_hi
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            h["slug"], h["name_en"], h["name_hi"], h["tagline_en"], h["tagline_hi"],
            h["description_en"], h["description_hi"], h["weight"], h["price_inr"], h["price_gbp"],
            h["badge_en"], h["badge_hi"], h["image"],
            json.dumps(h["items_included_en"], ensure_ascii=False),
            json.dumps(h["items_included_hi"], ensure_ascii=False)
        ))

    # Populate reviews
    for rev in REVIEWS:
        cursor.execute("""
        INSERT INTO faral_reviews (name, city_en, city_hi, rating, item_en, item_hi, text_en, text_hi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (rev["name"], rev["city_en"], rev["city_hi"], rev["rating"], rev["item_en"], rev["item_hi"], rev["text_en"], rev["text_hi"]))

    conn.commit()
    conn.close()
    print("Vanshika Swadisht Faral Selling Store Database successfully initialized!")

if __name__ == "__main__":
    init_faral_db()
