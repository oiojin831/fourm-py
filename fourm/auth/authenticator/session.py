import datetime

from flask import session

form ... import models as m
from base import Authenticator

class SessionAuthenticator(Authenticator):
    def logout(self):
        session.pop('timestamp', None)
        session.pop('user_id', None)

    def get_user(self):
        user_id = session.get('user_id', None)
        timestamp = session.get('timestamp', None)

        if not (user_id and timestamp):
            return None

        # Validate session
        time = datetime.datetime.fromtimestamp(timestamp)
        user = m.User.query.get(user_id)

        # Existence
        if user is None:
            self.logout()
            return None
        # is expired
        chage_date = datetime.datetime(
            *user.password_changed_at.timetuple()[:6]
        )
        if time < change_date:
            self.logout()
            return None
        session.permanent_session_lifetime = 60 * 60 * 24 * 31 
        return user