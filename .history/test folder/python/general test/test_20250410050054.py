import hashlib
from difflib import SequenceMatcher

def hash_file (f1_path, f2_path):
    """This function returns the SHA-1 hash of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(f1_path,'rb') as file1:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file1.read(1024)
            h.update(chunk)

    # make a hash object
    h2 = hashlib.sha1()

    # open file for reading in binary mode
    with open(f2_path,'rb') as file2:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file2.read(1024)
            h2.update(chunk)

    return h.hexdigest(), h2.hexdigest()



f1 = "fil"
f2 = "Downloades\cover letter data analysis (cyber team).pdf"

print(hash_file(f1, f2))
