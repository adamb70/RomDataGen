import os
import sys
import glob
import zipfile
from flask import Flask, send_file, render_template

from RomUtilityScripts.RomUtilityScriptsBase import settings
from RomUtilityScripts.Alchemy.GenerateFiles import generate_alchemy_files
from worldgen import worldgen_blueprint
from validator import validator_blueprint


proj_path = os.path.abspath(os.path.dirname(__file__))
settings.KEYFILE = os.path.join(proj_path, 'Mistvalin-b3c187e87518.json')
settings.KEYFILE_TEXT = os.environ.get('KEYFILE')
settings.GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

os.makedirs('./Output', exist_ok=True)

rom_data_gen = Flask(__name__)
rom_data_gen.register_blueprint(worldgen_blueprint)
rom_data_gen.register_blueprint(validator_blueprint)


@rom_data_gen.route('/')
def hello_world():
    return render_template('main.html')


@rom_data_gen.route('/validator')
def validation_view():
    return render_template('validator.html')


@rom_data_gen.route('/alchemy/build_all_alchemy_data/<generate_ground>')
def build_all_alchemy_data(generate_ground):
    if generate_ground.lower == 'true':
        generate_alchemy_files(generate_ground_items=True)
    else:
        generate_alchemy_files(generate_ground_items=False)

    filepaths = glob.glob('./Output/Alchemy/*.*')

    zipf = zipfile.ZipFile('Output/AlchemyData.zip', 'w', zipfile.ZIP_DEFLATED)
    for fp in filepaths:
        filename = os.path.basename(fp)
        zipf.write(fp, filename)
    zipf.close()

    return send_file('Output/AlchemyData.zip', mimetype='zip', attachment_filename='AlchemyData.zip', as_attachment=True)








@rom_data_gen.route('/worldgen/test')
def test():
    filepath = 'Output/VoxelMaterials.sbc'
    filename = os.path.basename(filepath)
    return send_file(filepath, mimetype='text/xml', attachment_filename=filename, as_attachment=True)


if __name__ == '__main__':
    rom_data_gen.run()
