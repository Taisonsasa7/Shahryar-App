class GameManager:
    def _init_(self):
        # المكتبة مقسمة لنوعين: External (روابط) و Internal (ألعاب HTML5 داخل الغرفة)
        self.library = {
            "pubg": {"type": "external", "url": "https://www.pubgmobile.com/play"},
            "football_pro": {"type": "external", "url": "https://www.fifa.com/play"},
            "ludo_star": {"type": "internal", "src": "https://games.example.com/ludo"}, # مثال لألعاب HTML5
            "quiz_battle": {"type": "internal", "src": "https://games.example.com/quiz"}
        }

    def get_game(self, game_id):
        return self.library.get(game_id, None)

    def generate_game_view(self, game_id):
        game = self.get_game(game_id)
        if not game:
            return "عذراً، هذه اللعبة غير موجودة في مكتبتنا."
        
        if game['type'] == "external":
            return {"action": "REDIRECT", "url": game['url']}
        else:
            return {"action": "LOAD_IFRAME", "src": game['src']}
# gifts_system/gifts_manager.py

class GiftsManager:
    # ... (الأجزاء السابقة كما هي)

    def get_formatted_invoice(self, sender_name):
        total_gift_value = sum(item['value'] for item in self.current_invoice)
        service_fee = total_gift_value * 0.10  # حساب 10% رسوم خدمة
        grand_total = total_gift_value + service_fee
        
        invoice_text = f"\n--- 🧾 فاتورة خدمات شهرار لـ {sender_name} ---\n"
        for i, entry in enumerate(self.current_invoice, 1):
            invoice_text += f"{i}. {entry['mic']}: {entry['gift']} ({entry['value']} كوينز)\n"
        
        invoice_text += f"----------------------\n"
        invoice_text += f"إجمالي الهدايا: {total_gift_value} كوينز\n"
        invoice_text += f"رسوم خدمة الذكاء الاصطناعي (10%): {service_fee} كوينز\n"
        invoice_text += f"المبلغ الإجمالي المستحق: {grand_total} كوينز\n"
        invoice_text += f"--- الذكاء الاصطناعي: 'نورتنا يا {sender_name}، كرمك فوق الوصف!' ---"
        return invoice_tex
# هذا الجزء لاختبار الكود داخل نفس الملف
if _name_ == "_main_":
    # إنشاء نسخة للاختبار
    test_engine = MiningEngine()
    
    # تجربة سريعة للتحقق
    print("--- اختبار المحرك المالي ---")
    diamonds = test_engine.calculate_diamonds(5)
    print(f"نتيجة الاختبار: 5 دولار تساوي {diamonds} ماسة.")
    print("---------------------------")
