import sys
import pickle
import os
import time
import pathlib



def clear():
    os.system("cls")


def load(name_of_file):
    with open(os.path.join("logs/" , name_of_file), "rb") as file:
        data = pickle.load(file)

    return data


def dump_data_to_file(data, filename):
    with open(os.path.join("logs/" , filename), "wb+") as file:
        pickle.dump(data, file)


def prompt():
    print("\n>>> ", end="")
    return input()


def instaniate_files():
    if not os.path.isdir("logs"):
        os.mkdir("logs")


def print_files():
    for i in os.listdir("logs"):
        text = Data()
        text.load_data(i)
        text = text.get_data("text")
        abbreviated_content = "[\\n]".join(text.split("\n"))[:50]
        print(f"{i} - {abbreviated_content}...")
        print("")

    print("-" * 40)


class Data():
    def __init__(self):
        self.data_dictionary = {}

    def get_data(self, key):
        return self.data_dictionary.get(key)

    def add_data(self, key, value):
        self.data_dictionary[key] = value
    
    def instantiate_data(self):
        self.add_data("unix_time", str(time.time()))
        self.add_data("human_time", str(time.ctime()))
        self.add_data("text", "")

    def save_data(self, name_of_file):
        dump_data_to_file(self, name_of_file)

    def load_data(self, name_of_file):
        new_data = load(name_of_file)
        self.data_dictionary = new_data.data_dictionary





def main():
    while 1:
        clear()
        print("1 ) Make a log\n")
        print("2 ) Read a log\n")
        print("exit ) Exit\n")

        choice = prompt()
        clear()

        if choice == "exit":
            sys.exit()
        elif choice == "1":
            print("What would you like the name of the log to be?")
            name = prompt()
            while name == "cancel":
                clear()
                print("Invalid name. Please reinput now.")
                name = prompt()

            log = Data()

            log.instantiate_data()
            log.add_data("beginning_time", str(time.time()))
            clear()
            print("What would you like the contents of the log to be?\n::\n" , end="")
            contents = input()
            log.add_data("end_time", str(time.time()))
            contents = contents.split("\\n")
            contents = "\n".join(contents)
            log.add_data("text", contents)
            clear()
            print("Is there any extra data that you would like to add?\n")
            extra_data = input()
            extra_data = extra_data.split(",")
            extra_data = [key_and_pair.split(":") for key_and_pair in extra_data]
            for values in extra_data:
                log.add_data(values[0], values[1])
            log.save_data(name)


            print("Saved data. Log Created.")
            prompt()

        elif choice == "2":
            print_files()
            print(f"\n\nWhat file would you like to read?")
            print("\n -- If you didn't mean to select this option type \"cancel\"",
            "    Not case sensitive", sep="\n")
            file_choice = prompt()
            if file_choice.lower() == "cancel":
                clear()
                main()
            while file_choice not in os.listdir("logs"):
                clear()
                print_files()
                print("\n\nWhat file would you like to read?")
                file_choice = prompt()
                if file_choice.lower() == "cancel":
                    clear()
                    main()

            clear()
            data_of_file = Data()
            data_of_file.load_data(file_choice)
            current_file = f"Current File = {file_choice}"
            print(current_file)
            print(len(current_file) * ".")
            for key in data_of_file.data_dictionary:
                print(f"\"{key}\" : {data_of_file.get_data(key)}")
                print(20 * "-")
            prompt()
            clear()



if __name__ == "__main__":
    instaniate_files()
    print("Logger beta 2.1.2")
    print("Made by Zed")
    prompt()
    main()
