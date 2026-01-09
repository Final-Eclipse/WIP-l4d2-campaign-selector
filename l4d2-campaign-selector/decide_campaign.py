import json

# Get current mod
# If yes is clicked, write that mod to a file for liked mods
# If no is clicked, write that mod to a file for disliked mods
# If maybe is clicked, write that mod to a file for maybe mods
class ModDecider():
    def __init__(self):  
        self.liked_mods = []
        self.disliked_mods = []
        self.all_mods = self.get_all_mods()

        self.current_liked_mods = self.get_liked_mods()
        self.current_disliked_mods = self.get_disliked_mods()

    def get_all_mods(self):
        """Returns all mods scraped from the Steam Workshop in JSON format."""
        with open("left_4_dead_2_scraper/l4d2_mods.json", "r") as file:
            file_contents = file.read()
            all_mods = json.loads(file_contents)

        return all_mods
    
    def yes_button_pressed(self):
        # Add mod to liked_mods
        # Add mod to liked mods text file
        # Do the same for no button
        # pass
        self.liked_mods.append(self.current_mod)
    
    def no_button_pressed(self):
        pass
        self.disliked_mods.append(self.current_mod)

    def set_mod_likeness(self):
        for mod_title, mod_details in self.all_mods.items():
            if mod_title in self.current_liked_mods or mod_title in self.current_disliked_mods:
                continue

            print(mod_title)
            decision = input("Type like or dislike. ").lower().strip()

            if decision == "like":
                self.liked_mods.append(mod_title)
            elif decision == "dislike":
                self.disliked_mods.append(mod_title)
            elif decision == "quit":
                break
    
    def add_liked_mods_to_file(self):
        with open("l4d2_campaign_selector/l4d2_liked_mods.txt", "r+") as file:
            file_contents = file.read()
            print(file_contents)
            # file.write(str(self.liked_mods))

    def add_disliked_mods_to_file(self):
        with open("l4d2_campaign_selector/l4d2_disliked_mods.txt", "r+") as file:
            file_contents = file.read()
            file.write(str(self.disliked_mods))

    # When adding new mods to file do not overwrite, append
    # Get file contents
    # file.write(file_contents + new_contents)
    def get_liked_mods(self):
        with open("l4d2_campaign_selector/l4d2_liked_mods.txt", "r") as file:
            file_contents = file.read()

        file_contents = file_contents.replace("[", "")
        file_contents = file_contents.replace("]", "")
        file_contents = file_contents.replace("'", "")
        file_contents = file_contents.split(", ")

        return file_contents

    def get_disliked_mods(self):
        with open("l4d2_campaign_selector/l4d2_disliked_mods.txt", "r") as file:
            file_contents = file.read()

        file_contents = file_contents.replace("[", "")
        file_contents = file_contents.replace("]", "")
        file_contents = file_contents.replace("'", "")
        file_contents = file_contents.split(", ")

        return file_contents
    
    def get_current_mod(self):
        # Rereads the files to get the latest version
        self.current_liked_mods = self.get_liked_mods()
        self.current_disliked_mods = self.get_disliked_mods()

        for mod_title in self.all_mods:
            if mod_title not in self.current_liked_mods and mod_title not in self.current_disliked_mods:
                self.current_mod = mod_title
                return self.current_mod
        
    # def update_current_mod(self):
    
if __name__ == "__main__":
    x = ModDecider()
    # x.set_mod_likeness()
    x.get_current_mod()
    x.yes_button_pressed()
    x.add_liked_mods_to_file()
    x.add_disliked_mods_to_file()
    
    print(x.get_current_mod())
    # x.set_mod_likeness()
    

    # print(x.get_liked_mods())
    # print(x.get_disliked_mods())

    # print()
    # print(x.liked_mods)
    # print(x.disliked_mods)



