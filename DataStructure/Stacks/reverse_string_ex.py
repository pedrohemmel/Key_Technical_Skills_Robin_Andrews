import stack

def reverse_string(my_string):
    reversed_string = ""

    s = Stack()

    for char in my_string:
        s.push(char)

    while not s.is_empty():
        reversed_string += s.pop()

    return reversed_string

if __name__ == "__main__":
    print(reverse_string("pedro"))