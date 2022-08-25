#Importa bibliotecas os, sys and PyPDF2
import sys, ctypes
from PyPDF2 import PdfFileMerger

#Initializa PdfFileMerger e cria lista com arquivos carregados pelo ?pdfMerge?.bat
msgBox = ctypes.windll.user32.MessageBoxW
output = PdfFileMerger()
caminhoArquivos = sys.argv[1:]

#Concatena arquivos carregados
for arquivo in caminhoArquivos:
    if (arquivo[-3:] == "pdf"):
        output.append(arquivo)
    
    else:
        msgBox(None,"Este programa só aceita arquivos do tipo PDF","pdfMerge - Erro",0)
        sys.exit()

#Define nome e endereço final do arquivo
arquivoFinal = caminhoArquivos[0][:-4]

#Cria arquivo final na pasta
with open(arquivoFinal + " - Mesclado.pdf", "wb") as output_stream:
    output.write(output_stream)