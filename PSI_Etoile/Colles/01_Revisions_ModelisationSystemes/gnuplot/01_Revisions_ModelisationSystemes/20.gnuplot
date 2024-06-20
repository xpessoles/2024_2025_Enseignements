set table "gnuplot/01_Revisions_ModelisationSystemes/20.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:1] [] [] log10(10**t),(t<log10(1)?20*log10(24):+20*log10(24)+40*log10(1)-40*log10(10**t))+(t < log10(1./40) ? 20*log10(1) : 20*log10(0.1*10.0*1/(40))-20*log10(10**t))
