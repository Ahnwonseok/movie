from flask import Blueprint

bp =Blueprint('user',__name__,url_prefix='/user') #url_prefix는 기본 디폴트값

@bp.route('/') #->127.0.0.1:5000 + '/user/' + '/'
def index():
    return 'Welcome to Main Index'