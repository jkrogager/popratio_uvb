
Cosmic Extragalactic Background for PopRatio
============================================

The original implementation of the extragalactic background field
in PopRatio `(Silva & Viegas 2001) <https://arxiv.org/abs/astro-ph/0010533>`_
uses the model from Madau, Haardt & Rees (1999). Since then various
improved models have emerged, e.g., the updated Haardt & Madau (2012)
or `Khaire & Srianand (2018) <https://arxiv.org/abs/1801.09693>`_.
Here I present the implementation of the Khaire & Srianand (2018; KS18)
extragalctic background field for use in PopRatio.

The original code is available at the `PopRatio webpage <http://www.ignacioalex.com/popratio/>`_.

If you use this patch in your work, please cite my paper on arXiv
and of course cite the original paper by
`(Silva & Viegas 2001) <https://arxiv.org/abs/astro-ph/0010533>`_.

Installation
============

The patch is given in `FieldInt_KS18.f90`. In order to compile this in PopRatio
you should copy this file to the source directory of PopRatio and rename the
file to `FieldInt.f90` (I recommend that you keep a backup of the original file):

.. code-block:: bash

    cp FieldInt_KS18.f90 /path/to/popratio
    cd /path/to/popratio
    mv FieldInt.f90 FieldInt_orig.f90
    mv FieldInt_KS18.f90 FieldInt.f90

Hereafter, you just need to change the function call to ``Fuvb`` in PopRatio.f90.
Find all the calls to ``Fuvb``, if you haven't changed anything in PopRatio.f90
before there will only be one around line 600, and change the call as follows:

.. code::

    Fuvb(lambda,z,3) --> Fuvb(lambda,z)

That's it! You are now ready to compile the code and run popratio.
