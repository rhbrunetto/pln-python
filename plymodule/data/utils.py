import collections

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

def flatten_2(l, lista):
    if l is not None:
        h, t = l
        lista.append(h)
        flatten_2(t, lista)
    return lista