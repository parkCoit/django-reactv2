import os
import platform
myos = platform.system()
root = r"C:\Users\bitcamp\django-react\DjangoServer"


def dir_path(param):
    if (param == "blog") :
        return os.path.join(root, param)
    elif (param == "dlearn") :
        return os.path.join(root, param)
    elif (param == "multiplex") :
        return os.path.join(root, param)
    elif (param == "nlp") :
        return os.path.join(root, param)
    elif (param == "shop"):
        return os.path.join(root, param)
    elif (param == "stroke") :
        return os.path.join(root, param)
    elif (param == "webcrawler") :
        return os.path.join(root, param)

if __name__ == '__main__':
    print(">> "+dir_path("blog"))