


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
    <ul class="dropdown-menu" aria-labelledby="bookDropdown"><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=2k-proxy-composite onchange="change();">&nbsp;2k Proxy Composite</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=ancientwmg onchange="change();">&nbsp;AncientWMG</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=c-itrace onchange="change();">&nbsp;C-iTRACE</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=coral-sr/ca-calibration onchange="change();">&nbsp;Coral Sr/Ca calibration</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=detecting-paleoclimate-transitions-with-lerm onchange="change();">&nbsp;Detecting Paleoclimate Transitions with LERM</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=lmr-cmip6 onchange="change();">&nbsp;LMR-CMIP6</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=paleoensembles onchange="change();">&nbsp;PaleoEnsembles</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=paleopca onchange="change();">&nbsp;PaleoPCA</label></li><li><label class="dropdown-item checkbox book"><input type="checkbox" rel=pyleoclim-science onchange="change();">&nbsp;Pyleoclim science</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Domains</button>
    <ul class="dropdown-menu" aria-labelledby="domainsDropdown"><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=aws onchange="change();">&nbsp;AWS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=bayesian-statistics onchange="change();">&nbsp;Bayesian Statistics</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=c14 onchange="change();">&nbsp;C14</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cmip6 onchange="change();">&nbsp;CMIP6</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=calibration onchange="change();">&nbsp;Calibration</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=common-era onchange="change();">&nbsp;Common Era</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=deglaciation onchange="change();">&nbsp;Deglaciation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=holocene-climate onchange="change();">&nbsp;Holocene climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=lmr onchange="change();">&nbsp;LMR</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=mystery-interval onchange="change();">&nbsp;Mystery Interval</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=pca onchange="change();">&nbsp;PCA</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=pmip onchange="change();">&nbsp;PMIP</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=pamodaco onchange="change();">&nbsp;PaMoDaCo</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoceanography onchange="change();">&nbsp;Paleoceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleocenography onchange="change();">&nbsp;Paleocenography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sr/ca onchange="change();">&nbsp;Sr/Ca</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=statistics onchange="change();">&nbsp;Statistics</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=volcanic-input onchange="change();">&nbsp;Volcanic Input</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=age-uncertainty onchange="change();">&nbsp;age uncertainty</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=calibration onchange="change();">&nbsp;calibration</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cloud-ready-data onchange="change();">&nbsp;cloud-ready data</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=clustering onchange="change();">&nbsp;clustering</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=coordinate-systems onchange="change();">&nbsp;coordinate systems</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=coral onchange="change();">&nbsp;coral</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=correlation onchange="change();">&nbsp;correlation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cross-wavelet-analysis onchange="change();">&nbsp;cross-wavelet analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-assimilation onchange="change();">&nbsp;data assimilation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-viz onchange="change();">&nbsp;data viz</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=end onchange="change();">&nbsp;eNd</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=endmember-mixing onchange="change();">&nbsp;endmember mixing</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=insolation onchange="change();">&nbsp;insolation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=machine-learning onchange="change();">&nbsp;machine learning</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=model-output onchange="change();">&nbsp;model output</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=model-data-comparison onchange="change();">&nbsp;model-data comparison</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=modeling onchange="change();">&nbsp;modeling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoceanography onchange="change();">&nbsp;paleoceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoclimate onchange="change();">&nbsp;paleoclimate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoclimatology onchange="change();">&nbsp;paleoclimatology</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=proxy-composite onchange="change();">&nbsp;proxy composite</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=reconstruction onchange="change();">&nbsp;reconstruction</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=spectral-analysis onchange="change();">&nbsp;spectral analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=statistics onchange="change();">&nbsp;statistics</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=temperature onchange="change();">&nbsp;temperature</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=timeseries-modeling onchange="change();">&nbsp;timeseries modeling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=tracers onchange="change();">&nbsp;tracers</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=watermass-geometry onchange="change();">&nbsp;watermass geometry</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=wavelet-analysis onchange="change();">&nbsp;wavelet analysis</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="formatsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Formats</button>
    <ul class="dropdown-menu" aria-labelledby="formatsDropdown"><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=calibration onchange="change();">&nbsp;Calibration</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=extras onchange="change();">&nbsp;Extras</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=figures onchange="change();">&nbsp;Figures</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=getting-started onchange="change();">&nbsp;Getting Started</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=lifehacks onchange="change();">&nbsp;Lifehacks</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=motivation onchange="change();">&nbsp;Motivation</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=paleoclimate-applications onchange="change();">&nbsp;Paleoclimate Applications</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=plume-distance onchange="change();">&nbsp;Plume Distance</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=science-bits onchange="change();">&nbsp;Science Bits</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=temporal-interpretation onchange="change();">&nbsp;Temporal Interpretation</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Packages</button>
    <ul class="dropdown-menu" aria-labelledby="packagesDropdown"><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=aws onchange="change();">&nbsp;AWS</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=great-tables onchange="change();">&nbsp;Great Tables</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ammonyte onchange="change();">&nbsp;ammonyte</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=arviz onchange="change();">&nbsp;arviz</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=basemap onchange="change();">&nbsp;basemap</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cartopy onchange="change();">&nbsp;cartopy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cfr onchange="change();">&nbsp;cfr</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=climlab onchange="change();">&nbsp;climlab</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=eofs onchange="change();">&nbsp;eofs</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake onchange="change();">&nbsp;intake</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ipywidgets onchange="change();">&nbsp;ipywidgets</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=matplotlib onchange="change();">&nbsp;matplotlib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=numpy onchange="change();">&nbsp;numpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pandas onchange="change();">&nbsp;pandas</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pens onchange="change();">&nbsp;pens</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pyleoclim onchange="change();">&nbsp;pyleoclim</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pylipd onchange="change();">&nbsp;pylipd</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pymc onchange="change();">&nbsp;pymc</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=scikit-learn onchange="change();">&nbsp;scikit-learn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=scipy onchange="change();">&nbsp;scipy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=seaborn onchange="change();">&nbsp;seaborn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=sqlalchemy onchange="change();">&nbsp;sqlalchemy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=statsmodel onchange="change();">&nbsp;statsmodel</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=statsmodels onchange="change();">&nbsp;statsmodels</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;xarray</label></li></ul>
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
                        :tags: c-itrace c14 deglaciation lifehacks mystery-interval paleoceanography science-bits cartopy clustering coordinate-systems data-viz end intake machine-learning matplotlib model-output oceanography pandas scikit-learn seaborn tracers watermass-geometry xarray
                    
                        .. card:: C-iTrace Paleobook :bdg-danger:`C-iTRACE`
                            :link: https://linked.earth/citrace_paleobook/README.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-primary:`C14` :bdg-primary:`oceanography` :bdg-primary:`eNd` :bdg-primary:`tracers` :bdg-primary:`machine learning` :bdg-primary:`Deglaciation` :bdg-primary:`coordinate systems` :bdg-primary:`data viz` :bdg-primary:`watermass geometry` :bdg-primary:`clustering` :bdg-primary:`model output` :bdg-primary:`Paleoceanography` :bdg-primary:`Mystery Interval`, :bdg-secondary:`cartopy` :bdg-secondary:`seaborn` :bdg-secondary:`matplotlib` :bdg-secondary:`xarray` :bdg-secondary:`scikit-learn` :bdg-secondary:`pandas` :bdg-secondary:`intake`, :bdg-success:`Science Bits` :bdg-success:`Lifehacks`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: aws aws cmip6 holocene-climate lmr lmr-cmip6 lifehacks science-bits volcanic-input cartopy cloud-ready-data coordinate-systems data-viz intake ipywidgets matplotlib model-output pandas pyleoclim xarray
                    
                        .. card:: LMR-CMIP6 Paleobook :bdg-danger:`LMR-CMIP6`
                            :link: https://linked.earth/LMR_CMIP_paleobook/README.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-primary:`Volcanic Input` :bdg-primary:`Holocene climate` :bdg-primary:`LMR` :bdg-primary:`AWS` :bdg-primary:`cloud-ready data` :bdg-primary:`coordinate systems` :bdg-primary:`data viz` :bdg-primary:`CMIP6` :bdg-primary:`model output`, :bdg-secondary:`pyleoclim` :bdg-secondary:`cartopy` :bdg-secondary:`matplotlib` :bdg-secondary:`AWS` :bdg-secondary:`xarray` :bdg-secondary:`ipywidgets` :bdg-secondary:`pandas` :bdg-secondary:`intake`, :bdg-success:`Science Bits` :bdg-success:`Lifehacks`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: 2k-proxy-composite science-bits cfr numpy pandas proxy-composite pyleoclim seaborn temperature
                    
                        .. card:: Reproducing the Hockey Stick - Proxy composite over the past 2,000 years using the cfr package :bdg-danger:`2k Proxy Composite`
                            :link: https://khider.github.io/DISK-proxyComposite/intro.html
                            :img-top: https://raw.githubusercontent.com/khider/DISK-proxyComposite/main/proxycomposite/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-primary:`proxy composite` :bdg-primary:`temperature`, :bdg-secondary:`pyleoclim` :bdg-secondary:`seaborn` :bdg-secondary:`cfr` :bdg-secondary:`pandas` :bdg-secondary:`numpy`, :bdg-success:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: ancientwmg science-bits basemap clustering endmember-mixing matplotlib pandas scikit-learn scipy sqlalchemy tracers watermass-geometry
                    
                        .. card:: Watermass Geometry Proto exercise :bdg-danger:`AncientWMG`
                            :link: https://jordanplanders.github.io/past_life_wmg/intro.html
                            :img-top: https://raw.githubusercontent.com/jordanplanders/past_life_wmg/main/ancient_wmgr_book/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-primary:`clustering` :bdg-primary:`endmember mixing` :bdg-primary:`tracers` :bdg-primary:`watermass geometry`, :bdg-secondary:`matplotlib` :bdg-secondary:`scipy` :bdg-secondary:`sqlalchemy` :bdg-secondary:`scikit-learn` :bdg-secondary:`pandas` :bdg-secondary:`basemap`, :bdg-success:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras figures ammonyte data-viz matplotlib pyleoclim
                    
                        .. card:: Detecting paleoclimate transitions with Laplacian Eigenmaps of Recurrence Matrices (LERM) :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/intro.html
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow.png
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte` :bdg-secondary:`matplotlib`, :bdg-success:`Figures` :bdg-success:`Extras`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits age-uncertainty cartopy climlab correlation cross-wavelet-analysis insolation model-output model-data-comparison paleoceanography paleoclimate pyleoclim pylipd spectral-analysis wavelet-analysis xarray
                    
                        .. card:: Reproducible workflows using the Pyleoclim package :bdg-danger:`Pyleoclim science`
                            :link: https://linked.earth/PyleoclimPaper/README.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-primary:`paleoclimate` :bdg-primary:`correlation` :bdg-primary:`paleoceanography` :bdg-primary:`age uncertainty` :bdg-primary:`spectral analysis` :bdg-primary:`model-data comparison` :bdg-primary:`cross-wavelet analysis` :bdg-primary:`insolation` :bdg-primary:`wavelet analysis` :bdg-primary:`model output`, :bdg-secondary:`pyleoclim` :bdg-secondary:`cartopy` :bdg-secondary:`climlab` :bdg-secondary:`xarray` :bdg-secondary:`pylipd`, :bdg-success:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: bayesian-statistics calibration calibration coral-sr/ca-calibration getting-started great-tables paleocenography sr/ca statistics arviz calibration coral matplotlib paleoceanography pandas pyleoclim pymc statsmodel
                    
                        .. card:: Coral Sr/Ca Calibration - An Example from Dry Tortugas :bdg-danger:`Coral Sr/Ca calibration`
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/intro.html
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/coral_logo.jpg
                            :img-alt: coral_logo.jpg
                            
                            :bdg-primary:`Calibration` :bdg-primary:`Statistics` :bdg-primary:`paleoceanography` :bdg-primary:`coral` :bdg-primary:`calibration` :bdg-primary:`Paleocenography` :bdg-primary:`Sr/Ca` :bdg-primary:`Bayesian Statistics`, :bdg-secondary:`pyleoclim` :bdg-secondary:`Great Tables` :bdg-secondary:`matplotlib` :bdg-secondary:`statsmodel` :bdg-secondary:`pymc` :bdg-secondary:`pandas` :bdg-secondary:`arviz`, :bdg-success:`Calibration` :bdg-success:`Getting Started`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pca paleopca science-bits cartopy eofs matplotlib modeling paleoceanography pandas pyleoclim xarray
                    
                        .. card:: Investigating interhemispheric precipitation changes over the past millennium :bdg-danger:`PaleoPCA`
                            :link: https://projectpythia.org/paleoPCA-cookbook/README.html
                            :img-top: https://raw.githubusercontent.com/khider/paleoPCA/main/thumbnails/LinkedEarth.png
                            :img-alt: LinkedEarth.png
                            
                            :bdg-primary:`paleoceanography` :bdg-primary:`modeling` :bdg-primary:`PCA`, :bdg-secondary:`pyleoclim` :bdg-secondary:`cartopy` :bdg-secondary:`eofs` :bdg-secondary:`matplotlib` :bdg-secondary:`xarray` :bdg-secondary:`pandas`, :bdg-success:`Science Bits`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: common-era motivation pmip pamodaco paleoensembles paleoclimate-applications plume-distance temporal-interpretation data-assimilation data-viz matplotlib paleoclimatology pandas pens pyleoclim reconstruction scipy seaborn statistics statsmodels timeseries-modeling
                    
                        .. card:: Comparing Paleoclimate Ensembles :bdg-danger:`PaleoEnsembles`
                            :link: https://linked.earth/pens/ug-eg24.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/pens_logo.png
                            :img-alt: pens_logo.png
                            
                            :bdg-primary:`Common Era` :bdg-primary:`PaMoDaCo` :bdg-primary:`data assimilation` :bdg-primary:`paleoclimatology` :bdg-primary:`timeseries modeling` :bdg-primary:`statistics` :bdg-primary:`data viz` :bdg-primary:`reconstruction` :bdg-primary:`PMIP`, :bdg-secondary:`pyleoclim` :bdg-secondary:`statsmodels` :bdg-secondary:`pens` :bdg-secondary:`seaborn` :bdg-secondary:`matplotlib` :bdg-secondary:`scipy` :bdg-secondary:`pandas`, :bdg-success:`Plume Distance` :bdg-success:`Motivation` :bdg-success:`Paleoclimate Applications` :bdg-success:`Temporal Interpretation`

            
        

+++++++++++++++
Chapters
+++++++++++++++

.. grid:: 1 2 2 2



                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace lifehacks cartopy data-viz matplotlib notebook oceanography pandas seaborn tracers xarray
                    
                        .. card:: pyODV
                            :link: https://linked.earth/citrace_paleobook/pyODV
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/pyodv_demo.png
                            :img-alt: pyodv_demo.png
                            
                            :bdg-danger:`C-iTRACE`
                            
                            :bdg-primary:`oceanography` :bdg-primary:`tracers` :bdg-primary:`data viz`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`pandas` :bdg-secondary:`seaborn`, :bdg-success:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace lifehacks cartopy coordinate-systems intake matplotlib model-output notebook oceanography pandas xarray
                    
                        .. card:: data_on_a_model_grid
                            :link: https://linked.earth/citrace_paleobook/working_with_data_on_a_model_grid
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/citrace_model_grid.png
                            :img-alt: citrace_model_grid.png
                            
                            :bdg-danger:`C-iTRACE`
                            
                            :bdg-primary:`model output` :bdg-primary:`oceanography` :bdg-primary:`coordinate systems`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`pandas` :bdg-secondary:`intake`, :bdg-success:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace science-bits cartopy end matplotlib model-output notebook pandas xarray
                    
                        .. card:: model_data_comp
                            :link: https://linked.earth/citrace_paleobook/data_scatter_on_pcolor
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/section_eNd_uncertaintyrange.png
                            :img-alt: section_eNd_uncertaintyrange.png
                            
                            :bdg-danger:`C-iTRACE`
                            
                            :bdg-primary:`model output` :bdg-primary:`eNd`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`pandas`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace science-bits cartopy clustering machine-learning matplotlib notebook scikit-learn watermass-geometry xarray
                    
                        .. card:: clustering
                            :link: https://linked.earth/citrace_paleobook/clustering
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/cluster_section.png
                            :img-alt: cluster_section.png
                            
                            :bdg-danger:`C-iTRACE`
                            
                            :bdg-primary:`clustering` :bdg-primary:`machine learning` :bdg-primary:`watermass geometry`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`scikit-learn`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace c14 deglaciation mystery-interval paleoceanography science-bits cartopy matplotlib notebook pandas xarray
                    
                        .. card:: model_downcore_D14C
                            :link: https://linked.earth/citrace_paleobook/PaMoDaCo_downcore_D14C
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/C14_downcore_modelmarchitto.png
                            :img-alt: C14_downcore_modelmarchitto.png
                            
                            :bdg-danger:`C-iTRACE`
                            
                            :bdg-primary:`C14` :bdg-primary:`Paleoceanography` :bdg-primary:`Deglaciation` :bdg-primary:`Mystery Interval`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`pandas`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: aws aws cmip6 lmr-cmip6 lifehacks cloud-ready-data data-viz intake notebook pandas xarray
                    
                        .. card:: data_from_esm_cloudcat
                            :link: https://linked.earth/LMR_CMIP_paleobook/data_from_esm_cloudcat
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/data_from_esm_cloudcat.png
                            :img-alt: data_from_esm_cloudcat.png
                            
                            :bdg-danger:`LMR-CMIP6`
                            
                            :bdg-primary:`AWS` :bdg-primary:`cloud-ready data` :bdg-primary:`data viz` :bdg-primary:`CMIP6`, :bdg-secondary:`intake` :bdg-secondary:`AWS` :bdg-secondary:`xarray` :bdg-secondary:`pandas`, :bdg-success:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 lmr-cmip6 lifehacks cartopy coordinate-systems matplotlib model-output notebook pandas xarray
                    
                        .. card:: spatial_snapshots
                            :link: https://linked.earth/LMR_CMIP_paleobook/spatial_snapshots_xarray_bonuses
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/spatial_snapshots_xarray_bonuses.png
                            :img-alt: spatial_snapshots_xarray_bonuses.png
                            
                            :bdg-danger:`LMR-CMIP6`
                            
                            :bdg-primary:`model output` :bdg-primary:`CMIP6` :bdg-primary:`coordinate systems`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`pandas`, :bdg-success:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: lmr-cmip6 lifehacks ipywidgets matplotlib model-output notebook
                    
                        .. card:: widget_primer
                            :link: https://linked.earth/LMR_CMIP_paleobook/widget_primer
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/widget_primer.png
                            :img-alt: widget_primer.png
                            
                            :bdg-danger:`LMR-CMIP6`
                            
                            :bdg-primary:`model output`, :bdg-secondary:`ipywidgets` :bdg-secondary:`matplotlib`, :bdg-success:`Lifehacks`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 lmr lmr-cmip6 science-bits cartopy matplotlib model-output notebook pandas pyleoclim xarray
                    
                        .. card:: CMIP6_LMR
                            :link: https://linked.earth/LMR_CMIP_paleobook/CMIP6_LMR
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/CMIP6_LMR.png
                            :img-alt: CMIP6_LMR.png
                            
                            :bdg-danger:`LMR-CMIP6`
                            
                            :bdg-primary:`model output` :bdg-primary:`LMR` :bdg-primary:`CMIP6`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`pandas` :bdg-secondary:`pyleoclim`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 holocene-climate lmr lmr-cmip6 science-bits volcanic-input cartopy ipywidgets matplotlib notebook xarray
                    
                        .. card:: VICS_dashboard
                            :link: https://linked.earth/LMR_CMIP_paleobook/VICS_dashboard
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/VICS_dashboard.png
                            :img-alt: VICS_dashboard.png
                            
                            :bdg-danger:`LMR-CMIP6`
                            
                            :bdg-primary:`Volcanic Input` :bdg-primary:`Holocene climate` :bdg-primary:`LMR` :bdg-primary:`CMIP6`, :bdg-secondary:`xarray` :bdg-secondary:`matplotlib` :bdg-secondary:`cartopy` :bdg-secondary:`ipywidgets`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: 2k-proxy-composite science-bits cfr notebook numpy pandas proxy-composite pyleoclim seaborn temperature
                    
                        .. card:: Hockey Stick
                            :link: https://khider.github.io/DISK-proxyComposite/HockeyStick
                            :img-top: https://raw.githubusercontent.com/khider/DISK-proxyComposite/main/proxycomposite/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-danger:`2k Proxy Composite`
                            
                            :bdg-primary:`proxy composite` :bdg-primary:`temperature`, :bdg-secondary:`numpy` :bdg-secondary:`seaborn` :bdg-secondary:`pandas` :bdg-secondary:`pyleoclim` :bdg-secondary:`cfr`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: ancientwmg science-bits basemap endmember-mixing matplotlib notebook pandas scipy sqlalchemy tracers watermass-geometry
                    
                        .. card:: Capstone notebook
                            :link: https://jordanplanders.github.io/past_life_wmg/jlanders_capstone_fixed
                            :img-top: https://raw.githubusercontent.com/jordanplanders/past_life_wmg/main/ancient_wmgr_book/thumbnails/ttest_flows_thumb.png
                            :img-alt: ttest_flows_thumb.png
                            
                            :bdg-danger:`AncientWMG`
                            
                            :bdg-primary:`watermass geometry` :bdg-primary:`tracers` :bdg-primary:`endmember mixing`, :bdg-secondary:`basemap` :bdg-secondary:`scipy` :bdg-secondary:`matplotlib` :bdg-secondary:`pandas` :bdg-secondary:`sqlalchemy`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: ancientwmg science-bits basemap clustering matplotlib notebook scikit-learn watermass-geometry
                    
                        .. card:: Cluster Centers
                            :link: https://jordanplanders.github.io/past_life_wmg/clustering_centers_on_raw
                            :img-top: https://raw.githubusercontent.com/jordanplanders/past_life_wmg/main/ancient_wmgr_book/thumbnails/centers_thumb.png
                            :img-alt: centers_thumb.png
                            
                            :bdg-danger:`AncientWMG`
                            
                            :bdg-primary:`clustering` :bdg-primary:`watermass geometry`, :bdg-secondary:`basemap` :bdg-secondary:`scikit-learn` :bdg-secondary:`matplotlib`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_1
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_1
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_2
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_2
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/odp.png
                            :img-alt: odp
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_3
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_3
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/leloup_paillard_odp_lp.png
                            :img-alt: leloup_paillard_odp_lp
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_4
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_4
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/sensitivity_1.png
                            :img-alt: sensitivity_1
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_5
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_5
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/ice_core.png
                            :img-alt: ice_core
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_6
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_6
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/8k_noise.png
                            :img-alt: 8k_noise
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_7
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_7
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/density.png
                            :img-alt: density
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm figures ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Figure_8
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Figure_8
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/resolution.png
                            :img-alt: resolution
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Figures`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Holocene_Ice_Analysis
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Holocene_Ice_Analysis
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Extras`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Holocene_Ice_Window_Increment
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Holocene_Ice_Window_Increment
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Extras`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: detecting-paleoclimate-transitions-with-lerm extras ammonyte data-viz matplotlib notebook pyleoclim
                    
                        .. card:: Holocene_Ice_Window_Size
                            :link: https://alexkjames.github.io/Detecting_Paleoclimate_Transitions_with_LERM/Holocene_Ice_Window_Size
                            :img-top: https://raw.githubusercontent.com/alexkjames/Detecting_Paleoclimate_Transitions_with_LERM/main/thumbnails/full_workflow.png
                            :img-alt: full_workflow
                            
                            :bdg-danger:`Detecting Paleoclimate Transitions with LERM`
                            
                            :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`ammonyte`, :bdg-success:`Extras`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits climlab cross-wavelet-analysis insolation notebook paleoceanography pyleoclim pylipd spectral-analysis wavelet-analysis xarray
                    
                        .. card:: Chasing cyclicities
                            :link: https://linked.earth/PyleoclimPaper/Chasing_orbital_cyclicities
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/wavelet.png
                            :img-alt: wavelet.png
                            
                            :bdg-danger:`Pyleoclim science`
                            
                            :bdg-primary:`spectral analysis` :bdg-primary:`wavelet analysis` :bdg-primary:`cross-wavelet analysis` :bdg-primary:`insolation` :bdg-primary:`paleoceanography`, :bdg-secondary:`xarray` :bdg-secondary:`pyleoclim` :bdg-secondary:`pylipd` :bdg-secondary:`climlab`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits model-output model-data-comparison notebook paleoclimate pyleoclim spectral-analysis xarray
                    
                        .. card:: Model-Data Confrontation
                            :link: https://linked.earth/PyleoclimPaper/Model_data_confrontation
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/spectralslope.png
                            :img-alt: spectralslope.png
                            
                            :bdg-danger:`Pyleoclim science`
                            
                            :bdg-primary:`model output` :bdg-primary:`spectral analysis` :bdg-primary:`model-data comparison` :bdg-primary:`paleoclimate`, :bdg-secondary:`xarray` :bdg-secondary:`pyleoclim`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pyleoclim-science science-bits age-uncertainty cartopy correlation notebook paleoclimate pyleoclim pylipd xarray
                    
                        .. card:: Correlations at Sea
                            :link: https://linked.earth/PyleoclimPaper/CrystalCorrelations
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/PyleoclimPaper/main/thumbnails/corrhist.png
                            :img-alt: corrhist.png
                            
                            :bdg-danger:`Pyleoclim science`
                            
                            :bdg-primary:`paleoclimate` :bdg-primary:`correlation` :bdg-primary:`age uncertainty`, :bdg-secondary:`xarray` :bdg-secondary:`pyleoclim` :bdg-secondary:`cartopy` :bdg-secondary:`pylipd`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: coral-sr/ca-calibration getting-started sr/ca calibration coral matplotlib notebook paleoceanography pandas pyleoclim
                    
                        .. card:: Data Exploration
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/DataExploration
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/dataexp.png
                            :img-alt: dataexp.png
                            
                            :bdg-danger:`Coral Sr/Ca calibration`
                            
                            :bdg-primary:`paleoceanography` :bdg-primary:`Sr/Ca` :bdg-primary:`coral` :bdg-primary:`calibration`, :bdg-secondary:`matplotlib` :bdg-secondary:`pyleoclim` :bdg-secondary:`pandas`, :bdg-success:`Getting Started`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: calibration calibration coral-sr/ca-calibration great-tables paleocenography statistics notebook statsmodel
                    
                        .. card:: Frequentist Calibration
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/FrequentistCalibration
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/table.png
                            :img-alt: table.png
                            
                            :bdg-danger:`Coral Sr/Ca calibration`
                            
                            :bdg-primary:`Statistics` :bdg-primary:`Calibration` :bdg-primary:`Paleocenography`, :bdg-secondary:`statsmodel` :bdg-secondary:`Great Tables`, :bdg-success:`Calibration`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: bayesian-statistics calibration calibration coral-sr/ca-calibration paleocenography arviz notebook pymc
                    
                        .. card:: Bayesian Calibration
                            :link: https://khider.github.io/dry-tortugas-calibration-fun/BayesianCalibration
                            :img-top: https://raw.githubusercontent.com/khider/dry-tortugas-calibration-fun/main/paleobook/thumbnails/bayes.png
                            :img-alt: bayes.png
                            
                            :bdg-danger:`Coral Sr/Ca calibration`
                            
                            :bdg-primary:`Bayesian Statistics` :bdg-primary:`Calibration` :bdg-primary:`Paleocenography`, :bdg-secondary:`pymc` :bdg-secondary:`arviz`, :bdg-success:`Calibration`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pca paleopca science-bits cartopy eofs matplotlib modeling notebook paleoceanography pandas pyleoclim xarray
                    
                        .. card:: Model-Data Comparison
                            :link: https://projectpythia.org/paleoPCA-cookbook/paleoPCA
                            :img-top: https://raw.githubusercontent.com/khider/paleoPCA/main/thumbnails/eof.png
                            :img-alt: eof.png
                            
                            :bdg-danger:`PaleoPCA`
                            
                            :bdg-primary:`paleoceanography` :bdg-primary:`PCA` :bdg-primary:`modeling`, :bdg-secondary:`xarray` :bdg-secondary:`pyleoclim` :bdg-secondary:`cartopy` :bdg-secondary:`matplotlib` :bdg-secondary:`pandas` :bdg-secondary:`eofs`, :bdg-success:`Science Bits`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: motivation paleoensembles data-assimilation data-viz matplotlib notebook paleoclimatology pens pyleoclim
                    
                        .. card:: motivation
                            :link: https://linked.earth/pens/notebooks/eg24-Fig1_motivation
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/motivation_thumbnail.png
                            :img-alt: motivation_thumbnail.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`paleoclimatology` :bdg-primary:`data assimilation` :bdg-primary:`data viz`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens` :bdg-secondary:`pyleoclim`, :bdg-success:`Motivation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pamodaco paleoensembles temporal-interpretation data-assimilation matplotlib notebook pens
                    
                        .. card:: Naïve resampling
                            :link: https://linked.earth/pens/notebooks/eg24-Fig2_naive_resampling
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/naive_thumbnail.png
                            :img-alt: naive_thumbnail.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`data assimilation` :bdg-primary:`PaMoDaCo`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens`, :bdg-success:`Temporal Interpretation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: paleoensembles temporal-interpretation data-assimilation matplotlib notebook pens seaborn statsmodels timeseries-modeling
                    
                        .. card:: LMRonline
                            :link: https://linked.earth/pens/notebooks/eg24-Fig3_4_LMRonline
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/LMRo_thumbnail.png
                            :img-alt: LMRo_thumbnail.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`data assimilation` :bdg-primary:`timeseries modeling`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens` :bdg-secondary:`statsmodels` :bdg-secondary:`seaborn`, :bdg-success:`Temporal Interpretation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: paleoensembles temporal-interpretation data-assimilation matplotlib notebook pens pyleoclim timeseries-modeling
                    
                        .. card:: resampling
                            :link: https://linked.earth/pens/notebooks/eg24-Fig5_resampling
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/resampling_thumbnail.png
                            :img-alt: resampling_thumbnail.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`data assimilation` :bdg-primary:`timeseries modeling`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens` :bdg-secondary:`pyleoclim`, :bdg-success:`Temporal Interpretation`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pamodaco paleoensembles plume-distance matplotlib notebook pens seaborn statistics
                    
                        .. card:: Definition & Properties
                            :link: https://linked.earth/pens/notebooks/eg24-Fig6_8_plume_distance
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/plume_dist.png
                            :img-alt: plume_dist.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`statistics` :bdg-primary:`PaMoDaCo`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens` :bdg-secondary:`seaborn`, :bdg-success:`Plume Distance`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pamodaco paleoensembles plume-distance matplotlib notebook pens seaborn statistics
                    
                        .. card:: Schematic
                            :link: https://linked.earth/pens/notebooks/eg24-Fig9_plume_distance-schematic
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/plume_schem.png
                            :img-alt: plume_schem.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`statistics` :bdg-primary:`PaMoDaCo`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens` :bdg-secondary:`seaborn`, :bdg-success:`Plume Distance`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: common-era paleoensembles paleoclimate-applications matplotlib notebook pens reconstruction scipy seaborn statistics
                    
                        .. card:: PAGES 2k (2019) ensemble
                            :link: https://linked.earth/pens/notebooks/eg24-Fig10_compare_PAGES2k2019_recons
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/PAGES2k_ensemble.png
                            :img-alt: PAGES2k_ensemble.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`reconstruction` :bdg-primary:`statistics` :bdg-primary:`Common Era`, :bdg-secondary:`matplotlib` :bdg-secondary:`seaborn` :bdg-secondary:`pens` :bdg-secondary:`scipy`, :bdg-success:`Paleoclimate Applications`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: common-era paleoensembles paleoclimate-applications matplotlib notebook pens reconstruction statistics
                    
                        .. card:: Büntgen et al (2021)
                            :link: https://linked.earth/pens/notebooks/eg24-Fig11_12_compare_LMRvsB21
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/B21_LMR.png
                            :img-alt: B21_LMR.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`reconstruction` :bdg-primary:`statistics` :bdg-primary:`Common Era`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens`, :bdg-success:`Paleoclimate Applications`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: pmip pamodaco paleoensembles paleoclimate-applications data-assimilation matplotlib notebook pandas pens pyleoclim
                    
                        .. card:: PMIP3
                            :link: https://linked.earth/pens/notebooks/eg24-Tab1_LMR_PMIP3_proximity_table
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/pens/jbook/thumbnails/PMIP3_LMR.png
                            :img-alt: PMIP3_LMR.png
                            
                            :bdg-danger:`PaleoEnsembles`
                            
                            :bdg-primary:`data assimilation` :bdg-primary:`PaMoDaCo` :bdg-primary:`PMIP`, :bdg-secondary:`matplotlib` :bdg-secondary:`pens` :bdg-secondary:`pyleoclim` :bdg-secondary:`pandas`, :bdg-success:`Paleoclimate Applications`
                            

        


.. raw:: html

    <div class="modal-backdrop"></div>


