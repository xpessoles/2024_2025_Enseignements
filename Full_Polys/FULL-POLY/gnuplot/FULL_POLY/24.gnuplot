set table "gnuplot/FULL_POLY/24.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-1:3] [] [] log10(10**t),(t < log10(1./1) ? 20*log10(75) : 20*log10(0.1*10.0*75/(1))-20*log10(10**t))+(t < log10(1./.25) ? 20*log10(1) : 20*log10(0.1*10.0*1/(.25))-20*log10(10**t))+20*log10(abs(1/(10**t)))-(t < log10(1./.0167) ? 20*log10(1) : 20*log10(0.1*10.0*1/(.0167))-20*log10(10**t))
