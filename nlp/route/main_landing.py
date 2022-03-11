# project/route/main_landing.py


#################
#### imports ####
#################
import re
from flask import render_template,request,redirect,url_for, Blueprint,send_from_directory,flash
import ebooklib
from ebooklib import epub
from flask_paginate import Pagination, get_page_parameter,get_page_args
from werkzeug.utils import secure_filename
import os
from bs4 import BeautifulSoup
import nltk
from flask import   jsonify, make_response
from nlp.models.Books import Books
from nlp.models.Search import Search
from nlp import app,db
blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
bp = Blueprint("main_landing", __name__)

@bp.route("/")
#@login_required
def index():
    return render_template('main/index.html')
@bp.route("/books", methods=['GET', 'POST'])
def book_list():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('main/list_book.html')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
            book = Books(filename)
            db.session.add(book)
            db.session.commit()
            books=Books.query.all()
            return render_template('main/list_book.html',books=books)
        return render_template('main/list_book.html')
    else:
        books=Books.query.all()
        return render_template('main/list_book.html',books=books)
@bp.route("/database")
def database():
    search=Search.query.all()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(search)
    pagination_users = get_data(search,offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('main/databse.html',search=pagination_users,pagination=pagination)
@bp.route("/query")
def databasesearch():
    if request.method == "GET":
        result = request.args.get("q")
        search_result=search_(result)
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        total = len(search_result)
        pagination_users = get_data(search_result,offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('main/search_database.html',search=pagination_users,pagination=pagination)
    else:
        return redirect(url_for('main_landing.index'))
@bp.route('/search', methods=("GET", "POST"))
def search():
    if request.method == "GET":
        result = request.args.get("q")
        bookname= request.args.get("b")
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        search_result=get_paragraph(bookname,result)  
        total = len(search_result)
        pagination_users = get_data(search_result,offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
        return render_template('main/search.html',search=pagination_users,pagination=pagination)
    else:
        return redirect(url_for('main_landing.index'))
@bp.route("/push")
def push():
    if request.args:
        search0 =request.args.get("search0")
        search = Search(search0)
        db.session.add(search)
        db.session.commit()
        search1 =request.args.get("search1")
        search = Search(search1)
        db.session.add(search)
        db.session.commit()
        search2 =request.args.get("search2")
        search = Search(search2)
        db.session.add(search)
        db.session.commit()
        search3 =request.args.get("search3")
        search = Search(search3)
        db.session.add(search)
        db.session.commit()
        search4 =request.args.get("search4")
        search = Search(search4)
        db.session.add(search)
        db.session.commit()
        search5 =request.args.get("search5")
        search = Search(search5)
        db.session.add(search)
        db.session.commit()
        search6 =request.args.get("search6")
        search = Search(search6)
        db.session.add(search)
        db.session.commit()
        search7 =request.args.get("search7")
        search = Search(search7)
        db.session.add(search)
        db.session.commit()
        search8 =request.args.get("search8")
        search = Search(search8)
        db.session.add(search)
        db.session.commit()
        search9 =request.args.get("search9")
        search = Search(search9)
        db.session.add(search)
        db.session.commit()
        res = make_response(jsonify({}), 200)
    return res
def get_data(data=[],offset=0, per_page=10):
    return data[offset: offset + per_page]
def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return '' .join(text)
def get_text(epub_path):
    texts = {}
    book = epub.read_epub(epub_path)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
   ## chapters = epub2thtml(epub_path)
    for c in items:
        texts[c.get_name()] = chapter_to_str(c)
    return texts
def get_paragraph(book_name,result):
   
    para=str(get_text(app.config['UPLOADED_PHOTOS_DEST']+book_name))
    Output = []
    tokens = nltk.sent_tokenize(para)
    for t in tokens:
    
        if re.search(result, t, re.IGNORECASE):
            Output.append(re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", t).replace('xa0', " ").replace("'text part0000 html'"," ").replace("'text part0001 html'"," ").replace("'text part0002 html'"," "))
    return Output
def search_(q):
    Output = []
    search=Search.query.all()
    
    for t in search:
        if re.search(q, str(t.result), re.IGNORECASE):
            Output.append(t.result)
    return Output
