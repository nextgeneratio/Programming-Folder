import hashlib
import difflib

def is_similler_file(file1, file2):
    """
    Compare two files to check if they are similar.
    """
    # Read the contents of the files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_contents = f1.readlines()
        file2_contents = f2.readlines()

    # Calculate the hash of the contents
    hash1 = hashlib.md5(''.join(file1_contents).encode()).hexdigest()
    hash2 = hashlib.md5(''.join(file2_contents).encode()).hexdigest()

    # If the hashes are equal, the files are similar
    if hash1 == hash2:
        return True

    # If the hashes are not equal, check for similarity using difflib
    diff = difflib.unified_diff(file1_contents, file2_contents)
    diff_list = list(diff)

    # If there are no differences, the files are similar
    if len(diff_list) == 0:
        return True

    return False

f1 = "D:\Downloades\CV analysis data (cyber Team).pdf"
f2 = "D:\Downloades\cover letter data analysis (cyber team).pdf"
