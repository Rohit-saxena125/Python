# Hello Ross Taylor! You just delved into python.
def _full_name(first_name, last_name):
    s= 'Hello {0} {1}! You just delved into python'.format(first_name,last_name)
    return s
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(_full_name(first_name , last_name))