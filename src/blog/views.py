from flask import request, render_template
from app import app
from .models import Category, Tag, Post


import random


def page():
    page_str = request.args.get('page')
    try:
        page = int(page_str)
    except (ValueError, TypeError):
        page = 1
    return page


@app.route('/')
@app.route('/page/<int:page_id>')
def index(page_id=1):
    # categories = Category.query.getall()
    categories = Category.query.all()

    # post = Post.query.getpost_perpage(page_id, app.config.PER_PAGE)
    post = Post.query  # filter_by(id=page_id, app.config.PER_PAGE)
    # hot = Post.query.hottest()[:20]
    hot = Post.query.all()[:20]
    # new = Post.query.newpost()[:20]
    new = Post.query.all()[:20]

    # tag = Tag.query.getall()
    tag = Tag.query.all()
    random.shuffle(tag)
    tag = tag[:20]

    # comments = Comment.query.newcomment()[:20]
    # articles = post  # .items
    articles = post.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/index.html',
        categories=categories,
        articles=articles,
        hotarticles=hot,
        newposts=new,
        tags=tag,
        # comments=comments,

        # page_id=page_id,
        # pagination=pagination[page_id - 1:page_id + 10],
        # last_page=pagination[-1],

        nav_current="index"
    )
