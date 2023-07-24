from flask import Blueprint

user = Blueprint('user', __name__)

import ap.user.views
