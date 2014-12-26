# -*- encoding: utf-8 -*-

import json
import re
from datetime import datetime

from flask import Response, Blueprint, render_template
from instagram.client import InstagramAPI

blueprint = Blueprint('insta', __name__)

access_token='76009.ff7dd43.dfc4f62be5ff42d08e2adb685e40e2ed'
api_at = InstagramAPI(access_token=access_token)
api = InstagramAPI(
        client_id='ff7dd432a30a4d178e1ad94f9baaa745',
        client_secret='acc0a7ce76464ab5913647a63375a6d3'
        )
# user_id = 76009
# recent_media, _next = api.user_recent_media(user_id=user_id, count=20)

# rename this it only applies to media
def to_default(media):
    if media.caption is not None:
        if has_menu(media.caption.text):
            return dict(
                text=None if media.caption is None else splitToHashes(media.caption.text),
                thumbnail=media.images['thumbnail'].url,
                low_resolution=media.images['low_resolution'].url,
                standard_resolution=media.images['standard_resolution'].url
            )

def wrap_json(li):
    return json.dumps(dict(data=li))

def remove_none(li):
    return [x for x in li if x is not None]

def has_menu(caption_text):
    if re.findall(r"^#!|#$|##", caption_text):
        return True
    else:
        return False

def splitToHashes(text):
    list = [splitToHashBang(text), splitToHashHash(text), splitToHashDollar(text)]
    return list

def splitToHashBang(text):
    bang = re.findall(r"#!\w+", text)
    print bang
    return bang

def splitToHashDollar(text):
    dollar = re.findall(r"#$\w+", text)
    return dollar

def splitToHashHash(text):
    hash = re.findall(r"##\w+", text)
    return hash



@blueprint.route('/<username>/menu')
def insta(username):
    user_id=api.user_search(q=username)[0].id
    # print user_id
    recent_media, _next = api.user_recent_media(user_id=user_id, count=20)
    li = remove_none(map(to_default, recent_media))
    while _next:
        recent_media, _next = api.user_recent_media(with_next_url=_next)
        partial_li = remove_none(map(to_default, recent_media))
        li = li + partial_li
       # print li
    return render_template('menu.html', li=li)
