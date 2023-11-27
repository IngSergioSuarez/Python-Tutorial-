cadena = "DSP: <sy><sy><sx>M002458-MRWR<cr>M007001458-MRWR<cr>0024500 PSI AE/SS<cr>003#1_Stone<cr>0041789<cr>005SAND<cr>0061345<cr>007ILLINOIS<cr>008510<cr>009FLYASH<cr>01095<cr>011WATER#1<cr>0120031.00<cr>013MIRRA110<cr>014000054.450<cr>015DAREX2<cr>016000004.240<cr>033000<cr>03410.00<cr>03706.00<cr>038005.00<cr>042N<cr>M003458-MRWR<cr><ex><et>"

# Encuentra la posición de <SX>
posicion_sx = cadena.find("<sx>")

# Elimina los espacios antes de <SX>
cadena_sin_espacios = cadena[:posicion_sx].replace(" ", "").replace("\t", "").replace("\n", "") + cadena[posicion_sx:]
print(cadena_sin_espacios)
print("hola")