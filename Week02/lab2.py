elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("Elements: ", elements)
#git add . && git commit -m "add elements array" && git push

# def funct_name():
 #   return True

 # def say_greeting(name, message="hi"):
 #   print(f" {message}, {name}")
# say_greeting("Melissa")
 #   say_greeting("Melissa, Hello")

def get_valid_int_input(prompt):
 while True:
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue