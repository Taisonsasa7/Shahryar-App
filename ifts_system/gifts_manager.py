# gifts_system/gifts_manager.py

class GiftsManager:
    def _init_(self):
        self.current_invoice = []

    def add_gift(self, receiver_mic, gift_name, value):
        self.current_invoice.append({"mic": receiver_mic, "gift": gift_name, "value": value})
        return self.get_formatted_invoice()

    def get_formatted_invoice(self):
        total = sum(item['value'] for item in self.current_invoice)
        invoice_text = "\n--- 🧾 فاتورة كرمك ---\n"
        for i, entry in enumerate(self.current_invoice, 1):
            invoice_text += f"{i}. {entry['mic']}: {entry['gift']} ({entry['value']} كوينز)\n"
        invoice_text += f"----------------------\nإجمالي الكرم: {total} كوينز"
        return invoice_text

    def clear_invoice(self):
        self.current_invoice = []
