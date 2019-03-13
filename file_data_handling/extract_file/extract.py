import tarfile
import zipfile
import os
import sys


def extract_tar_gz(data_root, filename, force=False):
    root = os.path.splitext(os.path.splitext(filename)[0])[0]  # tar. gz

    # os.path.exists will also return True if there's a regular file with that name.
    # os.path.isdir will only return True if that path exists and is a directory.
    if os.path.isdir(root) and not force:
        print('Already exist')
    else:
        print('Extracting....')
        tar = tarfile.open(filename)
        sys.stdout.flush()
        tar.extractall(data_root)
        tar.close()

    # store the folder name to return
    data_folders = [
        os.path.join(root, d) for d in sorted(os.listdir(root))
        if os.path.isdir(os.path.join(root, d))]

    return data_folders


def extract_zip(data_root, filename, force=False):
    root = os.path.splitext(filename)[0]

    if os.path.isdir(root) and not force:
        print('Already exist')
    else:
        print("Extracting...")
        zip_ref = zipfile.ZipFile(filename,'r')
        sys.stdout.flush()
        zip_ref.extractall(data_root)
        zip_ref.close()

    data_folders = [
        os.path.join(root, d) for d in sorted(os.listdir(root))
        if os.path.isdir(os.path.join(root, d))]

    return data_folders


def main():
    data_root = '.'
    data_folders = extract_zip(data_root, 'testdownload.zip')
    print(data_folders)


if __name__ == '__main__':
    main()
