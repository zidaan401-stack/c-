import sys
limit = sys.get_int_max_str_digits()
print("limit",limit)
num=10**4200
try:
    print(" not out of bound",len(str(num)))
    except:
    print("out of bound", len(str(num)))
