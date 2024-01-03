def do_something(x, y, z=None, /):
    print(f"{x=}, {y=}, {z=}")


do_something(2, 10)  # valid
do_something(2, 10, 17)  # valid
do_something(x=2, y=10)  # invalid because x and y are keyword arguments. TypeError
do_something(2, 10, z=17)  # invalid because z is keyword argument. TypeError
