set table "gnuplot/01_Revisions_ModelisationSystemes/19.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:3] [] [] log10(10**t),180/3.1415957*(atan((80**2-(10**t)**2)/(2*0.1*80*10**t))-3.1415957/2)+-90--180/3.1415957*atan(1*10**t)
