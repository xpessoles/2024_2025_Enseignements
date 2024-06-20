set table "gnuplot/01_Revisions_ModelisationSystemes_Eleve/22.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:1] [] [] log10(10**t),(t<log10(1)? 0:-180)+(t<log10(1./(40))? 0:-90)
