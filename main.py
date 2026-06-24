4. اضغط *Save changes* ثم *Reboot app*.

#### الخيار الثاني: حذف نظام التحقق (لإصلاح التطبيق فوراً والوصول للوحة التحكم)
إذا كنت لا تحتاج حالياً لنظام التحقق (TOTP) وتريد فقط أن يفتح التطبيق وتعرض البيانات، قم بتعديل الكود في ملف main.py على GitHub ليصبح كالتالي (هذا الكود سيتخطى خطوة الـ TOTP تماماً):

```python
import streamlit as st
from supabase import create_client

# إعداد الاتصال
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

st.title("لوحة تحكم السوبر أدمن 🌙")

# عرض البيانات مباشرة بدون تحقق
try:
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)
except Exception as e:
    st.error(f"خطأ في عرض البيانات: {e}")
