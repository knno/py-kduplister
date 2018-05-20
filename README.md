Hello, welcome to **KDuplister** v1.0!
### Description:
It detects duplicate files in a directory and subdirs, where the files that are the same (compared with `filecmp.cmp`) are displayed as entries.

### Usage:

```
// Displays help.
$ kdl.py [--help]

// Displays duplicate entries of files in directory.
$ kdl.py directory:

// Displays duplicate entries of current working directory.
$ kdl.py:
```

### Example Output:
```
$ kdl.py "ExampleTest"
```
#### Output:
```
Results:  1  Duplications:

 -  3  Files:

    -  ExampleTest\file1.txt
    -  ExampleTest\file2.txt
    -  ExampleTest\dir1\file1.txt
```