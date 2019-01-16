import os, shutil


def main():
    # change to desired directory
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())

    for dir_name, subdir_list, file_list in os.walk('.'):
        print(dir_name)
        print(subdir_list)
        print(file_list)
        extensions_to_folders_dict = {".doc": "dance"}
        for f in file_list:
            extension = os.path.splitext(f)[-1]
            print("I am")
            print(extension)
            key_exists = False
            for key in extensions_to_folders_dict:
                if key == extension:
                    print("i go into")
                    print(extensions_to_folders_dict[extension])
                    print()
                    key_exists = True

            if not key_exists:
                category = input("What category would you like to sort {} files into? ".format(extension))
                print("{} will now go into {}".format(extension, category))
                print()
                extensions_to_folders_dict[extension] = category

            category = extensions_to_folders_dict[extension]
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

            shutil.move(f, category)

main()
