set table "gnuplot/01_Revisions_ModelisationSystemes/21.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:1] [] [] log10(10**t),20*log10(abs(24/sqrt((1-(10**t/1)**2)**2+(2*0.1*(10**t/1))**2)))+20*log10(abs(1/sqrt(1+(40*10**t)**2)))
