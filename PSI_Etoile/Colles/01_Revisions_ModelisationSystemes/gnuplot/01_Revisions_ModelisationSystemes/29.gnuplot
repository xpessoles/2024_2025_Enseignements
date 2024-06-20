set table "gnuplot/01_Revisions_ModelisationSystemes/29.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:2] [] [] log10(10**t),-180/3.1415957*atan(0.2*10**t)
