# wordednum
A simple command-line program for converting a number to worded form.

This project is similar to [num2words](https://github.com/savoirfairelinux/num2words), by saviorfairelinux. My program is built to be a more portable, simpler alternative to that.

# Installation

To get the program, just clone the git repo
(`git clone https://github.com/mrcatface8885/wordednum`) and cd into the directory it
downloaded in. (`cd wordednum`) That's it! No true installation is required, because the
entire program is just a single Python script.

If you do want to install it, just move the Python script to a bin directory.

Installing locally: `mv wordednum.py ~/.local/bin/wordednum`

Installing system-wide: `mv wordednum.py /usr/bin/wordednum`

# Usage

At the moment, This program is extremely bare-bones. It can't do too many things right now.
I do plan on adding more features and making it more versatile. For now, here's how to use it
in its current state:

The program operates on the command line. to run it, type:

    wordednum <number1> <number2> <number3> ...

The <number> fields are arguments for the numbers to be converted. Multiple numbers can be
converted at once with this method.

The program will output the worded form of each value one after the other on its own line.

Here's an example of an output from this program:

    $ wordednum 69420 1337 5318008
    sixty-nine thousand four hundred twenty
    one thousand three hundred thirty-seven
    five million three hundred eighteen thousand eight
    $

This format means it's output can be easily piped and manipulated by other programs.

Right now, the only optional args for this program is `--version` (shorthand is `-v`), which,
unsuprisingly, makes it output the version number. The program will ignore all other args
given, and terminate after it prints the version to the screen.

    $ wordednum --version
    wordednum, revision 1
    Written by MrCatFace8885
    $

That's it. There's really not much to this program. As I said, I plan to improve it to make it
not suck as much, but for now, this is what I provide. Keep in mind that this program is yet
to support numbers with decimals, so inputs like `3.14159` or `6678.09002` will not work.
Negative values are supported, however.

Thank you for spending your time looking at this GitHub repo. it means a lot to me that
someone cares enough about my little project to continue reading through this readme. <3
