### Reference:
1. https://realpython.com/python-testing/
2. https://docs.python.org/zh-tw/3/library/unittest.html

### Without using unittest framework:
```
>>> assert sum([3, 2, 5]) == 10, "Should be 10"
# Output nothing because it is correct
```
```
>>> assert sum([3, 2, 5]) == 11, "Should be 11"
# AssertionError: Should be 11
```

### How the test script (tester.py) looks like:
```
def test():
    assert sum([3, 2, 5]) == 10, "Should be 10"

if __name__ == "__main__":
    test()
    print("Everything passed")
```
### How to run the test:
```
$ python tester.py
```
