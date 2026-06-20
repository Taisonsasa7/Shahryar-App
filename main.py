from room_manager import RoomManager

# تهيئة النظام
manager = RoomManager()

# تجربة الطلب (تغيير مشروب)
manager.swap_item("user_01", "Saudi", "saudi_gahwa", "moroccan_tea")

# تجربة إعطاء إكرامية
manager.process_tip(20)
