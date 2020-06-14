import json
import os

folder = '_pdfbuild/'
for file in os.listdir(folder):
    if file.endswith(".ipynb"):
        nbfile = folder+file
        print('stripping code from', nbfile)
        with open(nbfile) as json_file:
            data = json.load(json_file)

        for cell in data['cells']:
            if cell['cell_type']=='code':
                if 'tags' in cell['metadata'] and 'hide_input' in cell['metadata']['tags']:
                    cell['source'] = []

        with open(nbfile, 'w') as json_file:
            json.dump(data, json_file)
