def test_var_args(f_arg, *robin):
    print("first normal arg:", f_arg)
    for x in robin:
        print("another arg through *robin:", x)

test_var_args('yasoob', 'python', 'eggs', 'test')
