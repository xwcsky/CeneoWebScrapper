from app import app
import os
import 
import requests
from bs4 import BeautifulSoup
from app import utils

from flask import render_template, request, redirect, url_for

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract")
def display_form():
    return render_template("extract.html")

@app.route("/extract", method=("POST"))
def extract():
    product_id = request.form.get("product_id")

    while next_page:
        print(next_page)
        response = requests.get(next_page, headers=headers)
        if response.status_code == 200:
            page_dom = BeautifulSoup(response.text, "html.parser")
            opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
            for opinion in opinions:
                single_opinion = {
                    key: utils.extract_feature(opinion, *value)
                    for key, value in utils.selectors.items()

                }
                all_opinions.append(single_opinion)
            try:
                next_page = "https://www.ceneo.pl"+extract(page_dom, "a.pagination__next", "href")
            except TypeError:
                next_page = None
        else: print(response.status_code)

    return redirect(url_for("product",product_id=product_id))

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/author")
def author():
    return render_template("author.html")

@app.route("/product/<product_id>")
def product_id(product_id):
    return render_template("product.html", product_id=product_id)








