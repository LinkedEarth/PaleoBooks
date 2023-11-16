


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
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Domains</button>
    <ul class="dropdown-menu" aria-labelledby="domainsDropdown"><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=aws onchange="change();">&nbsp;AWS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=c14 onchange="change();">&nbsp;C14</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cmip6 onchange="change();">&nbsp;CMIP6</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=deglaciation onchange="change();">&nbsp;Deglaciation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=holocene-climate onchange="change();">&nbsp;Holocene climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=lmr onchange="change();">&nbsp;LMR</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=mystery-interval onchange="change();">&nbsp;Mystery Interval</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoceanography onchange="change();">&nbsp;Paleoceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=volcanic-input onchange="change();">&nbsp;Volcanic Input</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=cloud-ready-data onchange="change();">&nbsp;cloud-ready data</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=clustering onchange="change();">&nbsp;clustering</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=coordinate-systems onchange="change();">&nbsp;coordinate systems</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-viz onchange="change();">&nbsp;data viz</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=end onchange="change();">&nbsp;eNd</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=machine-learning onchange="change();">&nbsp;machine learning</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=model-output onchange="change();">&nbsp;model output</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=proxy-composite onchange="change();">&nbsp;proxy composite</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=temperature onchange="change();">&nbsp;temperature</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=tracers onchange="change();">&nbsp;tracers</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=watermass-geometry onchange="change();">&nbsp;watermass geometry</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="formatsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Formats</button>
    <ul class="dropdown-menu" aria-labelledby="formatsDropdown"><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=2k-proxy-composite onchange="change();">&nbsp;2k Proxy Composite</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=c-itrace onchange="change();">&nbsp;C-iTRACE</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=lmr-cmip6 onchange="change();">&nbsp;LMR-CMIP6</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=lifehacks onchange="change();">&nbsp;Lifehacks</label></li><li><label class="dropdown-item checkbox formats"><input type="checkbox" rel=science-bits onchange="change();">&nbsp;Science Bits</label></li></ul>
    </div>



    <div class="dropdown">
    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Packages</button>
    <ul class="dropdown-menu" aria-labelledby="packagesDropdown"><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=aws onchange="change();">&nbsp;AWS</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cartopy onchange="change();">&nbsp;cartopy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cfr onchange="change();">&nbsp;cfr</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake onchange="change();">&nbsp;intake</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ipywidgets onchange="change();">&nbsp;ipywidgets</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=matplotlib onchange="change();">&nbsp;matplotlib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=numpy onchange="change();">&nbsp;numpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pandas onchange="change();">&nbsp;pandas</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pyleoclim onchange="change();">&nbsp;pyleoclim</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=scikit-learn onchange="change();">&nbsp;scikit-learn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=seaborn onchange="change();">&nbsp;seaborn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;xarray</label></li></ul>
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
                    
                        .. card:: C-iTrace Paleobook
                            :link: https://linked.earth/citrace_paleobook/README.html
                        
                            .. image:: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/thumbnail.png
                                :alt: thumbnail.png
                                :align: center
                                :target: https://linked.earth/citrace_paleobook/README.html
                                :height: 80
                            
                            :bdg-primary:`tracers`, :bdg-primary:`machine learning`, :bdg-primary:`oceanography`, :bdg-primary:`coordinate systems`, :bdg-primary:`C14`, :bdg-primary:`Mystery Interval`, :bdg-primary:`eNd`, :bdg-primary:`model output`, :bdg-primary:`clustering`, :bdg-primary:`Deglaciation`, :bdg-primary:`data viz`, :bdg-primary:`Paleoceanography`, :bdg-primary:`watermass geometry`, :bdg-secondary:`xarray`, :bdg-secondary:`seaborn`, :bdg-secondary:`matplotlib`, :bdg-secondary:`pandas`, :bdg-secondary:`scikit-learn`, :bdg-secondary:`cartopy`, :bdg-secondary:`intake`, :bdg-info:`C-iTRACE`, :bdg-info:`Science Bits`, :bdg-info:`Lifehacks`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: aws aws cmip6 holocene-climate lmr lmr-cmip6 lifehacks science-bits volcanic-input cartopy cloud-ready-data coordinate-systems data-viz intake ipywidgets matplotlib model-output pandas pyleoclim xarray
                    
                        .. card:: LMR-CMIP6 Paleobook
                            :link: https://linked.earth/LMR_CMIP_paleobook/README.html
                        
                            .. image:: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/thumbnail.png
                                :alt: thumbnail.png
                                :align: center
                                :target: https://linked.earth/LMR_CMIP_paleobook/README.html
                                :height: 80
                            
                            :bdg-primary:`CMIP6`, :bdg-primary:`coordinate systems`, :bdg-primary:`LMR`, :bdg-primary:`AWS`, :bdg-primary:`Volcanic Input`, :bdg-primary:`Holocene climate`, :bdg-primary:`cloud-ready data`, :bdg-primary:`model output`, :bdg-primary:`data viz`, :bdg-secondary:`pyleoclim`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`pandas`, :bdg-secondary:`AWS`, :bdg-secondary:`cartopy`, :bdg-secondary:`intake`, :bdg-secondary:`ipywidgets`, :bdg-info:`LMR-CMIP6`, :bdg-info:`Science Bits`, :bdg-info:`Lifehacks`

            
        

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: 2k-proxy-composite science-bits cfr numpy pandas proxy-composite pyleoclim seaborn temperature
                    
                        .. card:: Reproducing the Hockey Stick - Proxy composite over the past 2,000 years using the cfr package
                            :link: https://khider.github.io/DISK-proxyComposite/intro.html
                        
                            .. image:: https://raw.githubusercontent.com/khider/DISK-proxyComposite/main/proxycomposite/thumbnails/thumbnail.png
                                :alt: thumbnail.png
                                :align: center
                                :target: https://khider.github.io/DISK-proxyComposite/intro.html
                                :height: 80
                            
                            :bdg-primary:`proxy composite`, :bdg-primary:`temperature`, :bdg-secondary:`pyleoclim`, :bdg-secondary:`numpy`, :bdg-secondary:`seaborn`, :bdg-secondary:`pandas`, :bdg-secondary:`cfr`, :bdg-info:`Science Bits`, :bdg-info:`2k Proxy Composite`

            
        

+++++++++++++++
Chapters
+++++++++++++++

.. grid:: 1 2 2 2



                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace lifehacks cartopy data-viz matplotlib notebook oceanography pandas seaborn tracers xarray
                    
                        .. card:: pyODV
                            :link: https://linked.earth/citrace_paleobook/notebooks/lifehacks/pyODV.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/pyodv_demo.png
                            :img-alt: pyodv_demo.png
                            
                            :bdg-primary:`oceanography`, :bdg-primary:`tracers`, :bdg-primary:`data viz`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`pandas`, :bdg-secondary:`seaborn`, :bdg-info:`notebook`, :bdg-info:`Lifehacks`, :bdg-info:`C-iTRACE`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace lifehacks cartopy coordinate-systems intake matplotlib model-output notebook oceanography pandas xarray
                    
                        .. card:: data_on_a_model_grid
                            :link: https://linked.earth/citrace_paleobook/notebooks/lifehacks/working_with_data_on_a_model_grid.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/citrace_model_grid.png
                            :img-alt: citrace_model_grid.png
                            
                            :bdg-primary:`model output`, :bdg-primary:`oceanography`, :bdg-primary:`coordinate systems`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`pandas`, :bdg-secondary:`intake`, :bdg-info:`notebook`, :bdg-info:`Lifehacks`, :bdg-info:`C-iTRACE`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace science-bits cartopy end matplotlib model-output notebook pandas xarray
                    
                        .. card:: model_data_comp
                            :link: https://linked.earth/citrace_paleobook/notebooks/science_bits/data_scatter_on_pcolor.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/section_eNd_uncertaintyrange.png
                            :img-alt: section_eNd_uncertaintyrange.png
                            
                            :bdg-primary:`model output`, :bdg-primary:`eNd`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`pandas`, :bdg-info:`notebook`, :bdg-info:`Science Bits`, :bdg-info:`C-iTRACE`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace science-bits cartopy clustering machine-learning matplotlib notebook scikit-learn watermass-geometry xarray
                    
                        .. card:: clustering
                            :link: https://linked.earth/citrace_paleobook/notebooks/science_bits/clustering.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/cluster_section.png
                            :img-alt: cluster_section.png
                            
                            :bdg-primary:`clustering`, :bdg-primary:`machine learning`, :bdg-primary:`watermass geometry`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`scikit-learn`, :bdg-info:`notebook`, :bdg-info:`Science Bits`, :bdg-info:`C-iTRACE`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: c-itrace c14 deglaciation mystery-interval paleoceanography science-bits cartopy matplotlib notebook pandas xarray
                    
                        .. card:: model_downcore_D14C
                            :link: https://linked.earth/citrace_paleobook/notebooks/science_bits/PaMoDaCo_downcore_D14C.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/citrace_paleobook/main/thumbnails/C14_downcore_modelmarchitto.png
                            :img-alt: C14_downcore_modelmarchitto.png
                            
                            :bdg-primary:`C14`, :bdg-primary:`Paleoceanography`, :bdg-primary:`Deglaciation`, :bdg-primary:`Mystery Interval`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`pandas`, :bdg-info:`notebook`, :bdg-info:`Science Bits`, :bdg-info:`C-iTRACE`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: aws aws cmip6 lmr-cmip6 lifehacks cloud-ready-data data-viz intake notebook pandas xarray
                    
                        .. card:: data_from_esm_cloudcat
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/lifehacks/data_from_esm_cloudcat.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/data_from_esm_cloudcat.png
                            :img-alt: data_from_esm_cloudcat.png
                            
                            :bdg-primary:`AWS`, :bdg-primary:`cloud-ready data`, :bdg-primary:`data viz`, :bdg-primary:`CMIP6`, :bdg-secondary:`intake`, :bdg-secondary:`AWS`, :bdg-secondary:`xarray`, :bdg-secondary:`pandas`, :bdg-info:`notebook`, :bdg-info:`Lifehacks`, :bdg-info:`LMR-CMIP6`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 lmr-cmip6 lifehacks cartopy coordinate-systems matplotlib model-output notebook pandas xarray
                    
                        .. card:: spatial_snapshots
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/lifehacks/spatial_snapshots_xarray_bonuses.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/spatial_snapshots_xarray_bonuses.png
                            :img-alt: spatial_snapshots_xarray_bonuses.png
                            
                            :bdg-primary:`model output`, :bdg-primary:`CMIP6`, :bdg-primary:`coordinate systems`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`pandas`, :bdg-info:`notebook`, :bdg-info:`Lifehacks`, :bdg-info:`LMR-CMIP6`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: lmr-cmip6 lifehacks ipywidgets matplotlib model-output notebook
                    
                        .. card:: widget_primer
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/lifehacks/widget_primer.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/widget_primer.png
                            :img-alt: widget_primer.png
                            
                            :bdg-primary:`model output`, :bdg-secondary:`ipywidgets`, :bdg-secondary:`matplotlib`, :bdg-info:`notebook`, :bdg-info:`Lifehacks`, :bdg-info:`LMR-CMIP6`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 lmr lmr-cmip6 science-bits cartopy matplotlib model-output notebook pandas pyleoclim xarray
                    
                        .. card:: CMIP6_LMR
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/science_bits/CMIP6_LMR.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/CMIP6_LMR.png
                            :img-alt: CMIP6_LMR.png
                            
                            :bdg-primary:`model output`, :bdg-primary:`LMR`, :bdg-primary:`CMIP6`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`pandas`, :bdg-secondary:`pyleoclim`, :bdg-info:`notebook`, :bdg-info:`Science Bits`, :bdg-info:`LMR-CMIP6`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: cmip6 holocene-climate lmr lmr-cmip6 science-bits volcanic-input cartopy ipywidgets matplotlib notebook xarray
                    
                        .. card:: VICS_dashboard
                            :link: https://linked.earth/LMR_CMIP_paleobook/notebooks/science_bits/VICS_dashboard.html
                            :img-top: https://raw.githubusercontent.com/LinkedEarth/LMR_CMIP_paleobook/main/thumbnails/VICS_dashboard.png
                            :img-alt: VICS_dashboard.png
                            
                            :bdg-primary:`Volcanic Input`, :bdg-primary:`Holocene climate`, :bdg-primary:`LMR`, :bdg-primary:`CMIP6`, :bdg-secondary:`xarray`, :bdg-secondary:`matplotlib`, :bdg-secondary:`cartopy`, :bdg-secondary:`ipywidgets`, :bdg-info:`notebook`, :bdg-info:`Science Bits`, :bdg-info:`LMR-CMIP6`
                            

        


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: 2k-proxy-composite science-bits cfr notebook numpy pandas proxy-composite pyleoclim seaborn temperature
                    
                        .. card:: Hockey Stick
                            :link: https://khider.github.io/DISK-proxyComposite/notebooks/science_bits/HockeyStick.html
                            :img-top: https://raw.githubusercontent.com/khider/DISK-proxyComposite/main/proxycomposite/thumbnails/thumbnail.png
                            :img-alt: thumbnail.png
                            
                            :bdg-primary:`proxy composite`, :bdg-primary:`temperature`, :bdg-secondary:`numpy`, :bdg-secondary:`seaborn`, :bdg-secondary:`pandas`, :bdg-secondary:`pyleoclim`, :bdg-secondary:`cfr`, :bdg-info:`notebook`, :bdg-info:`Science Bits`, :bdg-info:`2k Proxy Composite`
                            

        


.. raw:: html

    <div class="modal-backdrop"></div>


