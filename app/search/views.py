from flask import Blueprint
from flask import request, render_template

from app.dao.main_dao import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__)

@search_blueprint.route('/search/')
def search_page():
    query = request.args.get('s').lower()
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts)