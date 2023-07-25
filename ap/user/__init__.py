from flask import Blueprint

user = Blueprint('user', __name__)

import viva.ap.user.views
