# File: homework5.py

# ---Homework 1 + 2 Review---

# --Vocabulary Review--
'''
1. Git is the local software that keeps track of files in various repositiores while GitHub is a remote service that stores repositories.
2. The terminal is the software which allows you to interact with the computer and its files using commands while the command line is the text program which you type commands into.
3. Local repositories are stored only on the local computer while remote repositories can be accessed remotely and have to be uploaded and downloaded.
4. Version control is the act of updating repositories by committing files or pulling data from repositories.
5. The staging area is the place where new files which we intend on later committing to a repository are stored.
6. git add places updated files in the staging area.
7. git commit adds files in the staging area to the repository.
8. git push uploads a local repository to a designated remote repository.
9. git status gives a breakdown of the files which have been updated and added.
10. git pull downloads files from a remote repository into a local repository.
11. pwd prints the currently open file path.
12. ls lists the files in the current directory.
13. cd opens the directory named after cd.
14. nano opens the designated file in a software called nano allowing it to be altered.
15. touch can create a new file with the designated name.
16. mv moves a file from one location to another.
17. rm removes the designated file.
18. cat prints the contents of the designated file into the terminal.
'''

# --A Directory Tree--
'''
1. pwd
2. ls
3. cd ../brianna_repo, git pull origin main
4. mv homework.py ../judy_decal/homework
5. cd ../judy_decal/homework
6. cat homework.py
7. git add ., git commit -m "done with hw", git push origin main
8. git pull origin main, then try again
9. cd ../../../Recent
'''

# ---Homework 3 Review---

# --Data Types--
def checkDataType(value):
    return type(value).__name__ # I had to look up how to return just the name of the data type without "class"

# --Conditionals--
def evenOrOdd(int):
    if int%2 == 0:
        return 'Even'
    else:
        return 'Odd'

# ---Loops---
def sum_list(list):
    sum = 0
    for int in list:
        sum += int
    return sum
numbers = [1, 2, 3, 4, 5]

# ---Homework 4 Review---

# --Lists--
def duplicateList(list):
    x = []
    for i in list:
        x.append(i)
        x.append(i)
    return x

# --Debugging--
def square(num):
    return num * num

# ---Running Your Code---

print(duplicateList(['a', 'b', 'c']))