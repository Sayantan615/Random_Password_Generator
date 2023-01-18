import random
from js import document
# generates a password of length 8


def main():
    def generate_random_password() :
        special_char_array = ['$', '#', '@', '*', '(', '&']
        upper_case1 = chr(random.randint(65, 90))
        upper_case2 = chr(random.randint(65, 90))
        lower_case1 = chr(random.randint(97, 122))
        lower_case2 = chr(random.randint(97, 122))
        digit1 = str(int(random.randint(0, 9)))
        digit2 = str(int(random.randint(0, 9)))
        special_char1 = special_char_array[random.randint(0, len(special_char_array)-1)]
        special_char2 = special_char_array[random.randint(0, len(special_char_array)-1)]

        password = upper_case1 + upper_case2 + lower_case1 + lower_case2 + digit1 + digit2 + special_char1 + special_char2

        def shuffle_(str_):
            template = list(str_)
            random.shuffle(template)
            return ''.join(template)

        return shuffle_(password)

    result = generate_random_password()
    document.getElementById("output").innerText = result

document.getElementById("btn").onClick = main()

# To run it go to your terminal and cd to the project directory and run below command
# python3 -m http.server 80