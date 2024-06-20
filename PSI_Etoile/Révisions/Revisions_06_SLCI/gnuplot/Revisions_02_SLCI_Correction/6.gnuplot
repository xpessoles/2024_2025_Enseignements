set table "gnuplot/Revisions_02_SLCI_Correction/6.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:1] [] [] log10(10**t),-20*log10(abs(1/sqrt(1+(10*10**t)**2)))+20*log10(abs(1/(10**t)))+20*log10(abs(0.1))
