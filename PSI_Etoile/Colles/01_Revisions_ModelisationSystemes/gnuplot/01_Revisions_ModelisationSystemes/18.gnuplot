set table "gnuplot/01_Revisions_ModelisationSystemes/18.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:3] [] [] log10(10**t),20*log10(abs(4.5/sqrt((1-(10**t/80)**2)**2+(2*0.1*(10**t/80))**2)))+20*log10(abs(1/(10**t)))-20*log10(abs(1/sqrt(1+(1*10**t)**2)))
