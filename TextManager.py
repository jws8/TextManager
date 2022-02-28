
class TextManager():
    def __init__ (self):
        self.items = []
        self.message = ""
        self.file_location = ""
        print("Initializing TextManager...")
    def get_items(self):
        return self.items
    def input_to_text(self, file_location):
        self.file_location = file_location
        while True:
            item = input("item: ")
            if item == "":
                break #gotta get outta here
            #update file with new item
            self.write_file(item)
            #update items with new item
            self.items.append(item)
    #read_file() splits entire text contents into a list seperated by commas
    # and appends that list to menu_items list
    def read_file(self, file_location = None, symbol = None):
        symbol = ","
        self.file_location = file_location #questionable line 
        with open(self.file_location) as f:
            for line in f:
                self.items.append(line.split(symbol))
    def write_file(self, str):
        with open(self.file_location, "a") as f:
                f.write(str + ",")
#Run Template
#tm = TextManager()
#tm.input_to_text("tasks.txt")

        