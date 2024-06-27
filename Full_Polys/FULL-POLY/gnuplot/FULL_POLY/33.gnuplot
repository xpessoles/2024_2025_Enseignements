set table "gnuplot/FULL_POLY/33.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:3] [] [] log10(10**t),180/3.1415957*(atan((1**2-(10**t)**2)/(2*.1*1*10**t))-3.1415957/2)--90--180/3.1415957*atan(0.01*10**t)
