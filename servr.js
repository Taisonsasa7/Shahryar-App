// كود توزيع الأرباح وتحديد العمولات (يُوضع في السيرفر الرئيسي)

function processPurchase(usdAmount) {
    const exchangeRate = 10000; // 1 USD = 10,000 Diamonds
    const totalDiamonds = usdAmount * exchangeRate;

    // توزيع النسب حسب الدستور (60/10/30)
    const adminShare = totalDiamonds * 0.60;
    const agentShare = totalDiamonds * 0.10;
    const hostShare = totalDiamonds * 0.30;

    return {
        totalDiamonds,
        adminShare,
        agentShare,
        hostShare,
        status: "Finalized - Non-Refundable" // تطبيق سياسة اللا-استرداد برمجياً
    };
}

// مثال عند عملية شحن
const transaction = processPurchase(100); // شحن بـ 100 دولار
console.log(transaction);
