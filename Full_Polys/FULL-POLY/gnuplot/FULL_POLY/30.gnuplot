set table "gnuplot/FULL_POLY/30.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=1:5] [] [] log10(10**t),(t < log10(1./0.000794) ? 20*log10(1773) : 20*log10(0.1*10.0*1773/(0.000794))-20*log10(10**t))+20*log10(abs(1/(10**t)))
