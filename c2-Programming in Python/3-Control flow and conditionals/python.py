# a = 1;
# b = 0;
# if a > b:
#     print("a is greater than b");
# elif a == b:
#     print("a is equal to b");
# else:
#     print("a is less than b");

# a = True;
# b= False;
# if a or b:
#     print("a or b is true");
# if a and b:
#     print("a and b is true");
# if not a:
#     print("a is false");

# match case
http_status_code = 418
match http_status_code:
    case 400:
        print("Bad request")
    case 401 | 403 | 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the Internet")

#for loop

for i in range(1, 11):
    print(i)



    

