import numpy
def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    np_a = numpy.array(a);
    np_b = numpy.array(b);
    if (np_a.shape[1] != np_b.shape[0]): return -1;
    c = np_a @ np_b;
    return c;