mypy stub files for transcrypt, jQuery and jQueryMobile combination
===============================================================================
Transcrypt is the powerful tool for development of HTML application.
But the debugging is a little difficult by some cross platform issues.

mypy is the good tool for invest the python code health before
deploying them (converting by transcrypt).
We can use mypy and transcrypt in the normal situation.

BTW, we need to resolve the cross browser issue for touching HTML,
DOM or events and there is some library to solve these issue. for example,
[jQuery](http://jquery.com/) is famous library.
(I had used Monkey script long time ago, but it stopped to development)


So, transcrypt and jQuery combination is well considerred,
but jQuery is very swiss-army-nife library and not well 'typed' and
mypy can't detect the problem with jQuery.

Finally, I wrote the jQuery and browser stubs for mypy
in my applications for more smoothly development.

| term          | version |
|:-------------:|:-------:|
| mypy          | 0.530   |
| transcrypt    | 3.6.50  |
| jQuery        | 1.8.3   |
| jQuery Mobile | 1.4.5   |
| d3.js         | 3.4.13  |
| browser       | Firefox 60.0.1 |


Demonstration
----------------------
### running

```
  $ transcrypt test.py
  $ wget https://code.jquery.com/jquery-1.8.3.min.js
  $ python -m http.server &
  $ browser test.html
```


### mypy

```
  $ export MYPYPATH=stub
  $ mypy --strict test.py
```

or, edit test.py with vim ALE plugin.


How to use
----------------------
### enable stub path before run mypy

```
    $ export MYPYPATH=stub
```

### do not affect stub in transcrypt

```python
    # __pragma__("skip")
    from stub_firefox import location  # apply type information
    # __pragma__("noskip")

    # translate location(python-stub) to location(javascript globals).
    location.href = "http://github.com/"
```

if you don't like this hack, you can do more clear way.

```python
    from stub_firefox import location as _location # apply type information

    # translate location(python-stub) to location(javascript globals).
    # __pragma__("alias", "_location", "location")
    location.href = "http://github.com/"
```


Transcrypt K/H
----------------------
### can't use `*` function
- There are a lot of functions in javascript world, I did not
    prepare all of these.
- please pull your requests.


### can't use `bind` / `unbind` / `click` functions.
- it is not supported, use `on()` or `off()`.


### can't use 'python yield' = 'javascript-Generator'

```
    def fn():
        # type: () -> Iterator[int]
        for i in range(10):
            yield i

    for i in fn():
        i
```

produces

```
    function fn() {
        iter = range(10)
        idx = 0
        for (idx = 0; idx < iter.length; i++) {
            var i = iter[i];
            yield i
        }
    }

    iter = fn()
    idx = 0
    for (idx = 0; idx < iter.length; i++) {
        var i = iter[i];
    }
```

but `iter` is the Generator of javascript, so
we should treat the Generator with for `let ... of statement`.
transcrypt was made for wide development and consider the compativility
problems and `for let ... of` statement will not be converted in current
version 3.6.50.


TODO
----------------------
- split branch to support jQuery 1.8, 2.10, 3.3...
- split module jQuery, jQueryMobile, Pickadate

.. vi: ft=markdown
