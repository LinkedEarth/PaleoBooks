


=====================


Gallery
========

PaleoBooks is a compendium of digital resources to bridge the gap between paleoclimate observations and models, and between past, present and future. The goal is as much to encourage adoption of open-source, free languages like R and Python by the observational paleoscience community as it is to encourage the modeling community to leverage the unique information coming from paleo archives.

The scholarly objects shown below are of several types:

* Tutorials on how to overcome a particular technical difficulty (“Life Hacks”)
* Tutorials on how to leverage open-source code to achieve easier, more transparent, or more powerful scientific workflows (“Science Bits”)
* Examples of novel paleoscience using the Python ecosystem e.g. as turn-key supplementary material from recent publications (“Papers”)

In the following, “PaleoBooks” refers to curated collections of Jupyter Notebooks organized around various themes. “Chapters” refers to the components of these PaleoBooks. A system of tags allows both PaleoBooks and individual chapters to be associated with one another based on individual themes or methodologies, in addition to their host PaleoBook. These tags enable searching along 3 directions:

* “Domains” refers to scientific themes or methodologies
* “Formats” refers to the type of resource (Life Hacks, Science Bits, or Papers)
* “Packages” refers to the packages being used in each notebook (e.g. Xarray)

The gallery below is a work in progress, and we encourage you to :ref:`contribute<contributor-guide>` your own analyses if you think they might bring enlightenment to, and/or ease the life of, fellow scientists.



.. raw:: html

    <div class="d-sm-flex mt-3 mb-4">
    <div class="d-flex gallery-menu">
    </div>
    <div class="ml-auto d-flex">
    <div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="bookDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Book</button>
    <ul class="dropdown-menu" aria-labelledby="bookDropdown"><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=2k-proxy-composite onchange="change();">&nbsp;2k Proxy Composite</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=asian-speleothem-coherency onchange="change();">&nbsp;Asian Speleothem Coherency</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=c-itrace onchange="change();">&nbsp;C-iTRACE</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=coral-sr/ca-calibration onchange="change();">&nbsp;Coral Sr/Ca calibration</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=detecting-paleoclimate-transitions-with-lerm onchange="change();">&nbsp;Detecting Paleoclimate Transitions with LERM</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=lmr-cmip6 onchange="change();">&nbsp;LMR-CMIP6</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=paleoensembles onchange="change();">&nbsp;PaleoEnsembles</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=paleopca onchange="change();">&nbsp;PaleoPCA</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=prototypewmg onchange="change();">&nbsp;PrototypeWMG</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=pyleoclim-science onchange="change();">&nbsp;Pyleoclim science</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=geochronr onchange="change();">&nbsp;geoChronR</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Domains</button>
    <ul class="dropdown-menu" aria-labelledby="domainsDropdown"><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=aws onchange="change();">&nbsp;AWS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=bayesian-statistics onchange="change();">&nbsp;Bayesian Statistics</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=c14 onchange="change();">&nbsp;C14</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cmip6 onchange="change();">&nbsp;CMIP6</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=calibration onchange="change();">&nbsp;Calibration</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=common-era onchange="change();">&nbsp;Common Era</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=deglaciation onchange="change();">&nbsp;Deglaciation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=holocene-climate onchange="change();">&nbsp;Holocene climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=lmr onchange="change();">&nbsp;LMR</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=lipd onchange="change();">&nbsp;LiPD</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=mystery-interval onchange="change();">&nbsp;Mystery Interval</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=pca onchange="change();">&nbsp;PCA</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=pmip onchange="change();">&nbsp;PMIP</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=pamodaco onchange="change();">&nbsp;PaMoDaCo</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoceanography onchange="change();">&nbsp;Paleoceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleocenography onchange="change();">&nbsp;Paleocenography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sr/ca onchange="change();">&nbsp;Sr/Ca</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=statistics onchange="change();">&nbsp;Statistics</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=volcanic-input onchange="change();">&nbsp;Volcanic Input</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=age-modeling onchange="change();">&nbsp;age modeling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=age-uncertainty onchange="change();">&nbsp;age uncertainty</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=calibration onchange="change();">&nbsp;calibration</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cloud-ready-data onchange="change();">&nbsp;cloud-ready data</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=clustering onchange="change();">&nbsp;clustering</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=coordinate-systems onchange="change();">&nbsp;coordinate systems</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=coral onchange="change();">&nbsp;coral</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=correlation onchange="change();">&nbsp;correlation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cross-wavelet-analysis onchange="change();">&nbsp;cross-wavelet analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-analysis onchange="change();">&nbsp;data analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-assimilation onchange="change();">&nbsp;data assimilation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-viz onchange="change();">&nbsp;data viz</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-wrangling onchange="change();">&nbsp;data wrangling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=dimension-reduction onchange="change();">&nbsp;dimension reduction</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=end onchange="change();">&nbsp;eNd</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=endmember-mixing onchange="change();">&nbsp;endmember mixing</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=ensemble onchange="change();">&nbsp;ensemble</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=insolation onchange="change();">&nbsp;insolation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=machine-learning onchange="change();">&nbsp;machine learning</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=mapping onchange="change();">&nbsp;mapping</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=model-output onchange="change();">&nbsp;model output</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=model-data-comparison onchange="change();">&nbsp;model-data comparison</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=modeling onchange="change();">&nbsp;modeling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoceanography onchange="change();">&nbsp;paleoceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoclimate onchange="change();">&nbsp;paleoclimate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoclimatology onchange="change();">&nbsp;paleoclimatology</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=proxy-composite onchange="change();">&nbsp;proxy composite</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=reconstruction onchange="change();">&nbsp;reconstruction</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=regression onchange="change();">&nbsp;regression</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=spectral-analysis onchange="change();">&nbsp;spectral analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=statistics onchange="change();">&nbsp;statistics</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=temperature onchange="change();">&nbsp;temperature</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=tidyverse onchange="change();">&nbsp;tidyverse</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=timeseries-modeling onchange="change();">&nbsp;timeseries modeling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=tracers onchange="change();">&nbsp;tracers</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=uncertainty-quantification onchange="change();">&nbsp;uncertainty quantification</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=visualization onchange="change();">&nbsp;visualization</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=watermass-geometry onchange="change();">&nbsp;watermass geometry</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=wavelet-analysis onchange="change();">&nbsp;wavelet analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=wavelets onchange="change();">&nbsp;wavelets</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="formatsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Formats</button>
    <ul class="dropdown-menu" aria-labelledby="formatsDropdown"><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=calibration onchange="change();">&nbsp;Calibration</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=core-methods onchange="change();">&nbsp;Core Methods</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=data-manipulation onchange="change();">&nbsp;Data Manipulation</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=exploring-the-data onchange="change();">&nbsp;Exploring the Data</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=extensions onchange="change();">&nbsp;Extensions</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=extras onchange="change();">&nbsp;Extras</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=getting-started onchange="change();">&nbsp;Getting Started</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=lifehacks onchange="change();">&nbsp;Lifehacks</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=loading-data onchange="change();">&nbsp;Loading Data</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=main-analysis onchange="change();">&nbsp;Main Analysis</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=motivation onchange="change();">&nbsp;Motivation</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=paleoclimate-applications onchange="change();">&nbsp;Paleoclimate Applications</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=plume-distance onchange="change();">&nbsp;Plume Distance</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=science-bits onchange="change();">&nbsp;Science Bits</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=temporal-interpretation onchange="change();">&nbsp;Temporal Interpretation</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="languageDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Language</button>
    <ul class="dropdown-menu" aria-labelledby="languageDropdown"><li><label class="dropdown-item checkbox language"><input type="checkbox" rel=r onchange="change();">&nbsp;R</label></li><li><label class="dropdown-item checkbox language"><input type="checkbox" rel=python onchange="change();">&nbsp;python</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Packages</button>
    <ul class="dropdown-menu" aria-labelledby="packagesDropdown"><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=aws onchange="change();">&nbsp;AWS</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=great-tables onchange="change();">&nbsp;Great Tables</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ammonyte onchange="change();">&nbsp;ammonyte</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=arviz onchange="change();">&nbsp;arviz</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=basemap onchange="change();">&nbsp;basemap</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cartopy onchange="change();">&nbsp;cartopy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cfr onchange="change();">&nbsp;cfr</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=climlab onchange="change();">&nbsp;climlab</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=dplyr onchange="change();">&nbsp;dplyr</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=eofs onchange="change();">&nbsp;eofs</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geochronr onchange="change();">&nbsp;geoChronR</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ggplot2 onchange="change();">&nbsp;ggplot2</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake onchange="change();">&nbsp;intake</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ipywidgets onchange="change();">&nbsp;ipywidgets</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=lipdr onchange="change();">&nbsp;lipdR</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=matplotlib onchange="change();">&nbsp;matplotlib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=numpy onchange="change();">&nbsp;numpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=oxcaar onchange="change();">&nbsp;oxcAAR</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pandas onchange="change();">&nbsp;pandas</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pens onchange="change();">&nbsp;pens</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=purrr onchange="change();">&nbsp;purrr</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pylipd onchange="change();">&nbsp;pyLiPD</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pyleoclim onchange="change();">&nbsp;pyleoclim</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pylipd onchange="change();">&nbsp;pylipd</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pymc onchange="change();">&nbsp;pymc</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=readr onchange="change();">&nbsp;readr</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=scikit-learn onchange="change();">&nbsp;scikit-learn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=scipy onchange="change();">&nbsp;scipy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=seaborn onchange="change();">&nbsp;seaborn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=sqlalchemy onchange="change();">&nbsp;sqlalchemy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=statsmodel onchange="change();">&nbsp;statsmodel</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=statsmodels onchange="change();">&nbsp;statsmodels</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;xarray</label></li></ul>
    </div>


    </div>
    </div>
    <script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>


+++++++++++++++
PaleoBooks
+++++++++++++++

.. grid:: 1 2 2 2


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace c14 deglaciation lifehacks mystery-interval paleoceanography science-bits cartopy clustering coordinate-systems data-viz end intake machine-learning matplotlib model-output oceanography pandas python scikit-learn seaborn tracers watermass-geometry xarray
                        :outline: teal
                    
                        .. card:: C-iTrace Paleobook :bdg-danger:`C-iTRACE` :bdg-teal:`python`
                            :link: https://linked.earth/citrace_paleobook/README.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-emerald:`data viz` :bdg-emerald:`coordinate systems` :bdg-emerald:`clustering` :bdg-emerald:`machine learning` :bdg-emerald:`tracers` :bdg-emerald:`oceanography` :bdg-emerald:`Paleoceanography` :bdg-emerald:`C14` :bdg-emerald:`Mystery Interval` :bdg-emerald:`watermass geometry` :bdg-emerald:`Deglaciation` :bdg-emerald:`eNd` :bdg-emerald:`model output`, :bdg-success:`matplotlib` :bdg-success:`scikit-learn` :bdg-success:`cartopy` :bdg-success:`seaborn` :bdg-success:`xarray` :bdg-success:`pandas` :bdg-success:`intake`, :bdg-primary:`Lifehacks` :bdg-primary:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: aws aws cmip6 holocene-climate lmr lmr-cmip6 lifehacks science-bits volcanic-input cartopy cloud-ready-data coordinate-systems data-viz intake ipywidgets matplotlib model-output pandas pyleoclim python xarray
                        :outline: teal
                    
                        .. card:: LMR-CMIP6 Paleobook :bdg-danger:`LMR-CMIP6` :bdg-teal:`python`
                            :link: https://linked.earth/LMR_CMIP_paleobook/README.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-emerald:`LMR` :bdg-emerald:`data viz` :bdg-emerald:`coordinate systems` :bdg-emerald:`CMIP6` :bdg-emerald:`cloud-ready data` :bdg-emerald:`Volcanic Input` :bdg-emerald:`Holocene climate` :bdg-emerald:`AWS` :bdg-emerald:`model output`, :bdg-success:`pyleoclim` :bdg-success:`ipywidgets` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`xarray` :bdg-success:`intake` :bdg-success:`pandas` :bdg-success:`AWS`, :bdg-primary:`Lifehacks` :bdg-primary:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: 2k-proxy-composite science-bits cfr numpy pandas proxy-composite pyleoclim python seaborn temperature
                        :outline: teal
                    
                        .. card:: Reproducing the Hockey Stick - Proxy composite over the past 2,000 years using the cfr package :bdg-danger:`2k Proxy Composite` :bdg-teal:`python`
                            :link: https://khider.github.io/DISK-proxyComposite/intro.html
                            :img-top: https://raw.githubusercontent.com/khider/DISK-proxyComposite/main/proxycomposite/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-emerald:`temperature` :bdg-emerald:`proxy composite`, :bdg-success:`pyleoclim` :bdg-success:`cfr` :bdg-success:`seaborn` :bdg-success:`numpy` :bdg-success:`pandas`, :bdg-primary:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: prototypewmg science-bits basemap clustering endmember-mixing matplotlib pandas python scikit-learn scipy sqlalchemy tracers watermass-geometry
                        :outline: teal
                    
                        .. card:: Watermass Geometry Proto exercise :bdg-danger:`PrototypeWMG` :bdg-teal:`python`
                            :link: https://jordanplanders.github.io/past_life_wmg/intro.html
                            :img-top: https://raw.githubusercontent.com/jordanplanders/past_life_wmg/main/ancient_wmgr_book/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-emerald:`clustering` :bdg-emerald:`tracers` :bdg-emerald:`endmember mixing` :bdg-emerald:`watermass geometry`, :bdg-success:`matplotlib` :bdg-success:`scikit-learn` :bdg-success:`basemap` :bdg-success:`sqlalchemy` :bdg-success:`scipy` :bdg-success:`pandas`, :bdg-primary:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras main-analysis ammonyte data-viz matplotlib pyleoclim python
                        :outline: teal
                    
                        .. card:: Detecting paleoclimate transitions with Laplacian Eigenmaps of Recurrence Matrices (LERM) :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/intro.html
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow.png
                            
                            :bdg-emerald:`data viz`, :bdg-success:`ammonyte` :bdg-success:`matplotlib` :bdg-success:`pyleoclim`, :bdg-primary:`Main Analysis` :bdg-primary:`Extras`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits age-uncertainty cartopy climlab correlation cross-wavelet-analysis insolation model-output model-data-comparison paleoceanography paleoclimate pyleoclim pylipd python spectral-analysis wavelet-analysis xarray
                        :outline: teal
                    
                        .. card:: Reproducible workflows using the Pyleoclim package :bdg-danger:`Pyleoclim science` :bdg-teal:`python`
                            :link: https://linked.earth/PyleoclimPaper/README.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-emerald:`spectral analysis` :bdg-emerald:`insolation` :bdg-emerald:`paleoceanography` :bdg-emerald:`wavelet analysis` :bdg-emerald:`model-data comparison` :bdg-emerald:`correlation` :bdg-emerald:`cross-wavelet analysis` :bdg-emerald:`age uncertainty` :bdg-emerald:`paleoclimate` :bdg-emerald:`model output`, :bdg-success:`pyleoclim` :bdg-success:`climlab` :bdg-success:`cartopy` :bdg-success:`pylipd` :bdg-success:`xarray`, :bdg-primary:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: bayesian-statistics calibration calibration coral-sr/ca-calibration getting-started great-tables paleocenography sr/ca statistics arviz calibration coral matplotlib paleoceanography pandas pyleoclim pymc python statsmodel
                        :outline: teal
                    
                        .. card:: Coral Sr/Ca Calibration - An Example from Dry Tortugas :bdg-danger:`Coral Sr/Ca calibration` :bdg-teal:`python`
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/intro.html
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/coral_logo.jpg
                            :img-alt: coral_logo.jpg
                            
                            :bdg-emerald:`Bayesian Statistics` :bdg-emerald:`coral` :bdg-emerald:`paleoceanography` :bdg-emerald:`Calibration` :bdg-emerald:`Paleocenography` :bdg-emerald:`Statistics` :bdg-emerald:`calibration` :bdg-emerald:`Sr/Ca`, :bdg-success:`pyleoclim` :bdg-success:`arviz` :bdg-success:`matplotlib` :bdg-success:`statsmodel` :bdg-success:`Great Tables` :bdg-success:`pandas` :bdg-success:`pymc`, :bdg-primary:`Getting Started` :bdg-primary:`Calibration`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pca paleopca science-bits cartopy eofs matplotlib modeling paleoceanography pandas pyleoclim python xarray
                        :outline: teal
                    
                        .. card:: Investigating interhemispheric precipitation changes over the past millennium :bdg-danger:`PaleoPCA` :bdg-teal:`python`
                            :link: https://projectpythia.org/paleoPCA-cookbook/README.html
                            :img-top: https://raw.githubusercontent.com/khider/paleoPCA/main/thumbnails/LinkedEarth.png
                            :img-alt: LinkedEarth.png
                            
                            :bdg-emerald:`PCA` :bdg-emerald:`paleoceanography` :bdg-emerald:`modeling`, :bdg-success:`pyleoclim` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`xarray` :bdg-success:`pandas` :bdg-success:`eofs`, :bdg-primary:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: common-era motivation pmip pamodaco paleoensembles paleoclimate-applications plume-distance temporal-interpretation data-assimilation data-viz matplotlib paleoclimatology pandas pens pyleoclim python reconstruction scipy seaborn statistics statsmodels timeseries-modeling
                        :outline: teal
                    
                        .. card:: Comparing Paleoclimate Ensembles :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/ug-eg25.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/pens_logo.png
                            :img-alt: pens_logo.png
                            
                            :bdg-emerald:`PaMoDaCo` :bdg-emerald:`data viz` :bdg-emerald:`reconstruction` :bdg-emerald:`paleoclimatology` :bdg-emerald:`data assimilation` :bdg-emerald:`Common Era` :bdg-emerald:`statistics` :bdg-emerald:`timeseries modeling` :bdg-emerald:`PMIP`, :bdg-success:`pyleoclim` :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`statsmodels` :bdg-success:`seaborn` :bdg-success:`scipy` :bdg-success:`pandas`, :bdg-primary:`Paleoclimate Applications` :bdg-primary:`Plume Distance` :bdg-primary:`Motivation` :bdg-primary:`Temporal Interpretation`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency exploring-the-data loading-data main-analysis ammonyte basemap data-analysis data-viz data-wrangling matplotlib pylipd pyleoclim pylipd python
                        :outline: teal
                    
                        .. card:: Regime Shifts in Holocene Paleohydrology as Recorded by Asian Speleothems :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/intro.html
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/speleothem_timeseries_map.png
                            :img-alt: speleothem_timeseries_map.png
                            
                            :bdg-emerald:`data analysis` :bdg-emerald:`data viz` :bdg-emerald:`data wrangling`, :bdg-success:`pyleoclim` :bdg-success:`ammonyte` :bdg-success:`pyLiPD` :bdg-success:`matplotlib` :bdg-success:`basemap` :bdg-success:`pylipd`, :bdg-primary:`Loading Data` :bdg-primary:`Exploring the Data` :bdg-primary:`Main Analysis`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: core-methods data-manipulation extensions lipd pca r age-modeling age-uncertainty calibration correlation data-wrangling dimension-reduction dplyr ensemble geochronr geochronr ggplot2 lipdr mapping oxcaar purrr readr regression spectral-analysis tidyverse uncertainty-quantification visualization wavelets
                        :outline: mauve
                    
                        .. card:: geoChronR Vignettes (McKay et al., 2021) :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: http://nickmckay.github.io/GeoChronR/articles/Introduction.html
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/logo.png
                            :img-alt: logo.png
                            
                            :bdg-emerald:`spectral analysis` :bdg-emerald:`mapping` :bdg-emerald:`data wrangling` :bdg-emerald:`regression` :bdg-emerald:`age modeling` :bdg-emerald:`PCA` :bdg-emerald:`tidyverse` :bdg-emerald:`dimension reduction` :bdg-emerald:`visualization` :bdg-emerald:`wavelets` :bdg-emerald:`LiPD` :bdg-emerald:`ensemble` :bdg-emerald:`calibration` :bdg-emerald:`correlation` :bdg-emerald:`uncertainty quantification` :bdg-emerald:`age uncertainty`, :bdg-success:`readr` :bdg-success:`lipdR` :bdg-success:`purrr` :bdg-success:`oxcAAR` :bdg-success:`dplyr` :bdg-success:`ggplot2`, :bdg-primary:`Core Methods` :bdg-primary:`Extensions` :bdg-primary:`Data Manipulation`

            
        

+++++++++++++++
Chapters
+++++++++++++++

.. grid:: 1 2 2 2



                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace lifehacks cartopy data-viz matplotlib notebook oceanography pandas python seaborn tracers xarray
                        :outline: teal
                        
                        .. card:: ODV style plots with Python :bdg-danger:`C-iTRACE` :bdg-teal:`python`
                            :link: https://linked.earth/citrace_paleobook/notebooks/lifehacks/pyODV
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/pyodv_demo.png
                            :img-alt: pyodv_demo.png
                            
                            
                            
                            :bdg-emerald:`oceanography` :bdg-emerald:`tracers` :bdg-emerald:`data viz`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`pandas` :bdg-success:`seaborn`, :bdg-primary:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace lifehacks cartopy coordinate-systems intake matplotlib model-output notebook oceanography pandas python xarray
                        :outline: teal
                        
                        .. card:: Working with data on a model grid :bdg-danger:`C-iTRACE` :bdg-teal:`python`
                            :link: https://linked.earth/citrace_paleobook/notebooks/lifehacks/working_with_data_on_a_model_grid
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/citrace_model_grid.png
                            :img-alt: citrace_model_grid.png
                            
                            
                            
                            :bdg-emerald:`model output` :bdg-emerald:`oceanography` :bdg-emerald:`coordinate systems`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`pandas` :bdg-success:`intake`, :bdg-primary:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace science-bits cartopy end matplotlib model-output notebook pandas python xarray
                        :outline: teal
                        
                        .. card:: eNd model-data comparison (section) :bdg-danger:`C-iTRACE` :bdg-teal:`python`
                            :link: https://linked.earth/citrace_paleobook/notebooks/science_bits/data_scatter_on_pcolor
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/section_eNd_uncertaintyrange.png
                            :img-alt: section_eNd_uncertaintyrange.png
                            
                            
                            
                            :bdg-emerald:`model output` :bdg-emerald:`eNd`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`pandas`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace science-bits cartopy clustering machine-learning matplotlib notebook python scikit-learn watermass-geometry xarray
                        :outline: teal
                        
                        .. card:: Paleo watermass geometry using clustering :bdg-danger:`C-iTRACE` :bdg-teal:`python`
                            :link: https://linked.earth/citrace_paleobook/notebooks/science_bits/clustering
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/cluster_section.png
                            :img-alt: cluster_section.png
                            
                            
                            
                            :bdg-emerald:`clustering` :bdg-emerald:`machine learning` :bdg-emerald:`watermass geometry`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`scikit-learn`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace c14 deglaciation mystery-interval paleoceanography science-bits cartopy matplotlib notebook pandas python xarray
                        :outline: teal
                        
                        .. card:: D14C model-data comparison (downcore) :bdg-danger:`C-iTRACE` :bdg-teal:`python`
                            :link: https://linked.earth/citrace_paleobook/notebooks/science_bits/PaMoDaCo_downcore_D14C
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/C14_downcore_modelmarchitto.png
                            :img-alt: C14_downcore_modelmarchitto.png
                            
                            
                            
                            :bdg-emerald:`C14` :bdg-emerald:`Paleoceanography` :bdg-emerald:`Deglaciation` :bdg-emerald:`Mystery Interval`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`pandas`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: aws aws cmip6 lmr-cmip6 lifehacks cloud-ready-data data-viz intake notebook pandas python xarray
                        :outline: teal
                        
                        .. card:: Accessing cloud-hosted CMIP6 output :bdg-danger:`LMR-CMIP6` :bdg-teal:`python`
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/lifehacks/data_from_esm_cloudcat
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/data_from_esm_cloudcat.png
                            :img-alt: data_from_esm_cloudcat.png
                            
                            
                            
                            :bdg-emerald:`AWS` :bdg-emerald:`cloud-ready data` :bdg-emerald:`data viz` :bdg-emerald:`CMIP6`, :bdg-success:`intake` :bdg-success:`AWS` :bdg-success:`xarray` :bdg-success:`pandas`, :bdg-primary:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 lmr-cmip6 lifehacks cartopy coordinate-systems matplotlib model-output notebook pandas python xarray
                        :outline: teal
                        
                        .. card:: Spatiotemporal diagnostics using `xarray` :bdg-danger:`LMR-CMIP6` :bdg-teal:`python`
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/lifehacks/spatial_snapshots_xarray_bonuses
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/spatial_snapshots_xarray_bonuses.png
                            :img-alt: spatial_snapshots_xarray_bonuses.png
                            
                            
                            
                            :bdg-emerald:`model output` :bdg-emerald:`CMIP6` :bdg-emerald:`coordinate systems`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`pandas`, :bdg-primary:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: lmr-cmip6 lifehacks ipywidgets matplotlib model-output notebook python
                        :outline: teal
                        
                        .. card:: Data exploration with `ipywidgets` :bdg-danger:`LMR-CMIP6` :bdg-teal:`python`
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/lifehacks/widget_primer
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/widget_primer.png
                            :img-alt: widget_primer.png
                            
                            
                            
                            :bdg-emerald:`model output`, :bdg-success:`ipywidgets` :bdg-success:`matplotlib`, :bdg-primary:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 lmr lmr-cmip6 science-bits cartopy matplotlib model-output notebook pandas pyleoclim python xarray
                        :outline: teal
                        
                        .. card:: Comparing CMIP6 & LMR :bdg-danger:`LMR-CMIP6` :bdg-teal:`python`
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/science_bits/CMIP6_LMR
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/CMIP6_LMR.png
                            :img-alt: CMIP6_LMR.png
                            
                            
                            
                            :bdg-emerald:`model output` :bdg-emerald:`LMR` :bdg-emerald:`CMIP6`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`pandas` :bdg-success:`pyleoclim`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 holocene-climate lmr lmr-cmip6 science-bits volcanic-input cartopy ipywidgets matplotlib notebook python xarray
                        :outline: teal
                        
                        .. card:: LMR & Volcanic Aerosols :bdg-danger:`LMR-CMIP6` :bdg-teal:`python`
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/science_bits/VICS_dashboard
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/VICS_dashboard.png
                            :img-alt: VICS_dashboard.png
                            
                            
                            
                            :bdg-emerald:`Volcanic Input` :bdg-emerald:`Holocene climate` :bdg-emerald:`LMR` :bdg-emerald:`CMIP6`, :bdg-success:`xarray` :bdg-success:`matplotlib` :bdg-success:`cartopy` :bdg-success:`ipywidgets`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: 2k-proxy-composite science-bits cfr notebook numpy pandas proxy-composite pyleoclim python seaborn temperature
                        :outline: teal
                        
                        .. card:: Hockey Stick :bdg-danger:`2k Proxy Composite` :bdg-teal:`python`
                            :link: https://khider.github.io/DISK-proxyComposite/HockeyStick
                            :img-top: https://raw.githubusercontent.com/khider/DISK-proxyComposite/main/proxycomposite/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            
                            
                            :bdg-emerald:`proxy composite` :bdg-emerald:`temperature`, :bdg-success:`numpy` :bdg-success:`seaborn` :bdg-success:`pandas` :bdg-success:`pyleoclim` :bdg-success:`cfr`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: prototypewmg science-bits basemap endmember-mixing matplotlib notebook pandas python scipy sqlalchemy tracers watermass-geometry
                        :outline: teal
                        
                        .. card:: Capstone notebook :bdg-danger:`PrototypeWMG` :bdg-teal:`python`
                            :link: https://jordanplanders.github.io/past_life_wmg/CapstoneProject/jlanders_capstone_fixed
                            :img-top: https://raw.githubusercontent.com/jordanplanders/past_life_wmg/main/ancient_wmgr_book/thumbnails/ttest_flows_thumb.png
                            :img-alt: ttest_flows_thumb.png
                            
                            
                            
                            :bdg-emerald:`watermass geometry` :bdg-emerald:`tracers` :bdg-emerald:`endmember mixing`, :bdg-success:`basemap` :bdg-success:`scipy` :bdg-success:`matplotlib` :bdg-success:`pandas` :bdg-success:`sqlalchemy`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: prototypewmg science-bits basemap clustering matplotlib notebook python scikit-learn watermass-geometry
                        :outline: teal
                        
                        .. card:: Cluster Centers :bdg-danger:`PrototypeWMG` :bdg-teal:`python`
                            :link: https://jordanplanders.github.io/past_life_wmg/CapstoneProject/clustering_centers_on_raw
                            :img-top: https://raw.githubusercontent.com/jordanplanders/past_life_wmg/main/ancient_wmgr_book/thumbnails/centers_thumb.png
                            :img-alt: centers_thumb.png
                            
                            
                            
                            :bdg-emerald:`clustering` :bdg-emerald:`watermass geometry`, :bdg-success:`basemap` :bdg-success:`scikit-learn` :bdg-success:`matplotlib`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Method overview :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/Method_Overview
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: LERM applied to ODP cores :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/ODP_LERM
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/odp.png
                            :img-alt: odp
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: LERM applied to synthetic ODP cores :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/Synthetic_ODP_LERM
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/leloup_paillard_odp_lp.png
                            :img-alt: leloup_paillard_odp_lp
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Sensitivity to resolution :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/Resolution_Sensitivity
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/sensitivity_1.png
                            :img-alt: sensitivity_1
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: LERM applied to ice cores :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/IceCore_LERM
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/ice_core.png
                            :img-alt: ice_core
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Sensitivity to events :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/Event_Sensitivity
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/8k_noise.png
                            :img-alt: 8k_noise
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Regime transition probability on synthetic ensembles :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_7
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/density.png
                            :img-alt: density
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm main-analysis ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Resolution changes on real data :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Main_Analysis/Resolution_Analysis
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/resolution.png
                            :img-alt: resolution
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Holocene Ice Analysis :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Extras/Holocene_Ice_Analysis
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Extras`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Holocene Ice Window Increment :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Extras/Holocene_Ice_Window_Increment
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Extras`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras ammonyte data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Holocene Ice Window Size :bdg-danger:`Detecting Paleoclimate Transitions with LERM` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/notebooks/Extras/Holocene_Ice_Window_Size
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            
                            
                            :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`ammonyte`, :bdg-primary:`Extras`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits climlab cross-wavelet-analysis insolation notebook paleoceanography pyleoclim pylipd python spectral-analysis wavelet-analysis xarray
                        :outline: teal
                        
                        .. card:: Chasing cyclicities :bdg-danger:`Pyleoclim science` :bdg-teal:`python`
                            :link: https://linked.earth/PyleoclimPaper/OrbitalCycles/Chasing_orbital_cyclicities
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/wavelet.png
                            :img-alt: wavelet.png
                            
                            
                            
                            :bdg-emerald:`spectral analysis` :bdg-emerald:`wavelet analysis` :bdg-emerald:`cross-wavelet analysis` :bdg-emerald:`insolation` :bdg-emerald:`paleoceanography`, :bdg-success:`xarray` :bdg-success:`pyleoclim` :bdg-success:`pylipd` :bdg-success:`climlab`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits model-output model-data-comparison notebook paleoclimate pyleoclim python spectral-analysis xarray
                        :outline: teal
                        
                        .. card:: Model-Data Confrontation :bdg-danger:`Pyleoclim science` :bdg-teal:`python`
                            :link: https://linked.earth/PyleoclimPaper/MDConfrontation/Model_data_confrontation
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/spectralslope.png
                            :img-alt: spectralslope.png
                            
                            
                            
                            :bdg-emerald:`model output` :bdg-emerald:`spectral analysis` :bdg-emerald:`model-data comparison` :bdg-emerald:`paleoclimate`, :bdg-success:`xarray` :bdg-success:`pyleoclim`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits age-uncertainty cartopy correlation notebook paleoclimate pyleoclim pylipd python xarray
                        :outline: teal
                        
                        .. card:: Correlations at Sea :bdg-danger:`Pyleoclim science` :bdg-teal:`python`
                            :link: https://linked.earth/PyleoclimPaper/CrystalCorrelations/CrystalCorrelations
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/corrhist.png
                            :img-alt: corrhist.png
                            
                            
                            
                            :bdg-emerald:`paleoclimate` :bdg-emerald:`correlation` :bdg-emerald:`age uncertainty`, :bdg-success:`xarray` :bdg-success:`pyleoclim` :bdg-success:`cartopy` :bdg-success:`pylipd`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: coral-sr/ca-calibration getting-started sr/ca calibration coral matplotlib notebook paleoceanography pandas pyleoclim python
                        :outline: teal
                        
                        .. card:: Data Exploration :bdg-danger:`Coral Sr/Ca calibration` :bdg-teal:`python`
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/DataExploration
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/dataexp.png
                            :img-alt: dataexp.png
                            
                            
                            
                            :bdg-emerald:`paleoceanography` :bdg-emerald:`Sr/Ca` :bdg-emerald:`coral` :bdg-emerald:`calibration`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim` :bdg-success:`pandas`, :bdg-primary:`Getting Started`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: calibration calibration coral-sr/ca-calibration great-tables paleocenography statistics notebook python statsmodel
                        :outline: teal
                        
                        .. card:: Frequentist Calibration :bdg-danger:`Coral Sr/Ca calibration` :bdg-teal:`python`
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/FrequentistCalibration
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/table.png
                            :img-alt: table.png
                            
                            
                            
                            :bdg-emerald:`Statistics` :bdg-emerald:`Calibration` :bdg-emerald:`Paleocenography`, :bdg-success:`statsmodel` :bdg-success:`Great Tables`, :bdg-primary:`Calibration`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: bayesian-statistics calibration calibration coral-sr/ca-calibration paleocenography arviz notebook pymc python
                        :outline: teal
                        
                        .. card:: Bayesian Calibration :bdg-danger:`Coral Sr/Ca calibration` :bdg-teal:`python`
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/BayesianCalibration
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/bayes.png
                            :img-alt: bayes.png
                            
                            
                            
                            :bdg-emerald:`Bayesian Statistics` :bdg-emerald:`Calibration` :bdg-emerald:`Paleocenography`, :bdg-success:`pymc` :bdg-success:`arviz`, :bdg-primary:`Calibration`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pca paleopca science-bits cartopy eofs matplotlib modeling notebook paleoceanography pandas pyleoclim python xarray
                        :outline: teal
                        
                        .. card:: Model-Data Comparison :bdg-danger:`PaleoPCA` :bdg-teal:`python`
                            :link: https://projectpythia.org/paleoPCA-cookbook/notebooks/paleoPCA
                            :img-top: https://raw.githubusercontent.com/khider/paleoPCA/main/thumbnails/eof.png
                            :img-alt: eof.png
                            
                            
                            
                            :bdg-emerald:`paleoceanography` :bdg-emerald:`PCA` :bdg-emerald:`modeling`, :bdg-success:`xarray` :bdg-success:`pyleoclim` :bdg-success:`cartopy` :bdg-success:`matplotlib` :bdg-success:`pandas` :bdg-success:`eofs`, :bdg-primary:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: motivation paleoensembles data-assimilation data-viz matplotlib notebook paleoclimatology pens pyleoclim python
                        :outline: teal
                        
                        .. card:: motivation :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig1_motivation
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/motivation_thumbnail.png
                            :img-alt: motivation_thumbnail.png
                            
                            
                            
                            :bdg-emerald:`paleoclimatology` :bdg-emerald:`data assimilation` :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`pyleoclim`, :bdg-primary:`Motivation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pamodaco paleoensembles temporal-interpretation data-assimilation matplotlib notebook pens python
                        :outline: teal
                        
                        .. card:: Naïve resampling :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig2_naive_resampling
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/naive_thumbnail.png
                            :img-alt: naive_thumbnail.png
                            
                            
                            
                            :bdg-emerald:`data assimilation` :bdg-emerald:`PaMoDaCo`, :bdg-success:`matplotlib` :bdg-success:`pens`, :bdg-primary:`Temporal Interpretation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: paleoensembles temporal-interpretation data-assimilation matplotlib notebook pens python seaborn statsmodels timeseries-modeling
                        :outline: teal
                        
                        .. card:: LMRonline :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig3_4_LMRonline
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/LMRo_thumbnail.png
                            :img-alt: LMRo_thumbnail.png
                            
                            
                            
                            :bdg-emerald:`data assimilation` :bdg-emerald:`timeseries modeling`, :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`statsmodels` :bdg-success:`seaborn`, :bdg-primary:`Temporal Interpretation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: paleoensembles temporal-interpretation data-assimilation matplotlib notebook pens pyleoclim python timeseries-modeling
                        :outline: teal
                        
                        .. card:: resampling :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig5_resampling
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/resampling_thumbnail.png
                            :img-alt: resampling_thumbnail.png
                            
                            
                            
                            :bdg-emerald:`data assimilation` :bdg-emerald:`timeseries modeling`, :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`pyleoclim`, :bdg-primary:`Temporal Interpretation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pamodaco paleoensembles plume-distance matplotlib notebook pens python seaborn statistics
                        :outline: teal
                        
                        .. card:: Definition & Properties :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig6_8_plume_distance
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/plume_dist.png
                            :img-alt: plume_dist.png
                            
                            
                            
                            :bdg-emerald:`statistics` :bdg-emerald:`PaMoDaCo`, :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`seaborn`, :bdg-primary:`Plume Distance`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pamodaco paleoensembles plume-distance matplotlib notebook pens python seaborn statistics
                        :outline: teal
                        
                        .. card:: Schematic :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig9_plume_distance-schematic
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/plume_schem.png
                            :img-alt: plume_schem.png
                            
                            
                            
                            :bdg-emerald:`statistics` :bdg-emerald:`PaMoDaCo`, :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`seaborn`, :bdg-primary:`Plume Distance`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: common-era paleoensembles paleoclimate-applications matplotlib notebook pens python reconstruction scipy seaborn statistics
                        :outline: teal
                        
                        .. card:: PAGES 2k (2019) ensemble :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig10_compare_PAGES2k2019_recons
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/PAGES2k_ensemble.png
                            :img-alt: PAGES2k_ensemble.png
                            
                            
                            
                            :bdg-emerald:`reconstruction` :bdg-emerald:`statistics` :bdg-emerald:`Common Era`, :bdg-success:`matplotlib` :bdg-success:`seaborn` :bdg-success:`pens` :bdg-success:`scipy`, :bdg-primary:`Paleoclimate Applications`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: common-era paleoensembles paleoclimate-applications matplotlib notebook pens python reconstruction statistics
                        :outline: teal
                        
                        .. card:: Büntgen et al (2021) :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Fig11_12_compare_LMRvsB21
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/B21_LMR.png
                            :img-alt: B21_LMR.png
                            
                            
                            
                            :bdg-emerald:`reconstruction` :bdg-emerald:`statistics` :bdg-emerald:`Common Era`, :bdg-success:`matplotlib` :bdg-success:`pens`, :bdg-primary:`Paleoclimate Applications`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pmip pamodaco paleoensembles paleoclimate-applications data-assimilation matplotlib notebook pandas pens pyleoclim python
                        :outline: teal
                        
                        .. card:: PMIP3 :bdg-danger:`PaleoEnsembles` :bdg-teal:`python`
                            :link: https://linked.earth/pens/notebooks/eg25-Tab1_LMR_PMIP3_proximity_table
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/PMIP3_LMR.png
                            :img-alt: PMIP3_LMR.png
                            
                            
                            
                            :bdg-emerald:`data assimilation` :bdg-emerald:`PaMoDaCo` :bdg-emerald:`PMIP`, :bdg-success:`matplotlib` :bdg-success:`pens` :bdg-success:`pyleoclim` :bdg-success:`pandas`, :bdg-primary:`Paleoclimate Applications`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency loading-data data-wrangling notebook pylipd python
                        :outline: teal
                        
                        .. card:: Getting data into LiPD :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Loading_Data/Getting_data_into_LiPD
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/pyLiPD_logo.png
                            :img-alt: pyLiPD_logo.png
                            
                            
                            
                            :bdg-emerald:`data wrangling`, :bdg-success:`pyLiPD`, :bdg-primary:`Loading Data`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency loading-data data-wrangling notebook pyleoclim pylipd python
                        :outline: teal
                        
                        .. card:: Loading Data :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Loading_Data/Load_Data_Pyleoclim
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/pyleoclim_insignia_full_white.png
                            :img-alt: pyleoclim_insignia_full_white.png
                            
                            
                            
                            :bdg-emerald:`data wrangling`, :bdg-success:`pylipd` :bdg-success:`pyleoclim`, :bdg-primary:`Loading Data`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency exploring-the-data data-analysis data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Detrended Stackplot :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Exploring_the_Data/DetrendedStack_Figure
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/detrended_ensembles.png
                            :img-alt: detrended_ensembles.png
                            
                            
                            
                            :bdg-emerald:`data viz` :bdg-emerald:`data analysis`, :bdg-success:`pyleoclim` :bdg-success:`matplotlib`, :bdg-primary:`Exploring the Data`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency exploring-the-data basemap data-analysis data-viz notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Mapping Data :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Exploring_the_Data/Map_Data
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/speleothem_timeseries_map.png
                            :img-alt: speleothem_timeseries_map.png
                            
                            
                            
                            :bdg-emerald:`data viz` :bdg-emerald:`data analysis`, :bdg-success:`pyleoclim` :bdg-success:`basemap`, :bdg-primary:`Exploring the Data`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency main-analysis data-analysis data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Synthetic Data :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Main_Analysis/Synthetic_Data
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/synthetic_snr.png
                            :img-alt: synthetic_snr.png
                            
                            
                            
                            :bdg-emerald:`data viz` :bdg-emerald:`data analysis`, :bdg-success:`pyleoclim` :bdg-success:`matplotlib`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency main-analysis data-analysis data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Kernel Density Estimation :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Main_Analysis/KDE_Plots
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/interval_4k_diff_snr.png
                            :img-alt: interval_4k_diff_snr.png
                            
                            
                            
                            :bdg-emerald:`data analysis` :bdg-emerald:`data viz`, :bdg-success:`matplotlib` :bdg-success:`pyleoclim`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency main-analysis ammonyte data-analysis data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: Detecting Regime Shifts :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Main_Analysis/LERM_Plot
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/speleothem_lerm.png
                            :img-alt: speleothem_lerm.png
                            
                            
                            
                            :bdg-emerald:`data viz` :bdg-emerald:`data analysis`, :bdg-success:`pyleoclim` :bdg-success:`ammonyte` :bdg-success:`matplotlib`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: asian-speleothem-coherency main-analysis data-analysis data-viz matplotlib notebook pyleoclim python
                        :outline: teal
                        
                        .. card:: MC PCA Analysis :bdg-danger:`Asian Speleothem Coherency` :bdg-teal:`python`
                            :link: https://alexkjames.github.io/AsianSpeleothemCoherency/notebooks/Main_Analysis/MC_PCA_Analysis
                            :img-top: https://raw.githubusercontent.com/alexkjames/AsianSpeleothemCoherency/main/thumbnails/mcpca_all_1.png
                            :img-alt: mcpca_all_1.png
                            
                            
                            
                            :bdg-emerald:`data viz` :bdg-emerald:`data analysis`, :bdg-success:`pyleoclim` :bdg-success:`matplotlib`, :bdg-primary:`Main Analysis`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: core-methods r age-modeling geochronr geochronr lipdr notebook uncertainty-quantification
                        :outline: mauve
                        
                        .. card:: Introduction :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/Introduction
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/introduction.png
                            :img-alt: introduction.png
                            
                            
                            
                            :bdg-emerald:`age modeling` :bdg-emerald:`uncertainty quantification`, :bdg-success:`geoChronR` :bdg-success:`lipdR`, :bdg-primary:`Core Methods`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: core-methods r age-uncertainty correlation geochronr geochronr ggplot2 notebook
                        :outline: mauve
                        
                        .. card:: Ensemble Correlation :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/correlation
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/correlation.png
                            :img-alt: correlation.png
                            
                            
                            
                            :bdg-emerald:`correlation` :bdg-emerald:`age uncertainty`, :bdg-success:`geoChronR` :bdg-success:`ggplot2`, :bdg-primary:`Core Methods`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: core-methods r calibration geochronr geochronr ggplot2 notebook readr regression
                        :outline: mauve
                        
                        .. card:: Regression & Calibration-in-Time :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/regression
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/regression.png
                            :img-alt: regression.png
                            
                            
                            
                            :bdg-emerald:`regression` :bdg-emerald:`calibration`, :bdg-success:`geoChronR` :bdg-success:`readr` :bdg-success:`ggplot2`, :bdg-primary:`Core Methods`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: core-methods r geochronr geochronr notebook spectral-analysis wavelets
                        :outline: mauve
                        
                        .. card:: Spectral Analysis :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/spectral_analysis
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/spectral_analysis.png
                            :img-alt: spectral_analysis.png
                            
                            
                            
                            :bdg-emerald:`spectral analysis` :bdg-emerald:`wavelets`, :bdg-success:`geoChronR`, :bdg-primary:`Core Methods`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: core-methods pca r dimension-reduction geochronr geochronr notebook
                        :outline: mauve
                        
                        .. card:: Ensemble PCA :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/PCA
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/PCA.png
                            :img-alt: PCA.png
                            
                            
                            
                            :bdg-emerald:`PCA` :bdg-emerald:`dimension reduction`, :bdg-success:`geoChronR`, :bdg-primary:`Core Methods`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: data-manipulation r geochronr geochronr ggplot2 notebook visualization
                        :outline: mauve
                        
                        .. card:: Plot Timeseries Stack :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/PlotTimeseriesStack
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/plot_stack.png
                            :img-alt: plot_stack.png
                            
                            
                            
                            :bdg-emerald:`visualization`, :bdg-success:`geoChronR` :bdg-success:`ggplot2`, :bdg-primary:`Data Manipulation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: data-manipulation r data-wrangling geochronr geochronr mapping notebook
                        :outline: mauve
                        
                        .. card:: Filtering & Mapping :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/TsFilteringAndMapping
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/filter_map.png
                            :img-alt: filter_map.png
                            
                            
                            
                            :bdg-emerald:`data wrangling` :bdg-emerald:`mapping`, :bdg-success:`geoChronR`, :bdg-primary:`Data Manipulation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: data-manipulation r data-wrangling dplyr geochronr geochronr notebook purrr tidyverse
                        :outline: mauve
                        
                        .. card:: Tidy Filtering & Mapping :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/tidyIso2k
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/tidy_filter.png
                            :img-alt: tidy_filter.png
                            
                            
                            
                            :bdg-emerald:`data wrangling` :bdg-emerald:`tidyverse`, :bdg-success:`geoChronR` :bdg-success:`dplyr` :bdg-success:`purrr`, :bdg-primary:`Data Manipulation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: extensions r age-modeling geochronr geochronr notebook oxcaar
                        :outline: mauve
                        
                        .. card:: OxCal Integration :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/oxCal
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/oxcal.png
                            :img-alt: oxcal.png
                            
                            
                            
                            :bdg-emerald:`age modeling`, :bdg-success:`geoChronR` :bdg-success:`oxcAAR`, :bdg-primary:`Extensions`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: extensions lipd r ensemble geochronr geochronr notebook
                        :outline: mauve
                        
                        .. card:: Add Ensemble to LiPD :bdg-danger:`geoChronR` :bdg-mauve:`R`
                            :link: https://nickmckay.github.io/GeoChronR/articles/AddEnsemble
                            :img-top: https://raw.githubusercontent.com/nickmckay/GeoChronR/master/thumbnails/add_ensemble.png
                            :img-alt: add_ensemble.png
                            
                            
                            
                            :bdg-emerald:`LiPD` :bdg-emerald:`ensemble`, :bdg-success:`geoChronR`, :bdg-primary:`Extensions`
                            

        


.. raw:: html

    <div class="modal-backdrop"></div>


