from flask import Blueprint, request, redirect, url_for, session, render_template, flash, jsonify
from Service.Records import Record_operation


records = Blueprint('records', __name__)


@records.route('/records', methods=['GET'])
def get_records():
    username = session.get('username')
    if not username:
        return redirect(url_for('user.login', message='请先登录'))

    r = Record_operation()
    result = r.get_records(username)
    return render_template('records.html', records=result.json['data'])