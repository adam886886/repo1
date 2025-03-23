from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from Project.db import get_db

class User:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password_hash = generate_password_hash(password)
        
    def save_to_db(self):
        db = get_db()
        try:
            db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (self.username, self.password_hash),
            )
            db.commit()
        except db.IntegrityError:
            return f"User {self.username} is already registered."
        return None