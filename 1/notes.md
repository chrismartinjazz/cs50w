# 1 Git

## Key benefits

- Collaborate on files with other, push and merge together.
- Test changes to code on a separate branch and merge later.
- Revert back to old versions.

## Commands

```bash
# Clone in
git clone <url of git repository>

# Working on files, updating and pushing up
git add <filename>
git commit -m "<message>"
git status
git push

# Get the most recent version from GitHub
git pull
```

## Merging

```txt
a = 1
<<<<< HEAD
b = 2                         <- your changes
=====
b = 0                         <- remote changes
>>>>> 57656c636sdoijopij4o... <- conflicting commit's hash
c = 3
d = 4
e = 5
```

To address - remove all the markers, decide on the final version of the file. Remove blank lines, commit the changes.