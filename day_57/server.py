from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    year = today.year
    return render_template("index.html", num=random_number, year=year)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_blogs = response.json()
    blog_no = num
    print(blog_no)
    return render_template("blog.html", posts=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)

