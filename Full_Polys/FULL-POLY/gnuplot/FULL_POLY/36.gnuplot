set table "gnuplot/FULL_POLY/36.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:1] [] [] log10(10**t),-(t<log10(1./(10))? 0:-90)+-90
