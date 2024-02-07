from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e09cd284c3cf21bac1141edc96627d44'


posts = [
	{
		'author': 'Walter Mitty',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'May 22 2024'
	},
	{
		'author': 'Joe Doe',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted': 'February 3 2024'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")



@app.route("/register", methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))

    return render_template('register.html', title='Login', form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
