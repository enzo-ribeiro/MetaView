from PIL import Image
from PIL.ExifTags import TAGS
from rich.console import Console
from rich.table import Table
from pypdf import PdfReader
def MetaIMG():
    image_input = input("Quel est le chemin de l'image ? \n")
    image = Image.open(image_input)
    ret = {}
    infos = image._getexif()

    if infos != None:
        for tag, value in infos.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        table = Table(title="MetaData", style="cyan")
        table.add_column("Key", justify="center", style="magenta")
        table.add_column("Value", justify="center", style="magenta")
        for key, value in ret.items():
            #print(key, " - ", value)
            if key == "UserComment":
                value=value.replace("\x00".encode(), ''.encode())
            table.add_row(str(key),str(value))
        console = Console()
        console.print(table)

    else:
        print("L'image n'a pas de métadonnées :(")

def MetaPDF():
    pdf_input = input("Quel est le chemin de le PDF ? \n")
    pdf = PdfReader(open(pdf_input, "rb"))
    meta_reader = pdf.metadata
    print(str(meta_reader))
    table = Table(title="PDF MetaData", style="cyan")
    table.add_column("Key", justify="center", style="magenta")
    table.add_column("Value", justify="center", style="magenta")
    for key, value in meta_reader.items():
        table.add_row(str(key), str(value))
    console = Console()
    console.print(table)




IMGorPDF = input("Quel type de fichier voulez-vous analyser ? \n\t(1) - Image \n\t(2) - PDF\n")

if IMGorPDF == "1":
    MetaIMG()

elif IMGorPDF == "2":
    MetaPDF()

else:
    print("AAAAAAAAAAAAAAAAAAARGH !!!!")

