import threading
class MetaData(type):
    _instance=None
    _lock = threading.Lock()
    def __call__(cls, *args, **kwds):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, *kwds)
        return cls._instance

class MyClass(metaclass=MetaData):
    def __init__(self,url):
        self.url = url

    def show(self):
        print(f"OBJECT URL = {self.url}")

obj1 = MyClass("youtube")
obj2 = MyClass("facebook")
obj1.show()
obj2.show()
print(obj1 is obj2)
# =============================================================================

# SINGLETON + METACLASS — REVISION NOTES

# =============================================================================

#

# THE CODE (reference implementation)

# -----------------------------------------------------------------------------

# class SingletonMeta(type):

#     _instances = {}

#     def __call__(cls, *args, **kwargs):

#         if cls not in cls._instances:

#             cls._instances[cls] = super().__call__(*args, **kwargs)

#         return cls._instances[cls]

#

# class DatabaseConnection(metaclass=SingletonMeta):

#     def __init__(self, url):

#         self.url = url

#

# In one line: first call builds the object and caches it in the dict;

# every later call returns the cached one. Nothing new gets built.

#

#

# 1. __new__  vs  __init__

# -----------------------------------------------------------------------------

#   __new__   -> CREATES the object.  first arg = cls.  MUST return the object.

#   __init__  -> CONFIGURES it.       first arg = self. MUST return None.

#

#   Order: __new__ runs first, then __init__ on the object it returned.

#

#   KEY RULE: __init__ only runs if __new__ returns an instance of cls.

#             Return something else -> __init__ is skipped entirely.

#

#   Real use of __new__: subclassing immutables (int, str, tuple) — can't

#   mutate them in __init__ because they're already frozen.

#       class PositiveInt(int):

#           def __new__(cls, v):

#               if v < 0: raise ValueError

#               return super().__new__(cls, v)

#

#

# 2. __call__ — makes an object usable with ()

# -----------------------------------------------------------------------------

#   Any class defining __call__ -> its instances become callable.

#       double(5)  ==  type(double).__call__(double, 5)

#   Same family as len(x)->__len__, x[0]->__getitem__.

#

#   Why not just a function? The object keeps state between calls and can

#   have other methods (limiter.count, limiter.reset()). A closure can hold

#   state but you can't inspect or reset it from outside.

#

#   WHAT IT RETURNS:

#     - your own __call__ on a normal class -> anything you want, no rule

#     - type.__call__ (runs on Foo()) -> THE NEW INSTANCE

#

#   type.__call__ is roughly:

#       def __call__(cls, *args, **kwargs):

#           obj = cls.__new__(cls, *args, **kwargs)     # create

#           if isinstance(obj, cls):

#               obj.__init__(*args, **kwargs)           # configure

#           return obj                                  # <- what you receive

#

#   ^ That isinstance check is the "__init__ gets skipped" rule from §1.

#   ^ __init__'s return value is discarded; the object from __new__ comes out.

#

#

# 3. Metaclass

# -----------------------------------------------------------------------------

#   A metaclass is the class OF a class.  type is the default one.

#       type(f)    -> Foo      (Foo made f)

#       type(Foo)  -> type     (type made Foo)

#

#   The class statement is sugar. These are identical:

#       class Foo: x = 1

#       Foo = type("Foo", (), {"x": 1})       # name, bases, namespace

#

#   TWO HOOKS, TWO MOMENTS:

#       Meta.__new__ / __init__  -> ONCE, when the class is defined

#       Meta.__call__            -> EVERY TIME you instantiate the class

#

#   The singleton uses __call__ because it's the single chokepoint sitting

#   ABOVE both __new__ and __init__. Skip super().__call__() and hand back a

#   cached object -> nothing is created, nothing is re-initialized.

#

#

# 4. Metaclass vs normal inheritance  (the main distinction)

# -----------------------------------------------------------------------------

#   Inheritance  -> controls what your OBJECTS can do.

#                   class Dog(Animal): every Dog object gets Animal's methods.

#   Metaclass    -> controls what your CLASSES can do.

#                   class DB(metaclass=SingletonMeta): the class DB itself

#                   gets SingletonMeta's behaviour.

#

#   DB is NOT a kind of SingletonMeta, and its instances gain no methods.

#   SingletonMeta is the factory that produced DB, rigged so that

#   instantiating DB gets intercepted.

#

#   Analogy: inheritance = child getting traits from a parent.

#            metaclass   = the mould that stamped out the parent.

#

#

# 5. super()  — no cls/self passed

# -----------------------------------------------------------------------------

#   super() means "let my parent handle this". Here the parent is type,

#   and type.__call__ is the normal create-then-init machinery — we delegate

#   instead of rewriting it.

#

#   Python 3 no-arg super() auto-fills BOTH the class and the instance:

#       super().__call__(*a, **kw)  ==  super(SingletonMeta, cls).__call__(*a, **kw)

#   So do NOT pass cls/self again — it would be sent twice.

#

#       class Dog(Animal):

#           def __init__(self, name, breed):

#               super().__init__(name)        # NOT super().__init__(self, name)

#

#   "cls" vs "self" is only naming convention. In SingletonMeta.__call__, cls

#   IS the instance (a metaclass's instances are classes). super() treats

#   them identically.

#

#   EXCEPTION — __new__ is a static method, no binding to inherit, so cls is

#   passed as a real argument:

#       return super().__new__(cls)

#

#   GOTCHA: no-arg super() only works inside a method in a class body.

#   In a plain function or lambda -> RuntimeError. Use the 2-arg form there.

#

#

# 6. Why *args, **kwargs are forwarded to super()

# -----------------------------------------------------------------------------

#   *args   = catch-all for positional args

#   **kwargs = catch-all for keyword args

#

#   SingletonMeta doesn't know what arguments the target class needs

#   (DB wants url; another class may want three things). It collects whatever

#   came in and passes it straight through so __init__ receives it.

#   Without this, only zero-argument classes would work.

#

#

# 7. Other singleton variants

# -----------------------------------------------------------------------------

#   (a) __new__ override — the common answer, but BUGGY:

#           returns a real instance, so __init__ re-runs on EVERY call and

#           overwrites state.  a = S(1); b = S(2)  ->  a is b True, a.value 2

#       The metaclass avoids this by intercepting above __new__/__init__.

#

#   (b) Decorator — less machinery, usually preferable:

#           def singleton(cls):

#               inst = {}

#               def get(*a, **kw):

#                   if cls not in inst: inst[cls] = cls(*a, **kw)

#                   return inst[cls]

#               return get

#           @singleton

#           class Cache: ...

#

#   (c) Module-level instance — the most Pythonic. Modules import once, so

#       `db = DatabaseConnection(...)` in db.py is a singleton, zero machinery.

#

#

# 8. Thread safety

# -----------------------------------------------------------------------------

#   _lock = threading.Lock()

#   def __call__(cls, *a, **kw):

#       if cls not in cls._instances:            # outer check: skip lock

#           with cls._lock:                      #   on the common path

#               if cls not in cls._instances:    # inner check: re-verify

#                   cls._instances[cls] = super().__call__(*a, **kw)

#       return cls._instances[cls]

#

#   = double-checked locking. Outer if avoids lock cost after the first

#     creation; inner if guards against two threads both passing the outer

#     check before either acquired the lock.

#

#

# 9. INTERVIEW TALKING POINTS

# -----------------------------------------------------------------------------

#   - Raise the __init__-reruns bug voluntarily; shows you know why the

#     metaclass version exists.

#   - Downsides of singletons: global state, hidden dependencies, state leaks

#     between unit tests. Dependency injection is often better.

#   - When metaclasses are actually used: ORMs (Django, SQLAlchemy), ABCMeta,

#     serialization libs — register/validate classes at definition time.

#   - Lighter alternatives: __init_subclass__ (3.6+) or a class decorator.

#   - Tim Peters: if you're wondering whether you need metaclasses, you don't.

#

# =============================================================================
 

