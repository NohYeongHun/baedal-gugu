from app import db

class rabbitTimeRanking(db.Model):
    __tablename__ ='rabbitTimeRanking'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    kinds_id = db.Column(db.Integer, db.ForeignKey('rabbitKinds.id'), nullable=False)
    time_id = db.Column(db.Integer, db.ForeignKey('rabbitTime.id'), nullable=False)
    time_rank =db.Column(db.Integer, nullable=True)