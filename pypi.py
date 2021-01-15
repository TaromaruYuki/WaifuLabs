import sys, os, const

if __name__ == "__main__":
    args = sys.argv
    del args[0]

    if sys.platform == "win32":
        if len(args) == 0:
            print("Argument wasnt specified. Valid args are `pypi` and `testpypi`")
        if args[0].lower() == "pypi":
            os.system("python setup.py sdist bdist_wheel")
            os.system(f"twine upload -u {const.USERNAME} -p {const.PASSWORD} dist/*")
        elif args[0].lower() == "testpypi":
            os.system("python setup.py sdist bdist_wheel")
            os.system(f"twine upload -u {const.USERNAME} -p {const.TPASSWORD} dist/*")
        