import os
import sys

# print(os.environ['PATH'])
# paths = os.environ['PATH'].split(';')

# for path in paths:
#     print(path)

result = os.system('ls -l')
print(result)

if len(sys.argv) < 2:
    print("잘못된 명령행입니다.", file = sys.stderr)