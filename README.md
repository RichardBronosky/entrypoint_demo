# entrypoint_demo

a simple Python entrypoint demonstration

----------

Everyone's favorite setuptools Entry Point is the handy [console_scripts]. But,
as it turns out, that is just one usage of this very useful concept. You get
that *for free*, but if you want to use [entry points] to make your project more
magical you are going to have to do a little work. Luckily it's not hard and
this project aims to demo it so clearly that you can't go wrong.

## Usage

* Clone this repo and cd into it.

 - You can't pip install it from the github URL because it contains 2 different
   Python packages.

```bash
git clone https://github.com/RichardBronosky/entrypoint_demo.git
cd entrypoint_demo
```

* Install the first package.

```bash
pip install ./epd_main
# must have the ./ in there to indicate a local path and not pypi
```

* Check out [the results](https://bpaste.net/show/546872592282)

```python
from pprint import pprint
from epd_main import my_tools
pprint(my_tools.__dict__)
my_tools.my_pot()
```

* Install the second package.

```bash
pip install ./epd_plugin
# must have the ./ in there to indicate a local path and not pypi
```

* Check out [the results](https://bpaste.net/show/0a0171469249)

```python
from pprint import pprint
from epd_main import my_tools
pprint(my_tools.__dict__)
my_tools.my_knife()
```

### Did you get that?

The Python code we used was the same in both tests, but the results were
significantly different. Installing the `epd_plugin` package changed the content
of `epd_main.my_tools` by adding more tools! That's cool. You can design a
package to be extended by another package. No need to change any code or
**configuration**. All you do is `pip install` a package. That's awesome.

### Wait!

> Did you just say **configuration** and **pip install**?

YES! You can use this same technique to `pip install` configuration. Ever heard
of "Configuration as Code"? You can design your packages to be configured and
extended by installing other packages.

### Oh, :-\

> I can't just configure and extend an existing package? I have to author or
  edit the package?

Well, this technique is called "Entry Points" and is a feature of setuptools. It
was intended for all of the developers to be *willing participants* in the
practice. There are other ways to Monkey Patch code, but this more of a
collaboration.

## Other Details

So you've seen what it can do and we've discussed why you want to do it. Let's
look behind the curtain.

### How it works

Each of the packages define `entry_point` names and a list of key value pairs in
their setup.py. ([epd_main/setup.py], [epd_plugin/setup.py])

Then in the epd_main package I use `pkg_resources` to do something pretty cool
([I must say]). In the `__init__.py` I define `my_tools` as a subclassed object
and use `setattr()` to [attach the functions]. The end result is that you can
import just that object just as you would a module.



### What you should avoid

You may be tempted to try to [add functions to the global namespace] of a module.
I have included an example of this also, but it breaks [static code analysis]
and makes you code non-[reentrant]. The are hard Computer Science-y things. I
prefer to not get into arguments about these things. There are enough geniuses
telling me not to do it, that I just don't.

* Just so you don't do this on your own thinking you've done something awesome.
  Check out [the results](https://bpaste.net/show/ca2621ad2501)

        from pprint import pprint
        from epd_main import broken_tools as my_tools
        # You don't want to see the __dict__ of an imported module. I'm filtering out the private stuff
        pprint({k:v for (k,v) in my_tools.__dict__.iteritems() if k[0] != '_'})
        my_tools.my_knife()

* Since I've already shown you how to get similar access to your functions
  without the `globals()` hackery, you can enjoy seeing how to do it without
  actually putting it into your project.


[console_scripts]: http://stackoverflow.com/a/782984/117471
[entry points]: http://stackoverflow.com/a/9615473/117471
[I must say]: https://www.youtube.com/watch?v=vAE4AOP6xKs#t=5
[epd_main/setup.py]: https://github.com/RichardBronosky/entrypoint_demo/blob/master/epd_main/setup.py#L60-L64
[epd_plugin/setup.py]: https://github.com/RichardBronosky/entrypoint_demo/blob/master/epd_plugin/setup.py#L60-L64
[attach the functions]: https://github.com/RichardBronosky/entrypoint_demo/blob/master/epd_main/epd_main/__init__.py#L7-L8
[static code analysis]: http://www.pylint.org/
[reentrant]: http://www.quora.com/When-is-a-function-reentrant-How-does-that-relate-to-it-being-thread-safe
[add functions to the global namespace]: https://github.com/RichardBronosky/entrypoint_demo/blob/master/epd_main/epd_main/broken_tools.py#L4-L5
