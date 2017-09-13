# Practical Vim
> Drew Neil

## Sentences

To recap, our options are as follows.

## Preliminary
- The <C-p> notation is equivalent to Ctrl-p
- <CR> press ESC
- <S-TAP> press shift and tab
- cw command deletes to the end of the current word and switches to Insert mode
- the $ symbol indicates that a command line is to be executed in an external shell, whereas the : prompt indicates that the command line is to be executed internally from Command-Line mode
- ? Use Command-Line mode to perform a backward search
- = Use Command-Line mode to evaluate a Vim script expression
- in MacVim you can interact with the system clipboard using Cmd-X and Cmd-V, save a document with Cmd-S, or close a window with Cmd-W

## Chapter 1

###  Normal models
#### dot command
The dot command lets us repeat the last change. It is the most powerful and versatile command in Vim. a change is created each time we dip into Insert mode (From the moment we enter Insert mode (by pressing i, for example) until we return to Normal mode (by pressing <Esc>),)

#### u command
undo the changes

#### >G command
increases the indentation from the current line until the end of the file.

#### a/A
While the a command appends after the current cursor position, the A command appends at the end of the current line.

#### s
The s command compounds two steps into one: it deletes the character under the cursor and then enters Insert mode.

#### f
The f{char} command tells Vim to look ahead for the next occurrence of the specified character and then move the cursor directly to it if a match is found

#### ;/,
the ; command will repeat the last search that the f command performed.
, command which repeats the last f{char} search in the reverse direction.

#### *
place our cursor on the word and hit the * key, equally to search the word at the cursor.

#### cw
the cw command deletes to the end of the word and then drops us into Insert mode

## Chapter 2

###  Normal models

#### daw
The daw command is easily remembered by the mnemonic delete a word

#### ctrl-a/ctrl-x
The <C-a> and <C-x> commands perform addition and subtraction on numbers. running 10<C-a> would modify it to read 15. So if the cursor is not already positioned
on a number, then the <C-a> command will look ahead for a digit on the current
line.

#### d{motion}/c{motion}/y{motion}
dl delete a character, dap delete a paragraph. Operator:
c Change
d Delete
y Yank into register
g~ Swap case
gu Make lowercase
gU Make uppercase
\> Shift right
< Shift left
= Autoindent
! Filter {motion} lines through an external program

## Chapter 3

### Insert mode

#### ctrl-h/ctrl-w/ctrl-u
<C-h> Delete back one character (backspace)
<C-w> Delete back one word
<C-u> Delete back to start of line

#### ctrl-o/<ESC>/ctrl-[
<Esc> Switch to Normal mode
<C-[> Switch to Normal mode
<C-o> Switch to Insert Normal mode

#### Insert Normal mode
We can fire off a single command, after which we’ll be returned to
Insert mode immediately. From Insert mode, we can switch to Insert Normal
mode by pressing <C-o>

### Normal mode

#### zz
The zz command redraws
the screen with the current line in the middle of the window, which allows
us to read half a screen above and below the line we’re working on.
