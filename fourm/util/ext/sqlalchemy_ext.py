# -*- encoding: utf-8 -*-
import urllib

def engine_url(db_info):
    if isinstance(db_info, basestring):
        return db_info
    # type checking이 안되서 이거하는건가?