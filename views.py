#root for website
from flask import Blueprint #blueprint means defining the different URLs/sub directories

views = Blueprint('views', __name__)

#defining first view/root
@views.route('/')  #/ = main page
def home():
  return "<h1>Test</h1>"