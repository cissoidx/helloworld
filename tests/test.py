from os import sys, path
sys.path.append(path.dirname(
                    path.dirname(
                        path.abspath(__file__))))

from helloworld.hello import hello
from helloworld.world.world import print_world

def main():
    hello.print_hello()
    print_world()
    return

if __name__ == "__main__":
    main()
