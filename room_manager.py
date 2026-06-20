# نظام إدارة الغرف والميكروفونات في شهريار
class RoomManager:
    def _init_(self):
        self.rooms = {}

    def create_room(self, room_id):
        self.rooms[room_id] = {
            'users': [],
            'active_mics': [],
            'status': 'active'
        }
        return f"Room {room_id} created."

    def join_room(self, room_id, user_id):
        if room_id in self.rooms:
            self.rooms[room_id]['users'].append(user_id)
            return f"User {user_id} joined room {room_id}."
        return "Room not found."

    def toggle_mic(self, room_id, user_id, action):
        # action: "on" or "off"
        if room_id in self.rooms:
            if action == "on" and user_id not in self.rooms[room_id]['active_mics']:
                self.rooms[room_id]['active_mics'].append(user_id)
            elif action == "off" and user_id in self.rooms[room_id]['active_mics']:
                self.rooms[room_id]['active_mics'].remove(user_id)
            return f"Mic for {user_id} is now {action}."
        return "Room not found."

# اختبار سريع للنظام
manager = RoomManager()
print(manager.create_room("Room_101"))
print(manager.join_room("Room_101", "User_A"))
print(manager.toggle_mic("Room_101", "User_A", "on"))
