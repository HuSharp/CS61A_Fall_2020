<!--
 * @Descripttion: 
 * @version: 
 * @Author: HuSharp
 * @Date: 2021-02-28 17:00:40
 * @LastEditors: HuSharp
 * @LastEditTime: 2021-02-28 17:00:41
 * @@Email: 8211180515@csu.edu.cn
-->

# 范用方法 generic operations

## 1、字符串转换

Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。

### `repr` 和 `str`

Python 规定，所有对象都应该能够产生两种不同的字符串表示：一种是人类可解释的文本，另一种是 Python 可解释的表达式。字符串的构造函数`str`返回人类可读的字符串。在可能的情况下，`repr`函数返回一个 Python 表达式，它可以求值为等价的对象。`repr`的文档字符串解释了这个特性：

```python
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half)
'1/2'
>>> print(half)
1/2
```


```python
>>> s = 'hello'
>>> repr(s)
"'hello'"
>>> eval(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'hello' is not defined
>>> eval(repr(s))
'hello'
>>> eval(str(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'hello' is not defined
>>> str(s)
'hello'
```

### `__str__`对类的影响

如果一个类中定义了`__str__()`方法，那么在打印对象时，默认输出该方法的返回值。这也是一个非常重要的方法，需要用户自己定义。　

下面的类，没有定义`__str__()`方法，打印结果是：`<__main__.Foo object at 0x000000000210A358>`

```python
class Foo:
    pass

obj = Foo()
print(obj)
```

定义了`__str__()`方法后，打印结果是：'jack'。

```python
class Foo:

    def __str__(self):
        return 'jack'

obj = Foo()
print(obj)
```


且 当没有 `__str__` 函数时，使用 str 会调用 repr

```python
class Bear:
    '''A Bear'''
    def __repr__(self):
        return 'Bear()'

>>> a = Bear()
>>> repr(a)
'Bear()'
>>> str(a)
'Bear()'
>>> a.__repr__()
'Bear()'
>>> a.__str__()
'Bear()'
```

对比此时 `__str__` 函数存在

```python
>>> a = Bear()
>>> a.__repr__()
'Bear()'
>>> a.__str__()
'a bear!'
>>> str(a)
'a bear!'
>>> repr(a)
'Bear()'
```


再次对比

```python
class Bear:
    '''A Bear'''
    def __init__(self):
        self.__repr__ = lambda:'Bear_attr: repr'
        self.__str__ = lambda:'Bear_attr: str'  

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear!'

# -------- 打印输出
b = Bear()
print(b)
print(str(b))
print(repr(b))
print(b.__str__())
print(b.__repr__())

a bear!
a bear!
Bear()
Bear_attr: str
Bear_attr: repr
```

发现若是调用 `str(x)`  和 `repr(x)`，是直接求该实例的类函数

若是调用 `x.__str__`  和 `x.__repr__`，则是先求该对象的属性，再看函数

大致实现如下

```python
def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return t.__repr__(x)
```



## `__add__`: 加运算  `__sub__`: 减运算      `__mul__`: 乘运算      `__div__`: 除运算  `__mod__`: 求余运算 `__pow__`: 幂运算

这些都是算术运算方法，需要你自己为类设计具体运算代码。有些Python内置数据类型，比如int就带有这些方法。Python支持运算符的重载，也就是重写。

```
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
```
