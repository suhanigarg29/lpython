# This test handles actual LPython implementations of functions from the numpy
# module.
from ltypes import i32, i64, f64, TypeVar, overload
from numpy import empty, int64

e: f64 = 2.718281828459045

n: i32
n = TypeVar("n")

def zeros(n: i32) -> f64[n]:
    A: f64[n]
    A = empty(n)
    i: i32
    for i in range(n):
        A[i] = 0.0
    return A

def ones(n: i32) -> f64[n]:
    A: f64[n]
    A = empty(n)
    i: i32
    for i in range(n):
        A[i] = 1.0
    return A

def arange(n: i32) -> i64[n]:
    A: i64[n]
    A = empty(n, dtype=int64)
    i: i32
    for i in range(n):
        A[i] = i
    return A

@overload
def sqrt(n: i32) -> f64:
    return n**(1/2)

@overload
def sqrt(f: f64) -> f64:
    return f**(1/2)

@overload
def exp(n: i32) -> f64:
    return e**n

@overload
def exp(f: f64) -> f64:
    return e**f

@overload
def fabs(f: f64) -> f64:
    if f < 0.0:
        return -f
    return f

@overload
def fabs(n: i32) -> f64:
    if n < 0:
        return -1.0*n
    return 1.0*n

num: i32
num = TypeVar("num")
def linspace(start: f64, stop: f64, num: i32) -> f64[num]:
    A: f64[num]
    A = empty(num)
    i: i32
    for i in range(num):
        A[i] = start + (stop-start)*i/(num-1)
    return A

def test_zeros():
    a: f64[4]
    a = zeros(4)
    eps: f64
    eps = 1e-12
    assert abs(a[0] - 0.0) < eps
    assert abs(a[1] - 0.0) < eps
    assert abs(a[2] - 0.0) < eps
    assert abs(a[3] - 0.0) < eps

def test_ones():
    a: f64[4]
    a = ones(4)
    eps: f64
    eps = 1e-12
    assert abs(a[0] - 1.0) < eps
    assert abs(a[1] - 1.0) < eps
    assert abs(a[2] - 1.0) < eps
    assert abs(a[3] - 1.0) < eps

def test_arange():
    a: i64[4]
    a = arange(4)
    assert a[0] == 0
    assert a[1] == 1
    assert a[2] == 2
    assert a[3] == 3

def test_sqrt():
    a: f64
    a2: f64
    a = sqrt(2)
    a2 = sqrt(5.6)
    eps: f64
    eps = 1e-12
    assert abs(a - 1.4142135623730951) < eps
    assert abs(a2 - 2.3664319132398464) < eps

def test_exp():
    a: f64
    a = exp(6)
    a2: f64
    a2 = exp(5.6)
    eps: f64
    eps = 1e-12
    assert abs(a - 403.4287934927351) < eps
    assert abs(a2 - 270.42640742615254) < eps

def test_fabs():
    a: f64
    a = fabs(-3.7)
    a2: f64
    a2 = fabs(-3)
    eps: f64
    eps = 1e-12
    assert abs(a - 3.7) < eps
    assert abs(a2 - 3.0) < eps

def test_linspace():
    a: f64[4]
    a = linspace(1., 7., 4)
    eps: f64
    eps = 1e-12
    assert abs(a[0] - 1.0) < eps
    assert abs(a[1] - 3.0) < eps
    assert abs(a[2] - 5.0) < eps
    assert abs(a[3] - 7.0) < eps

def check():
    test_zeros()
    test_ones()
    test_arange()
    test_sqrt()
    test_exp()
    test_fabs()
    test_linspace()

check()