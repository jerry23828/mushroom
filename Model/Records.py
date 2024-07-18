from Database_config import db_init as db
# from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
# from sqlalchemy.orm import mapper
Base = db.Model


class Records(db.Model):
    __tablename__ = 'Records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.username'), nullable=False)
    detection_time = db.Column(db.DateTime, default=datetime.utcnow)
    predicted_class = db.Column(db.String(255), nullable=False)
    confidence = db.Column(db.String(255), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    model_used = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'detection_time': self.detection_time.strftime('%Y-%m-%d %H:%M:%S'),
            'predicted_class': self.predicted_class,
            'confidence': self.confidence,
            'image_path': self.image_path,
            'model_used': self.model_used
        }