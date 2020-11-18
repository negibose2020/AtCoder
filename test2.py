import os
from contextlib import redirect_stdout

def main():
    print(0)

if __name__=='__name__':
    main()

# with redirect_stdout(open(os.devnull,'w')):
main()