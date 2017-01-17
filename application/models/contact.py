# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import EmailType, ChoiceType
from flask import flash

class Contact(Base):
    
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    email = db.Column(EmailType, nullable=False, info={"label": "Email"})
    phone_mobile = db.Column(db.String(50), nullable=False, unique=True)
    phone_work = db.Column(db.String(50))
    phone_fax = db.Column(db.String(50))
    phone_other = db.Column(db.String(50))
    
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    org_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False, info={"label": "Organisation"})
    activities = db.relationship('Activity', backref='contact')
    

    def __repr__(self):
        return str(self.id)
