set table "gnuplot/FULL_POLY/26.table"; set format "%.5f"
set samples 200.0; set parametric; plot [t=-1:3] [] [] log10(10**t),(t<log10(1./(1))? 0:-90)+(t<log10(1./(.25))? 0:-90)+-90-(t < log10(1./.0167) ? 20*log10(1) : 20*log10(0.1*10.0*1/(.0167))-20*log10(10**t))
