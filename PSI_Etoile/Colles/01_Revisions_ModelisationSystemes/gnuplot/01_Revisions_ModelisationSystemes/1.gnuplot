set table "gnuplot/01_Revisions_ModelisationSystemes/1.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:2] [] [] log10(10**t),20*log10(abs(2))
