
import os, shutil

__author__ = 'Lindsay Ward'


def insert_underscore(string, index):
    return string[:index] + '_' + string[index:]


def main():
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')



            # Option 1: rename file to new name - in place
            #os.rename(filename, final_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp2/' + new_name)

    # Processing subdirectories using os.walk()
    os.chdir('..')
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)

        old_dir = os.getcwd()
        os.chdir(dir_name)

        for filename in file_list:
            final_name = neaten_file_name(filename)
            os.rename(filename, final_name)
            print(final_name)

        os.chdir(old_dir)


def neaten_file_name(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = new_name[0].upper() + new_name[1:]
    intermediate_name = new_name[0]
    for index, character in enumerate(new_name[1:]):
        if character.isupper() and new_name[index - 1].isalpha() and not new_name[index] == "_":
            intermediate_name += "_" + character
        else:
            intermediate_name += character

    # print(intermediate_name)
    final_name = intermediate_name[0]
    for index, character in enumerate(intermediate_name[1:]):
        if character.islower() and intermediate_name[index] == "_":
            character = str(character)
            character = character.upper()
            final_name += character
        else:
            final_name += character
    return final_name


main()
