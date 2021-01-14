# Write a super useful function to generate multiplication tables.

# You shoud be able to define the following arguments:

# width (by default 10) 
# height (by default 10)
# sep_width (by default 3 - number of whitespaces between columns)
# print_header (by default False - print header "Multiplication Table 10 x 10" or not)
# print_footer (by default True - print footer in form of line of 30 "-" characters)
# sep_width, print_header and print_footer should be keyword-only arguments.

# If you pass additional non-keyword or keyword arguments the function should return TypeError like this (if you are using and checking kwargs yourself):

# raise TypeError("Function gen_mul_table() takes only two positional and three keyword arguments")
# or (if you are using keyword-only syntax):

# TypeError: gen_mul_table() takes from 0 to 2 positional arguments but 3 were given



def gen_mul_table(width=10,height=10,*, print_header=True, sep_width=4, print_footer=False):
    if print_header:
        print(f"Multiplication table {width} x {height}")
    result =''
    for i in range(1,height+1):
        result += ((f'{{:>{sep_width}}}')*width).format(*range(1*i,height*i+1,i))+'\n'
    print(result)
    if print_footer:
        print("_"*30)
    return result.rstrip()

gen_mul_table(5, 5)
gen_mul_table(4, 4, print_header=True, sep_width=4, print_footer=False)
# gen_mul_table(3, 3, 5)