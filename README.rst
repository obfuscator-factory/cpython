=============================
Obfuscated Python Interpreter
=============================

> This is a proof of cocnept, use at your own risk
> This is a proof of concept, no good engineering here
> This is a proof concept, always repeat warnig twice

What is it?
-----------

This is a proof of concept for automatic generation of custom, obfuscated
Python interpreter. Run::

    $ mkdir _build && cd _build
    $ ../configure --help

And be amazed in front of the new options to enable/disable Interpreter
obfuscations.

Notes
-----

Some obfuscation limit the kind of code you can run with your custom
interpreter.

The ``--enable-gen-opcode`` flag requires a special file
``obfuscate/most_used_opcodes``. You can generate it using a set of ``pyc`` and
the script in ``obfuscate/visit_bytecode.py``, as in::

    $ python obfuscate/visit_bytecode.py obfuscate/most_used_opcodes my.pyc another.pyc

Once this file is generated, run::

    $ make

In order to modify existing ``pyc`` to use the new opcodes, run::

    $ python obfuscate/rewrite_bytecode.py in.pyc out.pyc obfuscate/most_used_opcodes

Credits
-------

- Serge Guelton <sguelton@quarkslab.com>
- Nicolas Szlifierski <nicoals.szlifierski@telecom-bretagne.eu>
