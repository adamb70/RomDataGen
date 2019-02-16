import os
import zipfile
from flask import Flask, send_file, render_template

from RomUtilityScripts.WorldGen.VoxelMaterials import GenerateVoxelMatFiles
from .app import rom_data_gen


@rom_data_gen.route('/worldgen/build_material_groups')
def build_material_groups():
    filepath = GenerateVoxelMatFiles.generate_material_groups()
    filename = os.path.basename(filepath)
    return send_file(filepath, mimetype='text/xml', attachment_filename=filename, as_attachment=True)


@rom_data_gen.route('/worldgen/build_voxel_materials')
def build_voxel_materials():
    filepath = GenerateVoxelMatFiles.generate_voxel_materials()
    filename = os.path.basename(filepath)
    return send_file(filepath, mimetype='text/xml', attachment_filename=filename, as_attachment=True)


@rom_data_gen.route('/worldgen/build_mining_definitions')
def build_mining_definitions():
    filepath = GenerateVoxelMatFiles.generate_mining_definitions()
    filename = os.path.basename(filepath)
    return send_file(filepath, mimetype='text/xml', attachment_filename=filename, as_attachment=True)


@rom_data_gen.route('/worldgen/build_all_voxelmat_data')
def build_all_voxelmat_data():
    filepaths = GenerateVoxelMatFiles.generate_voxel_files()

    zipf = zipfile.ZipFile('Output/VoxelFiles.zip', 'w', zipfile.ZIP_DEFLATED)
    for fp in filepaths:
        filename = os.path.basename(fp)
        zipf.write(fp, filename)
    zipf.close()

    return send_file('Output/VoxelFiles.zip', mimetype='zip', attachment_filename='VoxelFiles.zip', as_attachment=True)
