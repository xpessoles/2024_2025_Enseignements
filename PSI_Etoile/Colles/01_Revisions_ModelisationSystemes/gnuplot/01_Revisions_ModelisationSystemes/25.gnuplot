set table "gnuplot/01_Revisions_ModelisationSystemes/25.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:3] [] [] log10(10**t),20*log10(abs(75/sqrt(1+(1*10**t)**2)))+20*log10(abs(1/sqrt(1+(.25*10**t)**2)))+20*log10(abs(1/(10**t)))-20*log10(abs(1/sqrt(1+(.0167*10**t)**2)))
