set table "gnuplot/FULL_POLY/16.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=1:5] [] [] log10(10**t),20*log10(abs(1/sqrt(1+(0.01*10**t)**2)))+20*log10(abs(1/sqrt(1+(0.0005*10**t)**2)))+20*log10(abs(1/(10**t)))
