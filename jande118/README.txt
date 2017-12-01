Things to address:
  * main script for grabbing data?
  * "smushing" files

How to extract other libraries?
  * scripts?
  * usage?

scourceforge.net
libraries.io and then look at package managers
https://libraries.io/data 
  the second one Libaries.io-open-data-1.0.1.zip

extracted 
************
*Cytoscape:*
************

import > network > file > *.csv
Source = Dependency Names 
Leaves =

--------------------------------------------------
Reproducibility and using libraries.io, 
  version information good for reproducibility

Keeping:
  - dependency name (source)
  - project name (target)
  - dependency kind 
    (not for now, but might be good attribute) 
  - version (multigraphs might result)

Don't keep:
  - dependency platform
  - project_id

Most outdegree: most relied-upon

Talking about how data file affects views, view size

Layout > Hierarchical Layout etc. but also try google

Tools > NetworkAnalyzer > Network Analysis > Analyze Network
  - then choose directed or undirected
  - OutDegree? should be able to get from analysis
  - clustering coefficients, ecentricity, 
  - clustering in CytoScape?

Degree... 

Highlight OutDegree stuff

