

class Greeter:
    name = ""
    def my_name(self, name):
        self.name = name

    def greet(self):
        if self.name is not "":
            greet_message = "Hello " + self.name
        else:
            greet_message = "Please provide a name"
        return greet_message

