# import sys
#
# print(sys.path)
#
# import sys
# sys.path.append("D:\\git\\book-code\\python_base\\project2\\module")
# from calculator import add

# print(add(2, 3))

import sys
from os.path import dirname, abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path + "\\module")

from calculator import add


print(add(2, 3))

