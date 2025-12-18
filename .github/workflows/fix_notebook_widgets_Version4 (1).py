import glob
import nbformat

def fix_widgets_metadata(ipynb_path):
    nb = nbformat.read(ipynb_path, as_version=nbformat.NO_CONVERT)
    if 'widgets' in nb.metadata:
        print(f"Removing widgets from {ipynb_path}")
        del nb.metadata['widgets']
        nbformat.write(nb, ipynb_path)
        return True
    return False

fixed = False
for nb in glob.glob('**/*.ipynb', recursive=True):
    if fix_widgets_metadata(nb):
        fixed = True
if fixed:
    print('Some notebooks were fixed. Please commit the changes.')
else:
    print('No notebook widgets metadata needed fixing.')