from urllib.request import *
import os


def download_file(url, data_root, filename, expected_byte, force=False):
    # force flag here for forcing download despite of existing this file (Force = True)
    dest_filename = os.path.join(data_root, filename)
    if force or not os.path.exists(dest_filename):
        print('Attempting to download: ', filename)
        filename, _ = urlretrieve(url, dest_filename)
        print('Finish downloading')
        statinfo = os.stat(dest_filename)
        if statinfo.st_size - expected_byte < 1:
            print('number of byte as expected')
        else:
            print('number of byte not as expected')
    elif os.path.exists(dest_filename):
        print('File existed')
    else:
        raise Exception('Fail to download')

    return dest_filename


def main():
    url = "https://drive.google.com/uc?export=download&id=0B6O77opfHxDDXzJadk1CZGtRZTg"
    data_root = '.'
    dest_filename = download_file(url, data_root, 'testdownload.pdf', 30000)
    print(dest_filename)


if __name__ == '__main__':
    main()
