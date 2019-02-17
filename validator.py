import os
import zipfile
from flask import send_file, render_template, Blueprint

from RomUtilityScripts.DataUtils import Validation, GithubFiles


validator_blueprint = Blueprint('validator', __name__, )


@validator_blueprint.route('/validator/missing_models')
def missing_models():
    missing_models = Validation.find_missing_models_git(GithubFiles.get_data_urls())
    return render_template('listview.html', items=missing_models)

@validator_blueprint.route('/validator/missing_icons')
def missing_icons():
    missing_models = Validation.find_missing_icons_git(GithubFiles.get_data_urls())
    return render_template('listview.html', items=missing_models)

@validator_blueprint.route('/validator/unused_icons')
def unused_icons():
    missing_models = Validation.find_unused_icons_git(GithubFiles.get_data_urls())
    return render_template('listview.html', items=missing_models)

@validator_blueprint.route('/validator/unused_models')
def unused_models():
    missing_models = Validation.find_unused_models_git(GithubFiles.get_data_urls())
    return render_template('listview.html', items=missing_models)
