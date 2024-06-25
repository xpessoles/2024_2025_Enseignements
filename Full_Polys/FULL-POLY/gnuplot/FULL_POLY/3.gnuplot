set table "gnuplot/FULL_POLY/3.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=1:5] [] [] log10(10**t),(t<log10(1./(0.000794))? 0:-90)+-90
