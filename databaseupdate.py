import sqlite3

class Post:
    # Post sınıfı tanımı (yukarıdaki gibi)
    def __init__(self, post_id, title, text=None,
                    downs=None, ups=None, author=None,
                    created_at=None, subreddit=None) -> None:
            self.post_id = post_id
            self.title = title
            self.text = text if text is not None else ""
            self.downs = downs if downs is not None else -1
            self.ups = ups if ups is not None else -1
            self.author = author if author is not None else ""
            self.created_at = created_at if created_at is not None else ""
            self.subreddit = subreddit if subreddit is not None else ""

    def __repr__(self) -> str:
        return f"{self.post_id}, {self.title}, {self.text}, {self.downs}, {self.ups}, {self.author}, {self.created_at}, {self.subreddit}"


def stored_to_uploaded(post_id: str):
    # Veritabanı bağlantısını açalım
    conn = sqlite3.connect('request.db')
    c = conn.cursor()

    # stored tablosundan ilgili post_id değerine sahip kaydı seçelim
    c.execute("SELECT * FROM stored WHERE post_id = ?", (post_id,))
    result = c.fetchone()
    if result is None:
        raise Exception(f"Post not found: {post_id}")

    # Post sınıfı ile bir nesne oluşturalım ve uploaded tablosuna ekleyelim
    post = Post(*result)
    c.execute("INSERT INTO uploaded VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (post.post_id, post.title, post.text, post.downs, post.ups, post.author, post.created_at, post.subreddit))

    # stored tablosundan ilgili kaydı silelim
    c.execute("DELETE FROM stored WHERE post_id = ?", (post_id,))

    # Değişiklikleri kaydedelim ve veritabanı bağlantısını kapatalım
    conn.commit()
    conn.close()

# Kullanım örneği
post_ids_to_move = ["13yju7h","13yi65z" ]

for post_id in post_ids_to_move:
    try:
        stored_to_uploaded(post_id)
        print(f"Post with post_id '{post_id}' has been moved from 'stored' to 'uploaded' table.")
    except Exception as e:
        print(e)