set table "gnuplot/01_Revisions_ModelisationSystemes/28.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:2] [] [] log10(10**t),20*log10(abs(500/sqrt(1+(0.2*10**t)**2)))
