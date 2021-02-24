# import and use module
"""
import mymath

area = mymath.area(5)
print("area = {}".format(area))
"""
# runtime import
moduleName = "mymath"

math = __import__(moduleName)
area = math.area(5)
print("area = {}".format(area))
print(__name__)
