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



f1 = "file1.pdf"
f2 = "file2.pdf"

f1_hash, f2_hash = hash_file(f1, f2)

if f1_hash == f2_hash:
    print("The files are identical")
else:
    print("The files are different")
    # Read the contents of the files
    with open(f1, 'rb') as file1:
        file1_content = file1.read()
    with open(f2, 'rb') as file2:
        file2_content = file2.read()

    # Calculate the similarity ratio
    similarity_ratio = SequenceMatcher(None, file1_content, file2_content).ratio()

    print(f"Similarity ratio: {similarity_ratio:.2f}")
    if similarity_ratio > 0.8:
        print("The files are similar")
    else:
        print("The files are not similar")
        
