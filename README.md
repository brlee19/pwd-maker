# pwd-maker
Because lastpass's generate password functionality in its chrome extension has been broken for months (for me anyway), I made this simple CLI tool to create random passwords and copy them to the clipboard.

```
usage: main.py [-h] [--no {lower,upper,num,sym}] [password_length]

positional arguments:
  password_length               password length, default is 10

optional arguments:
  -h, --help                    show this help message and exit
  --no {lower,upper,num,sym}    character sets to exclude
```


To run this directly from Terminal, create a file like the below, somewhere in your $PATH...


```
# Call pwd-maker script

cd /path/to/cloned-repo
pipenv run python main.py "$@"
```

...and make it executable with `chmod +x`
