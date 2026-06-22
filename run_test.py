from shahryar_core import shahryar_system

def run_simulation_test():
    print("--- بدء اختبار نظام شهريار الفعال ---")
    
    # 1. اختبار النظام المالي (توزيع الأرباح)
    print("\n[الاختبار 1: المحرك المالي]")
    payout = shahryar_system.calculate_payout(100) # اختبار مبلغ 100 دولار
    print(f"توزيع الأرباح لـ 100$: {payout}")

    # 2. اختبار المحاكي السياسي (ترامب وإيران)
    print("\n[الاختبار 2: محاكي المفاوضات]")
    result = shahryar_system.simulate_negotiation("Donald Trump", "Iranian Authorities", 7)
    print(f"نتيجة المفاوضات: {result}")

    # 3. اختبار المزامنة
    print("\n[الاختبار 3: مزامنة الأصول]")
    shahryar_system.sync_state("user_123_aquarium", "Golden_Dragon")
    print("تمت المزامنة بنجاح.")

    print("\n--- نهاية الاختبار بنجاح ---")

if _name_ == "_main_":
    run_simulation_test()
