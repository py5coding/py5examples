# py5 Examples

![py5 logo](images/logo.png)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/py5coding/py5examples/HEAD?urlpath=lab)

[![py5 downloads](https://pepy.tech/badge/py5/month)](https://pepy.tech/project/py5)

[![Downloads](https://pepy.tech/badge/py5/week)](https://pepy.tech/project/py5)

py5 is a new version of [Processing][processing] for Python 3.8+. The goal of py5 is to create a version of Processing that is [integrated into the Python ecosystem](https://py5coding.org/integrations/python_ecosystem_integrations.html). Built into the library are thoughtful choices about how to best get py5 to work with other popular Python libraries and tools such as [Jupyter](https://jupyter.org/), [numpy](https://numpy.org/), [shapely](https://shapely.readthedocs.io/en/stable/), [trimesh](https://trimesh.org/), [matplotlib](https://matplotlib.org/), and [Pillow](https://python-pillow.org/).

py5 is an excellent choice for educators looking to teach Python in the context of creative coding and is currently used in classrooms all around the world. The documentation website includes [introductory tutorials](https://py5coding.org/tutorials/intro_to_py5_and_python.html) as well as extensive [reference documentation](https://py5coding.org/reference/summary.html), complete with example code.

Here is a simple example of a working py5 Sketch, written in module mode:

``` python
import py5


def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)


py5.run_sketch()
```

If you have Java 11 installed on your computer, you can install py5 using pip:

``` bash
pip install py5
```

[Detailed installation instructions](https://py5coding.org/content/install.html) are available on the documentation website. There are some [Special Notes for Mac Users](https://py5coding.org/content/macos_users.html) that you should read if you use macOS.

There are currently five basic ways to use py5. They are:

* **module mode**: create a sketch with `setup()` and `draw()` functions that call methods provided by the `py5` library. The above example is created in module mode.
* **class mode**: create a Python class inherited from `py5.Sketch`. This mode supports multiple Sketches running at the same time.
* **imported mode**: simplified code that omits the `py5.` prefix. This mode is supported by the py5 Jupyter notebook kernel and the `run_sketch` command line utility.
* **static mode**: functionless code to create static images. This mode is supported by the py5bot Jupyter notebook kernel, the `%%py5bot` IPython magic, and the `run_sketch` command line utility.
* **processing mode**: make calls to Python from a Processing (Java) Sketch. This mode enables py5 to function as bridge, connecting the Python and Java ecosystems through a new `callPython()` method.

py5generator is a meta-programming project that creates the py5 library. To view the actual installed py5 library code, look at the [py5 repository][py5_repo]. All py5 library development is done through py5generator.

[py5_repo]: https://github.com/py5coding/py5
[processing]: https://github.com/processing/processing4
[jpype]: https://github.com/jpype-project/jpype

[jupyter]: https://jupyter.org/
[numpy]: https://numpy.org/
[pillow]: https://python-pillow.org/
