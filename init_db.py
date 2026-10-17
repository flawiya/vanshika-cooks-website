"""
Database initialization script for Vanshika Cooks bilingual food & recipe website.
Includes full English and Hindi translations for all recipes, ingredients, instructions, and tips.
"""

import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "vanshika_cooks.db")

RECIPES = [
    {
        "slug": "paneer-butter-masala",
        "title_en": "Restaurant-Style Paneer Butter Masala",
        "title_hi": "शाही पनीर बटर मसाला (रेस्टोरेंट स्टाइल)",
        "summary_en": "Velvety, rich, and aromatic cottage cheese cubes simmered in a silky tomato-cashew makhani gravy infused with kasuri methi.",
        "summary_hi": "रेशमी टमाटर और काजू की मखमली ग्रेवी में बनी स्वादिष्ट पनीर करी, कसूरी मेथी और मक्खन की खुशबू के साथ।",
        "category": "main",
        "category_en": "Main Course",
        "category_hi": "मुख्य व्यंजन",
        "prep_time": 15,
        "cook_time": 25,
        "total_time": 40,
        "servings": 4,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 380,
        "image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Fresh Malai Paneer", "amount": 250, "unit": "g", "note": "cut into 1-inch cubes"},
            {"item": "Ripe Tomatoes", "amount": 4, "unit": "medium", "note": "roughly chopped"},
            {"item": "Whole Cashews (Kaju)", "amount": 15, "unit": "pieces", "note": "soaked in warm water for 15 mins"},
            {"item": "Butter (Makhan)", "amount": 2, "unit": "tbsp", "note": "divided"},
            {"item": "Ghee or Cooking Oil", "amount": 1, "unit": "tbsp", "note": "for tempering"},
            {"item": "Ginger-Garlic Paste", "amount": 1, "unit": "tbsp", "note": "freshly crushed"},
            {"item": "Kashmiri Red Chilli Powder", "amount": 1.5, "unit": "tsp", "note": "for vibrant red hue"},
            {"item": "Garam Masala", "amount": 0.5, "unit": "tsp", "note": "aromatic home blend"},
            {"item": "Kasuri Methi (Dried Fenugreek)", "amount": 1, "unit": "tbsp", "note": "crushed between palms"},
            {"item": "Fresh Heavy Cream (Malai)", "amount": 3, "unit": "tbsp", "note": "whisked smoothly"},
            {"item": "Sugar or Honey", "amount": 0.5, "unit": "tsp", "note": "to balance tomato acidity"},
            {"item": "Salt", "amount": 1, "unit": "tsp", "note": "or to taste"}
        ],
        "ingredients_hi": [
            {"item": "ताज़ा मलाई पनीर", "amount": 250, "unit": "ग्राम", "note": "चौकोर टुकड़ों में कटा हुआ"},
            {"item": "पके लाल टमाटर", "amount": 4, "unit": "मध्यम", "note": "मोटे कटे हुए"},
            {"item": "काजू", "amount": 15, "unit": "पीस", "note": "15 मिनट गुनगुने पानी में भीगे हुए"},
            {"item": "मक्खन (बटर)", "amount": 2, "unit": "बड़ा चम्मच", "note": "विभाजित"},
            {"item": "देसी घी या तेल", "amount": 1, "unit": "बड़ा चम्मच", "note": "तड़के के लिए"},
            {"item": "अदरक-लहसुन पेस्ट", "amount": 1, "unit": "बड़ा चम्मच", "note": "ताज़ा कुटा हुआ"},
            {"item": "कश्मीरी लाल मिर्च पाउडर", "amount": 1.5, "unit": "छोटा चम्मच", "note": "प्राकृतिक लाल रंग के लिए"},
            {"item": "गरम मसाला", "amount": 0.5, "unit": "छोटा चम्मच", "note": "घर का बना"},
            {"item": "कसूरी मेथी", "amount": 1, "unit": "बड़ा चम्मच", "note": "हाथों से रगड़कर डाली हुई"},
            {"item": "ताज़ा मलाई या क्रीम", "amount": 3, "unit": "बड़ा चम्मच", "note": "अच्छी तरह फैंटी हुई"},
            {"item": "चीनी या शहद", "amount": 0.5, "unit": "छोटा चम्मच", "note": "टमाटर के खट्टेपन को संतुलित करने के लिए"},
            {"item": "नमक", "amount": 1, "unit": "छोटा चम्मच", "note": "स्वादानुसार"}
        ],
        "steps_en": [
            "Boil the chopped tomatoes and soaked cashews in 1 cup of water for 10 minutes until soft. Let cool completely and blend into a silk-smooth makhani paste.",
            "Strain the pureed paste through a fine-mesh sieve into a bowl for that signature luxurious restaurant-like texture.",
            "Heat 1 tbsp butter and 1 tbsp ghee in a heavy-bottomed kadai. Add ginger-garlic paste and sauté for 1 minute until raw aroma dissipates.",
            "Stir in Kashmiri red chilli powder on low flame, then immediately pour in the strained tomato-cashew puree to prevent spices from burning.",
            "Cook the gravy on medium-low flame for 8-10 minutes until oil droplets begin to glisten on the surface.",
            "Add salt, garam masala, and a touch of sugar. Gently slide in the soft paneer cubes and simmer on low heat for 3-4 minutes so paneer absorbs the gravy.",
            "Finish by crushing kasuri methi between your palms over the dish and gently folding in the fresh cream and remaining butter. Serve piping hot with garlic naan or jeera rice!"
        ],
        "steps_hi": [
            "एक पैन में कटे टमाटर और भीगे काजू को 1 कप पानी में 10 मिनट तक उबालें जब तक वे नरम न हो जाएं। ठंडा करके मिक्सी में एकदम बारीक मखमली पेस्ट बना लें।",
            "रेस्टोरेंट जैसा रेशमी टेक्सचर पाने के लिए इस पेस्ट को छलनी से छान लें।",
            "कड़ाही में 1 चम्मच मक्खन और 1 चम्मच देसी घी गरम करें। अदरक-लहसुन का पेस्ट डालकर धीमी आंच पर 1 मिनट भूनें।",
            "धीमी आंच पर कश्मीरी लाल मिर्च पाउडर डालें और तुरंत छाना हुआ प्यूरी डालकर अच्छी तरह मिलाएँ ताकि मसाला जले नहीं।",
            "ग्रेवी को मध्यम-धीमी आंच पर 8-10 मिनट तक पकाएं जब तक कि किनारों से मक्खन चमकने न लगे।",
            "नमक, गरम मसाला और हल्की सी चीनी मिलाएं। अब पनीर के टुकड़े डालें और धीमी आंच पर 3-4 मिनट तक पकने दें ताकि पनीर में स्वाद समा जाए।",
            "अंत में हाथों से मसली हुई कसूरी मेथी, ताज़ा क्रीम और बचा हुआ मक्खन डालकर गैस बंद करें। गरमा-गरम बटर नान या जीरा राइस के साथ परोसें!"
        ],
        "pro_tips_en": [
            "Always soak paneer cubes in lukewarm salted water for 10 minutes before adding to the gravy to keep them ultra-soft.",
            "Straining the tomato-cashew puree is the true secret behind velvet-smooth restaurant texture.",
            "Never boil paneer for too long, or it will become chewy and rubbery."
        ],
        "pro_tips_hi": [
            "पनीर को ग्रेवी में डालने से पहले 10 मिनट हल्के गुनगुने नमकीन पानी में भिगोकर रखें, इससे पनीर हमेशा रुई जैसा मुलायम रहेगा।",
            "टमाटर-काजू की प्यूरी को छलनी से छानना ही रेस्टोरेंट जैसी मखमली ग्रेवी का असली राज़ है।",
            "पनीर डालने के बाद कभी भी ज्यादा देर तक न उबालें, वरना पनीर सख्त हो जाएगा।"
        ]
    },
    {
        "slug": "crispy-masala-dosa",
        "title_en": "Crispy Golden Masala Dosa with Potato Podimas",
        "title_hi": "कुरकुरा मसाला डोसा और खुशबूदार आलू भाजी",
        "summary_en": "Paper-thin, golden-brown fermented rice-lentil crepe wrapped around a fragrant tempered mustard-curry leaf potato masala.",
        "summary_hi": "चावल और उड़द दाल का कुरकुरा सुनहरा डोसा, राई और कढ़ी पत्ते के तड़के वाले स्वादिष्ट आलू मसाले के साथ।",
        "category": "breakfast",
        "category_en": "Breakfast",
        "category_hi": "नाश्ता",
        "prep_time": 20,
        "cook_time": 20,
        "total_time": 40,
        "servings": 4,
        "difficulty_en": "Medium",
        "difficulty_hi": "मध्यम",
        "diet_tag_en": "Gluten-Free & Vegan",
        "diet_tag_hi": "ग्लूटेन-मुक्त एवं वीगन",
        "calories": 290,
        "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Fermented Dosa Batter", "amount": 3, "unit": "cups", "note": "naturally fermented overnight"},
            {"item": "Boiled Potatoes", "amount": 4, "unit": "medium", "note": "peeled and roughly crumbled"},
            {"item": "Onions", "amount": 2, "unit": "medium", "note": "thinly sliced lengthwise"},
            {"item": "Green Chillies", "amount": 3, "unit": "pieces", "note": "slit or finely chopped"},
            {"item": "Mustard Seeds (Rai)", "amount": 1, "unit": "tsp", "note": "for tempering"},
            {"item": "Chana Dal & Urad Dal", "amount": 1, "unit": "tsp each", "note": "for crunchy texture"},
            {"item": "Curry Leaves", "amount": 12, "unit": "leaves", "note": "fresh and aromatic"},
            {"item": "Turmeric Powder (Haldi)", "amount": 0.5, "unit": "tsp", "note": "for vibrant yellow tint"},
            {"item": "Cold-pressed Sesame Oil or Ghee", "amount": 3, "unit": "tbsp", "note": "for crisping the dosa"},
            {"item": "Fresh Coriander", "amount": 2, "unit": "tbsp", "note": "chopped"},
            {"item": "Salt", "amount": 1, "unit": "tsp", "note": "to taste"}
        ],
        "ingredients_hi": [
            {"item": "खमीर उठा डोसा बैटर", "amount": 3, "unit": "कप", "note": "रातभर खमीर उठा हुआ"},
            {"item": "उबले आलू", "amount": 4, "unit": "मध्यम", "note": "छीलकर हाथ से मोटे तोड़े हुए"},
            {"item": "प्याज", "amount": 2, "unit": "मध्यम", "note": "लंबे पतले कटे हुए"},
            {"item": "हरी मिर्च", "amount": 3, "unit": "पीस", "note": "बारीक कटी हुई"},
            {"item": "राई (सरसों के दाने)", "amount": 1, "unit": "छोटा चम्मच", "note": "तड़के के लिए"},
            {"item": "चना दाल और उड़द दाल", "amount": 1, "unit": "छोटा चम्मच प्रत्येक", "note": "कुरकुरेपन के लिए"},
            {"item": "कढ़ी पत्ता", "amount": 12, "unit": "पत्ते", "note": "ताज़ा"},
            {"item": "हल्दी पाउडर", "amount": 0.5, "unit": "छोटा चम्मच", "note": "सुंदर रंग के लिए"},
            {"item": "तिल का तेल या देसी घी", "amount": 3, "unit": "बड़ा चम्मच", "note": "डोसा सेकने के लिए"},
            {"item": "ताज़ा हरा धनिया", "amount": 2, "unit": "बड़ा चम्मच", "note": "बारीक कटा हुआ"},
            {"item": "नमक", "amount": 1, "unit": "छोटा चम्मच", "note": "स्वादानुसार"}
        ],
        "steps_en": [
            "For potato masala: Heat 1 tbsp oil in a pan. Splutter mustard seeds, then add chana dal, urad dal, curry leaves, and green chillies until dal turns golden.",
            "Add sliced onions and sauté on medium heat until soft and translucent (do not brown).",
            "Stir in turmeric powder and salt, then fold in the crumbled boiled potatoes along with 3 tbsp of water. Mash gently with the back of the spatula to create a moist, spreadable filling. Garnish with coriander.",
            "Heat a cast iron tawa or heavy non-stick skillet. Sprinkle water droplets—they should sizzle and evaporate instantly. Wipe dry with a kitchen towel.",
            "Pour a ladleful of fermented batter into the center, and using spiral outward circular strokes, spread thinly into a wide circle.",
            "Drizzle ghee or oil around the edges and over the center. Cook on medium-high flame until the underside turns deeply golden and edges lift effortlessly.",
            "Place 3 tablespoons of hot potato masala in the center, fold over, and serve piping hot with fresh coconut chutney and spicy piping sambar!"
        ],
        "steps_hi": [
            "आलू मसाला: पैन में 1 चम्मच तेल गरम करें। राई तड़काएं, फिर चना दाल, उड़द दाल, कढ़ी पत्ता और हरी मिर्च डालकर दाल सुनहरा होने तक भूनें।",
            "लंबे कटे प्याज डालें और गुलाबी व पारदर्शी होने तक भूनें (प्याज को भूरा न करें)।",
            "हल्दी और नमक डालें, फिर हाथ से मसले आलू और 3 चम्मच पानी डालकर मिलाएं। करछी से हल्का सा मैश करें ताकि मसाला नम और फैलाने योग्य बन जाए। हरा धनिया डालें।",
            "तवे (लोहे या नॉन-स्टिक) को तेज गरम करें। पानी के छींटे मारें और सूती कपड़े से पोंछ लें।",
            "तवे के बीच में एक बड़ा चमचा बैटर डालें और गोल-गोल घुमाते हुए किनारों तक पतला फैलाएं।",
            "किनारों और बीच में घी या तेल छिड़कें। मध्यम आंच पर तब तक सेकें जब तक नीचे से सुनहरा और क्रिस्पी न हो जाए और किनारे खुद तवे को छोड़ने लगें।",
            "बीच में 3 चम्मच तैयार आलू मसाला रखें, डोसे को मोड़ें और ताज़ा नारियल की चटनी व गरम सांभर के साथ परोसें!"
        ],
        "pro_tips_en": [
            "Add a pinch of sugar or 1 tsp besan to the batter right before spreading for that bakery-level golden hue and crispiness.",
            "Always maintain the tawa temperature: wipe with a damp cloth between each dosa.",
            "Moist potato masala with a splash of water prevents the dosa from drying out."
        ],
        "pro_tips_hi": [
            "बैटर में सेकने से ठीक पहले एक चुटकी चीनी या 1 चम्मच बेसन मिलाने से डोसा एकदम सुनहरा और कुरकुरा बनता है।",
            "हर डोसा बनाने से पहले तवे को गीले कपड़े से पोंछकर तापमान नियंत्रित करना बेहद जरूरी है।",
            "आलू में 2-3 चम्मच पानी डालकर पकाने से मसाला नम रहता है और डोसा सूखा नहीं लगता।"
        ]
    },
    {
        "slug": "mumbai-street-pav-bhaji",
        "title_en": "Authentic Mumbai Street-Style Butter Pav Bhaji",
        "title_hi": "मुंबई स्पेशल स्ट्रीट-स्टाइल बटर पाव भाजी",
        "summary_en": "Spicy, buttery, mashed mixed vegetable gravy slow-simmered on a wide tawa, served with fluffy pan-toasted butter pav, onions, and lime.",
        "summary_hi": "सब्जियों और खास पाव भाजी मसाले की चटपटी मक्खन वाली भाजी, साथ में तवे पर सिंका हुआ नरम बटर पाव, बारीक प्याज और नींबू।",
        "category": "snack",
        "category_en": "Snacks & Street Food",
        "category_hi": "नाश्ता व चाट",
        "prep_time": 20,
        "cook_time": 25,
        "total_time": 45,
        "servings": 5,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 420,
        "image": "https://images.unsplash.com/photo-1606491956689-2ea866880c84?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Boiled Potatoes", "amount": 3, "unit": "large", "note": "peeled"},
            {"item": "Boiled Cauliflower Florets", "amount": 1, "unit": "cup", "note": "softly boiled"},
            {"item": "Green Peas (Matar)", "amount": 0.75, "unit": "cup", "note": "boiled fresh or frozen"},
            {"item": "Finely Chopped Capsicum", "amount": 1, "unit": "large", "note": "crunchy green bell pepper"},
            {"item": "Finely Chopped Red Onions", "amount": 2, "unit": "medium", "note": "finely diced"},
            {"item": "Ripe Tomatoes Pureed", "amount": 4, "unit": "large", "note": "fresh pureed"},
            {"item": "Amul Butter", "amount": 4, "unit": "tbsp", "note": "generous street-style butter"},
            {"item": "Pav Bhaji Masala", "amount": 2.5, "unit": "tbsp", "note": "premium aromatic blend"},
            {"item": "Kashmiri Red Chilli Paste", "amount": 2, "unit": "tbsp", "note": "soaked dry red chillies ground with garlic"},
            {"item": "Kasuri Methi", "amount": 1, "unit": "tsp", "note": "crushed"},
            {"item": "Soft Ladi Pav", "amount": 8, "unit": "buns", "note": "fresh baker's pav"},
            {"item": "Lemon & Coriander", "amount": 1, "unit": "set", "note": "for garnishing"}
        ],
        "ingredients_hi": [
            {"item": "उबले आलू", "amount": 3, "unit": "बड़े", "note": "छीले हुए"},
            {"item": "उबली फूलगोभी", "amount": 1, "unit": "कप", "note": "अच्छी तरह उबली हुई"},
            {"item": "हरी मटर", "amount": 0.75, "unit": "कप", "note": "उबली हुई"},
            {"item": "बारीक कटी शिमला मिर्च", "amount": 1, "unit": "बड़ी", "note": "एकदम बारीक कटी"},
            {"item": "बारीक कटा प्याज", "amount": 2, "unit": "मध्यम", "note": "महीन कटा हुआ"},
            {"item": "टमाटर की प्यूरी", "amount": 4, "unit": "बड़े", "note": "ताज़ा पीसे हुए"},
            {"item": "अमूल मक्खन (बटर)", "amount": 4, "unit": "बड़ा चम्मच", "note": "असली स्ट्रीट स्टाइल स्वाद"},
            {"item": "पाव भाजी मसाला", "amount": 2.5, "unit": "बड़ा चम्मच", "note": "खुशबूदार"},
            {"item": "कश्मीरी लाल मिर्च-लहसुन पेस्ट", "amount": 2, "unit": "बड़ा चम्मच", "note": "भीगी मिर्च व लहसुन का पेस्ट"},
            {"item": "कसूरी मेथी", "amount": 1, "unit": "छोटा चम्मच", "note": "रगड़कर डाली हुई"},
            {"item": "ताज़ा लादी पाव", "amount": 8, "unit": "पीस", "note": "नरम बेकरी पाव"},
            {"item": "नींबू और हरा धनिया", "amount": 1, "unit": "सेट", "note": "सजावट व परोसने के लिए"}
        ],
        "steps_en": [
            "In a large pressure cooker or pot, boil potatoes, cauliflower, and green peas until fork-tender. Drain and mash roughly.",
            "Heat 2 tbsp butter and 1 tbsp oil in a wide tawa or large kadai. Add finely chopped onions and sauté until translucent.",
            "Add the finely diced capsicum and sauté for 2 minutes to keep its fresh green crunch.",
            "Add the garlic-red chilli paste and sauté for 1 minute until fragrant. Pour in the fresh tomato puree, cover, and cook until butter separates.",
            "Stir in pav bhaji masala, salt, and kasuri methi. Add the boiled mashed vegetables and 1 cup of hot water.",
            "Use a heavy potato masher right in the pan to mash everything together continuously while simmering for 10-12 minutes on low heat, adding water as needed to reach desired velvety consistency.",
            "Finish with a generous dollop of butter and fresh coriander. Slice pav buns lengthwise, toast in sizzling butter with a pinch of pav bhaji masala and coriander on the tawa, and serve with cut onions and fresh lime wedges."
        ],
        "steps_hi": [
            "प्रेशर कुकर में आलू, फूलगोभी और मटर को नरम होने तक उबाल लें। पानी छानकर मैशर से मोटा मैश कर लें।",
            "चौड़े तवे या कड़ाही में 2 चम्मच मक्खन और 1 चम्मच तेल गरम करें। बारीक कटा प्याज डालकर गुलाबी होने तक भूनें।",
            "बारीक कटी शिमला मिर्च डालें और 2 मिनट भूनें ताकि उसका क्रंच बना रहे।",
            "लहसुन-लाल मिर्च का पेस्ट डालकर 1 मिनट भूनें। अब ताज़ा टमाटर प्यूरी डालें और तब तक पकाएं जब तक मक्खन अलग न दिखने लगे।",
            "पाव भाजी मसाला, नमक और कसूरी मेथी मिलाएं। अब उबली मैश की हुई सब्जियां और 1 कप गरम पानी डालें।",
            "तवे पर ही पोटैटो मैशर से सब्जियों को लगातार 10-12 मिनट तक दबाते हुए धीमी आंच पर पकाएं जब तक भाजी एकसार और गाढ़ी न हो जाए।",
            "ऊपर से ढेर सारा मक्खन और हरा धनिया डालें। तवे पर मक्खन, थोड़ी सी भाजी या पाव भाजी मसाला डालकर पाव को बीच से काटकर दोनों तरफ से अच्छी तरह सेकें और नींबू-प्याज के साथ पेश करें।"
        ],
        "pro_tips_en": [
            "The magic secret of Juhu beach pav bhaji is grinding soaked Kashmiri chillies with garlic into a fiery red paste.",
            "Never puree the vegetables in a mixer—always hand-mash on the tawa for that authentic coarse street texture.",
            "Toasting the pav in the pan drippings with a pinch of bhaji masala elevates the flavor tenfold."
        ],
        "pro_tips_hi": [
            "जुहू बीच जैसी असली भाजी का राज़ है साबुत कश्मीरी मिर्च को भिगोकर लहसुन के साथ ताज़ा पीसना।",
            "सब्जियों को मिक्सी में कभी न पीसें—तवे पर पोटैटो मैशर से हाथ से मैश करने पर ही असली स्ट्रीट जैसा टेक्सचर आता है।",
            "पाव को सेकते समय तवे पर हल्का सा पाव भाजी मसाला और मक्खन छिड़ककर सेकें, स्वाद दोगुना हो जाएगा।"
        ]
    },
    {
        "slug": "royal-dal-makhani",
        "title_en": "Dhaba-Style Slow Cooked Dal Makhani",
        "title_hi": "ढाबा स्टाइल स्लो-कुक्ड दाल मखनी",
        "summary_en": "Whole black urad lentils and kidney beans slow-simmered for hours with rustic spices, cream, cultured butter, and infused with smoky charcoal dhungar.",
        "summary_hi": "काली साबुत उड़द और राजमा से धीमी आंच पर घंटों पकी हुई दाल, मक्खन, क्रीम और असली कोयले के धुंघार (स्मोकी फ्लेवर) के साथ।",
        "category": "main",
        "category_en": "Main Course",
        "category_hi": "मुख्य व्यंजन",
        "prep_time": 15,
        "cook_time": 60,
        "total_time": 75,
        "servings": 5,
        "difficulty_en": "Medium",
        "difficulty_hi": "मध्यम",
        "diet_tag_en": "High-Protein & Veg",
        "diet_tag_hi": "हाई-प्रोटीन शाकाहारी",
        "calories": 360,
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Whole Black Urad Dal (Sabut Urad)", "amount": 1, "unit": "cup", "note": "soaked overnight for 8-10 hours"},
            {"item": "Dark Kidney Beans (Rajma)", "amount": 0.25, "unit": "cup", "note": "soaked with the dal"},
            {"item": "Ripe Tomatoes Pureed", "amount": 4, "unit": "medium", "note": "smoothly pureed"},
            {"item": "Ginger-Garlic Paste", "amount": 1.5, "unit": "tbsp", "note": "freshly pounded"},
            {"item": "Salted Butter (Makhan)", "amount": 4, "unit": "tbsp", "note": "divided into stages"},
            {"item": "Fresh Dairy Cream", "amount": 0.25, "unit": "cup", "note": "heavy cream"},
            {"item": "Degi Mirch Powder", "amount": 1.5, "unit": "tsp", "note": "for color and gentle warmth"},
            {"item": "Garam Masala", "amount": 0.5, "unit": "tsp", "note": "ground spice mix"},
            {"item": "Kasuri Methi", "amount": 1, "unit": "tbsp", "note": "roasted and powdered"},
            {"item": "Natural Lump Charcoal (for Dhungar)", "amount": 1, "unit": "small piece", "note": "for authentic smoky aroma"}
        ],
        "ingredients_hi": [
            {"item": "साबुत काली उड़द दाल", "amount": 1, "unit": "कप", "note": "रातभर 8-10 घंटे भीगी हुई"},
            {"item": "चित्रा राजमा", "amount": 0.25, "unit": "कप", "note": "दाल के साथ भीगा हुआ"},
            {"item": "टमाटर की प्यूरी", "amount": 4, "unit": "मध्यम", "note": "ताज़ा पीसी हुई"},
            {"item": "अदरक-लहसुन पेस्ट", "amount": 1.5, "unit": "बड़ा चम्मच", "note": "ताज़ा कुटा हुआ"},
            {"item": "मक्खन (बटर)", "amount": 4, "unit": "बड़ा चम्मच", "note": "विभिन्न चरणों में डालने के लिए"},
            {"item": "ताज़ा मलाई या क्रीम", "amount": 0.25, "unit": "कप", "note": "फैंटी हुई"},
            {"item": "देगी मिर्च पाउडर", "amount": 1.5, "unit": "छोटा चम्मच", "note": "सुंदर रंग और स्वाद के लिए"},
            {"item": "गरम मसाला", "amount": 0.5, "unit": "छोटा चम्मच", "note": "घर का बना"},
            {"item": "कसूरी मेथी", "amount": 1, "unit": "बड़ा चम्मच", "note": "हल्की भुनी व कुटी हुई"},
            {"item": "प्राकृतिक लकड़ी का कोयला", "amount": 1, "unit": "छोटा टुकड़ा", "note": "असली स्मोकी धुंघार के लिए"}
        ],
        "steps_en": [
            "Wash soaked dal and rajma thoroughly until water runs clear. Pressure cook with 4 cups of water, 1 tsp salt, and 1 tbsp butter for 6-7 whistles until completely soft and mashable.",
            "Use the back of a ladle to mash about a third of the dal against the side of the pot to release natural starches for a creamy texture.",
            "In a heavy pot, melt 2 tbsp butter. Add ginger-garlic paste and cook for 2 minutes until aromatic.",
            "Add Degi mirch and immediately stir in the fresh tomato puree. Cook for 8-10 minutes until oil droplets separate.",
            "Transfer the boiled dal along with its cooking liquid into the tomato masala. Bring to a gentle boil.",
            "Reduce heat to the lowest setting and let the dal simmer uncovered for at least 45 minutes to an hour, stirring frequently and adding warm water as needed.",
            "Stir in garam masala, roasted kasuri methi, remaining 2 tbsp butter, and fresh cream. Simmer for another 5 minutes.",
            "Dhungar smoke step: Place a small steel bowl on the dal. Heat a piece of charcoal red hot over the gas flame, place in the bowl, pour 1/2 tsp ghee over the coal, and instantly cover the pot with a tight lid for 4 minutes to trap the smoke. Garnish with a swirl of cream and serve!"
        ],
        "steps_hi": [
            "भीगी हुई उड़द और राजमा को 3-4 बार साफ पानी से धोएं। कुकर में 4 कप पानी, 1 चम्मच नमक और 1 चम्मच मक्खन डालकर 6-7 सीटी आने तक अच्छी तरह उबालें।",
            "दाल को चमचे के पिछले हिस्से से थोड़ा सा मैश करें ताकि प्राकृतिक गाढ़ापन आ जाए।",
            "भारी तले के बर्तन में 2 चम्मच मक्खन गरम करें। अदरक-लहसुन का पेस्ट डालकर 2 मिनट भूनें।",
            "देगी मिर्च डालें और तुरंत ताज़ा टमाटर प्यूरी डालकर 8-10 मिनट तक पकाएं जब तक मसाला तेल न छोड़ दे।",
            "उबली हुई दाल को पानी समेत इस तड़के में पलट दें और उबाल आने दें।",
            "आंच एकदम धीमी कर दें और दाल को कम से कम 45 से 60 मिनट तक धीमी आंच पर कढ़ने (सिमर होने) दें। बीच-बीच में चलाते रहें और आवश्यकतानुसार गरम पानी डालें।",
            "गरम मसाला, भुनी कसूरी मेथी, बचा हुआ मक्खन और क्रीम मिलाएं। 5 मिनट और धीमी आंच पर पकाएं।",
            "स्मोकी धुंघार: दाल के बीच में छोटी कटोरी रखें। कोयले को गैस पर लाल दहकाएं, कटोरी में रखें, उस पर 1/2 चम्मच घी डालें और तुरंत ढक्कन 4 मिनट के लिए बंद कर दें। ऊपर से क्रीम डालकर गरमा-गरम परोसें!"
        ],
        "pro_tips_en": [
            "The magic of authentic dal makhani lies in the slow simmer—the longer it bubbles on low flame, the creamier it becomes.",
            "Never discard the dal soaking water; wash well beforehand and cook in fresh filtered water.",
            "The charcoal dhungar takes this dish straight to highway dhaba grandeur."
        ],
        "pro_tips_hi": [
            "असली दाल मखनी का स्वाद धीमी आंच पर कढ़ने से आता है—जितनी देर यह धीमी आंच पर पकेगी, उतनी ही मखमली बनेगी।",
            "दाल को पकाने से पहले अच्छी तरह धो लें और ताज़े पानी में उबालें।",
            "कोयले का धुंघार इस दाल को सीधा मशहूर ढाबों जैसा लाजवाब स्मोकी फ्लेवर देता है।"
        ]
    },
    {
        "slug": "shahi-gulab-jamun",
        "title_en": "Melt-in-Mouth Shahi Gulab Jamun",
        "title_hi": "हलवाई स्टाइल रसीले शाही गुलाब जामुन",
        "summary_en": "Golden-brown khoya and paneer spheres fried to perfection and soaked in a warm, fragrant saffron and green cardamom sugar syrup.",
        "summary_hi": "मावा (खोया) और ताज़ा पनीर से बने रुई जैसे मुलायम गुलाब जामुन, केसर और इलायची की खुशबूदार चाशनी में डूबे हुए।",
        "category": "dessert",
        "category_en": "Desserts & Sweets",
        "category_hi": "मिठाइयाँ",
        "prep_time": 25,
        "cook_time": 25,
        "total_time": 50,
        "servings": 6,
        "difficulty_en": "Medium",
        "difficulty_hi": "मध्यम",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 310,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Soft Mawa / Khoya", "amount": 200, "unit": "g", "note": "grated fresh"},
            {"item": "Fresh Paneer", "amount": 60, "unit": "g", "note": "crumbled fine"},
            {"item": "All-Purpose Flour (Maida)", "amount": 3, "unit": "tbsp", "note": "for gentle binding"},
            {"item": "Baking Powder", "amount": 0.25, "unit": "tsp", "note": "precise measurement for soft rise"},
            {"item": "Sugar", "amount": 1.75, "unit": "cups", "note": "for syrup"},
            {"item": "Water", "amount": 1.75, "unit": "cups", "note": "for syrup"},
            {"item": "Green Cardamom Pods", "amount": 4, "unit": "pods", "note": "crushed"},
            {"item": "Saffron Strands (Kesar)", "amount": 12, "unit": "strands", "note": "for aroma and gold tint"},
            {"item": "Rose Water", "amount": 1, "unit": "tsp", "note": "for royal fragrance"},
            {"item": "Pure Ghee", "amount": 2, "unit": "cups", "note": "for deep frying"}
        ],
        "ingredients_hi": [
            {"item": "नरम मावा (खोया)", "amount": 200, "unit": "ग्राम", "note": "ताज़ा कद्दूकस किया हुआ"},
            {"item": "ताज़ा पनीर", "amount": 60, "unit": "ग्राम", "note": "बारीक मसला हुआ"},
            {"item": "मैदा", "amount": 3, "unit": "बड़ा चम्मच", "note": "बाइंडिंग के लिए"},
            {"item": "बेकिंग पाउडर", "amount": 0.25, "unit": "छोटा चम्मच", "note": "गुलाब जामुन फूलने के लिए"},
            {"item": "चीनी", "amount": 1.75, "unit": "कप", "note": "चाशनी के लिए"},
            {"item": "पानी", "amount": 1.75, "unit": "कप", "note": "चाशनी के लिए"},
            {"item": "हरी इलायची", "amount": 4, "unit": "पीस", "note": "कुटी हुई"},
            {"item": "केसर के धागे", "amount": 12, "unit": "धागे", "note": "शाही खुशबू और रंग के लिए"},
            {"item": "गुलाब जल", "amount": 1, "unit": "छोटा चम्मच", "note": "सुगंध के लिए"},
            {"item": "देसी घी", "amount": 2, "unit": "कप", "note": "तलने के लिए"}
        ],
        "steps_en": [
            "Make the syrup: Boil sugar and water together with crushed cardamom and saffron for 6-8 minutes until sticky (half-string consistency, just like honey on fingers). Stir in rose water, turn off heat, and keep warm.",
            "Knead the dough: On a clean marble board or plate, knead grated mawa and paneer with the heel of your palm for 5 minutes until completely smooth with no grains.",
            "Add maida and baking powder. Gently bring together into a soft, crack-free dough without over-kneading.",
            "Shape into small, crack-free marble-sized balls (they will double in size when fried and soaked).",
            "Heat ghee in a deep kadai over very low heat. Test one ball first—it should gently rise to the surface without breaking.",
            "Gently swirl the warm ghee around the balls without touching them directly. Fry on slow flame for 10-12 minutes until uniformly deep golden brown.",
            "Drain immediately from ghee and plunge directly into the warm sugar syrup. Let them soak for at least 2 hours until plump and juicy. Serve warm!"
        ],
        "steps_hi": [
            "चाशनी बनाएं: पैन में चीनी, पानी, कुटी इलायची और केसर डालकर 6-8 मिनट उबालें जब तक चाशनी शहद जैसी चिपचिपी (आधे तार की) न हो जाए। गुलाब जल डालकर गैस बंद करें और चाशनी को गुनगुना रहने दें।",
            "आटा गूंथना: एक बड़ी परात में कद्दूकस मावा और पनीर को हथेली से 5 मिनट तक अच्छी तरह मसलें जब तक वह एकदम चिकना व दानेरहित न हो जाए।",
            "मैदा और बेकिंग पाउडर मिलाएं और हल्के हाथों से एकसार कर नरम डो बना लें (ज्यादा जोर से न गूंथें)।",
            "डो से छोटी-छोटी बिना दरार (crack-free) वाली गोलियां बना लें।",
            "कड़ाही में धीमी आंच पर घी गरम करें। पहले एक गोली डालकर टेस्ट करें—वह धीरे-धीरे ऊपर तैरनी चाहिए।",
            "कलछी से घी को गोल-गोल घुमाएं ताकि जामुन खुद घूमें। धीमी आंच पर 10-12 मिनट तक एक समान सुनहरा भूरा होने तक तलें।",
            "घी से निकालकर तुरंत गुनगुनी चाशनी में डालें। कम से कम 2 घंटे चाशनी में भीगने दें ताकि वे चाशनी सोखकर रसीले बन जाएं। गरमा-गरम परोसें!"
        ],
        "pro_tips_en": [
            "The secret to crack-free jamuns is kneading the khoya and paneer until the fat releases and turns buttery smooth.",
            "The ghee must be at low temperature—if it's too hot, the outsides will brown while the centers remain dense and uncooked.",
            "The sugar syrup must be warm, not boiling hot, or the jamuns will collapse."
        ],
        "pro_tips_hi": [
            "गुलाब जामुन फटने से बचाने का राज़ है मावा और पनीर को हथेली से तब तक मसलना जब तक वह मक्खन जैसा चिकना न हो जाए।",
            "घी का तापमान हमेशा हल्का गरम (धीमी आंच) होना चाहिए—तेज घी में ऊपर से जामुन काले हो जाएंगे और अंदर से कच्चे रह जाएंगे।",
            "चाशनी गुनगुनी होनी चाहिए, खौलती हुई चाशनी में डालने से गुलाब जामुन पिचक सकते हैं।"
        ]
    },
    {
        "slug": "amritsari-chole-bhature",
        "title_en": "Authentic Amritsari Pindi Chole & Puffy Bhature",
        "title_hi": "अमृतसरी पिंडी छोले और फूले-फूले कुरकुरे भटूरे",
        "summary_en": "Dark, spicy, and tangy chickpeas infused with black tea and anardana, paired with pillowy, crisp, balloon-puffed bhature.",
        "summary_hi": "चाय पत्ती और अनारदाने के खट्टे-तीखे स्वाद वाले अमृतसरी छोले, गरमा-गरम गुब्बारे जैसे फूले हुए खस्ता भटूरों के साथ।",
        "category": "main",
        "category_en": "Main Course",
        "category_hi": "मुख्य व्यंजन",
        "prep_time": 30,
        "cook_time": 40,
        "total_time": 70,
        "servings": 4,
        "difficulty_en": "Medium",
        "difficulty_hi": "मध्यम",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 510,
        "image": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Kabuli Chana (Chickpeas)", "amount": 1.5, "unit": "cups", "note": "soaked overnight with a pinch of baking soda"},
            {"item": "Black Tea Bag / Leaves", "amount": 2, "unit": "tea bags", "note": "for authentic dark color"},
            {"item": "Dry Pomegranate Powder (Anardana)", "amount": 1.5, "unit": "tbsp", "note": "for characteristic tang"},
            {"item": "Amritsari Chole Masala", "amount": 2, "unit": "tbsp", "note": "roasted cumin, coriander, amchur"},
            {"item": "All-Purpose Flour (Maida)", "amount": 2, "unit": "cups", "note": "for bhature"},
            {"item": "Fine Semolina (Sooji)", "amount": 3, "unit": "tbsp", "note": "for long-lasting crispness"},
            {"item": "Fresh Curd (Dahi)", "amount": 0.33, "unit": "cup", "note": "for natural fermentation"},
            {"item": "Baking Powder", "amount": 0.5, "unit": "tsp", "note": "for puff"},
            {"item": "Green Chillies & Ginger Juliennes", "amount": 3, "unit": "tbsp", "note": "for classic topping"},
            {"item": "Desi Ghee", "amount": 3, "unit": "tbsp", "note": "for final tadka"}
        ],
        "ingredients_hi": [
            {"item": "काबुली चना", "amount": 1.5, "unit": "कप", "note": "रातभर चुटकी भर मीठे सोडे के साथ भीगा हुआ"},
            {"item": "चाय पत्ती की पोटली / टी बैग", "amount": 2, "unit": "पीस", "note": "असली गहरे काले रंग के लिए"},
            {"item": "अनारदाना पाउडर", "amount": 1.5, "unit": "बड़ा चम्मच", "note": "खास चटपटे स्वाद के लिए"},
            {"item": "अमृतसरी छोले मसाला", "amount": 2, "unit": "बड़ा चम्मच", "note": "भुना जीरा, धनिया, अमचूर युक्त"},
            {"item": "मैदा", "amount": 2, "unit": "कप", "note": "भटूरों के लिए"},
            {"item": "बारीक सूजी", "amount": 3, "unit": "बड़ा चम्मच", "note": "कुरकुरापन बनाए रखने के लिए"},
            {"item": "ताज़ा दही", "amount": 0.33, "unit": "कप", "note": "प्राकृतिक खमीर के लिए"},
            {"item": "बेकिंग पाउडर", "amount": 0.5, "unit": "छोटा चम्मच", "note": "भटूरे फूलने के लिए"},
            {"item": "अदरक के लच्छे व हरी मिर्च", "amount": 3, "unit": "बड़ा चम्मच", "note": "तड़के और गार्निश के लिए"},
            {"item": "देसी घी", "amount": 3, "unit": "बड़ा चम्मच", "note": "आखिरी तड़के के लिए"}
        ],
        "steps_en": [
            "Boil chickpeas in a pressure cooker with tea bags, cinnamon, black cardamom, salt, and water for 6-7 whistles until meltingly tender. Discard tea bags.",
            "In a kadai, heat 2 tbsp oil and sauté ginger-garlic paste and pureed onions until golden brown.",
            "Add dry spices: coriander powder, roasted cumin, anardana, and chole masala. Cook on low heat with 3 tbsp of boiled chana water until fragrant.",
            "Add boiled chana and simmer for 15-20 minutes, lightly mashing some chickpeas with a ladle to thicken the gravy.",
            "Finish with a sizzling ghee tadka of slit green chillies, ginger juliennes, and hing poured over the bubbling chole.",
            "For bhature: Mix maida, sooji, salt, sugar, baking powder, curd, and warm water into a soft pliable dough. Rest covered with a damp cloth for 2 hours.",
            "Roll into oval disks and slide into smoking hot oil. Press lightly with a perforated spoon until it inflates like a balloon. Flip and fry until golden crisp. Serve immediately!"
        ],
        "steps_hi": [
            "प्रेशर कुकर में काबुली चना, चाय की पोटली, दालचीनी, बड़ी इलायची, नमक और पानी डालकर 6-7 सीटी तक उबालें जब तक चना एकदम नरम न हो जाए। पोटली निकाल दें।",
            "कड़ाही में 2 चम्मच तेल गरम करके अदरक-लहसुन पेस्ट और प्याज का पेस्ट सुनहरा होने तक भूनें।",
            "अनारदाना पाउडर, धनिया पाउडर, भुना जीरा और छोले मसाला डालें। थोड़ा सा चने का पानी डालकर धीमी आंच पर मसाले भूनें।",
            "उबले छोले मिलाएं और 15-20 मिनट धीमी आंच पर पकाएं। कुछ छोलों को करछी से मैश करें ताकि गाढ़ापन आ जाए।",
            "ऊपर से देसी घी में हींग, कटी हरी मिर्च और अदरक के लच्छों का गरमा-गरम तड़का लगाएं।",
            "भटूरे का आटा: मैदा, सूजी, नमक, हल्की चीनी, बेकिंग पाउडर, दही और गुनगुने पानी से नरम आटा गूंथें। गीले कपड़े से ढककर 2 घंटे आराम दें।",
            "लोई को ओवल आकार में बेलें और तेज गरम तेल में डालें। कलछी से हल्का दबाते ही भटूरा गुब्बारे जैसा फूल जाएगा। पलटकर सुनहरा सेकें और तुरंत परोसें!"
        ],
        "pro_tips_en": [
            "A tea bag in the pressure cooker yields that quintessential dark street-side Punjabi chole color without any artificial coloring.",
            "Adding a few spoonfuls of fine sooji ensures the bhature remain puffy and crisp on the table rather than turning soggy immediately.",
            "Oil temperature for bhature must be piping hot—if the oil is lukewarm, bhature will absorb oil and fail to inflate."
        ],
        "pro_tips_hi": [
            "कुकर में चाय की पोटली या टी बैग डालने से बिना किसी कृत्रिम रंग के असली पंजाबी छोलों जैसा डार्क रंग आता है।",
            "भटूरे के आटे में सूजी मिलाने से भटूरा प्लेट में आने के बाद भी काफी देर तक फूला और खस्ता बना रहता है।",
            "भटूरे तलते समय तेल धुआंधार गरम होना चाहिए—हल्के गरम तेल में भटूरा तेल पी लेगा और फूलेगा नहीं।"
        ]
    },
    {
        "slug": "masala-chai-ginger-infusion",
        "title_en": "Authentic Masala Chai & Fresh Ginger Infusion",
        "title_hi": "कड़क अदरक-इलायची मसाला चाय",
        "summary_en": "The soul of an Indian kitchen—strong Assam CTC black tea brewed with crushed ginger, green cardamom, cloves, and whole milk.",
        "summary_hi": "भारतीय रसोई की जान—असम की कड़क चायपत्ती, ताज़ा कुटा अदरक, छोटी इलायची, लौंग और दूध की लाजवाब मसालेदार चाय।",
        "category": "drinks",
        "category_en": "Beverages",
        "category_hi": "पेय पदार्थ",
        "prep_time": 5,
        "cook_time": 10,
        "total_time": 15,
        "servings": 2,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शाकाहारी",
        "calories": 110,
        "image": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 0,
        "ingredients_en": [
            {"item": "Water", "amount": 1.25, "unit": "cups", "note": "filtered water"},
            {"item": "Full Cream Milk", "amount": 1, "unit": "cup", "note": "for rich velvety body"},
            {"item": "Strong Assam CTC Tea", "amount": 2.5, "unit": "tsp", "note": "premium black tea"},
            {"item": "Fresh Ginger (Adrak)", "amount": 1, "unit": "inch", "note": "freshly crushed in mortar-pestle"},
            {"item": "Green Cardamom Pods (Elaichi)", "amount": 3, "unit": "pods", "note": "cracked open"},
            {"item": "Cloves (Laung)", "amount": 2, "unit": "buds", "note": "for gentle warmth"},
            {"item": "Sugar or Jaggery (Gud)", "amount": 2, "unit": "tsp", "note": "or to taste"}
        ],
        "ingredients_hi": [
            {"item": "पानी", "amount": 1.25, "unit": "कप", "note": "साफ पानी"},
            {"item": "फुल क्रीम दूध", "amount": 1, "unit": "कप", "note": "मलाईदार स्वाद के लिए"},
            {"item": "कड़क असम चायपत्ती", "amount": 2.5, "unit": "छोटा चम्मच", "note": "सीटीसी चायपत्ती"},
            {"item": "ताज़ा अदरक", "amount": 1, "unit": "इंच", "note": "ओखली में ताज़ा कुटा हुआ"},
            {"item": "छोटी इलायची", "amount": 3, "unit": "पीस", "note": "मुंह खोलकर कुटी हुई"},
            {"item": "लौंग", "amount": 2, "unit": "पीस", "note": "हल्की गर्माहट के लिए"},
            {"item": "चीनी या गुड़", "amount": 2, "unit": "छोटा चम्मच", "note": "स्वादानुसार"}
        ],
        "steps_en": [
            "In a saucepan, bring water to a rolling boil.",
            "Add crushed fresh ginger, cardamom, and cloves. Let spices simmer vigorously in the water for 2 full minutes to release their essential oils.",
            "Add the black tea leaves and sugar. Boil for 1-2 minutes until water turns deeply dark red-amber.",
            "Pour in the full-cream milk. Bring to a rolling boil on medium-high flame until chai rises to the rim of the pot.",
            "Lower flame, let it subside, and repeat the rolling boil twice more for 3-4 minutes to develop a thick, cohesive, rich brew.",
            "Strain through a fine tea strainer directly into clay kulhads or cups. Serve with hot pakoras or biscuits!"
        ],
        "steps_hi": [
            "सॉसपैन में पानी को तेज उबालें।",
            "ताज़ा कुटा हुआ अदरक, इलायची और लौंग डालें। मसालों को 2 मिनट तक उबलने दें ताकि उनका पूरा अर्क और सुगंध पानी में उतर आए।",
            "चायपत्ती और चीनी डालें। 1-2 मिनट उबालें जब तक पानी का रंग गहरा लाल-कत्थई न हो जाए।",
            "अब फुल क्रीम दूध डालें। मध्यम-तेज आंच पर एक अच्छा उबाल आने दें जब तक चाय बर्तन के मुंह तक न आ जाए।",
            "आंच धीमी करें और फिर से 2-3 बार उफान आने दें (3-4 मिनट तक कढ़ाएं) ताकि चाय में असली गाढ़ापन और स्वाद आ जाए।",
            "छलनी से सीधे कुल्हड़ या कप में छानें और गरमा-गरम पकोड़े या बिस्कुट के साथ आनंद लें!"
        ],
        "pro_tips_en": [
            "Always boil the spices in water first before adding milk—milk proteins can seal the spices and block their oils from infusing.",
            "If using jaggery (gud), add it only after turning off the gas flame to prevent the milk from curdling."
        ],
        "pro_tips_hi": [
            "दूध डालने से पहले मसालों को पानी में अच्छी तरह खौलाना सबसे महत्वपूर्ण है, तभी चाय में असली कड़क स्वाद आता है।",
            "अगर गुड़ की चाय बना रहे हैं, तो गैस बंद करने के बाद ही गुड़ मिलाएं ताकि दूध फटे नहीं।"
        ]
    },
    {
        "slug": "royal-mango-kulfi",
        "title_en": "No-Churn Royal Alphonso Mango Kulfi",
        "title_hi": "शाही मलाईदार मैंगो कुल्फी (बिना झंझट)",
        "summary_en": "Traditional Indian frozen dessert made with thick reduced milk, pure Alphonso mango pulp, saffron, and crushed pistachios.",
        "summary_hi": "गाढ़े रबड़ीदार दूध, हापुस आम के गूदे, केसर और पिस्ते से बनी पारंपरिक शाही मलाईदार मैंगो कुल्फी।",
        "category": "dessert",
        "category_en": "Desserts & Sweets",
        "category_hi": "मिठाइयाँ",
        "prep_time": 15,
        "cook_time": 20,
        "total_time": 35,
        "servings": 6,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegetarian & Gluten-Free",
        "diet_tag_hi": "शाकाहारी व ग्लूटेन-मुक्त",
        "calories": 240,
        "image": "https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 0,
        "ingredients_en": [
            {"item": "Full Cream Milk", "amount": 1, "unit": "liter", "note": "whole buffalo or cow milk"},
            {"item": "Ripe Alphonso Mango Pulp", "amount": 1.5, "unit": "cups", "note": "fresh pureed without fiber"},
            {"item": "Condensed Milk", "amount": 0.5, "unit": "cup", "note": "for rich caramel creaminess"},
            {"item": "Milk Powder", "amount": 3, "unit": "tbsp", "note": "for instant mawa texture"},
            {"item": "Cardamom Powder", "amount": 0.5, "unit": "tsp", "note": "freshly ground"},
            {"item": "Pistachios & Almonds", "amount": 3, "unit": "tbsp", "note": "finely slivered"},
            {"item": "Saffron Strands", "amount": 10, "unit": "strands", "note": "soaked in 1 tbsp warm milk"}
        ],
        "ingredients_hi": [
            {"item": "फुल क्रीम दूध", "amount": 1, "unit": "लीटर", "note": "गाढ़ा दूध"},
            {"item": "पके हापुस आम का पल्प", "amount": 1.5, "unit": "कप", "note": "बिना रेशे का ताज़ा पल्प"},
            {"item": "कंडेंस्ड मिल्क", "amount": 0.5, "unit": "कप", "note": "मलाईदार मिठास के लिए"},
            {"item": "मिल्क पाउडर", "amount": 3, "unit": "बड़ा चम्मच", "note": "मावा जैसा टेक्सचर देने के लिए"},
            {"item": "इलायची पाउडर", "amount": 0.5, "unit": "छोटा चम्मच", "note": "ताज़ा पिसा हुआ"},
            {"item": "पिस्ता और बादाम", "amount": 3, "unit": "बड़ा चम्मच", "note": "बारीक कटे हुए"},
            {"item": "केसर के धागे", "amount": 10, "unit": "धागे", "note": "1 चम्मच गुनगुने दूध में भीगे हुए"}
        ],
        "steps_en": [
            "In a wide heavy kadai, bring milk to a boil. Lower flame and simmer, scraping the malai (clotted cream) from the sides back into the milk until reduced to half its original volume.",
            "Whisk in the milk powder, condensed milk, and saffron milk. Simmer for another 5 minutes until it resembles a thick pourable rabdi.",
            "Turn off heat and let the rabdi cool completely to room temperature. (Never mix mango pulp into hot milk, or it will curdle!)",
            "Once completely cool, fold in the fresh mango pulp, cardamom powder, and half the chopped nuts using a gentle whisk until silky smooth.",
            "Pour into kulfi molds or earthen matkas. Top with remaining slivered pistachios and insert wooden sticks.",
            "Freeze for at least 8 hours or overnight until solidly set. Demold by rubbing the molds between your warm palms for 10 seconds and serve immediately!"
        ],
        "steps_hi": [
            "कड़ाही में दूध को उबालें। आंच धीमी करके दूध को तब तक पकाएं जब तक वह घटकर आधा न रह जाए। किनारों पर जमी मलाई को खुरचकर दूध में ही मिलाते रहें।",
            "मिल्क पाउडर, कंडेंस्ड मिल्क और केसर वाला दूध मिलाएं। 5 मिनट और पकाएं जब तक यह गाढ़ी रबड़ी न बन जाए।",
            "गैस बंद करें और रबड़ी को कमरे के तापमान पर पूरी तरह ठंडा होने दें। (गरम दूध में कभी आम न मिलाएं, वरना दूध फट सकता है!)",
            "रबड़ी ठंडी होने पर ताज़ा आम का पल्प, इलायची पाउडर और आधे कटे मेवे डालकर अच्छी तरह फेंटें।",
            "कुल्फी मोल्ड्स या मिट्टी की मटकियों में भरें। ऊपर से बचे हुए पिस्ता डालें और कुल्फी स्टिक लगाएं।",
            "फ्रीजर में 8 घंटे या रातभर जमने के लिए रखें। मोल्ड को हथेलियों के बीच 10 सेकंड रगड़कर डिमोल्ड करें और ठंडी-ठंडी परोसें!"
        ],
        "pro_tips_en": [
            "Cooling the reduced milk completely before adding mango pulp is non-negotiable to prevent curdling.",
            "Adding a touch of milk powder gives that dense, traditional khoya texture without standing over the stove for 2 hours."
        ],
        "pro_tips_hi": [
            "दूध को पूरी तरह ठंडा करने के बाद ही आम का पल्प मिलाएं, गरम में मिलाने से कुल्फी का दूध फट सकता है।",
            "मिल्क पाउडर मिलाने से घंटों मेहनत किए बिना एकदम बाजार जैसी दानेदार मावे वाली कुल्फी बनती है।"
        ]
    },
    {
        "slug": "crispy-onion-palak-pakoras",
        "title_en": "Monsoon Crispy Onion & Spinach Pakoras",
        "title_hi": "बारिश स्पेशल कुरकुरे प्याज और पालक के पकोड़े",
        "summary_en": "Extra-crispy golden fritters made with thinly sliced onions, baby spinach leaves, crushed coriander seeds, carom seeds, and gram flour.",
        "summary_hi": "पतले लच्छेदार प्याज, ताज़ा पालक, कुटे धनिए और अजवाइन से बने सुपर कुरकुरे पकोड़े, हरी तीखी चटनी के साथ।",
        "category": "quick",
        "category_en": "Quick 15-Min",
        "category_hi": "झटपट 15 मिनट",
        "prep_time": 10,
        "cook_time": 10,
        "total_time": 20,
        "servings": 4,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegan & Gluten-Free",
        "diet_tag_hi": "वीगन व ग्लूटेन-मुक्त",
        "calories": 220,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 0,
        "ingredients_en": [
            {"item": "Thinly Sliced Red Onions", "amount": 3, "unit": "medium", "note": "separated into loose rings"},
            {"item": "Fresh Spinach Leaves (Palak)", "amount": 1, "unit": "cup", "note": "washed and roughly chopped"},
            {"item": "Gram Flour (Besan)", "amount": 1, "unit": "cup", "note": "sifted"},
            {"item": "Rice Flour (Chawal ka Atta)", "amount": 2, "unit": "tbsp", "note": "secret for long-lasting crunch"},
            {"item": "Carom Seeds (Ajwain)", "amount": 1, "unit": "tsp", "note": "crushed between palms"},
            {"item": "Crushed Coriander Seeds (Sabut Dhaniya)", "amount": 1, "unit": "tbsp", "note": "coarsely pounded"},
            {"item": "Green Chillies", "amount": 2, "unit": "pieces", "note": "finely chopped"},
            {"item": "Turmeric & Kashmiri Chilli Powder", "amount": 0.5, "unit": "tsp each", "note": "for color and flavor"},
            {"item": "Hot Oil", "amount": 1, "unit": "tbsp", "note": "poured into batter for crispiness"},
            {"item": "Oil for Frying", "amount": 2, "unit": "cups", "note": "mustard or peanut oil"}
        ],
        "ingredients_hi": [
            {"item": "पतले कटे प्याज के लच्छे", "amount": 3, "unit": "मध्यम", "note": "हाथ से अलग किए हुए"},
            {"item": "ताज़ा पालक के पत्ते", "amount": 1, "unit": "कप", "note": "धोकर मोटे कटे हुए"},
            {"item": "बेसन", "amount": 1, "unit": "कप", "note": "छना हुआ"},
            {"item": "चावल का आटा", "amount": 2, "unit": "बड़ा चम्मच", "note": "सुपर क्रिस्पी बनाने का सीक्रेट"},
            {"item": "अजवाइन", "amount": 1, "unit": "छोटा चम्मच", "note": "हाथों से मसलकर डाली हुई"},
            {"item": "कुटा साबुत धनिया", "amount": 1, "unit": "बड़ा चम्मच", "note": "दरदरा कुटा हुआ"},
            {"item": "हरी मिर्च", "amount": 2, "unit": "पीस", "note": "बारीक कटी हुई"},
            {"item": "हल्दी और कश्मीरी लाल मिर्च पाउडर", "amount": 0.5, "unit": "छोटा चम्मच प्रत्येक", "note": "रंग व स्वाद के लिए"},
            {"item": "गरम तेल", "amount": 1, "unit": "बड़ा चम्मच", "note": "घोल में मोयन के लिए"},
            {"item": "तलने के लिए तेल", "amount": 2, "unit": "कप", "note": "सरसों या मूंगफली का तेल"}
        ],
        "steps_en": [
            "In a wide mixing bowl, combine sliced onions, chopped spinach, salt, crushed ajwain, pounded coriander seeds, green chillies, and spice powders. Massage with your fingers for 2 minutes—the onions will release their natural juices.",
            "Sprinkle besan and rice flour over the onion-spinach mixture. Do not add water yet; let the natural moisture bind the flour.",
            "Drizzle 1 tbsp of sizzling hot oil into the mixture. Mix lightly—the batter should coat the vegetables loosely without being a thick runny paste.",
            "Heat oil in a kadai on medium heat. Drop small, loose, jagged clusters of the mixture into the hot oil.",
            "Fry on medium heat for 4-5 minutes, turning occasionally until beautifully golden brown and ultra crisp.",
            "Drain onto a wire rack (not paper towels, which steam them soft). Sprinkle with chaat masala and serve with mint chutney and masala chai!"
        ],
        "steps_hi": [
            "बड़े बर्तन में कटे प्याज, पालक, नमक, अजवाइन, कुटा साबुत धनिया, हरी मिर्च और मसाले डालें। हाथों से 2 मिनट अच्छी तरह मसलें ताकि प्याज अपना पानी छोड़ दे।",
            "अब बेसन और चावल का आटा छिड़कें। अभी पानी बिल्कुल न डालें; प्याज के प्राकृतिक पानी से ही बाइंडिंग होने दें।",
            "घोल पर 1 चम्मच खौलता हुआ गरम तेल डालें। हल्के हाथ से मिलाएं—मिश्रण गाढ़ा लेप नहीं, बल्कि सब्जियों पर हल्की कोटिंग जैसा होना चाहिए।",
            "कड़ाही में मध्यम आंच पर तेल गरम करें। छोटे-छोटे अनगढ़े पकोड़े तेल में छोड़ें।",
            "मध्यम आंच पर 4-5 मिनट तक पलट-पलट कर सुनहरा और कुरकुरा होने तक तलें।",
            "तार वाली जाली पर निकालें (टिशू पेपर पर न रखें ताकि वे भाप से नरम न पड़ें)। ऊपर से चाट मसाला छिड़कें और पुदीने की चटनी व कड़क चाय के साथ परोसें!"
        ],
        "pro_tips_en": [
            "Never add excess water to onion pakora batter! The onion's own released moisture creates the crispiest lachha pakoras.",
            "Rice flour + 1 tbsp hot oil added to the raw batter guarantees pakoras stay crunchy for over an hour."
        ],
        "pro_tips_hi": [
            "प्याज के पकोड़ों में अलग से पानी बिल्कुल न डालें—प्याज के खुद के पानी से ही सबसे कुरकुरे लच्छेदार पकोड़े बनते हैं।",
            "चावल का आटा और घोल में 1 चम्मच खौलता गरम तेल डालने से पकोड़े 1 घंटे बाद भी एकदम कुरकुरे रहते हैं।"
        ]
    }
]

KITCHEN_TIPS = [
    {
        "icon": "fa-bread-slice",
        "category_en": "Roti & Baking",
        "category_hi": "रोटी व बेकिंग",
        "title_en": "The Secret to Balloon-Puffy, Cotton-Soft Rotis Every Time",
        "title_hi": "हर बार रुई जैसी मुलायम और गुब्बारे जैसी फूलने वाली रोटी का राज़",
        "content_en": "Always knead the whole wheat dough with lukewarm water and let it rest covered for at least 15-20 minutes before rolling. The resting period activates gluten naturally, ensuring tender, moist rotis that stay soft till dinner!",
        "content_hi": "गेहूं का आटा हमेशा हल्के गुनगुने पानी से गूंथें और बेलने से पहले कम से कम 15-20 मिनट ढककर आराम दें। इससे ग्लूटेन एक्टिवेट होता है और रोटियां घंटों तक रुई जैसी मुलायम बनी रहती हैं।"
    },
    {
        "icon": "fa-pepper-hot",
        "category_en": "Spice Secrets",
        "category_hi": "मसालों का सीक्रेट",
        "title_en": "Never Burn Kashmiri Red Chilli Powder",
        "title_hi": "कश्मीरी लाल मिर्च को कभी न जलने देने का सही तरीका",
        "content_en": "To get that vibrant crimson color in gravies without scorching the spices, always dissolve red chilli powder and turmeric in 2 tablespoons of warm water before adding to hot oil, or drop the heat to low and add tomatoes immediately.",
        "content_hi": "सब्जी में खूबसूरत लाल रंग पाने और मसाले को जलने से बचाने के लिए, लाल मिर्च और हल्दी को हमेशा 2 चम्मच पानी में घोलकर गरम तेल में डालें, या फिर आंच धीमी करके तुरंत टमाटर प्यूरी मिला दें।"
    },
    {
        "icon": "fa-cheese",
        "category_en": "Dairy Care",
        "category_hi": "डेयरी टिप्स",
        "title_en": "How to Keep Store-Bought Paneer Ultra-Soft",
        "title_hi": "बाजार के पनीर को हमेशा हलवाई जैसा सॉफ्ट रखने की ट्रिक",
        "content_en": "Submerge paneer cubes in a bowl of warm water with 1/2 tsp salt for 10 minutes before sliding into gravies. The moisture plumps up the proteins, preventing the rubbery texture often caused by cold refrigeration.",
        "content_hi": "पनीर के टुकड़ों को ग्रेवी में डालने से पहले 10 मिनट हल्के गुनगुने नमकीन पानी में भिगोकर रखें। इससे पनीर बिल्कुल ताज़ा, स्पंजी और मक्खन जैसा मुलायम बना रहता है।"
    },
    {
        "icon": "fa-leaf",
        "category_en": "Fresh Produce",
        "category_hi": "ताज़ा सब्जियां",
        "title_en": "Keep Fresh Coriander and Mint Crisp for 3 Weeks",
        "title_hi": "हरा धनिया और पुदीना 3 हफ्तों तक एकदम ताज़ा और हरा रखने का नुस्खा",
        "content_en": "Trim stems slightly, discard any wilted leaves, and store the unwashed bunch upright in a glass jar with 1 inch of water at the bottom. Cover loosely with a reusable zip pouch and refrigerate.",
        "content_hi": "धनिए की जड़ों को थोड़ा छांटें, बिना धोए एक कांच के जार में 1 इंच पानी भरकर धनिए को सीधा रखें और ऊपर से प्लास्टिक या सूती थैली से ढीला ढककर फ्रिज में रखें। पत्तियां हफ्तों तक ताज़ा रहेंगी।"
    }
]

TESTIMONIALS = [
    {
        "name": "Pooja Sharma",
        "city_en": "Delhi, India",
        "city_hi": "दिल्ली, भारत",
        "rating": 5,
        "recipe_tried_en": "Restaurant-Style Paneer Butter Masala",
        "recipe_tried_hi": "शाही पनीर बटर मसाला",
        "text_en": "I tried Vanshika's Paneer Butter Masala recipe for our Diwali family dinner. The tip to strain the tomato puree made it taste 100% like a 5-star restaurant! My mother-in-law asked for the recipe!",
        "text_hi": "मैंने दिवाली डिनर पर वंशिका की पनीर बटर मसाला रेसिपी बनाई। प्यूरी छानने वाले सीक्रेट से इसका स्वाद बिल्कुल फाइव-स्टार रेस्टोरेंट जैसा आया! सासू माँ ने भी रेसिपी नोट की!"
    },
    {
        "name": "Rohan Mehta",
        "city_en": "Mumbai, India",
        "city_hi": "मुंबई, भारत",
        "rating": 5,
        "recipe_tried_en": "Mumbai Street-Style Pav Bhaji",
        "recipe_tried_hi": "मुंबई स्पेशल बटर पाव भाजी",
        "text_en": "Living away from Mumbai, I craved authentic Chowpatty pav bhaji. The garlic-red chilli paste technique in this recipe is gold standard. Took me straight back home!",
        "text_hi": "मुंबई से बाहर रहने पर असली चौपाटी वाली पाव भाजी बहुत याद आती थी। इस रेसिपी में लहसुन-मिर्च पेस्ट वाली ट्रिक कमाल की है। बिल्कुल मुंबई का असली स्वाद आ गया!"
    },
    {
        "name": "Simran Kaur",
        "city_en": "Chandigarh, India",
        "city_hi": "चंडीगढ़, भारत",
        "rating": 5,
        "recipe_tried_en": "Dhaba-Style Slow Cooked Dal Makhani",
        "recipe_tried_hi": "ढाबा स्टाइल दाल मखनी",
        "text_en": "The charcoal dhungar technique is an absolute game-changer! The Dal Makhani was velvety, deeply smoky, and better than any Punjabi highway dhaba.",
        "text_hi": "कोयले के धुंघार वाली तकनीक ने तो कमाल ही कर दिया! दाल मखनी इतनी मखमली और स्मोकी बनी कि हाईवे के बड़े-बड़े ढाबे भी इसके आगे फेल हैं।"
    },
    {
        "name": "Ananya Joshi",
        "city_en": "Pune, India",
        "city_hi": "पुणे, भारत",
        "rating": 5,
        "recipe_tried_en": "Crispy Golden Masala Dosa",
        "recipe_tried_hi": "कुरकुरा मसाला डोसा",
        "text_en": "Finally cracked restaurant-level crispy dosas at home! Switching between English and Hindi on this site makes it so easy to cook with my grandmother.",
        "text_hi": "आखिरकार घर पर ही रेस्टोरेंट जैसा कुरकुरा डोसा बन गया! वेबसाइट पर इंग्लिश और हिन्दी स्विच करने का विकल्प बहुत बढ़िया है, दादी के साथ कुकिंग करना आसान हो गया।"
    }
]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        title_en TEXT NOT NULL,
        title_hi TEXT NOT NULL,
        summary_en TEXT NOT NULL,
        summary_hi TEXT NOT NULL,
        category TEXT NOT NULL,
        category_en TEXT NOT NULL,
        category_hi TEXT NOT NULL,
        prep_time INTEGER NOT NULL,
        cook_time INTEGER NOT NULL,
        total_time INTEGER NOT NULL,
        servings INTEGER NOT NULL,
        difficulty_en TEXT NOT NULL,
        difficulty_hi TEXT NOT NULL,
        diet_tag_en TEXT NOT NULL,
        diet_tag_hi TEXT NOT NULL,
        calories INTEGER NOT NULL,
        image TEXT NOT NULL,
        instagram_reel TEXT,
        is_featured INTEGER DEFAULT 0,
        ingredients_en TEXT NOT NULL,
        ingredients_hi TEXT NOT NULL,
        steps_en TEXT NOT NULL,
        steps_hi TEXT NOT NULL,
        pro_tips_en TEXT NOT NULL,
        pro_tips_hi TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kitchen_tips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        icon TEXT NOT NULL,
        category_en TEXT NOT NULL,
        category_hi TEXT NOT NULL,
        title_en TEXT NOT NULL,
        title_hi TEXT NOT NULL,
        content_en TEXT NOT NULL,
        content_hi TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS testimonials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city_en TEXT NOT NULL,
        city_hi TEXT NOT NULL,
        rating INTEGER NOT NULL,
        recipe_tried_en TEXT NOT NULL,
        recipe_tried_hi TEXT NOT NULL,
        text_en TEXT NOT NULL,
        text_hi TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS newsletter_subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        preferred_lang TEXT DEFAULT 'en',
        subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact_inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        subject TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Clear existing recipe and tips data to allow clean re-population
    cursor.execute("DELETE FROM recipes")
    cursor.execute("DELETE FROM kitchen_tips")
    cursor.execute("DELETE FROM testimonials")

    # Insert recipes
    for r in RECIPES:
        cursor.execute("""
        INSERT INTO recipes (
            slug, title_en, title_hi, summary_en, summary_hi,
            category, category_en, category_hi,
            prep_time, cook_time, total_time, servings,
            difficulty_en, difficulty_hi, diet_tag_en, diet_tag_hi,
            calories, image, instagram_reel, is_featured,
            ingredients_en, ingredients_hi, steps_en, steps_hi,
            pro_tips_en, pro_tips_hi
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            r["slug"], r["title_en"], r["title_hi"], r["summary_en"], r["summary_hi"],
            r["category"], r["category_en"], r["category_hi"],
            r["prep_time"], r["cook_time"], r["total_time"], r["servings"],
            r["difficulty_en"], r["difficulty_hi"], r["diet_tag_en"], r["diet_tag_hi"],
            r["calories"], r["image"], r["instagram_reel"], r["is_featured"],
            json.dumps(r["ingredients_en"], ensure_ascii=False),
            json.dumps(r["ingredients_hi"], ensure_ascii=False),
            json.dumps(r["steps_en"], ensure_ascii=False),
            json.dumps(r["steps_hi"], ensure_ascii=False),
            json.dumps(r["pro_tips_en"], ensure_ascii=False),
            json.dumps(r["pro_tips_hi"], ensure_ascii=False)
        ))

    # Insert kitchen tips
    for t in KITCHEN_TIPS:
        cursor.execute("""
        INSERT INTO kitchen_tips (icon, category_en, category_hi, title_en, title_hi, content_en, content_hi)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (t["icon"], t["category_en"], t["category_hi"], t["title_en"], t["title_hi"], t["content_en"], t["content_hi"]))

    # Insert testimonials
    for test in TESTIMONIALS:
        cursor.execute("""
        INSERT INTO testimonials (name, city_en, city_hi, rating, recipe_tried_en, recipe_tried_hi, text_en, text_hi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (test["name"], test["city_en"], test["city_hi"], test["rating"], test["recipe_tried_en"], test["recipe_tried_hi"], test["text_en"], test["text_hi"]))

    conn.commit()
    conn.close()
    print("Database initialized successfully with bilingual recipes and content!")

if __name__ == "__main__":
    init_db()
