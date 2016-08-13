{{cookiecutter.project_name}}
{{cookiecutter.project_name | length*"="}}

{{cookiecutter.project_short_description}}

Setup
-----

Create a virtualenv and install the project:

.. code-block:: bash

    pyvenv env
    source env/bin/activate
    pip install -e .


Development
-----------

First, initialize the development database:

.. code-block:: bash

    python manage.py db upgrade head

To start the application, run:

.. code-block:: bash

    python manage.py serve

Testing
-------

Install tox:

.. code-block:: bash

    pip install tox

Run the tests against the python versions defined in the `tox.ini`:

.. code-block:: bash

    tox
