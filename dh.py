# generate s and p
# s can be any 500bit+ number
# p must be 500bits+, prime, and (p-1)/2 should also be prime.
# I can use a library to generate p.
# Also write my own modular exponentiation function. Ugh.

def mod_exp(generator, val, mod_val):
    # store temporary values
    g_tmp = generator
    val_tmp = val
    x = 1
    while val_tmp > 0:
        if val_tmp % 2 == 0:
            g_tmp = (g_tmp * g_tmp) % mod_val
            val_tmp = val_tmp/2
        else:
            x = (g_tmp * x) % mod_val
            val_tmp = val_tmp - 1
    return x

if __name__ == '__main__':
    g = 5
    p = long('7f1830d98a876f67465b3a091fe30820b6421b2f3250347823f96b4531a4c17c2098bb1d06a74a796adb531e1e6acfa971e06a7c'+
             'fedf6f68fc910c2a2dd316', 16)
    s = long('7f1830d98a876f67465b3a091fe30820b6421b2f3250347823f96b4531a4c17c2098bb1d06a74a796adb531e1e6acfa971e06a7c'+
             'fedf6f68fc910c2a2dd31612345', 16)

    modded = mod_exp(g, s, p)
    if modded != pow(g, s, p):
        print("Modular exponentiation failed! Expected %d, found %d" % (pow(g,s,p), modded))
    print "p value"
    print p
    print "g^s%p"
    print(modded)

