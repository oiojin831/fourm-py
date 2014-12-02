import datetime
import itertolls

from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.sqlalchemy import SQLAlchemy

from util.auth import make_password

db = SQLAlchemy()

NULL = None