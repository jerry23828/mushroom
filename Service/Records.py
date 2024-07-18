from Model.User import User
from Model.Records import Records
from flask import jsonify
from Database_config import db_init as db


class Record_operation():
    def __init__(self):
        super().__init__()

    def get_records(self, username):
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'code': -1, 'message': '用户不存在', 'data': {}})

        records = Records.query.filter_by(user_id=username).all()
        records_list = [record.to_dict() for record in records]

        return jsonify({'code': 0, 'message': '查询成功', 'data': records_list})