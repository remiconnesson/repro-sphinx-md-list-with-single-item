1. `pip install -r requirements`

2. `cd docs && sphinx-build -M markdown build`

3. `cat docs/build/markdown/index.md`

this will result in a file that is not valid markdown. (the list marker is missing)


```markdown
### func.func1(param1: int)

This is a function with a single parameter.

* **Parameters**
  **param1** – This is a single parameter.
```

4. but the actual source file is `src/func.py`

```python
def func1(param1: int):
   """This is a function with a single parameter.

   :param param1: This is a single parameter.
   """
   pass
```







