## Introduction

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/miscellaneous_python_program/master/find_the_latest_file/example.png" width = "700" height = "400"/>
</p>

Find the latest file from specified directory.

## Notes

```
os.path.getmtime(path)
```

Return the time of last modification of path. The return value is a number giving the number of seconds since the epoch (see the time module). Raise os.error if the file does not exist or is inaccessible.

```
os.path.getctime(path)
```
Return the system’s ctime which, on some systems (like Unix) is the time of the last change, and, on others (like Windows), is the creation time for path. The return value is a number giving the number of seconds since the epoch (see the time module). Raise os.error if the file does not exist or is inaccessible.