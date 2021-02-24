Object-Oriented Programming

是一种组织模块化程序的方法

### class

```python
>>> b = r
>>> b is r
True
```

通常，使用赋值将对象绑定到新名称并不会创建新对象。


#### `__init__ `一般被称为 constructor

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的`__init__`方法，在创建实例的时候，就把`name`，`score`等属性绑上去：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```

注意：特殊方法`__init__ `前后分别有两个下划线！！！

注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`就指向创建的实例本身。

有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但`self`不需要传，Python解释器自己会把实例变量传进去：

```python
>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59
```

但是，既然`Student`实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在`Student`类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和`Student`类本身是关联起来的，我们称之为**类的方法**：

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
```

要定义一个方法，除了第一个参数是`self`外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了`self`不用传递，其他参数正常传入：

```python
>>> bart.print_score()
Bart Simpson: 59
```

#### 方法 和 函数的差异

```python
>>> type(Rational.print)
<class 'function'>
>>> r = Rational(3, 4)
>>> type(r.print)
<class 'method'>
```

方法会自动绑定第一个参数 self ， 因此调用函数体执行有两种方法

```python
>>> r.print()
3  /  4
>>> Rational.print(r)
3  /  4
```

#### access attribute

并且可以通过 getattr 和 hasattr 进行更改判断

```python
>>> getattr(hu, 'score')
100
>>> hasattr(hu, 'score')
True
```

#### 值得注意的是！

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```

内部属性的更改

```python
class Student(object):
    class_att = 10
    ....

>>> hu = Student('hu', 90)
>>> jin = Student('jin', 90)
>>> hu.class_att
10
>>> hu.class_att = 'hu'
>>> jin.class_att
10
>>> hu.class_att
'hu'
```

#### private

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

```
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问`实例变量.__name`和`实例变量.__score`了：
