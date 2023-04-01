from __future__ import print_function
import os
from subprocess import call
from builtins import input

curr_folder = os.path.basename(os.path.normpath(os.getcwd()))

weights_filename = 'pytorch_model.bin'
weights_folder = 'model'
weights_path = f'{weights_folder}/{weights_filename}'
if curr_folder == 'scripts':
    weights_path = f'../{weights_path}'
weights_download_link = 'https://www.dropbox.com/s/q8lax9ary32c7t9/pytorch_model.bin?dl=0#'


MB_FACTOR = float(1<<20)

def prompt():
    while True:
        valid = {
            'y': True,
            'ye': True,
            'yes': True,
            'n': False,
            'no': False,
        }
        choice = input().lower()
        if choice in valid:
            return valid[choice]
        else:
            print('Please respond with \'y\' or \'n\' (or \'yes\' or \'no\')')

download = True
if os.path.exists(weights_path):
    print(
        f'Weight file already exists at {weights_path}. Would you like to redownload it anyway? [y/n]'
    )
    download = prompt()
    already_exists = True
else:
    already_exists = False

if download:
    print(
        f'About to download the pretrained weights file from {weights_download_link}'
    )
    if not already_exists:
        print('The size of the file is roughly 85MB. Continue? [y/n]')
    else:
        os.unlink(weights_path)

    if already_exists or prompt():
        print('Downloading...')

        #urllib.urlretrieve(weights_download_link, weights_path)
        #with open(weights_path,'wb') as f:
        #    f.write(requests.get(weights_download_link).content)

        # downloading using wget due to issues with urlretrieve and requests
        sys_call = f'wget {weights_download_link} -O {os.path.abspath(weights_path)}'
        print(f"Running system call: {sys_call}")
        call(sys_call, shell=True)

        if os.path.getsize(weights_path) / MB_FACTOR < 80:
            raise ValueError(
                f"Download finished, but the resulting file is too small! It\'s only {os.path.getsize(weights_path)} bytes."
            )
        print(f'Downloaded weights to {weights_path}')
else:
    print('Exiting.')
