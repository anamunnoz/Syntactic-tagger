import subprocess

ruta_analyzer = r'C:\Users\anagm\Desktop\Tesis\winfreeling-4.2\freeling-win\freeling\bin\analyzer.exe'
ruta_cfg = r'C:\Users\anagm\Desktop\Tesis\winfreeling-4.2\freeling-win\freeling\share\freeling\config\es.cfg'

texto = "Creo que va a llover, pero no estoy seguro. Además, María dijo que saldría si el clima mejora."

try:
    proceso = subprocess.Popen(
        [ruta_analyzer, "-f", ruta_cfg],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    salida, error = proceso.communicate(input=texto.strip() + "\n\n")
    print(error)
    if error:
        print("⚠️ STDERR:")
        print(error)

    print("✅ SALIDA RAW:")
    print(salida)

    print("\n📘 ORACIONES DETECTADAS:")
    oraciones = salida.strip().split("</S>")
    for i, oracion in enumerate(oraciones):
        oracion = oracion.strip()
        if oracion:
            print(f"[{i+1}]")
            print(oracion + "\n")

except Exception as e:
    print("❌ Error al ejecutar FreeLing:", str(e))
