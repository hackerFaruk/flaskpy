from flask import Flask, render_template, url_for, request , redirect
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
    #tamamlananlar 
    completed =db.Column(db.Integer, default=0) 
    # oluşturulma tarini al
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #return a string when element is created 
    def __repr__(self):
        return '<Task %r>' % self.id


# used to create db at first
with app.app_context():
    # Create the database tables
    db.create_all()


# routeun kabul ettiğği methodlara db veri alma atmayı ekler (index.htmlde mevcut ) 
@app.route('/', methods=['POST','GET'])
def index():
    # task oluşturma
    # requestleri işleme
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

    #ekleme sırasında problem olursa diye hata yakalama 
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    # eğer request Get ise 
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

#task silmek 
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'





    return render_template('index.html')








if __name__ == "__main__":  
    app.run(debug=True)


