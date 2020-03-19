from flask import blueprint
main = Blueprint('main', __name__)

@main.route('/add_mob', methods=['POST'])
def method_name():
   pass