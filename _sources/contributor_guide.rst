.. _contributor-guide-jupyterbook-2:

Contributor Guide
=================

This is the main contributor guide for books built with Jupyter Book 2. If your
book still uses Jupyter Book 1, follow the `Jupyter Book 1 contributor guide
<contributor_guide_jupyterbook1.html>`_ instead.

.. toctree::
   :maxdepth: 1
   :hidden:

   contributor_guide_jupyterbook1

To make a great contribution you need to:

#. :ref:`write-your-book-jb2`
#. :ref:`build-your-book-jb2`
#. :ref:`run-remote-jb2` [Optional]
#. :ref:`Prepare your book to be added to the library <prepare-for-joining-the-library-jb2>`
#. :ref:`Submit a request to have your book added <submit-a-library-request-jb2>`

.. note::
    Consider sections 1 and 2 as a style guide. To be added to the library,
    you must have a fully published, hosted book with a landing page and the
    metadata described in section 4.

.. _write-your-book-jb2:

Write your book
---------------

Each library contribution needs well-organized content and a landing page (a
README or introduction). A template repository is available `here
<https://github.com/jordanplanders/paleobook_template>`_.

Content
*******

Structure your content into one or more sections, each addressing specific
themes or topics. Each section contains one or more notebooks or pages
(chapters) that delve into the details of the respective theme.

How you organize your book is up to you. We have found Lifehacks and Science
Bits to be useful themes, as many chapters fall under those two categories,
but that is by no means the only approach. The sections of a publication may
also provide a sensible structure. This organization will not be visible in
the gallery unless you specify it in ``chapter_meta.yml`` (see below).

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
    Every notebook or Markdown page must have a level-one heading (one ``#``).
    By default, Jupyter Book uses the page title or first heading in its table
    of contents. You may override that title in ``myst.yml`` and assign a
    different short name for the gallery in ``chapter_meta.yml``.

Landing Page
************

There is no required structure for your landing page, but the following
elements are useful (bold items are common section titles):

* **Title**: Clearly state the title of your Jupyter Book.
* **Author**: Provide information about the primary author or authors.
* **Contributors**: Check out `contrib.rocks`_ for an HTML snippet with avatars
  for contributors to your repository.
* **Funding Sources**: Identify funding that supported the work.
* **Quick Summary** (Byline): Give a concise summary. This is also a good place
  for a formatted citation if the book has a DOI.
* **Motivation**: Describe the scientific or technical motivation, relevant
  datasets, and associated projects.
* **Structure**: Briefly explain the content in each section.
* **References**: Note publications associated with the book.

.. _contrib.rocks: https://contrib.rocks/preview?repo=angular%2Fangular-ja

.. _build-your-book-jb2:

Build your book with Jupyter Book 2
-----------------------------------

Follow the `Jupyter Book 2 quickstart
<https://jupyterbook.org/stable/get-started/init/>`_. From the directory that
will contain the book configuration, initialize a project with:

.. code-block:: console

    jupyter book init

Jupyter Book 2 uses one main configuration file, ``myst.yml``. It contains the
book metadata, site options, and table of contents. The following shortened
example is adapted from the `Holocene CCM PaleoBook
<https://github.com/LinkedEarth/hol_temp_tsi_ccm_pb/blob/main/myst.yml>`_:

.. code-block:: yaml

    version: 1
    project:
      title: A Causal Examination of the Solar Influence on Holocene Climate
      description: |
        Convergent Cross-Mapping analysis testing whether Total Solar Irradiance
        causally influences Holocene temperature variability.
      authors:
        - name: Jordan P. Landers
        - name: Julien Emile-Geay
        - name: Alexander K. James
        - name: Stephan B. Munch
        - name: Deborah Khider
        - name: Edouard Bard
      github: https://github.com/LinkedEarth/hol_temp_tsi_ccm_pb
      toc:
        - file: intro.md
          title: Overview
        - title: "Part 1: Data Preparation & Exploration"
          children:
            - file: notebooks/0_Datasets/_overview.md
              title: Overview
            - file: notebooks/0_Datasets/1_setup__standardize_time_axes.ipynb
              title: Standardize Time Axes
    site:
      template: book-theme
      options:
        logo: logo.png
        logo_text: "Holocene Sun-Climate causality with CCM"
        hide_authors: true
        folders: true

Important details:

* Paths in ``project.toc`` are relative to ``myst.yml`` and include their file
  extensions.
* The first file in ``project.toc`` becomes the book's landing page.
* Use ``children`` for nested pages.
* ``site.options.folders: true`` preserves source folders in published page
  URLs. This is recommended when the book contains repeated filenames such as
  several ``overview.md`` pages.
* Include the book logo beside ``myst.yml`` (``logo.png`` is the recommended
  name) and reference it under ``site.options.logo``.
* Jupyter Book 2 does not execute notebooks during an ordinary build. Pass
  ``--execute`` only when you intentionally want to rerun them.

Preview the book locally with:

.. code-block:: console

    jupyter book start

Build static HTML with:

.. code-block:: console

    jupyter book build --html

For GitHub Pages, ``jupyter book init --gh-pages`` can generate a deployment
workflow. Other static hosts may publish the resulting ``_build/html``
directory. When publishing below a URL subdirectory, configure ``BASE_URL`` as
described in the Jupyter Book publishing documentation.

.. _run-remote-jb2:

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

* **Step 1**: Describe a reproducible environment in the repository. MyBinder
  can build from an environment or requirements file. You may instead create a
  container and publish it to a registry such as `DockerHub
  <https://hub.docker.com>`_ or `Quay.io <https://quay.io>`_.
  The `2i2c image tutorial
  <https://2i2c.org/community-showcase/admin/howto/environment/hub-user-image-template-guide.html>`_
  provides one approach.
* **Step 2**: If you use a prebuilt container, add the Binder configuration
  needed to locate it. See the `coral-visualization example
  <https://github.com/khider/coral-visualization>`_.
* **Step 3**: Test the repository through `MyBinder
  <https://mybinder.org>`_. Additional guidance is available from the
  `LEAPFROGS module <https://linked.earth/LeapFROGS/module6>`_.
* **Step 4**: Enable the Jupyter Book 2 launch integration in ``myst.yml``.

For example:

.. code-block:: yaml

    project:
      github: https://github.com/owner/repository
      jupyter:
        binder:
          url: https://mybinder.org
          repo: owner/repository
          ref: main

Launch-button and in-page execution behavior is still evolving, so consult the
current `MyST launch documentation
<https://mystmd.org/guide/website-launch-buttons>`_ when enabling it.

.. _prepare-for-joining-the-library-jb2:

Prepare for joining the library
-------------------------------

In order for your book to be added to the library, you need to provide some
additional information that the gallery uses to populate its fields.

#. In the same directory as ``myst.yml``, create folders named ``meta_data``
   and ``thumbnails``.
#. In ``meta_data``, create ``chapter_meta.yml``. Starting from a working
   example is recommended because YAML indentation is significant.
#. In ``thumbnails``, add one image for the book and one for each chapter.
   Images may be PNG or JPEG files.

In the gallery, the content of your book appears in two ways: as a single card
for the whole book and as individual cards for each selected chapter. Each card
contains a title, thumbnail image, and selection of tags. Each card is also
clickable and takes the reader to the relevant published page.

Book cards use the following information:

* **book title, author, and description**: specified in ``chapter_meta.yml``
* **book URL**: specified in the gallery submission
* **book thumbnail**: named in ``chapter_meta.yml`` and stored in
  ``thumbnails``
* **book tags**: combined from the chapter tags
* **book shortname tag**: the top-level ``shortname`` in
  ``chapter_meta.yml``

Chapter cards use:

* **chapter title**: ``shortname`` in ``chapter_meta.yml``
* **chapter URL**: constructed by matching ``filename`` in
  ``chapter_meta.yml`` to ``project.toc`` in ``myst.yml``
* **chapter thumbnail**: named in ``chapter_meta.yml`` and stored in
  ``thumbnails``
* **chapter tags**: specified in ``chapter_meta.yml``
* **book shortname tag**: inherited from the top-level book metadata

The safest ``filename`` convention is the complete source path relative to
``myst.yml``, matching the TOC's ``file`` value but omitting ``.ipynb`` or
``.md``. The following real pairing comes from the Holocene CCM PaleoBook:

.. code-block:: yaml

    # myst.yml
    project:
      toc:
        - file: intro.md
        - title: "Part 1: Data Preparation & Exploration"
          children:
            - file: notebooks/0_Datasets/1_setup__standardize_time_axes.ipynb

    # meta_data/chapter_meta.yml
    filename: notebooks/0_Datasets/1_setup__standardize_time_axes

Using complete paths prevents ambiguity when files in different directories
share the same name. The gallery converts the source path to the URL generated
by Jupyter Book 2; do not put the published URL slug in ``filename``.

Here is the corresponding top segment, adapted from the `Holocene CCM chapter
metadata
<https://github.com/LinkedEarth/hol_temp_tsi_ccm_pb/blob/main/meta_data/chapter_meta.yml>`_.
It includes the recommended gallery ``title`` and ``author`` fields so a pure
Jupyter Book 2 submission does not depend on a legacy ``_config.yml``:

.. code-block:: yaml

    title: A Causal Examination of the Solar Influence on Holocene Climate
    author: Jordan P. Landers, Julien Emile-Geay, Alexander K. James, Stephan B. Munch, Deborah Khider, Edouard Bard
    shortname: "HoloCCM"
    type: Paleobook
    description: "Causal analysis of the TSI-temperature relationship over the Holocene using Convergent Cross-Mapping"
    thumbnail: logo.png
    parts:
      - caption: "Data Preparation & Exploration"
        chapters:
          - shortname: "Standardize time axes"
            filename: "notebooks/0_Datasets/1_setup__standardize_time_axes"
            thumbnail: standardize_ts.png
            tags:
              domains: ['common time', 'data-processing']
              packages: [xarray, pandas]

The fields have the following meanings:

``title``
    The full title displayed on the book card.
``author``
    The book author or authors displayed by the gallery.
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
    The list of pages to display as chapter cards.
``shortname`` (chapter)
    The chapter name displayed on its card.
``filename``
    The complete source path, without ``.ipynb`` or ``.md``.
``thumbnail`` (chapter)
    The chapter thumbnail filename.
``tags``
    Gallery filters. ``domains`` describe subject matter, ``packages`` name
    software used, and format tags describe the chapter style.

The full publication title and authors also belong in ``myst.yml`` as standard
Jupyter Book metadata. Repeating them in ``chapter_meta.yml`` currently makes
the gallery ingestion contract explicit and removes any reliance on a legacy
``_config.yml``. The remaining fields supply the gallery shortname,
description, thumbnails, chapter selection, and tags.

Push the published book, ``myst.yml``, ``chapter_meta.yml``, and thumbnails to
the repository before submitting it.

.. _submit-a-library-request-jb2:

Submit a library request
------------------------

Once you have a built and published Jupyter Book with gallery metadata,
`submit a request on GitHub
<https://github.com/LinkedEarth/PaleoBooks/issues/new?assignees=&labels=gallery+submission&projects=&template=gallery-submission.md&title=>`_.

Provide:

#. Repository name (for example, ``hol_temp_tsi_ccm_pb``)
#. Repository URL (for example,
   ``https://github.com/LinkedEarth/hol_temp_tsi_ccm_pb``)
#. Branch (for example, ``main``)
#. URL of ``myst.yml`` (for example,
   ``https://github.com/LinkedEarth/hol_temp_tsi_ccm_pb/blob/main/myst.yml``)
#. Host domain (not a specific page URL)
#. GitHub user or organization (for example, ``LinkedEarth``)
#. Landing-page suffix, if applicable
#. Complete published landing-page URL

The ``myst.yml`` URL tells the gallery where the book root is located. The
gallery then reads ``meta_data/chapter_meta.yml`` and the inline
``project.toc`` from that location.
