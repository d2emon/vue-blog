from flask import render_template
from app import app, cache


@app.errorhandler(404)
@cache.cached()
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.route('/error/404')
@cache.cached()
def error_404():
    return render_template('error/404.html'), 404
