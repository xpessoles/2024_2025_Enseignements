set table "gnuplot/FULL_POLY/33.table"; set format "%.5f"
set samples 190.0; set parametric; plot [t=1:5] [] [] log10(10**t),-180/3.1415957*atan(0.000794*10**t)+-90
