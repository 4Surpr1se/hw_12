from flask import Blueprint, request, render_template

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')
