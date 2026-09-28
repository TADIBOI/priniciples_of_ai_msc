# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
#@title MIT License
#
# Copyright (c) 2020 Balázs Pintér 
#
# Permission is hereby granted, free of charge, to any person obtaining a
# # copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# %% [markdown]
# # Jupyter notebook basics
#
# We are going to use both Jupyter notebooks and plain Python code.
#
# - This is a markdown cell, the next ones are code cells
# - The notebook is running a kernel (here, Python), the code cells are executed by this kernel
# - Very useful to do any command or check shortcuts: Ctrl-Shift-C (p in earlier versions)
# - Move around: arrow keys or j, k
# - Run a cell and go to next cell: Shift+Enter
# - Go to edit mode to edit a cell: click or Enter
# - Get help about while editing: Shift-Tab, press twice to get more help
# - Back to command mode from edit mode: Esc
# - New cell above: a
# - New cell below: b
# - Delete cell: x
# - Run a cell and insert new cell below: Alt-Enter

# %% [markdown]
# # Python crash course
# Tutorial for reference: https://docs.python.org/3/tutorial/index.html

# %% [markdown]
# ## Variables and types
#
# Python is dynamically typed. The types belong to the objects and not their names.
#
# For example, `a = 3` assigns the object `3` to the name `a`. The name `a` will reference the object `3` from now on.
#
# `a` can be freely reassigned later.

# %%
a = 3 # int
a = True # bool
a = 4.2 # float

# %% [markdown]
# Python is strongly typed. For example, `'abc' + 3` would give an error.

# %% [markdown]
# ## Sequence types

# %%
a = 'abc' # str
b = [1, 2, 3, 4, 5] # list
c = (1, 2, 3, 4) # tuple

# %% [markdown]
# Tuples are denoted by the comma. Multiple assignment is possible with tuples:

# %%
a, b = 'abcdef', [1, 2, 3]

# %%
a, b

# %% [markdown]
# Strings and tuples are immutable: `a[0] = 'x'` gives an error.

# %%
l = [1, 'afgd', True] # lists can have different types in them, although usually they don't

# %% [markdown]
# ### Some operations

# %%
a[0], b[1] # indexing starts from 0

# %%
a[1:3:2] # slicing, up to but not including index 3

# %%
a[3:] # slicing from index 3

# %%
a + 'aa' # concatenation

# %%
a[:3] + a[3:] # gives back the original sequence

# %%
a[0::2] # from index 1 to 3

# %%
a[-1] # the last element

# %%
a[-2]

# %%
len(a), len(b), len(c) # lengths

# %%
# appending to a list
print(b)
b.append(34)
print(b)

# %%
# popping elements from a list
print(b)
b.pop(0)
print(b)
b.pop()
print(b)

# %% [markdown]
# ## Some expressions and statements

# %%
3 + 4, 3 * 4

# %%
a = 2
a += 3
a

# %%
13 / 4, 13 // 4

# %%
3 % 2

# %%
divmod(13,3)

# %%
3 == 4, 3 < 4, 4 < 3

# %%
3 < 4 < 5

# %%
3 < 4 and 4 < 5

# %%
a = 100
a += 1
a

# %% [markdown]
# ### if, for, while

# %%
a = 3
b = 3
if a < b:
    print("The condition is true.")
elif b < a:
    print("The first elif branch.")
else: print("The else branch.")

# %%
l = list(range(10))
l

# %%
l = range(10)
l

# %%
for e in l:
    print(e)

# %%
x = 1
while x < 10:
    print(x)
    if x % 3 != 0:
        x += 1
    else:
        x += 3

# %% [markdown]
# **Exercise**: Add all the even numbers in l and print the result.

# %%
x = 0 
for e in l:
    if e % 2 == 0:
        x += e
x

# %% [markdown]
# **Exercise**: Collect all the even numbers in l into a new list l_even.

# %%
l_even = (0)
for e in l:
    if e % 2 == 0:
        l_even.append(e)
l_even

# %% [markdown]
# **Exercise**: Solve the [FizzBuzz problem](https://en.wikipedia.org/wiki/Fizz_buzz)

# %%
for i in range (1,21):
    div_3 , div_5 = i % 3 == 0, 1 % 

# %% [markdown]
# ### break, continue, else

# %%
l = list(range(10))
import random
random.shuffle(l)
l

# %% [markdown]
# #### 3 versions of a search

# %%
to_find = 8
i = 0
for e in l:
    if e == to_find:
        print(f'Found {to_find} at index {i}')
        break
    i += 1
else:
    print(f'{to_find} was not found in the list')

# %%
list(enumerate(l))

# %%
to_find = 8
for i, e in enumerate(l):
    if e == to_find:
        print(f'Found {to_find} at index {i}')
        break
else:
    print(f'{to_find} was not found in the list')

# %%
to_find = 8
print(f'Found {to_find} at index {l.index(to_find)}') # we would have to handle the exception if the element is not in the list

# %% [markdown]
# #### continue

# %%
for i in range(10):
    if i % 3 != 0:
        continue
    print(i)

# %% [markdown]
# **Exercise**: Find the largest even number in l

# %%
l = list(range(20))
random.shuffle(l)
l

# %%
[e for e in l if e % 2 == 0]

# %% [markdown]
# ## 

# %% [markdown]
# ## List comprehensions

# %%
[x**2 for x in range(5)]

# %%
[(x, x**2) for x in range(5)]

# %%
[(x, x**2) for x in range(5) if x % 2 == 0]

# %% [markdown]
# **Exercise**: write a list comprehension to collect all the strings with length 3

# %%
l = ['bacd', 'abc', 'ab', 'a', 'bcd', 'cdef', 'cde']

# %%

# %% [markdown]
# ## Sets and dictionaries

# %% [markdown]
# ### Sets

# %%
a = {1, 2, 3, 4}
a

# %%
a.add(5)
a

# %%
a.add(5)
a

# %%
l = list(range(5)) + list(range(5))
l

# %%
set(l)

# %%
3 in a, 13 in a

# %%
for e in a:
    print(e)

# %% [markdown]
# **Exercise**: Add the unique elements of l. If you already encountered an element, don't add it to the sum

# %%
l = [1, 1, 2, 3, 2, 4, 5, 2, 3]

# %%

# %% [markdown]
# ### Dictionaries

# %%
d = {'a' : 1, 'b': 5}
d

# %%
d['a']

# %%
d['c'] = 35

# %% [markdown]
# You can assign to any key, but can only access existing keys: `d['d']` would give an error.

# %%
for key in d:
    print(key, d[key])

# %%
for key, value in d.items():
    print(key, value)

# %% [markdown]
# ### Set and dictionary comprehensions

# %%
{x**2 for x in a if x % 2 == 0}

# %%
d = {x: x**2 for x in range(10) if x%2 == 1}
d

# %% [markdown]
# **Exercise**: Invert the dictionary d. The keys should be the values, and the values should be the keys.

# %%
