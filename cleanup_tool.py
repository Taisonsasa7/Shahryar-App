def clean_project():
    print("--- بدء عملية التنظيف الذكي للملفات المكررة ---")
    for file_name in files_to_remove:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"تم حذف الملف: {file_name}")
        else:
            print(f"الملف غير موجود (تم حذفه مسبقاً): {file_name}")
    print("--- تم تنظيف المشروع بنجاح! ---")

if _name_ == "_main_":
    clean_project()
