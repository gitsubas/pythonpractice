def announce(f):
    def wrapper():
        print("The function is about to begin...")
        f()
        print("Done with the function!")
    return wrapper()

@announce
def hello():
    print("Hello, World!")