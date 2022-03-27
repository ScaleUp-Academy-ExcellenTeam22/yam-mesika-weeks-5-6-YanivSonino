import os


def find_deep(path):
    file = os.listdir(path)
    files_with_deep = []
    for name in file:
        if str(name).startswith("deep"):
            files_with_deep.append(name)
    return files_with_deep


print(find_deep('C:\\Users\\USER\\gitHub\\Notebooks1\\week05\\images'))


