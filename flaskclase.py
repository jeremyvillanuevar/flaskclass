from sqlalchemy import MetaData
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)

#db.init_app(app)


migrate = Migrate(app,db,render_as_batch=True)




class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True, name='id')
    username=db.Column(db.String(80),unique=True,nullable=False, name='username')
    email=db.Column(db.String(120),unique=True,nullable=False)
    name=db.Column(db.String(120),nullable=False)
    password=db.Column(db.String(120),nullable=False)
    posts=db.relationship('post',backref='author',lazy=True)
    def __repr__(self):
        #return '<User %r>' % self.content
        return "User('%s','%s','%s','%s')" % (self.username, self.email,self.name,self.posts)

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True, name='id')
    content=db.Column(db.String(300),nullable=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False, name='user_id')
    post_img=db.Column(db.String(300),nullable=True)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  
    def __repr__(self):
        return '<Post %r>' % self.content
    
with app.app_context():
    db.create_all()
    
#@app.route('/',methods=["POST"])
#def index():
    #return app.url_for('give_greeting', name='Mark')



@app.route('/helloworld')
def hello_world():
    return "Hello world"

@app.route('/routed')
def hello_world_otraruta():
    return "Hello world de otra ruta"

@app.route('/temp')
def hello_world_temp():
    lista ={1,2,3,4,5}
    return render_template("ejemplo.html",nombre="Jeremy",lista=lista)

@app.route("/hello/<username>")
def hello_user(username):
    print(app.url_for('hello_world_otraruta', name='Mark'))
    return "Hello {} !".format(username)

@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello, {0}!'.format(name)

@app.route('/obtener_lista')
def obtener_lista():
    lista = [
        {'num':1, 'visible':True},
        {"num":2, "visible":True},
        {"num":3, "visible":False}
    ]
    return jsonify(lista)

@app.route('/login')
def login():
    return render_template('login.html')


    
@app.route('/')
def index():
    # Ejemplo de posts (puedes reemplazar esto con lógica de base de datos)
    posts = [
        {'user': 'Usuario1', 'content': '¡Hola, mundo!', 'img': 'https://external.faqp4-2.fna.fbcdn.net/emg1/v/t13/13546349427847062928?url=https%3A%2F%2Felcomercio.pe%2Fresizer%2FqpkOmW8Ky06GRF7cAZiXUFZwL58%3D%2F980x528%2Fsmart%2Ffilters%3Aformat%28jpeg%29%3Aquality%2875%29%2Fcloudfront-us-east-1.images.arcpublishing.com%2Felcomercio%2FXSIPNAL7BRF73KSOUAA3ESJDQI.jpg&fb_obo=1&utld=elcomercio.pe&stp=c0.5000x0.5000f_dst-jpg_flffffff_p500x261_q75&_nc_eui2=AeEWrbq3tSsM3AVla19diAMCIt8kIX9gEXgi3yQhf2AReK1Pi-SILm7IiD3996SCKQnhOlkeI3FyCSL3bPBhqBMK&ccb=13-1&oh=06_AbH_wnP4e3Lig7H_dXLbp1H8T7f54Orb8uSUwqc2s9tGuQ&oe=65924F93&_nc_sid=c63717'},
        {'user': 'Usuario2', 'content': 'Bienvenido a mi red social.'},
        {'user': 'Usuario3', 'content': '¡Esto es una prueba!'},
    ]

    post = []
    all_users=User.query.all()
    for user in all_users:
        all_user_post = user.posts
        for post in user.posts:
            print(post.date_posted)
            posts.append({'user':user.username,'content':post.content,'img':post.post_img})
    #all_posts=Post.query.all()
    print(posts)
    posts=sorted(posts,key=lambda x: x['date_posted'])
    #print(all_users)
    return render_template('index.html', posts=posts)


if __name__=="__main__":
    migrate.db.create_all()    
    app.run(debug=True)