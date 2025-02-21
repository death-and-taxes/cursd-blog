#optional is a typing hint from python
from typing import Optional
#sqlalchemy module includes general purpose db functions  and classes
import sqlalchemy as sa 
#sqlalchemy.orm provides support for using models
import sqlalchemy.orm as so
from app import db

#class that represents users stored in database
#inherits from db.Model, the base class for all models from Flask-SQLAlchemy
class User(db.Model):
    """
    There are 4 fields that are set as class variables: id, username, email, password_hash
    each is assigned a type using Python's 'type hints' ex so.Mapped[int]
    Those type declarations define the type of column, and make the values required or 'non-nullable'
    if you want a column to be optional, you use the 'Optional' helper, see password hash
    """
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    emai: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))


#this method tells pytohn how to print objcts of this class
    def __repr__(self):
        return '<User {}'.format(self.username)