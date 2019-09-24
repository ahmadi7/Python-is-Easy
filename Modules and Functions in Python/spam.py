def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more " + x
        y += spam3()
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"
    x += spam2()
    print("In spam1, locals are {}".format(locals()))
    return x

print(spam1())
print(locals())
print(globals())