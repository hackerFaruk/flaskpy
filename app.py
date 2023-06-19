from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    #girdiler için id oluştur
    id=db.Column(db.Integer, primary_key=True)
    #girdi içeriğini kaydet
    content = db.Column(db.String(200), nullable=False)
    # oluşturulma tarini al
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #return a string when element is created 
    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":  
    app.run(debug=True)