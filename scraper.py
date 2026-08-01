import mysql.connector

print("1. جاري الاتصال بقاعدة البيانات taib_db...")

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="taib_db"
    )
    cursor = db.cursor()
    print("✅ تم الاتصال بنجاح!")
except Exception as e:
    print(f"❌ خطأ بالاتصال: {e}")
    exit()

# 1. إنشاء الجدول إن لم يكن موجوداً
cursor.execute("""
CREATE TABLE IF NOT EXISTS alibaba_recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    company_name VARCHAR(255),
    product_title VARCHAR(255),
    price VARCHAR(100),
    moq VARCHAR(100),
    rating VARCHAR(50)
)
""")

# 2. تفريغ الجدول لإعادة إضافة القائمة المحدثة
cursor.execute("TRUNCATE TABLE alibaba_recommendations")

# 3. القائمة اليدوية المباشرة (أرسل لي أي منتجات جديدة وأنا أضيفها لك هنا فوراً)
manual_products = [
    # --- قسم الساعات الذكية (smart watch) ---
    ("smart watch", "Shenzhen Colmi Technology Co., Ltd.", "COLMI P71 Smartwatch Bluetooth Calling", "3,712 IQD", "Min. order: 1 piece", "★ 4.8"),
    ("smart watch", "Shenzhen Phylink Electronics Co., Ltd.", "New Ultra Smart Watch Series 8 49mm NFC", "2,227 IQD", "Min. order: 2 pieces", "★ 4.6"),
    ("smart watch", "Guangzhou Lince Technology Co., Ltd.", "W68 Ultra Max Smart Watch 2.2 inch IPS", "5,197 IQD", "Min. order: 1 piece", "★ 4.9"),
    ("smart watch", "Yiwu City Jiaye E-Commerce Firm", "T800 Ultra Smart Watch Series 8 Waterproof", "1,856 IQD", "Min. order: 2 pieces", "★ 4.4"),
    ("smart watch", "Shenzhen Topnotch Technology Co., Ltd.", "H11 Ultra Smart Watch 49mm Screw Real Strap Lock", "6,682 IQD", "Min. order: 1 piece", "★ 4.7"),

    # --- قسم البروجكتر (projector) ---
    ("projector", "Shenzhen Touyinger Technology Co., Ltd.", "TouYinger Q10 Full HD 1080P Projector 9500 Lumens", "180,000 IQD", "Min. order: 1 piece", "★ 4.9"),
    ("projector", "Guangzhou Wanbo Electronic Technology", "Wanbo T2 Max Smart Mini Projector Portable 4K", "110,000 IQD", "Min. order: 2 pieces", "★ 4.7"),
    ("projector", "Shenzhen Magcubic Optoelectronics", "HY300 Android 11 Smart Projector Dual WiFi6", "50,000 IQD", "Min. order: 2 pieces", "★ 4.8")
]

# 4. إدخال القائمة دفعة واحدة
sql = """INSERT INTO alibaba_recommendations (category, company_name, product_title, price, moq, rating) 
         VALUES (%s, %s, %s, %s, %s, %s)"""

cursor.executemany(sql, manual_products)
db.commit()

print(f"🎉 تم بنجاح إضافة {len(manual_products)} منتج إلى قاعدة البيانات!")

cursor.close()
db.close()