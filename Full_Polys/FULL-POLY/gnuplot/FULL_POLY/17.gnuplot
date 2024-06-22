set table "gnuplot/FULL_POLY/17.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=1:5] [] [] log10(10**t),-180/3.1415957*atan(0.01*10**t)+-180/3.1415957*atan(0.0005*10**t)+-90
