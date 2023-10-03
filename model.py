class Post:

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