set table "gnuplot/FULL_POLY/16.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:3] [] [] log10(10**t),20*log10(abs(1/sqrt((1-(10**t/1)**2)**2+(2*.1*(10**t/1))**2)))-20*log10(abs(0.01/(10**t)))-20*log10(abs(1/sqrt(1+(0.01*10**t)**2)))
