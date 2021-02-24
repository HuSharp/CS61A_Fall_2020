### iterator

关于迭代的 for 语句

迭代器就是一个指针，当第一个 for 指到末尾后，之后的 for 就不能再输出了

```python
>>> k = iter(d.items())
>>> for i in k:
...     print(i)
...
('one', 3)
('two', 4)
('zero', 0)
>>> for i in k:
...     print(i)
...
```

lazy 作用

```python
def double(x):
    print(x, '-->', 2 * x)
    return 2 * x

>>> m = map(double, [3, 5, 7])
>>> next(m)
3 --> 6
6
```

我们发现，在使用 map 函数得到 iter m 后，输出 next(m) 此时的 3 还未变成 6，是在输出之后，才得到 6。因此，这类得到 iter 变量的内置函数，都拥有 lazy 的性质。

### yield 生成器

[**彻底理解Python中的yield**](https://www.jianshu.com/p/d09778f4e055)

* yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
* 简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
* 生成器是可以迭代的，但只可以读取它一次。因为用的时候才生成。（也是 lazy）

```python
def next_even(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


>>> t = next_even(2, 10)
>>> next(t)
2
>>> next(t)
4
>>> next(t)
6
>>> next(t)
8
>>> next(t)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> list(next_even(2, 10))
[2, 4, 6, 8]
```



```python
yield from a  
相当于
for x in a:
    yield x

```
