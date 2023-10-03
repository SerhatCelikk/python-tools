import sqlite3

# Veritabanına bağlanma işlemi
conn = sqlite3.connect('request.db')
cursor = conn.cursor()

# "stored" tablosundaki "text" sütunundaki kayıtları filtreleyerek silme işlemi
cursor.execute("DELETE FROM stored WHERE LENGTH(text) > 700 OR LENGTH(text) < 300")

# Değişiklikleri kaydet ve veritabanı bağlantısını kapat
conn.commit()
conn.close()
