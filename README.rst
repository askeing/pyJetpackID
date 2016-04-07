pyJetpackID
===========
.. image:: https://travis-ci.org/askeing/pyJetpackID.svg?branch=master
    :target: https://travis-ci.org/askeing/pyJetpackID

Takes the Jetpack add-on manifest object, and returns the add-on ID.

Usage
-----

.. code-block:: python

    from jetpackid.jetpackid import JetpackID

    file_path = '/path/to/package.json'
    JetpackID.get_id(file_path)

    manifest = dict(name="JETPACK_ID")
    JetpackID.get_id(manifest) # @JETPACK_ID
