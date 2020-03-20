from os import sys, path
sys.path.append(path.dirname(
                    path.dirname(
                        path.dirname(
                            path.abspath(__file__)))))

from helloworld.hello import hello

def main():
    hello.print_hello()
    return


if __name__ == "__main__":
    main()
