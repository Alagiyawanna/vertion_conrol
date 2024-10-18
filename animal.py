import sys

def cat():
    print('Meow')

def dog():
    print('baw')

def default():
    print('hello')

def main():
    if sys.argv[1] == 'cat':
        cat()

    else if sys.argv[2] == 'dog':
        dog()
            
    else:
        default()

if __name__ == '__main__':
    main()


