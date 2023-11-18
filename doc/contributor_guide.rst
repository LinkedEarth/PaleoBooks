
.. _contributor-guide:

Contributor Guide
=================

To make a great contribution you need to:

#. :ref:`write-your-book`
#. :ref:`build-your-book`
#. :ref:`Prepare your book to be added to the library<prepare-for-joining-the-library>`
#. :ref:`Submit a request to have your book added<submit-a-library-request>`

.. note::
    Consider sections 1 and 2 as a style guide. In order to be added to the library, you must have:
    #. a fully published and hosted book and
    #. metadata that follows the structure described in section 3!

.. _write-your-book:

Write your book
-----------------

Each library contribution needs well organized content and a landing page (a readme or intro).

Content:
*****************

Structure your content into one or more sections, each addressing specific themes or topics.
Each section contains one or more notebooks (chapters) that delve into the details of the respective theme.
How you organize your book is up to you. We have found Lifehacks and Science Bits to be useful sections, as our chapters have generally fallen under one of those two categories, but that is not the only way, and the best way is whatever way is most intuitive given your content.

*Lifehacks*
    Careful breakdowns of technically tricky, unintuitive or cumbersome tasks, e.g., data visualization tips or explanations about how to interact with a data product

*Science Bits*
    Step by step discussion of analysis or exploratory workflow, for example

*Paper*
    Notebooks describing the research behind a published work

.. note::
    Every notebook must have a level 1 header. If it has more than one, the first one will be taken as the title of the chapter *within your JupyterBook* (you can customize this as far as the library is concerned, but you may find this to be a useful tip as far as your book goes.)

Landing Page:
*****************

There isn't a required structure for your landing page, but we have found that the following elements are appropriate (bolded items are common section titles):

* Title: Clearly state the title of your Jupyter book.
* Quick Summary (Byline): Provide a concise summary of your book. This also a good place to include a formatted citation for your book if it has a DOI.
* **Motivation**: Offer an overview of the motivation behind building the book. This section should briefly touch on the science or technical skills explored in your chapters. It might also include information about any datasets involved or projects your book is associated with.
* **Author**: Provide information about the primary author or authors of the book.
* **Contributors**: Check out `contrib.rocks`_ for an html snippet with avatars for each contributor to your jupyterbook repo.
* **Structure**: Give a quick explanation of the content in each section of the book (more on this below).
* **References**: Include notes about any publications associated with the book.

.. _contrib.rocks: https://contrib.rocks/preview?repo=angular%2Fangular-ja


.. _build-your-book:

Build your book
----------------

There are various ways to go about this. The most straight forward is to follow the `Create your first book tutorial`_ on the JupyterBook website.

.. _Create your first book tutorial: https://jupyterbook.org/en/stable/start/your-first-book.html

A couple of notes:

* The tutorial project structure is very simple. For an example of a slightly more complex table of contents (`_toc.yml`), `look here`_.
* Make sure to modify the `_config.yml`. Here is `an example`_ to help.
    - make sure that `path_to_book` points to the directory in your repo where your book lives (in the example, this is *proxycomposite*)
    - `gh-import` will prompt you for your github username and password, and you will need to follow `these instructions about personal access tokens`_ to get a more secure password (github will not accept standard passwords for this purpose)
    - if you don't want the books to execute on build, include:

    .. code-block::

        execute:
            execute_notebooks: 'off'

* Include a copy of your book's thumbnail in the directory where your book is and call it `logo.png`. This is specified in the `_config.yml` and naming/locating it in a predictable place will save a headache.

.. _an example: https://github.com/khider/DISK-proxyComposite/blob/main/proxycomposite/_config.yml
.. _look here: https://github.com/LinkedEarth/citrace_paleobook/blob/main/_toc.yml
.. _these instructions about personal access tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic

.. _prepare-for-joining-the-library:

Prepare for joining the library
-------------------------------

In order for your book to be added to the library, you will need to provide some additional information we will use to populate various fields.

#. In the same directory as the _config.yml file, make a folder called `meta_data` and a folder called `thumbnails`
#. In `meta_data`, make a file called `chapter_meta.yml` and copy and paste the contents of `the C-iTrace PaleoBook chapter_meta.yml`_ to use as template. (The formatting of these files cam be particular, so it highly encouraged to start from one that is functional.)

.. _the C-iTrace PaleoBook chapter_meta.yml: https://github.com/LinkedEarth/citrace_paleobook/blob/main/meta_data/chapter_meta.yml

Here is the top segment:

.. code-block::

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
                - cartopy
                - pandas
                - seaborn
          - shortname: data_on_a_model_grid


This table provides an explanation of each element:

.. list-table::
    :header-rows: 1

    * - yml excerpt
      - explanation
    * - `shortname`
      - short word or phrase for your book
    * - `type`
      - if your book is not a PaleoBook, note the collection it belongs to
    * - `thumbnail`
      - the name of the thumbnail image for *the whole book* (assumed to be .png, if not indicated)
    * - parts
      - below this will be the sections your book is organized into
    * - `caption`
      - the name of the `part` (e.g. Lifehacks)
    * - chapters
      - below this will be the notebooks (chapters) included in this section
    * - `shortname`
      - the name of the chapter as you want it to appear on the chapter card
    * - `filename`
      - the name of the notebook (without `.ipynb`)
    * - `thumbnail`
      - the name of the thumbnail image for *this specific chapter* (assumed to be .png, if not indicated)
    * - tags
      - below this are the tags (among three categories: domains, packages, format) assigned to the chapter card in the library (note: tags should be short but may include spaces)
    * - domains
      - below this are tags related to domain knowledge (e.g. isotopes, linear regression)
    * - packages
      - below this are tags for packages leveraged in the chapter (e.g. pyleoclim)


Now onto the next chapter! (The next `shortname` will refer to the next chapter.)


3. In the `thumbnails` folder, add one thumbnail for the book, and one thumbnail for each chapter (labeled according to the name indicated in `chapter_meta.yml`)

Push these additional contributions to your github repo.

.. _submit-a-library-request:

Submit a library request
--------------------------

Once you have a fully built and published JupyterBook with extra metadata, `submit a request to be added on github`_!

.. _submit a request to be added on github: https://github.com/LinkedEarth/PaleoBooks/issues/new?assignees=&labels=gallery+submission&projects=&template=gallery-submission.md&title=

#. Name of the repository: *e.g., DISK-proxyComposite*
#. Repo url: *e.g., https://github.com/khider/DISK-proxyComposite*
#. Host for the JupyterBook: *e.g., https://khider.github.io NOT https://khider.github.io/DISK-proxyComposite/intro.html*
#. User: *e.g., khider*
#. Landing suffix (name of the page you want users to land on): *e.g., intro.html*
