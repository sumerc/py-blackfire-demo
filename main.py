from blackfire import apm, profile
from utils import burn_cpu, burn_io, monitor_me

def my_task():
    def do_nothing(): pass

    burn_cpu(0.1)
    burn_io(0.1)

    do_nothing()

    print("my_task ran!")

if __name__ == '__main__':
    my_task()
