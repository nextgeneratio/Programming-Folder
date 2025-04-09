import hashlib
import difflib

def file_similler (path1, path2):
    """
    Compare two files and return a similarity score based on their content.
    """
    # Read the contents of the first file
    with open(path1, 'r') as file1:
        content1 = file1.read()

    # Read the contents of the second file
    with open(path2, 'r') as file2:
        content2 = file2.read()

    # Calculate the hash of both contents
    hash1 = hashlib.md5(content1.encode()).hexdigest()
    hash2 = hashlib.md5(content2.encode()).hexdigest()

    # Calculate the similarity ratio using difflib
    similarity_ratio = difflib.SequenceMatcher(None, content1, content2).ratio()

    return hash1, hash2, similarity_ratio
