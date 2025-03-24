# Plan

## Initial explorations

- Read relevant sections in [The Python Language Reference](https://docs.python.org/3/reference/index.html)
  - Not suffienciently clear for me to understand the details about descriptors
- Looked at materials for _Python Epiphanies_ which is an online course I did in the past
  - Minimal coverage and not much help
- Looked for what was available in YouTube and found these two videos and they were quite helpful
  - [python descriptors! (advanced) anthony explains #519](https://www.youtube.com/watch?v=vBys0SwYvCQ)
    - the files `demo*.py` and `cached.py` capture my notes from this video
  - [8 things in Python you didn't realize are descriptors](https://www.youtube.com/watch?v=mMbVs17Vmo4)
    - the file `scratch.py` plus several items in `notes.md` capture my notes from this video
- I do not want the talk to 'recreate' either of these videos

## Outline

Based on what I learned from these videos plus my own thoughts, the first draft outline is:

- Introduction
- Motivation for writing this talk
  - Curious about how properties work
  - Internal lightning talk
- What are descriptors
  - The two types of descriptors
- Attribute lookup - basic view
- Basic non-data descriptor
- Basic data descriptor
- CartesianPoint2D
  - `x`, `y`: normal attributes
- Add `r`, `theta` as read-only attributes
- Add caching for `r`, `theta`
  - `x`, `y` now need to be data descriptors
- Make `r`, `theta` read-write attributes
- Change `r` to a validated descriptor (r >= 0)
- Attribute lookup - full view
- Uses of descriptors
  1. Class methods
  1. Properties
  1. Class methods and static methods
  1. Slots
  1. `__dict__`
  1. Validators
  1. SQLAlchemy Models (what about other packages? attrs? pydantic?) <- might not be worth mentioning a specific package

Something to consider - this will probably be more effective live coded. How to accomplish this in a way that keeps the flow smooth and the pace reasonable?

## Additional resources to explore

- _Python Programming Language_ by David Beazley, [**Lesson 10:Encapsulation (Owning the Dot)**](https://learning.oreilly.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_10_00/) (**EBK**)
- _Effective Python, 3rd Edition_ by Brett Slatkin, [**Item 60: Use Descriptors for Reusable @property Methods**](https://learning.oreilly.com/library/view/effective-python-125/9780138172398/ch08.xhtml#ch08lev1sec3) (**EBK**)
- _The Python Master_ by Robert Smallshire and Austin Bingham, **Chapter 4 - Descriptors**
