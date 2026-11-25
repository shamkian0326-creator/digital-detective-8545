# Mission 2 — Practise Terminal and file operations

## 1. Task / objective

Navigate the project, create and edit practice files, and use listing options, a pipe and a package manager.

## 2. Work completed

Created and listed an empty file, copied it and renamed the copy. Then wrote one line to the original, appended a second, and verified that the final backup contained both lines. Compared listings and inspected selected entries from the installed Homebrew inventory.

## 3. Commands / tools used

| Operation | Command | Purpose and observation |
| --- | --- | --- |
| Show current folder | `pwd` | Printed the absolute path ending in the mission folder. |
| List entries | `ls` | Showed the visible names in the practice directory. |
| List details | `ls -l` | Displayed file attributes. Both first files showed a size of zero. |
| Move to parent | `cd ..` | Moved from the mission folder to the project root. |
| Make a folder | `mkdir terminal-practice` | Created the folder containing the practice files. |
| Make an empty file | `touch notes.txt` | Created a file with no text. |
| Copy a file | `cp notes.txt temp.txt` | Created a new file with the same contents. |
| Rename a file | `mv temp.txt empty-backup.txt` | Gave the copy its final name. |
| Read a file | `cat notes.txt` | Initially printed nothing. After editing, it displayed two lines. |

`printf` supplied the text. `cmp` confirmed the second backup matched the edited original. `brew --version` showed the installed Homebrew version and `brew list --formula` returned the installed formulae, including Git and Python.

## 4. My understanding

- `>` replaces a file's contents when used to write new text. `>>` writes at the end, keeping the first line.
- `cp` leaves the original in place. `mv` changes where the file is found or what it is called.
- `pwd` shows the directory the shell uses to resolve relative paths. A listing shows the filenames available there.
- Plain `ls` omitted `.listing-demo`. In `ls -lah`, `-l` added details, `-a` revealed hidden entries and `-h` wrote sizes in readable units.
- In `ls -l | head -n 3`, the pipe sends the listing to `head`, which keeps just the first three lines.
- A package manager records what was installed and which other packages it requires. It gives users consistent commands for finding, installing, updating and removing packages.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Redacted Terminal output](terminal-output.txt), [two-line note](terminal-practice/notes.txt) and [the renamed backup](terminal-practice/notes-backup.txt).

## 8. Commit details

`Demonstrate file operations and Terminal options`. The checkpoint is listed in [this mission's GitHub history](https://github.com/shamkian0326-creator/digital-detective-8545/commits/main/mission-02-terminal/README.md).
