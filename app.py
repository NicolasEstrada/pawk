import sys


def main():

    while True:
        pass


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Closing app ...')
        sys.exit(0)
    except Exception as e:
        print('Unknown exception: {}'.format(e))
        sys.exit(2)
