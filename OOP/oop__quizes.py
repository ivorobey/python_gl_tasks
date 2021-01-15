# class A:
#     attr0 = 1
#     attr1 = 1

#     def __init__(self):
#         self.attr1 = "not 1"

# obj = A()
# obj.__dict__['attr2'] = 2

# print(obj.attr2, len(obj.__dict__))

# 2
# Which one from below statements is correct for static method in Python?

# 3
# What does the function super() do?

# Returns a method of a parent or sibling class.

# Returns a parent class.

# Returns a proxy object that delegates method calls to a parent or sibling class(es).

# Returns a method that returns only super quality values.

# # 4
# class parent:
#     def __init__(self):
#         self.v1 = 10

# class child(parent):
#     def __init__(self):
#         self.v2 = 100

# obj = child()
# print(obj.v1, obj.v2)

# 5
# class A: 
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return A(self.value + other.value)

#     def __str__(self):
#         return "A, value: {}".format(self.value)

# print(A(10) + A(20))


# 6
# class A: 
#     def m(self):
#         return "A"

# class B(A):
#     def m(self):
#         return super().m() + "B"

# print(B().m())


# 10
# class A: 
#     attr = 10
#     def __init__(self):
#         self.attr = 20

# print(A.attr, A().attr)