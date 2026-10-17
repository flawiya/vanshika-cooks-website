"""
Add authentic Diwali Faral recipes directly to Vanshika Cooks database
matching @vanshikacooks "वंशिका स्वादिष्ट फराळ 🪔" profile.
"""

import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "vanshika_cooks.db")

FARAL_RECIPES = [
    {
        "slug": "maharashtrian-bhajani-chakli",
        "title_en": "Authentic Maharashtrian Crispy Bhajani Chakli",
        "title_hi": "खमंग व काटेरी पारंपरिक भाजणी चकली",
        "summary_en": "Traditional spiral, ultra-crispy festive chaklis made from roasted multigrain bhajani flour with white sesame, carom seeds, and hing.",
        "summary_hi": "भाजणीच्या पिठाची कुरकुरीत, काटेरी व तोंडात विरघळणारी पारंपरिक चकली, तीळ, ओवा आणि हिंगाच्या खमंग फोडणीसह।",
        "category": "faral",
        "category_en": "Diwali Faral",
        "category_hi": "दिवाळी फराळ",
        "prep_time": 25,
        "cook_time": 30,
        "total_time": 55,
        "servings": 6,
        "difficulty_en": "Medium",
        "difficulty_hi": "मध्यम",
        "diet_tag_en": "Vegan & Pure Veg",
        "diet_tag_hi": "शुद्ध शाकाहारी व वीगन",
        "calories": 160,
        "image": "https://images.unsplash.com/photo-1605197150495-a2267b2d2f70?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Authentic Chakli Bhajani Flour", "amount": 2, "unit": "cups", "note": "roasted rice, chana dal, urad dal & coriander seed blend"},
            {"item": "White Sesame Seeds (Til)", "amount": 2, "unit": "tbsp", "note": "for nutty crunch"},
            {"item": "Carom Seeds (Ajwain)", "amount": 1, "unit": "tsp", "note": "crushed between palms"},
            {"item": "Boiling Hot Cooking Oil (Moyan)", "amount": 2, "unit": "tbsp", "note": "hot oil for crisp, melt-in-mouth texture"},
            {"item": "Kashmiri Red Chilli Powder", "amount": 1.5, "unit": "tsp", "note": "for warm red color"},
            {"item": "Turmeric Powder (Haldi)", "amount": 0.5, "unit": "tsp", "note": "for golden glow"},
            {"item": "Asafoetida (Hing)", "amount": 0.25, "unit": "tsp", "note": "for signature aroma"},
            {"item": "Hot Water", "amount": 1.25, "unit": "cups", "note": "for kneading soft pliable dough"},
            {"item": "Salt", "amount": 1, "unit": "tsp", "note": "to taste"},
            {"item": "Oil for Deep Frying", "amount": 3, "unit": "cups", "note": "fresh groundnut or sunflower oil"}
        ],
        "ingredients_hi": [
            {"item": "पारंपरिक चकली भाजणी पीठ", "amount": 2, "unit": "कप", "note": "भाजलेले तांदूळ, चणा डाळ, उडीद डाळ व धणे यांचे पीठ"},
            {"item": "पांढरे तीळ", "amount": 2, "unit": "मोठे चमचे", "note": "कुरकुरीतपणा व स्वादासाठी"},
            {"item": "ओवा", "amount": 1, "unit": "छोटा चमचा", "note": "हातावर चोळून घातलेला"},
            {"item": "कडकडीत गरम तेलाचे मोहन", "amount": 2, "unit": "मोठे चमचे", "note": "चकली खुसखुशीत होण्यासाठी"},
            {"item": "लाल तिखट (मिरची पावडर)", "amount": 1.5, "unit": "छोटे चमचे", "note": "रंग व चवीसाठी"},
            {"item": "हळद", "amount": 0.5, "unit": "छोटा चमचा", "note": "सुंदर रंगासाठी"},
            {"item": "हिंग", "amount": 0.25, "unit": "छोटा चमचा", "note": "खमंग वासासाठी"},
            {"item": "गरम पाणी", "amount": 1.25, "unit": "कप", "note": "पीठ मळण्यासाठी"},
            {"item": "मीठ", "amount": 1, "unit": "छोटा चमचा", "note": "चवीनुसार"},
            {"item": "तळण्यासाठी तेल", "amount": 3, "unit": "कप", "note": "शेंगदाणा किंवा सूर्यफूल तेल"}
        ],
        "steps_en": [
            "In a large parat (mixing bowl), combine bhajani flour, white sesame seeds, crushed ajwain, red chilli powder, turmeric, hing, and salt. Mix dry ingredients thoroughly.",
            "Pour 2 tablespoons of smoking hot oil (mohan) over the flour mixture. It will sizzle vigorously. Rub the oil into the flour with your fingertips until crumbly.",
            "Gradually add hot water in batches and knead into a smooth, pliable, non-sticky dough. Rest covered for 10 minutes.",
            "Grease the chakli maker (sohra) and star disc with a drop of oil. Pack with a portion of dough and secure tightly.",
            "Press and rotate clockwise onto small butter paper squares to form 4-5 neat concentric spirals with sharp, well-defined spikes (kante). Seal the outer tail gently.",
            "Heat oil in a kadai on medium flame. Slide chaklis into the oil without crowding. Do not touch for the first minute.",
            "Fry on medium heat for 4-5 minutes, flipping once, until bubbles subside and chaklis turn evenly golden and crisp. Drain on a wire rack and store in an airtight container once cool!"
        ],
        "steps_hi": [
            "मोठ्या परातीत भाजणीचे पीठ, पांढरे तीळ, हातावर चोळलेला ओवा, लाल तिखट, हळद, हिंग आणि मीठ एकत्र करून कोरडेच चांगले मिसळा.",
            "या पिठावर २ मोठे चमचे कडकडीत गरम तेलाचे मोहन घाला. फसफसणारा आवाज येईल. चमच्याने व नंतर हाताने मोहन पिठाला चोळून घ्या.",
            "थोडं थोडं गरम पाणी घालून मऊ, एकसंध आणि न तुटणारा गोळा मळून घ्या. १० मिनिटे झाकून ठेवा.",
            "चकलीच्या साच्याला (सोऱ्याला) आतून हलके तेल लावा. स्टार चकती बसवून त्यात पिठाचा गोळा भरा.",
            "बटर पेपरवर किंवा ताटावर गोलाकार काटेरी चकल्या पाडून घ्या. शेवटचे टोक हलकेच चिकटवून बंद करा.",
            "कढईत मध्यम आचेवर तेल गरम करा. एका वेळी ३-४ चकल्या तेलात सोडा. पहिली १ मिनिट अजिबात हलवू नका.",
            "मध्यम आचेवर दोन्ही बाजूंनी खरपूस तळा. तेलाचे बुडबुडे कमी झाले की चकली तयार झाली असे समजावे. जाळीवर काढून थंड झाल्यावर हवाबंद डब्यात भरा!"
        ],
        "pro_tips_en": [
            "Hot oil mohan (2 tbsp per 2 cups) is the absolute key—too much oil will make chaklis crumble in the pan; too little will make them hard.",
            "Always knead with warm/hot water so the dough becomes elastic and does not break while pressing out spirals.",
            "Oil temperature must be medium: in smoking oil they will brown outside while staying raw inside; in cold oil they will soak grease."
        ],
        "pro_tips_hi": [
            "२ कप पिठासाठी बरोबर २ मोठे चमचे कडकडीत तेलाचे मोहन पुरेसे असते—जास्त मोहन झाले तर चकली तेलात विरघळते आणि कमी झाले तर कडक होते.",
            "पीठ मळताना कोमट-गरम पाणीच वापरावे, यामुळे पीठ लवचिक होते आणि साच्यातून चकली पाडताना तुटत नाही.",
            "तळताना गॅसची आच मध्यम ठेवावी; मंद आचेवर तेल पिते आणि मोठ्या आचेवर बाहेरून करपून आतून मऊ राहते."
        ]
    },
    {
        "slug": "shahi-besan-ladoo",
        "title_en": "Shahi Ghee Danedar Besan Ladoo",
        "title_hi": "शुद्ध साजूक तुपातील दाणेदार बेसन लाडू",
        "summary_en": "Golden, melt-in-the-mouth festive ladoos made with coarsely ground gram flour roasted patiently in pure desi ghee, flavored with green cardamom and nutmeg.",
        "summary_hi": "शुद्ध साजूक तुपात खमंग भाजलेल्या जाडसर डाळीच्या पिठाचे दाणेदार लाडू, वेलची, जायफळ आणि काजू-पिस्त्याच्या शाही स्वादासह।",
        "category": "faral",
        "category_en": "Diwali Faral",
        "category_hi": "दिवाळी फराळ",
        "prep_time": 15,
        "cook_time": 35,
        "total_time": 50,
        "servings": 8,
        "difficulty_en": "Medium",
        "difficulty_hi": "मध्यम",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 210,
        "image": "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "Coarse Besan (Ladoo Besan)", "amount": 2, "unit": "cups", "note": "mota besan for danedar texture"},
            {"item": "Pure Desi Ghee", "amount": 0.75, "unit": "cup", "note": "melted clarified butter"},
            {"item": "Bura Sugar / Boora", "amount": 1, "unit": "cup", "note": "traditional unrefined crystalline sugar for crunch"},
            {"item": "Cardamom Powder (Elaichi)", "amount": 1, "unit": "tsp", "note": "freshly pounded"},
            {"item": "Nutmeg Powder (Jaiphal)", "amount": 0.25, "unit": "tsp", "note": "for traditional aroma"},
            {"item": "Cashews & Pistachios", "amount": 3, "unit": "tbsp", "note": "slivered & golden roasted"}
        ],
        "ingredients_hi": [
            {"item": "जाडसर बेसन (लाडूचे पीठ)", "amount": 2, "unit": "कप", "note": "दाणेदार लाडूसाठी"},
            {"item": "शुद्ध साजूक तूप", "amount": 0.75, "unit": "कप", "note": "घरचे साजूक तूप"},
            {"item": "तगार / बुरा साखर (पिठीसाखर)", "amount": 1, "unit": "कप", "note": "दाणेदार पोत येण्यासाठी"},
            {"item": "वेलची पूड", "amount": 1, "unit": "छोटा चमचा", "note": "ताजी कुटलेली"},
            {"item": "जायफळ पूड", "amount": 0.25, "unit": "छोटा चमचा", "note": "पारंपरिक सुगंधासाठी"},
            {"item": "काजू आणि पिस्ता काप", "amount": 3, "unit": "मोठे चमचे", "note": "तुपात भाजलेले"}
        ],
        "steps_en": [
            "Heat desi ghee in a heavy-bottomed kadai over low flame. Add coarse besan and stir continuously.",
            "Roast on slow flame for 25-30 minutes patiently. The besan will transition from dry and stiff to loose, glossy, and fragrant with a deep golden hue.",
            "Water sprinkle trick for danedar texture: Sprinkle 1 tbsp of cold water over the hot besan. It will froth vigorously and create instant tiny pearls (danas). Stir for 2 more minutes until moisture evaporates completely.",
            "Turn off the heat and transfer the roasted besan to a wide plate. Let it cool until comfortably warm (lukewarm).",
            "Add cardamom powder, nutmeg, roasted nuts, and bura sugar. Rub between your palms to mix uniformly.",
            "Take small portions and roll firmly between your palms into round, glossy ladoos. Garnish with a pistachio sliver and let set for 1 hour!"
        ],
        "steps_hi": [
            "जाड बुडाच्या कढईत साजूक तूप मंद आचेवर गरम करा. जाडसर बेसन घालून एकसारखे हलवत राहा.",
            "मंद आचेवर २५-३० मिनिटे पेशन्सने भाजा. हळूहळू बेसन सैल होईल, तूप सोडेल आणि घरात खमंग सुवास दरवळेल.",
            "दाणेदार टेक्सचरची ट्रिक: बेसन भाजल्यावर त्यावर १ मोठा चमचा थंड पाण्याचा हबका (शिंतोडा) मारा. बेसन फसफसेल आणि छान दाणे तयार होतील. २ मिनिटे परतून पाणी आटू द्या.",
            "गॅस बंद करा आणि मिश्रण परातीत काढून कोमट होऊ द्या (गरम मिश्रणात साखर कधीही घालू नका).",
            "मिश्रण कोमट झाल्यावर त्यात वेलची पूड, जायफळ, काजू-पिस्त्याचे काप आणि बुरा साखर (किंवा पिठीसाखर) घालून हाताने चांगले एकजीव करा.",
            "हातावर थोडे मिश्रण घेऊन गोल गरगरीत लाडू वळा. वरून पिस्त्याचा काप लावा आणि १ तास सेट होऊ द्या!"
        ],
        "pro_tips_en": [
            "Never add sugar to hot roasted besan! The heat will melt the sugar, turning the mixture runny and greasy, preventing ladoos from binding.",
            "Sprinkling a spoonful of water at the very end creates those iconic crystalline pearls that give halwai-style graininess.",
            "Roasting on low flame with patience is non-negotiable—high flame burns the outer flour leaving an unpleasant raw taste inside."
        ],
        "pro_tips_hi": [
            "बेसन गरम असताना साखर कधीही घालू नका—साखर वितळेल आणि मिश्रण पातळ होऊन लाडू वळता येणार नाहीत.",
            "शेवटी मारलेला पाण्याचा हबकाच लाडूंना हलवाईसारखा दाणेदार पोत देतो.",
            "बेसन नेहमी मंद आचेवरच भाजावे; घाई केल्यास डाळ कच्ची राहते व लाडू जिभेला चिकटतात."
        ]
    },
    {
        "slug": "khuskhushit-karanji",
        "title_en": "Crispy Layered Coconut-Mawa Karanji",
        "title_hi": "खुसखुशीत नारळ-खव्याची पारंपरिक करंजी",
        "summary_en": "Crescent-shaped crispy golden pastries with delicate flaky layers, stuffed with a decadent filling of roasted coconut, khoya, poppy seeds, and cardamom.",
        "summary_hi": "चंद्रकोरीच्या आकाराची खुसखुशीत करंजी, सुकं खोबरं, खवा, खसखस, सुकामेवा आणि वेलची-जायफळाच्या शाही सारणाने भरलेली।",
        "category": "faral",
        "category_en": "Diwali Faral",
        "category_hi": "दिवाळी फराळ",
        "prep_time": 30,
        "cook_time": 30,
        "total_time": 60,
        "servings": 6,
        "difficulty_en": "Advanced",
        "difficulty_hi": "विशेष",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 240,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 1,
        "ingredients_en": [
            {"item": "All-Purpose Flour (Maida)", "amount": 2, "unit": "cups", "note": "sifted for outer crust"},
            {"item": "Fine Semolina (Chiroti Rava)", "amount": 2, "unit": "tbsp", "note": "for crispy texture"},
            {"item": "Hot Ghee (Mohan)", "amount": 2, "unit": "tbsp", "note": "smoking hot for flaky crust"},
            {"item": "Fresh Grated Dry Coconut", "amount": 1.5, "unit": "cups", "note": "lightly roasted golden"},
            {"item": "Mawa / Khoya", "amount": 0.5, "unit": "cup", "note": "roasted pink"},
            {"item": "Powdered Sugar", "amount": 1, "unit": "cup", "note": "sifted"},
            {"item": "Poppy Seeds (Khas Khas)", "amount": 1.5, "unit": "tbsp", "note": "roasted"},
            {"item": "Cardamom & Nutmeg Powder", "amount": 1, "unit": "tsp", "note": "freshly pounded"},
            {"item": "Pure Ghee for Deep Frying", "amount": 2, "unit": "cups", "note": "or groundnut oil"}
        ],
        "ingredients_hi": [
            {"item": "मैदा", "amount": 2, "unit": "कप", "note": "चाळून घेतलेला"},
            {"item": "बारीक चिरोटी रवा", "amount": 2, "unit": "मोठे चमचे", "note": "कुरकुरीतपणासाठी"},
            {"item": "कडकडीत तुपाचे मोहन", "amount": 2, "unit": "मोठे चमचे", "note": "खुसखुशीत पारीसाठी"},
            {"item": "किसलेले सुके खोबरे", "amount": 1.5, "unit": "कप", "note": "मंद आचेवर भाजलेले"},
            {"item": "मावा (खवा)", "amount": 0.5, "unit": "कप", "note": "गुलाबी रंगावर भाजलेला"},
            {"item": "पिठीसाखर", "amount": 1, "unit": "कप", "note": "चाळलेली"},
            {"item": "खसखस", "amount": 1.5, "unit": "मोठा चमचा", "note": "भाजलेली"},
            {"item": "वेलची व जायफळ पूड", "amount": 1, "unit": "छोटा चमचा", "note": "सुगंधासाठी"},
            {"item": "तळण्यासाठी तूप किंवा तेल", "amount": 2, "unit": "कप", "note": "साजूक तूप"}
        ],
        "steps_en": [
            "For outer crust: Mix maida, chiroti rava, and pinch of salt. Pour smoking hot ghee over the flour and rub into crumbs. Knead with milk into a stiff, smooth dough. Cover with damp cloth for 30 minutes.",
            "For stuffing (Saran): In a dry pan, lightly roast dry grated coconut until light golden. Roast poppy seeds and mawa separately until fragrant. Cool completely, then combine with powdered sugar, cardamom, and nutmeg.",
            "Divide dough into small lime-sized balls. Roll into thin 4-inch circular puris.",
            "Place 1.5 tbsp of stuffing on one half. Apply a film of milk or water along the edge with your fingertip.",
            "Fold the other half over to create a crescent shape. Press edges firmly with fingers, then crimp with a karanji cutter (katne) or pinch with fork.",
            "Heat ghee on medium-low flame. Gently slide karanjis into the ghee and splash hot ghee over them with a ladle to create tiny blisters on the crust.",
            "Fry until delicate pale golden and crisp. Drain and cool completely before storing."
        ],
        "steps_hi": [
            "पारीसाठी: मैदा, बारीक रवा आणि चिमूटभर मीठ एकत्र करा. कडकडीत साजूक तुपाचे मोहन घालून हाताने चोळा. दुधाने घट्ट गोळा मळा आणि ओल्या कापडाखाली ३० मिनिटे ठेवा.",
            "सारणासाठी: किसलेले खोबरे मंद आचेवर हलके गुलाबी भाजा. खसखस व खवा वेगळा परता. पूर्ण थंड झाल्यावर त्यात पिठीसाखर, सुकामेवा, वेलची-जायफळ पूड मिसळा.",
            "पिठाचे लहान पेढ्याएवढे गोळे करून पातळ लाटून घ्या.",
            "मधोमध १.५ मोठा चमचा सारण भरा. कडांना बोटाने हलके दूध किंवा पाणी लावा.",
            "दुसरी बाजू वर दुमडून चंद्रकोर आकार द्या. कडा दाबून कातणीने (कटरने) नक्षीदार कापून घ्या.",
            "मध्यम-मंद आचेवर तूप गरम करा. करंज्या तेलात सोडून त्यावर कलथ्याने तूप उडवा जेणेकरून पारीवर छान खसखशीसारखे बारीक फोड येतील.",
            "हलक्या सोनेरी रंगावर तळून जाळीवर काढा. थंड झाल्यावर डब्यात भरा!"
        ],
        "pro_tips_en": [
            "Splashing hot ghee over the floating karanjis with a ladle creates signature tiny blisters on the crust that make it shatteringly crisp.",
            "Always ensure the stuffing has zero moisture and is completely cool before sealing to prevent steam from tearing the crust while frying."
        ],
        "pro_tips_hi": [
            "तळताना करंजीवर चमच्याने गरम तूप उडवल्याने पारीवर छान बारीक दाणेदार फोड येतात आणि ती जास्त खुसखुशीत होते.",
            "सारणात अजिबात ओलावा नसावा आणि ते पूर्ण थंड असावे, नाहीतर तळताना वाफ होऊन करंजी फुटू शकते."
        ]
    },
    {
        "slug": "patla-poha-chivda",
        "title_en": "Crispy Roasted Patla Poha Chivda",
        "title_hi": "खमंग भाजलेला पातळ पोहा चिवडा",
        "summary_en": "Light, crisp, and low-oil festive snack made from slow-roasted paper-thin flattened rice, tempered with crunchy peanuts, roasted dalia, curry leaves, and green chillies.",
        "summary_hi": "अगदी कमी तेलात कुरकुरीत भाजलेल्या पातळ पोह्यांचा चिवडा, शेंगदाणे, पंढरपुरी डाळे, कढीपत्ता आणि हिरव्या मिरचीच्या खमंग फोडणीसह।",
        "category": "faral",
        "category_en": "Diwali Faral",
        "category_hi": "दिवाळी फराळ",
        "prep_time": 15,
        "cook_time": 20,
        "total_time": 35,
        "servings": 8,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegan & Gluten-Free",
        "diet_tag_hi": "शुद्ध शाकाहारी व ग्लूटेन-मुक्त",
        "calories": 140,
        "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 0,
        "ingredients_en": [
            {"item": "Thin Flattened Rice (Patla Poha)", "amount": 500, "unit": "g", "note": "sun-dried or roasted crisp"},
            {"item": "Raw Peanuts (Shengdana)", "amount": 0.5, "unit": "cup", "note": "fried golden"},
            {"item": "Roasted Gram Dal (Dalia / Futana)", "amount": 0.5, "unit": "cup", "note": "crispy roasted"},
            {"item": "Dry Coconut Slices (Kopra)", "amount": 0.33, "unit": "cup", "note": "thinly sliced & fried pale golden"},
            {"item": "Curry Leaves (Kadi Patta)", "amount": 25, "unit": "leaves", "note": "fried completely crisp without moisture"},
            {"item": "Green Chillies", "amount": 4, "unit": "slit", "note": "fried crisp"},
            {"item": "Mustard Seeds & Cumin (Rai-Jeera)", "amount": 1, "unit": "tsp each", "note": "for tempering"},
            {"item": "Turmeric & Hing", "amount": 1, "unit": "tsp each", "note": "for vibrant yellow glow"},
            {"item": "Powdered Sugar", "amount": 1.5, "unit": "tbsp", "note": "for balanced sweet-savory punch"},
            {"item": "Cooking Oil", "amount": 3, "unit": "tbsp", "note": "only 3 tbsp for 500g poha!"}
        ],
        "ingredients_hi": [
            {"item": "पातळ पोहे", "amount": 500, "unit": "ग्रॅम", "note": "उन्हात वाळवलेले किंवा कढईत मंद आचेवर भाजलेले"},
            {"item": "शेंगदाणे", "amount": 0.5, "unit": "कप", "note": "खरपूस तळलेले"},
            {"item": "पंढरपुरी डाळे (फुटाणा डाळ)", "amount": 0.5, "unit": "कप", "note": "भाजलेली"},
            {"item": "सुक्या खोबऱ्याचे पातळ काप", "amount": 0.33, "unit": "कप", "note": "गुलाबी तळलेले"},
            {"item": "कढीपत्ता", "amount": 25, "unit": "पाने", "note": "तळून कुरकुरीत केलेला"},
            {"item": "हिरव्या मिरच्यांचे तुकडे", "amount": 4, "unit": "पीस", "note": "तळून कुरकुरीत केलेले"},
            {"item": "मोहरी आणि जिरे", "amount": 1, "unit": "छोटा चमचा प्रत्येक", "note": "फोडणीसाठी"},
            {"item": "हळद व हिंग", "amount": 1, "unit": "छोटा चमचा प्रत्येक", "note": "सुंदर रंगासाठी"},
            {"item": "पिठीसाखर", "amount": 1.5, "unit": "मोठे चमचे", "note": "खमंग गोड-तिखट चवीसाठी"},
            {"item": "खाद्यतेल", "amount": 3, "unit": "मोठे चमचे", "note": "फक्त ३ चमचे तेल!"}
        ],
        "steps_en": [
            "In a large wide kadai over lowest flame, gently roast thin poha in small batches for 4-5 minutes, tossing with light hands until crisp when pressed between fingers. Do not crush.",
            "Transfer roasted poha to a very large container or paper-lined tray.",
            "In a pan, heat 3 tbsp oil. Fry peanuts until golden crunch, then remove with slotted spoon and add to poha.",
            "In the same oil, fry dry coconut slices and dalia until lightly golden, then add to poha.",
            "To the remaining hot oil, add mustard seeds, cumin, green chillies, and curry leaves. Fry until chillies and curry leaves are 100% moisture-free and paper-crisp.",
            "Turn off heat, add turmeric, hing, and salt. Pour the sizzling aromatic tadka immediately over the roasted poha.",
            "Sprinkle powdered sugar over the warm chivda. Gently toss and turn with two large spatulas from bottom to top until uniformly bright yellow and coated. Cool and store!"
        ],
        "steps_hi": [
            "मोठ्या कढईत मंद आचेवर पातळ पोहे हलक्या हाताने ४-५ मिनिटे भाजा. बोटाने दाबल्यावर चुरा झाला पाहिजे. पोहे तुटू नयेत म्हणून अलगद हलवा.",
            "भाजलेले पोहे मोठ्या परातीत किंवा घमेल्यात काढून ठेवा.",
            "पॅनमध्ये ३ चमचे तेल गरम करा. शेंगदाणे खरपूस तळून पोह्यांवर घाला. त्यानंतर खोबऱ्याचे काप आणि डाळे तळून पोह्यांवर टाका.",
            "उरलेल्या गरम तेलात मोहरी, जिरे, हिरवी मिरची आणि कढीपत्ता घाला. मिरची व कढीपत्ता पूर्ण कुरकुरीत (कोरडा) होईपर्यंत तळा.",
            "गॅस बंद करून हळद, हिंग आणि मीठ घाला. ही खमंग गरमागरम फोडणी लगेच पोह्यांवर सर्वत्र ओता.",
            "वरून पिठीसाखर पसरा. दोन मोठ्या उलथण्यांनी खालून वर हलक्या हाताने पोहे तुटू न देता एकजीव करा. चिवडा छान पिवळाधमक आणि कुरकुरीत होईल!"
        ],
        "pro_tips_en": [
            "Frying the green chillies and curry leaves until bone-dry is the golden rule: even a droplet of water from moist leaves will soften the crisp poha.",
            "A touch of powdered sugar brings that iconic sweet-sour-spicy balanced punch of traditional festive chivda."
        ],
        "pro_tips_hi": [
            "मिरची आणि कढीपत्ता पूर्ण कोरडे व कुरकुरीत होईपर्यंत तळणे सर्वात महत्त्वाचे आहे; थोडाही ओलावा राहिल्यास पोहे मऊ पडतात.",
            "पिठीसाखर घातल्याने चिवड्याला अस्सल खमंग, गोडसर-तिखट चव येते."
        ]
    },
    {
        "slug": "god-shankarpali",
        "title_en": "Melt-in-Mouth Flaky Sweet Shankarpali",
        "title_hi": "पदराची खुसखुशीत बिस्किटासारखी गोड शंकरपाळी",
        "summary_en": "Crisp diamond-cut sweet festive cookies made from whole milk, melted pure ghee, and sugar, fried to a pale golden crisp with delicate flaky layers.",
        "summary_hi": "दूध, साखर आणि साजूक तुपाच्या अचूक प्रमाणात बनवलेली, पदर सुटलेली आणि जिभेवर विरघळणारी गोड शंकरपाळी।",
        "category": "faral",
        "category_en": "Diwali Faral",
        "category_hi": "दिवाळी फराळ",
        "prep_time": 20,
        "cook_time": 25,
        "total_time": 45,
        "servings": 8,
        "difficulty_en": "Easy",
        "difficulty_hi": "सरल",
        "diet_tag_en": "Vegetarian",
        "diet_tag_hi": "शुद्ध शाकाहारी",
        "calories": 190,
        "image": "https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?auto=format&fit=crop&w=1200&q=80",
        "instagram_reel": "https://www.instagram.com/vanshikacooks/",
        "is_featured": 0,
        "ingredients_en": [
            {"item": "Whole Milk (Doodh)", "amount": 0.5, "unit": "cup", "note": "warm"},
            {"item": "Pure Desi Ghee", "amount": 0.5, "unit": "cup", "note": "melted warm"},
            {"item": "Granulated Sugar", "amount": 0.5, "unit": "cup", "note": "dissolved in warm milk & ghee"},
            {"item": "All-Purpose Flour (Maida)", "amount": 2.5, "unit": "cups", "note": "or as much as liquid absorbs"},
            {"item": "Cardamom Powder", "amount": 0.5, "unit": "tsp", "note": "for aroma"},
            {"item": "Salt", "amount": 1, "unit": "pinch", "note": "balances sweetness"},
            {"item": "Ghee or Oil for Frying", "amount": 2.5, "unit": "cups", "note": "for slow crisp frying"}
        ],
        "ingredients_hi": [
            {"item": "दूध", "amount": 0.5, "unit": "कप", "note": "कोमट"},
            {"item": "साजूक तूप", "amount": 0.5, "unit": "कप", "note": "वितळवलेले"},
            {"item": "साखर", "amount": 0.5, "unit": "कप", "note": "दूध व तुपात विरघळवलेली"},
            {"item": "मैदा", "amount": 2.5, "unit": "कप", "note": "मिश्रणात बसेल तितका"},
            {"item": "वेलची पूड", "amount": 0.5, "unit": "छोटा चमचा", "note": "सुवासासाठी"},
            {"item": "मीठ", "amount": 1, "unit": "चिमूटभर", "note": "गोडी वाढवण्यासाठी"},
            {"item": "तळण्यासाठी तूप किंवा तेल", "amount": 2.5, "unit": "कप", "note": "मंद आचेवर तळण्यासाठी"}
        ],
        "steps_en": [
            "In a saucepan on low heat, combine milk, melted ghee, and sugar. Warm gently just until sugar dissolves completely. Do not boil. Let cool to lukewarm.",
            "In a bowl, add the lukewarm liquid, pinch of salt, and cardamom powder. Gradually add maida in batches, kneading into a semi-stiff pliable dough (neither too soft nor rock hard).",
            "Rest dough covered for 15 minutes.",
            "Divide into large portions. Roll out into a 1/4-inch thick flat disc (keep it slightly thick for beautiful flaky layers).",
            "Using a pizza cutter, knife, or diamond roller, cut into classic diamond or square shapes.",
            "Heat ghee/oil in a kadai on medium-low heat. Slide shankarpali in and fry patiently on low flame, stirring gently.",
            "They will puff up and develop visible layers. Remove when light golden brown (they will continue to darken slightly as they cool). Drain and enjoy!"
        ],
        "steps_hi": [
            "सॉसपॅनमध्ये दूध, वितळवलेले तूप आणि साखर एकत्र करा. मंद आचेवर साखर विरघळेपर्यंत कोमट करा (उकळू देऊ नका).",
            "मिश्रण कोमट झाल्यावर त्यात चिमूटभर मीठ आणि वेलची पूड घाला. जेवढा बसेल तेवढा मैदा थोडा थोडा घालत मध्यम घट्ट डो मळा.",
            "पीठ १५ मिनिटे झाकून ठेवा.",
            "मोठी जाडसर पोळी लाटा (साधारण १/४ इंच जाड ठेवावी, यामुळे भरपूर पदर सुटतात).",
            "कातणीने किंवा चाकूने हिऱ्याच्या (डायमंड) आकाराची शंकरपाळी कापून घ्या.",
            "कढईत मंद आचेवर तूप/तेल गरम करा. शंकरपाळी घालून मंद आचेवर सावकाश तळा.",
            "तळताना शंकरपाळी छान फुलेल आणि पदर दिसू लागतील. हलका सोनेरी रंग आला की काढा (बाहेर आल्यावरही तिचा रंग थोडा गडद होतो). थंड झाल्यावर खुसखुशीत बिस्किटासारखी लागेल!"
        ],
        "pro_tips_en": [
            "The magic golden ratio is: 1/2 cup milk + 1/2 cup ghee + 1/2 cup sugar (1:1:1 proportion). It yields 100% foolproof flaky shankarpali every time.",
            "Always roll slightly thick (around 1/4 inch) rather than paper thin so the layers can expand into flaky biscuits."
        ],
        "pro_tips_hi": [
            "शंकरपाळीचे अचूक प्रमाण: १/२ कप दूध + १/२ कप तूप + १/२ कप साखर (१:१:१ प्रमाण). हे प्रमाण वापरल्यास शंकरपाळी कधीही बिघडत नाही.",
            "पोळी जास्त पातळ न लाटता थोडी जाडसर लाटावी, त्यामुळे आत छान बिस्किटासारखे पदर सुटतात."
        ]
    }
]

def add_faral():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for r in FARAL_RECIPES:
        cursor.execute("DELETE FROM recipes WHERE slug = ?", (r["slug"],))
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
        print("Added Faral recipe:", r["slug"])

    conn.commit()
    conn.close()
    print("All Diwali Faral recipes successfully added to database!")

if __name__ == "__main__":
    add_faral()
