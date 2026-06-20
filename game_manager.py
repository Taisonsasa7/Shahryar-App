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
