from os import sys, path
sys.path.append(path.dirname(
                    path.dirname(
                        path.dirname(
                            path.abspath(__file__)))))

from helloworld.world import world

def main():
    world.print_world()
    return


if __name__ == "__main__":
    main()
