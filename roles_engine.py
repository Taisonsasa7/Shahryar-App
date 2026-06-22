# roles_engine.py
# نظام مستقل لإدارة أدوار المستخدمين داخل الغرف

def get_role_badge(role):
    """إرجاع العلامة البصرية المناسبة للدور."""
    badges = {
        "owner": "👑",
        "admin": "🛡️",
        "member": ""
    }
    return badges.get(role, "")

def check_user_access(user_id, room_id, database_manager):
    """
    التحقق من دور المستخدم من خلال استعلام قاعدة البيانات.
    يتم تمرير كائن قاعدة البيانات للقيام بالاستعلام.
    """
    # نفترض أن database_manager لديه دالة لجلب الدور
    role = database_manager.get_role_from_db(room_id, user_id)
    return role or "member"
