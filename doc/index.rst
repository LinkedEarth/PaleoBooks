
Cookbooks Gallery
=====================



Gallery
========

.. raw:: html

    <div class="d-sm-flex mt-3 mb-4">
    <div class="d-flex gallery-menu">
    </div>
    <div class="ml-auto d-flex">
    <div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

    <div class="dropdown">

    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Domains
    </button>
    <ul class="dropdown-menu" aria-labelledby="domainsDropdown">
    <li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=AWS-Cloud onchange="change();">&nbsp;AWS Cloud</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=AWS-cloud onchange="change();">&nbsp;AWS cloud</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Basemaps onchange="change();">&nbsp;Basemaps</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Data-Access onchange="change();">&nbsp;Data Access</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Data-access onchange="change();">&nbsp;Data access</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=GIS onchange="change();">&nbsp;GIS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Geospatial-data onchange="change();">&nbsp;Geospatial data</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=HRRR-model onchange="change();">&nbsp;HRRR model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=NASA-EarthData-GIBS onchange="change();">&nbsp;NASA EarthData GIBS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Satellite-imagery onchange="change();">&nbsp;Satellite imagery</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Spatial-analysis onchange="change();">&nbsp;Spatial analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate onchange="change();">&nbsp;climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-science onchange="change();">&nbsp;data science</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=machine-learning onchange="change();">&nbsp;machine learning</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=meteorology onchange="change();">&nbsp;meteorology</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=ml onchange="change();">&nbsp;ml</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=radar onchange="change();">&nbsp;radar</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=satellite onchange="change();">&nbsp;satellite</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=scientific-software-engineering onchange="change();">&nbsp;scientific software engineering</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=zarr onchange="change();">&nbsp;zarr</label></li>
    </ul>
    </div>


    <div class="dropdown">

    <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Packages
    </button>
    <ul class="dropdown-menu" aria-labelledby="packagesDropdown">
    <li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=IPython onchange="change();">&nbsp;IPython</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=Py-Art onchange="change();">&nbsp;Py-Art</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=Pyresample onchange="change();">&nbsp;Pyresample</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cartopy onchange="change();">&nbsp;cartopy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=dask onchange="change();">&nbsp;dask</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geoviews onchange="change();">&nbsp;geoviews</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=hvPlot onchange="change();">&nbsp;hvPlot</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake onchange="change();">&nbsp;intake</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-esm onchange="change();">&nbsp;intake-esm</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-markdown onchange="change();">&nbsp;intake-markdown</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-xarray onchange="change();">&nbsp;intake-xarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=kerchunk onchange="change();">&nbsp;kerchunk</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=matplotlib onchange="change();">&nbsp;matplotlib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=numpy onchange="change();">&nbsp;numpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=owslib onchange="change();">&nbsp;owslib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=panel onchange="change();">&nbsp;panel</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=tensorflow onchange="change();">&nbsp;tensorflow</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=verde onchange="change();">&nbsp;verde</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xESMF onchange="change();">&nbsp;xESMF</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;xarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xbatcher onchange="change();">&nbsp;xbatcher</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xesmf onchange="change();">&nbsp;xesmf</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=zarr onchange="change();">&nbsp;zarr</label></li>
    </ul>
    </div>

    </div>
    </div>
    <script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>



.. grid:: 2 3 3 4



    
                	.. grid-item::
                            
                		.. card:: CESM LENS on AWS Cookbook
                			:link: https://projectpythia.org/cesm-lens-aws-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/cesm-lens-aws-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`climate`, :bdg-secondary:`intake-esm`, :bdg-secondary:`xarray`, :bdg-secondary:`dask`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: CMIP6 Cookbook
                			:link: https://projectpythia.org/cmip6-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/cmip6-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`climate`, :bdg-secondary:`intake-esm`, :bdg-secondary:`xesmf`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: HRRR-AWS-Cookbook
                			:link: https://projectpythia.org/HRRR-AWS-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/HRRR-AWS-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`HRRR model`, :bdg-primary:`AWS cloud`, :bdg-primary:`zarr`, :bdg-secondary:`xarray`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: Radar Cookbook
                			:link: https://projectpythia.org/radar-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/radar-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`radar`, :bdg-secondary:`Py-Art`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: Intake Cookbook
                			:link: https://projectpythia.org/intake-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/intake-cookbook/main/thumbnail.svg
                			:img-alt:
                            
                			:bdg-primary:`Data access`, :bdg-secondary:`intake`, :bdg-secondary:`intake-xarray`, :bdg-secondary:`intake-markdown`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: Landsat ML Cookbook
                			:link: https://projectpythia.org/landsat-ml-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/landsat-ml-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`satellite`, :bdg-primary:`ml`, :bdg-primary:`climate`, :bdg-secondary:`hvPlot`, :bdg-secondary:`intake`, :bdg-secondary:`xarray`, :bdg-secondary:`dask`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: Kerchunk Cookbook
                			:link: https://projectpythia.org/kerchunk-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/kerchunk-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`AWS Cloud`, :bdg-primary:`Data Access`, :bdg-primary:`HRRR model`, :bdg-primary:`zarr`, :bdg-secondary:`kerchunk`, :bdg-secondary:`intake`, :bdg-secondary:`xarray`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: xbatcher for Machine Learning Part 1
                			:link: https://projectpythia.org/xbatcher-ML-1-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/xbatcher-ML-1-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`oceanography`, :bdg-primary:`machine learning`, :bdg-primary:`data science`, :bdg-primary:`scientific software engineering`, :bdg-secondary:`numpy`, :bdg-secondary:`xarray`, :bdg-secondary:`zarr`, :bdg-secondary:`intake`, :bdg-secondary:`matplotlib`, :bdg-secondary:`IPython`, :bdg-secondary:`tensorflow`, :bdg-secondary:`xbatcher`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: Dask Cookbook
                			:link: https://projectpythia.org/dask-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/dask-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`xarray`, :bdg-primary:`dask`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: ARCO ERA-5 Interactive Visualization
                			:link: https://projectpythia.org/ERA5_interactive-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/ERA5_interactive-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`meteorology`, :bdg-secondary:`zarr`, :bdg-secondary:`geoviews`, :bdg-secondary:`panel`, :bdg-secondary:`xarray`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: Web Map / Feature Services Cookbook
                			:link: https://projectpythia.org/web-map-feature-services-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/web-map-feature-services-cookbook/main/thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`Geospatial data`, :bdg-primary:`Basemaps`, :bdg-primary:`Satellite imagery`, :bdg-primary:`Spatial analysis`, :bdg-primary:`NASA EarthData GIBS`, :bdg-primary:`GIS`, :bdg-secondary:`hvPlot`, :bdg-secondary:`cartopy`, :bdg-secondary:`geoviews`, :bdg-secondary:`panel`, :bdg-secondary:`owslib`
            
            
        

    
                	.. grid-item::
                            
                		.. card:: (re)Gridding with xarray
                			:link: https://projectpythia.org/gridding-cookbook/README.html
                			:img-top: https://raw.githubusercontent.com/ProjectPythia/gridding-cookbook/main/grid_thumbnail.png
                			:img-alt:
                            
                			:bdg-primary:`xarray`, :bdg-primary:`verde`, :bdg-primary:`xESMF`, :bdg-primary:`Pyresample`
            
            
        

```

.. raw:: html

    <div class="modal-backdrop"></div>
    <script src="doc/_static/custom.js"></script>

