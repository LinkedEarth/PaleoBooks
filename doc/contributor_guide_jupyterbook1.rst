.. _contributor-guide-jupyterbook-1:

Contributor Guide for Jupyter Book 1
====================================

This secondary guide supports existing books built with Jupyter Book 1. New
books should normally follow the `main Jupyter Book 2 contributor guide
<contributor_guide.html>`_.

To make a great contribution you need to:

#. :ref:`write-your-book-jb1`
#. :ref:`build-your-book-jb1`
#. :ref:`run-remote-jb1` [Optional]
#. :ref:`Prepare your book to be added to the library <prepare-for-joining-the-library-jb1>`
#. :ref:`Submit a request to have your book added <submit-a-library-request-jb1>`

.. note::
    Consider sections 1 and 2 as a style guide. To be added to the library,
    you must have a fully published, hosted book with a landing page and the
    metadata described in section 4.

.. _write-your-book-jb1:

Write your book
---------------

Each library contribution needs well-organized content and a landing page (a
README or introduction). A template repository is available `here
<https://github.com/jordanplanders/paleobook_template>`_.

Content
*******

Structure your content into one or more sections, each addressing specific
themes or topics. Each section contains one or more notebooks (chapters) that
delve into the details of the respective theme.

How you organize your book is up to you. We have found Lifehacks and Science
Bits to be useful themes, as many of our chapters have fallen under those two
categories, but that is by no means the only way. For example, the sections of
a publication might be another sensible approach. This organizational
structure will not be visible in the gallery unless you specify it in
``chapter_meta.yml``.

*Lifehacks*
    Careful breakdowns of technically tricky, unintuitive, or cumbersome tasks,
    such as data-visualization tips or explanations of how to interact with a
    data product.

*Science Bits*
    Step-by-step discussions of analysis or exploratory workflows. These
    notebooks should focus more on scientific insights derived from analyses
    than on technical implementation.

*Paper Sections*
    Notebooks describing the research behind a published work. These might be
    organized by the sections of the publication or by the included figures.

.. note::
    Every notebook must have a level-one heading (one ``#``). The first such
    heading is used by default in the Jupyter Book table of contents. You may
    assign a different short name for the gallery in ``chapter_meta.yml``.

Landing Page
************

There is no required structure for your landing page, but the following
elements are useful (bold items are common section titles):

* **Title**: Clearly state the title of your Jupyter Book.
* **Author**: Provide information about the primary author or authors.
* **Contributors**: Check out `contrib.rocks
  <https://contrib.rocks/preview?repo=angular%2Fangular-ja>`_ for an HTML snippet
  with avatars for each contributor to your repository.
* **Funding Sources**: Include information about funding sources that supported
  the work in your book.
* **Quick Summary** (Byline): Provide a concise summary of your book. This is
  also a good place to include a formatted citation if the book has a DOI.
* **Motivation**: Offer an overview of the motivation behind building the book.
  Briefly introduce the science or technical skills explored in the chapters,
  relevant datasets, and projects with which the book is associated.
* **Structure**: Give a quick explanation of the content in each section.
* **References**: Include notes about publications associated with the book.

.. _build-your-book-jb1:

Build your book with Jupyter Book 1
-----------------------------------

Jupyter Book 1 uses two book files:

* ``_config.yml`` for book metadata and build settings
* ``_toc.yml`` for the table of contents

For working examples, see the C-iTRACE PaleoBook's `_config.yml
<https://github.com/LinkedEarth/citrace_paleobook/blob/main/_config.yml>`_ and
`_toc.yml
<https://github.com/LinkedEarth/citrace_paleobook/blob/main/_toc.yml>`_.

Follow the archived `Jupyter Book 1 documentation
<https://jupyterbook.org/v1/intro.html>`_ rather than the current Jupyter Book
2 quickstart.

In ``_config.yml``:

* Set ``repository.url``, ``repository.branch``, and, when needed,
  ``repository.path_to_book``.
* Reference the book logo under ``logo``. Keeping ``logo.png`` beside
  ``_config.yml`` is recommended.
* To prevent notebooks from executing during the build, include:

  .. code-block:: yaml

      execute:
        execute_notebooks: 'off'

In ``_toc.yml``, list the landing page as ``root`` and organize the remaining
files under ``chapters``, ``parts``, and ``sections``. TOC file values normally
omit ``.md`` and ``.ipynb`` extensions. For example:

.. code-block:: yaml

    format: jb-book
    root: intro
    parts:
      - caption: Science Bits
        chapters:
          - file: notebooks/example

Build the book with the Jupyter Book 1 environment and publish the generated
HTML using the hosting method appropriate to the project.

.. _run-remote-jb1:

Running your notebooks in the cloud [Optional]
----------------------------------------------

Imagine a world where every time you opened a scientific notebook, it just
worked. No dependency conflicts, no version mismatches, no endless
troubleshooting. You could explore, run, and reproduce the analysis exactly as
the original author intended--whether it was written yesterday or five years
ago. That is the power of containers. They capture the full computational
environment--Python version, libraries, and even system dependencies--ensuring
that your workflow is portable, consistent, and reproducible across time and
platforms. By wrapping science in containers, we free ourselves from the "it
works on my machine" trap and pave the way for truly shareable, reliable
computational research.

Now imagine a platform that takes this container and lets anyone run it in the
cloud. That is the beauty of `MyBinder <https://mybinder.org>`_. It can take a
container or repository environment and render the notebooks in a JupyterLab
environment. It does not require much work on your part.

* **Step 1**: Create a container and put it in a container registry such as
  `DockerHub <https://hub.docker.com>`_ or `Quay.io <https://quay.io>`_. We
  recommend Quay.io because it offers more free options for open science. The
  `2i2c image tutorial
  <https://2i2c.org/community-showcase/admin/howto/environment/hub-user-image-template-guide.html>`_
  explains one way to create custom images. This step is optional because
  MyBinder can create a container directly from an environment or requirements
  file in the repository. A pinned container can nevertheless protect the book
  against dependency changes over time.
* **Step 2**: To use a prebuilt image, create a ``binder`` folder containing
  the Dockerfile and ``config.json`` needed to identify the container. See the
  `coral-visualization example
  <https://github.com/khider/coral-visualization>`_.
* **Step 3**: Link and test the repository through `MyBinder
  <https://mybinder.org>`_. More help is available from the `LEAPFROGS module
  <https://linked.earth/LeapFROGS/module6>`_.
* **Step 4**: Configure ``launch_buttons`` in ``_config.yml`` according to the
  archived `Jupyter Book 1 launch-button documentation
  <https://jupyterbook.org/v1/interactive/launchbuttons.html>`_.

.. _prepare-for-joining-the-library-jb1:

Prepare for joining the library
-------------------------------

In order for your book to be added to the library, you need to provide some
additional information that the gallery uses to populate its fields.

#. In the same directory as ``_config.yml`` and ``_toc.yml``, create folders
   named ``meta_data`` and ``thumbnails``.
#. In ``meta_data``, create ``chapter_meta.yml``.
#. In ``thumbnails``, add one PNG or JPEG image for the book and one for each
   chapter.

.. note::
    YAML files are sensitive to indentation. Starting from a working example
    is strongly recommended.

In the gallery, the content of your book appears in two ways: as a single card
for the whole book and as individual cards for each selected chapter. Each card
contains a title, thumbnail image, and selection of tags. Each card is also
clickable and takes the reader to the relevant published page.

Book cards use:

* **book title, author, and description**: specified in ``chapter_meta.yml``
* **book URL**: specified in the gallery submission
* **book thumbnail**: named in ``chapter_meta.yml`` and stored in
  ``thumbnails``
* **book tags**: combined from the tags assigned to its chapters
* **book shortname tag**: the top-level ``shortname`` in
  ``chapter_meta.yml``, used to associate the book with its chapter cards

Chapter cards use:

* **chapter title**: ``shortname`` in ``chapter_meta.yml``
* **chapter URL**: constructed by matching ``filename`` in
  ``chapter_meta.yml`` to a ``file`` entry in ``_toc.yml``
* **chapter thumbnail**: named in ``chapter_meta.yml`` and stored in
  ``thumbnails``
* **chapter tags**: specified in ``chapter_meta.yml``
* **book shortname tag**: inherited from the top-level book metadata

Use the complete source path relative to ``_toc.yml``, without ``.ipynb`` or
``.md``. For example, this TOC entry:

.. code-block:: yaml

    - file: notebooks/lifehacks/pyODV

matches:

.. code-block:: yaml

    filename: notebooks/lifehacks/pyODV

The following top segment follows the `C-iTRACE chapter_meta.yml
<https://github.com/LinkedEarth/citrace_paleobook/blob/main/meta_data/chapter_meta.yml>`_
Jupyter Book 1 example:

.. code-block:: yaml

    shortname: C-iTRACE
    type: Paleobook
    thumbnail: thumbnail.png
    parts:
      - caption: Lifehacks
        chapters:
          - shortname: pyODV
            filename: pyODV
            thumbnail: pyodv_demo.png
            tags:
              domains:
                - oceanography
                - tracers
                - data viz
              packages:
                - xarray
                - matplotlib
                - pandas

The historical C-iTRACE metadata uses the unique basename ``pyODV``. The
gallery accepts that legacy shorthand, but the complete TOC-relative path is
recommended for new metadata because it remains unambiguous if two directories
contain notebooks with the same name.

The fields have the following meanings:

``title``
    The full title displayed on the book card when supplied in
    ``chapter_meta.yml``.
``author``
    The book author or authors displayed by the gallery when supplied in
    ``chapter_meta.yml``.
``description``
    A concise description for the book card.
``shortname``
    A short word or phrase used to associate the book with its chapter cards.
``type``
    The collection type. Use ``Paleobook`` unless another collection applies.
``thumbnail``
    The book-level thumbnail filename. If no extension is supplied, PNG is
    assumed.
``parts``
    Groups chapters by content type. A one-part book may instead put
    ``chapters`` at the top level.
``caption``
    The part name. It is also added to its chapters as a format tag.
``chapters``
    The list of notebooks to display as chapter cards.
``shortname`` (chapter)
    The chapter name displayed on its card.
``filename``
    The notebook path used in ``_toc.yml``, without ``.ipynb`` or ``.md``.
``thumbnail`` (chapter)
    The chapter thumbnail filename.
``tags``
    Gallery filters. ``domains`` describe subject matter, ``packages`` name
    software used, and format tags describe the chapter style.

Push the published book, ``_config.yml``, ``_toc.yml``,
``chapter_meta.yml``, and thumbnails to the repository before submitting it.

.. _submit-a-library-request-jb1:

Submit a library request
------------------------

Once you have a built and published Jupyter Book with gallery metadata,
`submit a request on GitHub
<https://github.com/LinkedEarth/PaleoBooks/issues/new?assignees=&labels=gallery+submission&projects=&template=gallery-submission.md&title=>`_.

Provide:

#. Repository name (for example, ``DISK-proxyComposite``)
#. Repository URL (for example,
   ``https://github.com/khider/DISK-proxyComposite``)
#. Branch (for example, ``main``)
#. URL of ``_config.yml`` (for example,
   ``https://github.com/khider/DISK-proxyComposite/blob/main/proxycomposite/_config.yml``)
#. Host domain (for example, ``https://khider.github.io``, not a specific page)
#. GitHub user or organization (for example, ``khider``)
#. Landing-page suffix (for example, ``intro.html``)
#. Complete published landing-page URL (for example,
   ``https://khider.github.io/DISK-proxyComposite/intro.html``)

The ``_config.yml`` URL tells the gallery where the book root is located. The
gallery then reads ``meta_data/chapter_meta.yml`` and ``_toc.yml`` from that
location.
