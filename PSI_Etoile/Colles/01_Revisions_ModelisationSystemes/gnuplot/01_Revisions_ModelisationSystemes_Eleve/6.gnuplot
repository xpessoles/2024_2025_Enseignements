set table "gnuplot/01_Revisions_ModelisationSystemes_Eleve/6.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-2:2] [] [] log10(10**t),(t < log10(1./0.2) ? 20*log10(20) : 20*log10(0.1*10.0*20/(0.2))-20*log10(10**t))
