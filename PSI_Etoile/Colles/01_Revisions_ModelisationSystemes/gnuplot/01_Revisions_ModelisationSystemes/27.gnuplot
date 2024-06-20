set table "gnuplot/01_Revisions_ModelisationSystemes/27.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:3] [] [] log10(10**t),-180/3.1415957*atan(1*10**t)+-180/3.1415957*atan(.25*10**t)+-90--180/3.1415957*atan(.0167*10**t)
