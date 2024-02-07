import argparse
parser = argparse.ArgumentParser()
# parser.parse_args()

"""
Running the script without any arguments (python3 prog.py) results in nothing displayed
to stdout.
python3 prog.py --help starts to display the usefulness of the argparse module. We have
done almost nothing, but already we get a nice help message. 
The --help option (-h) is the only option we get for free (i.e no need to specify it). Specifying
anything else results in error. But even then, we do get useful usage message, also for free.
"""

parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)

"""
add_argument() method which is what we use to specify command-line options the program is
willing to accept. In this case, I'v named it echo so that its in line with its function.
Calling the program now requires us to specify an option.
The parse_args() method actually returns some data from the options specified, in the case, echo. 
The variable is some form of 'magic' that argparse performs for free (i.e no need to specify 
which variable that value is stored in) You will also notice that its name matches the 
string argument given to the method, echo.
"""