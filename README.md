# The Space Trail

![Python 3.14+](https://img.shields.io/badge/Python-3.14%2B-blue) ![CEJBSBDSL](https://img.shields.io/badge/CEJBSBDSL-0.5.0-green)


![Terminal image with title in big ASCII art letters, "The space Trail"](images/TheSpaceTrail.png)

# How to play

Run the command `pip install rich` in your terminal.

### Cross Platform
Run `python -m src_tst`.

To bypass the intro sequence run `python -m src_tst.ignore`.

# CEJBSBDSL
CEJBSBDSL (Pronounced "See-Jizz-Bull") is a mistake. 
May the Code Efficent JSON-Based Story-Boarding Domain Specific language serve as a harrowing example for any aspiring programmer. Never make new infrastructure when it was made for you and can meet your needs.
We *already* had a lightweight scripting language to write our game in; Python! We should have just used Python and added some functions.
Instead, we chose to invent a DSL specifically for this game, we spent so much time making this language, all encompasing, expandable and flexible when we could have just made a few functions in Python.


We were so pre-occupied with whether or not we could, we never stopped to think if we should.

If you want to see the language spec look at [SDLC.md](SDLC.md).

If you want to look at some beatiful syntax sugar take a look at [/src_tst/storyline.json](/src_tst/storyline.json)

The entire CEJBSBDSL language can be accessed in [CEJBSBDSL.py](/CEJBSBDSL.py).
```
python CEJBSBDSL.py --file script.json --entry-point "run"
```

Example:
```
> python CEJBSBDSL.py --file .\src_tst\demo.json --entry-point "demo"
Hello, World!
```


# Problems/Questions

## I'm having trouble with rich compatibility
We used `rich==14.3.3`, so install the version we used with `pip install rich==14.3.3`. We also require a minimum vertical terminal size of 20, and horizontal size of 110. You can ignore this limitation by running `python -m src_tst.ignore`.

Help:
```
> python CEJBSBDSL.py --help
usage: CEJBSBDSL.py [-h] [-f FILE] [-e ENTRY_POINT] [-s SEED] [-v]

options:
  -h, --help            show this help message and exit
  -f, --file FILE       path to script
  -e, --entry-point ENTRY_POINT
                        program entry point (default: "init")
  -s, --seed SEED       random seed (default: 42)
  -v, --version         show program's version number and exit
```


## Can I contribute?
Go right ahead! I would not wish refactoring this code on my worst enemy but esoteric programming languages attract a certain kind of person.
We coded the parser to be quite lightweight, so you can make your own projects in CEJBSBDSL although, it is a terrible language.

