
.. _contributor-guide:

Contributor Guide
=================

To make a great contribution you need to:

#. :ref:`write-your-book`
#. :ref:`build-your-book`
#. :ref:`Prepare your book to be added to the library<prepare-for-joining-the-library>`
#. :ref:`Submit a request to have your book added<submit-a-library-request>`

.. note::
    Consider sections 1 and 2 (:ref:`write-your-book` and :ref:`build-your-book`) and as a style guide. In order to be added to the library, you must have a fully published, hosted book that includes a landing page file (markdown or similar) AND metadata that follows the structure described in section 3 (:ref:`Prepare your book to be added to the library<prepare-for-joining-the-library>`)!

.. _write-your-book:

Write your book
-----------------

Each library contribution needs well organized content and a landing page (a readme or intro).

Content:
*****************

Structure your content into one or more sections, each addressing specific themes or topics.
Each section contains one or more notebooks (chapters) that delve into the details of the respective theme.
How you organize your book is up to you. We have found Lifehacks and Science Bits to be useful themes, as many of our chapters have fallen under one of those two categories, but that is by no means the only way. For example, the sections of a publication might be another sensible approach. This organizational structure will not be visible in the gallery unless you specify it in the `chapter_meta.yml` file (see below for more details).

*Lifehacks*
    Careful breakdowns of technically tricky, unintuitive or cumbersome tasks, e.g., data visualization tips or explanations about how to interact with a data product.

*Science Bits*
    Step by step discussion of analysis or exploratory workflow. These notebooks should focus more on scientific insights derived from analyses than on technical implementation.

*Paper Sections*
    Notebooks describing the research behind a published work. These might be organized by the sections of the publication, or by the included figures.

.. note::
    Every notebook must have a level 1 header (one #). This header will be used in your JupyterBook table of contents. If your book has multiple level 1 headers, the first one will be used in your JupyterBook table of contents. You will have the opportunity to assign different names for the purpose of the gallery.

Landing Page:
*****************

There isn't a required structure for your landing page, but we have found that the following elements are appropriate (bolded items are common section titles):

* **Title**: Clearly state the title of your Jupyter book.
* **Quick Summary** (Byline): Provide a concise summary of your book. This also a good place to include a formatted citation for your book if it has a DOI.
* **Motivation**: Offer an overview of the motivation behind building the book. This section should briefly touch on the science or technical skills explored in your chapters. It might also include information about any datasets involved or projects your book is associated with.
* **Author**: Provide information about the primary author or authors of the book.
* **Contributors**: Check out `contrib.rocks`_ for an html snippet with avatars for each contributor to your JupyterBook repo.
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

* Include a copy of your book's thumbnail in the same directory as the `_config.yml` file and call it `logo.png`. This is specified in the `_config.yml` and naming/locating it in a predictable place will save a headache.

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

.. note::
    YAML files are very sensitive to indentation, so be careful when copying and pasting.

In the gallery, the content of your book will appear in two ways: as a single card for the whole book, and as individual cards for each chapter. Each card contains a title, a thumbnail image and a selection of tags. In addition, each card is clickable and will take a reader to the relevant page. The information for these cards is drawn from the YAML files.

Book cards will contain the following information:
    -  **book title**: specified in `_config.yml`
    -  **book url**: specified in information provided in the gallery submission form
    -  **book thumbnail**: specified in the `thumbnails` folder
    -  **book tags**: specified in `chapter_meta.yml`, encompassing all tags assigned to constituent chapters
    -  **book shortname tag**: specified in `chapter_meta.yml` as top level `shortname` and is used to associate the book with its chapters cards

Chapter cards will contain the following information:
    - **chapter title**: specified in `chapter_meta.yml` as `shortname`
    - **chapter url**: constructed from the book url and pointers associating `filename` specified in `chapter_meta.yml` to the relevant filename in the `_toc.yml`
    - **chapter thumbnail**: specified in the `thumbnails` folder
    - **chapter tags**: specified in `chapter_meta.yml`
    - **book shortname tag**: as mentioned above, this is used to associate the chapter with the book

Because chapter urls are constructed using information from the `_toc.yml`, it is important that the `filename` in `chapter_meta.yml` matches the filename associated with each `file` in the `_toc.yml`, and that the filename is unique within your book. For example, you may note have notebooks/lifehacks/mynotebook and notebooks/science_bits/mynotebook.

Additionally, a book is not required to have multiple `parts` in the `chapter_meta.yml` file. A "part" should be thought of as a content type (e.g. science bit, figure, method overview, tutorial). If your book is a single part, you can simply follow the top level book information (`shortname`, `type`, `thumbnail`) with `chapters:` and list the chapters as shown below. However, if the `chapter_meta.yml` includes parts, the part `caption` will be assigned to its chapters as a `format` tag. (Note: you may also specify format tags directly.)

**Reminder**: YAML files are very sensitive to indentation, so be careful when copying and pasting.

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
      - this top level short name is a short word or phrase that will be used to tag your book in the gallery. The title that appears on the book card in the gallery will be sourced from the _config.yml file.
    * - `type`
      - if your book is not a PaleoBook, note the collection it belongs to
    * - `thumbnail`
      - the name of the thumbnail image for *the whole book* (can be .png or .jpg, assumed to be .png if not indicated)
    * - parts
      - below this will be the content types your book is organized by (e.g., Lifehacks, Science Bits)
    * - `caption`
      - the name of the `part` (e.g., Lifehacks)
    * - chapters
      - below this will be the notebooks (chapters) included in this section
    * - `shortname`
      - the name of the chapter as you want it to appear on the chapter card
    * - `filename`
      - the name of the notebook (without `.ipynb`)
    * - `thumbnail`
      - the name of the thumbnail image for *this specific chapter* (can be .png or .jpg, assumed to be .png if not indicated)
    * - tags
      - below this are the tags (among three categories: domains, packages, format) assigned to the chapter card in the library (note: tags should be short but may include spaces)
    * - domains
      - below this are tags related to domain knowledge (e.g. isotopes, linear regression)
    * - packages
      - below this are tags for packages leveraged in the chapter (e.g. pyleoclim)
    * - format
      - below this are tags for the format of the chapter (e.g. science bit, peer-reviewed, lifehack, figure, etc.)


Now onto the next chapter! (The next `shortname` will refer to the next chapter.)


3. In the `thumbnails` folder, add one thumbnail for the book, and one thumbnail for each chapter (labeled according to the name indicated in `chapter_meta.yml`). All thumbnails should be of type .png or .jpg

Push these additional contributions to your github repo.

.. _submit-a-library-request:

Submit a library request
--------------------------

Once you have a fully built and published JupyterBook with extra metadata, `submit a request to be added on github`_!

.. _submit a request to be added on github: https://github.com/LinkedEarth/PaleoBooks/issues/new?assignees=&labels=gallery+submission&projects=&template=gallery-submission.md&title=

#. Name of the repository: *e.g., DISK-proxyComposite*
#. Repo url: *e.g., https://github.com/khider/DISK-proxyComposite*
#. Branch: *e.g., main*
#. Url of .config.yml: *e.g., https://github.com/khider/DISK-proxyComposite/blob/main/proxycomposite/_config.yml*
#. Host for the JupyterBook: *e.g., https://khider.github.io NOT https://khider.github.io/DISK-proxyComposite/intro.html*
#. User: *e.g., khider*
#. Landing suffix (name of the page you want users to land on): *e.g., intro.html*
#. Landing page url: *e.g., https://khider.github.io/DISK-proxyComposite/intro.html*