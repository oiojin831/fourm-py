# --*-- encoding: utf-8 -*-
"""

"""
import abc

class Authenticator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_user(self)

        raise NotImplementedError

    @abc.abstractmethod
    def logout(self)

        raise NotImplementedError
