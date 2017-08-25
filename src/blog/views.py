from flask import request, render_template
from app import app
from .models import Category, Tag, Post


import random


def page():
    page_str = request.args.get('page_id')
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
    articles = post.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/index.html',
        categories=categories,
        articles=articles,
        hotarticles=hot,
        newposts=new,
        tags=tag,
        # comments=comments,

        nav_current="index"
    )


@app.route('/category/<int:cat_id>')
@app.route('/category/<int:cat_id>/page/<int:page_id>')
def category(cat_id=1, page_id=1):
    # categories = Category.query.getall()
    categories = Category.query.all()

    # hot = Post.query.hottest()[:20]
    hot = Post.query.all()[:20]
    # new = Post.query.newpost()[:20]
    new = Post.query.all()[:20]

    # tag = Tag.query.getall()
    tag = Tag.query.all()
    random.shuffle(tag)
    tag = tag[:20]

    # comments = Comment.query.newcomment()[:20]

    cat = Category.query.get_or_404(cat_id)

    # p = pageby(cat.posts, page_id, per_page, Post.created_at.desc())
    articles = cat.posts.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/category.html',
        id=cat_id,
        cat=cat,
        categories=categories,
        articles=articles,
        hotarticles=hot,
        newpost=new,
        tags=tag,
        # comments=comments,
        page_id=page_id,
    )


@app.route('/article/<int:post_id>')
def article(post_id):
    # categories = Category.query.getall()
    categories = Category.query.all()

    # hot = Post.query.hottest()[:20]
    hot = Post.query.all()[:20]
    # new = Post.query.newpost()[:20]
    new = Post.query.all()[:20]

    # tag = Tag.query.getall()
    tag = Tag.query.all()
    random.shuffle(tag)
    tag = tag[:20]

    # comments = Comment.query.newcomment()[:20]

    # articles = Post.query.getall()
    articles = Post.query.all()
    random.shuffle(articles)
    articles = articles[:5]

    post = Post.query.get_or_404(post_id)
    # form = CommentForm()
    # postcoments = post.comments.all()
    post.views += 1
    # db.session.commit()
    return render_template(
        '/index/post.html',
        post=post,
        articles=articles,
        categories=categories,
        hotarticles=hot,
        newpost=new,
        tags=tag,
        # comments=comments,
        # postcoments=postcoments,
        # form=form
    )
