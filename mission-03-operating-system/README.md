# Mission 3 — Inspect macOS and running programs

## 1. Task / objective

Observe operating-system information, processes, storage, paths and file permissions, then connect them to OS responsibilities.

## 2. Work completed

Opened TextEdit, checked the OS and available space, and selected process rows for the evidence. Moved between the repository and this mission folder and checked the mode on the Mission 2 note.

## 3. Commands / tools used

| Check | Command | What the result showed |
| --- | --- | --- |
| Operating system | `sw_vers -productName` and `sw_vers -productVersion` | The system identified itself as macOS and reported its version. |
| Current account | `whoami` | Returned the account the shell was using. That value was redacted. |
| Storage | `df -h /System/Volumes/Data` | Displayed used and available space for the system's writable Data volume. |
| Processes | `open -a TextEdit`, `pgrep -x TextEdit`, `ps -ax -o pid=,comm=` | Opened the editor, checked it had started and found it in the process snapshot. |
| Navigation | `pwd` and `cd` | The displayed path gained the mission directory name after the change. |
| File permissions | `ls -l` | The owner bits of the practice note were `rw-`. |

## 4. My understanding

A process is an instance of a program while it is running. The PID column gives each listed process its identifier. TextEdit is an app process. The `launchd` process starts and manages system services.

An absolute path begins at `/`. The mission path was `/Users/[redacted]/.../digital-detective-8545/mission-03-operating-system` with the private prefix abbreviated. From the project root, the same folder can be reached with the relative path `mission-03-operating-system`.

| Bit | Meaning | Example |
| --- | --- | --- |
| `r` | Read the file. | View the note in an editor. |
| `w` | Change the file. | Save a new line. |
| `x` | Execute the file, or enter a directory when used on a directory. | Run an executable script. |

The owner could read and edit this note. The dash shows that execute permission was absent.

| Responsibility | Explanation | Example |
| --- | --- | --- |
| Process management | Starts processes and schedules their time on the CPU. | TextEdit runs while Terminal remains open. |
| Memory management | Allocates working memory and protects the memory belonging to each process. | An editor stores its open document in memory. |
| Device management | Coordinates the way apps use connected hardware. | The system delivers keystrokes to the editor. |
| File management | Organizes storage into directories and manages reading and writing. | A note can be opened by filename. |
| User interface / shell | Provides graphical controls and a command-line interface. | A file can be found through Finder or `ls`. |
| Security and permissions | Checks access before allowing operations on resources. | The permission bits control who can change a file. |

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Selected macOS output](system-snapshot.txt), including the storage readings, PID examples, redacted paths and permission bits.

## 8. Commit details

`Observe macOS processes and file permissions`. The checkpoint is listed in [this mission's GitHub history](https://github.com/shamkian0326-creator/digital-detective-8545/commits/main/mission-03-operating-system/README.md).
