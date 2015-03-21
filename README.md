IEMS5722-hw4-server\_side\_translator
========================

A server side translator, written in python, which handles translations required by
assignment 4.

---

How to run the server
---------------------

    $> cd PROJECT_ROOT
    $> python translator/server.py

Running Tests
-------------

You can run tests via the [nose library](https://pypi.python.org/pypi/nose).

Tests will be autodiscovered if they are in the `tests` folder, in files that start with `test_`.

To run the tests,

    nosetests -c .noserc

will run them based on the config settings in `.noserc`.

Two files will be placed in `test_results`:

* `nosetests.xml` - Logs what tests passed/failed, for CI software.
* `coverage.xml` - Logs the test coverage of your project, for CI software.

For more human-readable output, run

    nosetests -c .noserc_local

Then navigate to `test_results/coverage/index.html` and open it in your browser. This is the HTML interface for the
coverage report, and is very useful when writing tests to make sure your code is being executed.

`.coveragerc` contains the settings for the [coverage](https://pypi.python.org/pypi/coverage) library, and can be adjusted to filter analysis.

coverage will give errors when `nosetests` is run on an empty project - basically saying that there is no data.

Documentation
------------------------

Documentation is created via the [Sphinx](https://pypi.python.org/pypi/Sphinx) package. The docs live in the `docs` folder and use [RestructuredText](http://docutils.sourceforge.net/rst.html).

All doc files should use the `.rst` extension.

To generate html docs

	cd docs
	make html
	
Then open `docs/_build/html/index.html` in your browser to view them.

`docs/conf.py` holds a number of settings for Sphinx, including theme, copyright and plugins.

Three plugins are already enabled:

* sphinx.ext.autodoc - By documenting your Python source code in ReST format, Sphinx can extract your docstrings into the docs.
* sphinx.ext.coverage - Gives you stats on how much of your code is documented.
* sphinx.ext.viewcode - Allows you to view your source code directly from the docs.

**ReST resources**

* [Primer](http://docutils.sourceforge.net/docs/user/rst/quickstart.html)
* [User Reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
* [Cheat Sheet](http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt)
