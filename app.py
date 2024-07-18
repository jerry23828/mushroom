from Database_config import app
from flask import request, render_template

# user
from Routes.User import user
from Routes.Classify import image_bp
from Routes.Records import records

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(image_bp, url_prefix="/classify")
app.register_blueprint(records, url_prefix="/records")
app.secret_key = 'doxjjarjeh3die'


@app.route('/')
def home():
    # 获取闪现消息
    message = request.args.get('message')
    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
