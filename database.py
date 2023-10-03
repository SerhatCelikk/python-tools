import sqlite3
from typing import List
import datetime
import os

from model import Post

DATA_PATH = os.path.join(os.getcwd())
DATABASE_PATH = os.path.join(DATA_PATH, "request.db")

TABLES = [ "stored", "uploaded" ]

conn = sqlite3.connect(DATABASE_PATH)
c = conn.cursor()

def create_table():

    for table_name in TABLES:

        c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                post_id text,
                title text,
                text text,
                downs integer,
                ups integer,
                author text,
                created_at text,
                subreddit text
                )""")


create_table()

def insert_post(post: Post, database: str):

    if database not in TABLES: raise Exception(f"Database not found : {database}")

    with conn:
        c.execute(f'INSERT INTO {database}(post_id, title, text, downs, ups, author, created_at, subreddit) VALUES (:post_id, :title, :text, :downs, :ups, :author, :created_at, :subreddit)', {'post_id': post.post_id, 'title': post.title, 'text':post.text, 'downs':post.downs, 'ups':post.ups, 'author':post.author, 'created_at':post.created_at, 'subreddit':post.subreddit})

def get_all_post(database: str):

    if database not in TABLES: raise Exception(f"Database not found : {database}")

    with conn:
        c.execute(f'SELECT * FROM {database}')
        results = c.fetchall()
        posts = []
        for result in results:
            posts.append(Post(*result))
        return posts
    
def check_post_exists(post_id: str) -> bool:
    with conn:
        c.execute("SELECT EXISTS(SELECT 1 FROM stored WHERE post_id = ?)", (post_id,))
        result_stored = c.fetchone()
        if result_stored[0] == 1:
            return True

        c.execute("SELECT EXISTS(SELECT 1 FROM uploaded WHERE post_id = ?)", (post_id,))
        result_uploaded = c.fetchone()
        return result_uploaded[0] == 1
    
def check_post_exists_by_text(text: str) -> bool:
    with conn:
        c.execute("SELECT EXISTS(SELECT 1 FROM stored WHERE text = ?)", (text,))
        result_stored = c.fetchone()
        if result_stored[0] == 1:
            return True

        c.execute("SELECT EXISTS(SELECT 1 FROM uploaded WHERE text = ?)", (text,))
        result_uploaded = c.fetchone()
        return result_uploaded[0] == 1
    
def update_post_text_by_id(post_id: str, text: str, database: str):
    if database not in TABLES: raise Exception(f"Database not found : {database}")

    with conn:
        c.execute(f'UPDATE {database} SET text = :text WHERE post_id = :post_id', {'text': text, 'post_id': post_id})

def get_desc_posts(database: str, limit: int = 10) -> List[Post]:
    if database not in TABLES: raise Exception(f"Database not found : {database}")

    with conn:
        c.execute(f'SELECT * FROM {database} ORDER BY created_at DESC LIMIT {limit}')
        results = c.fetchall()
        posts = []
        for result in results:
            posts.append(Post(*result))
        return posts
    
def stored_to_uploaded(post_id: str):
    with conn:
        c.execute("SELECT * FROM stored WHERE post_id = ?", (post_id,))
        result = c.fetchone()
        if result is None:
            raise Exception(f"Post not found : {post_id}")
        post = Post(*result)
        insert_post(post, "uploaded")
        c.execute("DELETE FROM stored WHERE post_id = ?", (post_id,))