from app import db


class TableMixin(db.Model):
    """Base class that all models should inherit from.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    createdOn = db.Column(db.DateTime, default=db.func.current_timestamp())
    updatedOn = db.Column(db.DateTime, default=db.func.current_timestamp(),
                          onupdate=db.func.current_timestamp())
