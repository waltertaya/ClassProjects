from flask import Flask, render_template
app = Flask(__name__)


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
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
