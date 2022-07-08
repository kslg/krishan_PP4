# We can "import os" from the standard Python library
import os
# we need to do is to import the Flask class.
# The capital F indicates that it's a class name, so it's important to use a uppercase F here.
from flask import Flask

app = Flask(__name__)

# We use the route decorator to tell Flask what URL should trigger the function that follows.
# In Python, a decorator starts with the @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.
@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
