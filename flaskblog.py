from flask import Flask,render_template,request
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9f26b3cb54b5b4da5199c31135907789'

posts = [
    {
        'author' : 'shashank',
        'title'  : 'blogpost1',
        'content': 'first post content',
        'data_posted': 'april 20,2018'
    },
    {
        'author' : 'god',
        'title'  : 'blogpost2',
        'content': 'second post content',
        'data_posted': 'april 21,2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
 return render_template('about.html',title = 'alpha')

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title = 'Register', form = form)


if __name__ == "__main__":
    app.run(debug=True)


