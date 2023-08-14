import time
def get_timer(func):
    def wrapper():
        st=time.time()
        func()
        et=time.time()
        res=et-st
        print(f'It took {res:.2f} for {func.__name__}to run')
    return wrapper