from flask import g, request, render_template
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


def load_sidebar():
    # categories = Category.query.getall()
    g.categories = Category.query.all()

    # hot = Post.query.hottest()[:20]
    g.hotarticles = Post.query.all()[:20]
    # new = Post.query.newpost()[:20]
    g.newpost = Post.query.all()[:20]

    # tag = Tag.query.getall()
    tag = Tag.query.all()
    random.shuffle(tag)
    g.tags = tag[:20]

    # comments = Comment.query.newcomment()[:20]


@app.route('/')
@app.route('/page/<int:page_id>')
def index(page_id=1):
    load_sidebar()

    # post = Post.query.getpost_perpage(page_id, app.config.PER_PAGE)
    post = Post.query  # filter_by(id=page_id, app.config.PER_PAGE)
    articles = post.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/index.html',
        articles=articles,
        nav_current="index"
    )


@app.route('/category/<int:cat_id>')
@app.route('/category/<int:cat_id>/page/<int:page_id>')
def category(cat_id, page_id=1):
    load_sidebar()

    cat = Category.query.get_or_404(cat_id)

    # p = pageby(cat.posts, page_id, per_page, Post.created_at.desc())
    articles = cat.posts.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/category.html',
        id=cat_id,
        cat=cat,
        articles=articles,
    )


@app.route('/tag/<int:tag_id>')
@app.route('/tag/<int:tag_id>/page/<int:page_id>')
def tag(tag_id, page_id=1):
    load_sidebar()

    tagall = Tag.query.get_or_404(tag_id)
    name = tagall.name
    # p = Post.query.search_tag(name)
    p = Post.query
    articles = p.paginate(page(), app.config.get('RECORDS_ON_PAGE'))

    return render_template(
        '/index/tag.html',
        id=tag_id,
        tagall=tagall,
        articles=articles,
    )


@app.route('/article/<int:post_id>')
def article(post_id):
    load_sidebar()

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
        # postcoments=postcoments,
        # form=form
    )
