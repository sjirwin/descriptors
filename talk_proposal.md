# Talk Proposal

## Title

Behind the Magic: Unlocking Python's Descriptor Protocol

## Abstract

Ever wondered _how_ `@property` works? Or why setting an attribute sometimes just feels... different? That curiosity led me down a rabbit’s hole - one that ended at Python’s powerful, often invisible, Descriptor protocol.

In this talk, we’ll demystify descriptors through a journey that starts with a question and unfolds into a deeper understanding of how Python decides what to return when you access `obj.attr`. We’ll explore the two types of descriptors, peek into the attribute lookup chain, and examine examples - like a class with read-only, cached, and validated attributes.

Descriptors are hiding in plain sight, and you’ll walk away with a clear grasp of how they underpin many familiar features: properties, class/static methods, slots, and more. Whether you’ve used them unknowingly for years or never heard of them before, come peel back the curtain and learn more about one of the things that makes Python tick.

## Objective

This talk aims to demystify Python’s Descriptor protocol by giving attendees a clear, conceptual understanding of how attribute access and lookup actually work under the hood. Through examples and progressive refinements, we’ll explore both data and non-data descriptors and see how they are connected to everyday features like `@property`, `@classmethod`, and more.

While most Python developers rarely need to write their own descriptors, this talk will also demonstrate that doing so is straightforward once the underlying mechanics are understood. Attendees will leave with a new appreciation for the magic behind familiar syntax and, ideally, a spark of curiosity to explore Python’s internals more deeply.

## Detailed description

Descriptors are one of the most powerful - and most invisible - parts of Python. They’re the foundation for familiar features like `@property`, `@classmethod`, and even `__slots__`. However, despite their importance, many Python developers (my past self included) use them every day without knowing how they work.

This talk is driven by curiosity. After seeing a lightning talk on descriptors, I couldn’t stop wondering how `@property` actually works under the hood. That curiosity led me down a deep rabbit’s hole of Python internals - and ultimately led me to develop this talk.

We’ll primarily explore descriptors through live coding, starting with simple, focused examples and then gradually build up a core case study. Along the way, we’ll look at how Python handles attribute lookup, the difference between data and non-data descriptors, and how descriptors can be used for computed attributes, caching, and validation.

The goal is to demystify descriptors and show that they’re not just for language wizards - once you understand the underlying mechanics, writing your own is surprisingly straightforward. Attendees should walk away with a deeper understanding of Python’s object model and a new perspective on features they already use daily.

## Outline

- Introduction
  - Set expectations: intermediate/experienced Python users
  - Brief overview of what descriptors are and why they matter
- Motivation for This Talk
  - Sparked by curiosity: *"How do `@property` and `@classmethod` really work?"*
  - Internal lightning talk turned deep-dive
  - Realized how fundamental descriptors are to the Python object model
- What *Are* Descriptors?
  - Definition and purpose
  - The two types:
    - Data descriptors (`__get__`, `__set__`)
    - Non-data descriptors (`__get__` only)
- *Why* Write a Descriptor
  - Avoid duplicated code
- Attribute Lookup (Basic View)
  - Data Descriptor
  - `self.__dict__['attrib']`
  - Non-Data Descriptor
- Basic Descriptor Examples
  - Non-Data Descriptor
    - Simple example: computed read-only attribute
  - Data Descriptor
    - Adding a setter
    - Demonstrating difference in precedence
- Case Study: `CartesianPoint2D`
  - `x`, `y`: plain attributes
  - Add `r`, `theta`: computed as read-only (non-data descriptors)
  - Add caching to `r`, `theta`
    - `x`, `y` now need to be data descriptors
  - Make `r`, `theta` writable
    - Coordinate system conversion
  - Add validation to `r` (`r >= 0`)
- Attribute Lookup (Full View)
  - Data Descriptor
  - `self.__dict__['attrib']`
  - Non-Data Descriptor
  - Class attributes
  - Raise AttributeError (which triggers `__getattr__`)
- Common and Powerful Uses of Descriptors
  1. class methods (bound functions)
  2. `@property`
  3. `@classmethod` and `@staticmethod`
  4. `__slots__`
  5. Managing access to `__dict__`
  6. Validators
- Conclusion
  - Descriptors are hidden in plain sight
  - Key to understanding Python’s object model
  - Encouragement to explore Python internals

## Biography

Scott Irwin is a senior engineer at Bloomberg, where he has worn many hats. During his decade at Bloomberg, he has led teams, developed Python applications and libraries, and taught internal training courses.

Scott is also a Python educator who has led live online training events hosted on the O'Reilly learning platform.
