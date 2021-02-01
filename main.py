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
pathlib.join("")

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
        print(f"{i} - {text[0:50]}...")
        print("")

    print("-" * 40)


class Data():
    def __init__(self):
        self.data_dictionary = {}

    def get_data(self, key):
        try:
            return self.data_dictionary[key]
        except:
            return None

    def add_data(self, key, value):
        try:
            self.data_dictionary[key] = value
        except: 
            try:
                self.data_dictionary[key] = None
            except:
                try:
                    self.data_dictionary[value] = key
                except:
                    try:
                        self.data_dictionary[value] = None
                    except:
                        pass
    
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
    instaniate_files()
    print("Logger beta 2.1.0")
    print("Made by TLT_Bruh")

    prompt()

    while 1:
        clear()
        print("1 ) Make a log")
        print("2 ) Read a log")
        print("exit ) Exit")

        choice = prompt()
        clear()

        if choice == "exit":
            sys.exit()
        elif choice == "1":
            print("What would you like the name of the log to be?")
            name = prompt()
            log = Data()

            log.instantiate_data()
            log.add_data("beginning_time", str(time.time()))
            clear()
            print("What would you like the contents of the log to be?")
            contents = prompt()
            log.add_data("end_time", str(time.time()))

            log.add_data("text", contents)
            log.save_data(name)

            print("Saved data. Log Created.")
            prompt()

        elif choice == "2":
            print_files()
            print("\n\nWhat file would you like to read?")
            file_choice = prompt()
            while file_choice not in os.listdir("logs"):
                clear()
                print_files()
                print("\n\nWhat file would you like to read?")
                file_choice = prompt()

            clear()
            data_of_file = Data()
            data_of_file.load_data(file_choice)
            print(f"Current File = {file_choice}")
            print(len(f"Current File = {file_choice}") * ".")
            for key in data_of_file.data_dictionary:
                print(f"\"{key}\" : {data_of_file.get_data(key)}")
                print(20 * "-")
            prompt()
            clear()



if __name__ == "__main__":
    main()