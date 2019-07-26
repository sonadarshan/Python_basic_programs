from pathlib import Path
print("1.Search for all the files with extensions(*,*.txt,*.py)\n2.Create a directory\n3.Remove direcetory")
try:
    n=int(input('Enter your choice : '))
except ValueError:
    print("Enter the number properly")
    exit(0)

if n == 1:
    p = Path()
    inp = input("Enter the extension : ")
    for file in p.glob(inp):
        print(file)
elif n == 2:
    inp = input("Enter the name of new directory")
    p1 = Path(inp)
    if p1.exists():
        print('Directory already exists')
    else:
        p1.mkdir()
        print("Directory created")
else:
    inp = input("Enter the name of directory")
    p = Path(inp)
    p.rmdir()
    print('Directory removed')
