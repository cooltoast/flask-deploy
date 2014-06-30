from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/method/')
def method():
    return render_template('method.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('testtemplate.html', name=name) 

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
   	return 'post made' 
    else:
	return 'post not made'

if __name__ == '__main__':
    app.run()
