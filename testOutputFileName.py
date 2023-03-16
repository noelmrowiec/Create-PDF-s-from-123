import re

INVALID_CHARS_FOR_FILENAME = r"<>:\"\/\\\|?*"

s = ["goodfile$@%@fsdname",'goodfi.pdf', 'bad<file', "badfile>", 'bad:sdfasdfasdf', 'baddd"dd', 'bad//ffff', 'bad\dddd333', 'bad|dd', 'bad?df', 'bad*', 'good.pdf.pdf']

res = re.compile(r"[<>:\"\/\\|?*]+")

for testStr in s:
    if res.search(testStr):
        print("This:"+ testStr +"Character not valid in file name.")
    else:
        print("This:"+ testStr +"File name accepted")