from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.route('/error/404')
def error_404():
    return render_template('error/404.html'), 404
