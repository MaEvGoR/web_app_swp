from flask import Flask, render_template
from redis import Redis
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "keykey"
Bootstrap(app)


class LoginForm(FLaskForm):
	username = StringField('username')
	password = PasswordField('password')


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)