+ ref: https://stackoverflow.com/questions/15077424/python-os-path-exists-vs-os-path-isdir
os.path.exists will also return True if there's a regular file with that name.
os.path.isdir will only return True if that path exists and is a directory.
+ ref: https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method
Usage of sys.stdout.flush() method:
Python's standard out is buffered (meaning that it collects some of the data "written" to standard out before it writes it to the terminal). Calling sys.stdout.flush() forces it to "flush" the buffer, meaning that it will write everything in the buffer to the terminal, even if normally it would wait before doing so.
