import sys

jaehwan = sys.stdin.readline()
doctor = sys.stdin.readline()

if jaehwan.find('h') >= doctor.find('h'):
    print("go")
else:
    print("no")