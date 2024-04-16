from PIL import Image
from PIL.ExifTags import TAGS
from rich.console import Console
from rich.table import Table
from pypdf import PdfReader, PdfWriter
from datetime import datetime

def ReadIMG():
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
        print("L'image n'a pas de métadonnées :(\n")

def WriteIMG():
    image_input = input("Quel est le chemin de l'image ? \n")
    image = Image.open(image_input)

    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    image_without_exif.save(image_input)

    # as a good practice, close the file handler after saving the image.
    image_without_exif.close()
    print("Les metadonnées ont été supprimé !")

def ReadPDF():
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

def WritePDF():
    pdf_input = input("Quel est le chemin de le PDF ? \n")
    pdf = PdfReader(pdf_input)
    pdf_writer = PdfWriter()

    for page in pdf.pages:
        pdf_writer.add_page(page)

    metadata = pdf.metadata
    pdf_writer.add_metadata(metadata)

    utc_time = "-05'00'"
    time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")

    Author = str(input("Qui est l'auteur de PDF ?"))
    Producer = str(input("Qui est le producteur de ce PDF ?"))
    Title = str(input("Quel est le nom de ce PDF ?"))
    Subject = str(input("Quel est le sujet de ce PDF ?"))
    Keywords = str(input("Quel son les Keywords/Tags du PDF ?"))
    Creator = str(input("Qui est le créateur de ce PDF ?"))
    CustomField = input("Voulez-vous ajouter un champ personnalisé ?\n\t(1) - Oui\n\t(2) - Non")

    if CustomField == "1" :
        Write_custom = str(input("Quel texte voulez-vous ajouter ?"))
    else:
        Write_custom = str("")

    pdf_writer.add_metadata(
        {
            "/Author": Author,
            "/Producer": Producer,
            "/Title": Title,
            "/Subject": Subject,
            "/Keywords": Keywords,
            "/CreationDate": time,
            "/ModDate": time,
            "/Creator": Creator,
            "/CustomField": Write_custom,
        }
    )
    modifName = str(input("Quel est le nom du nouveau fichier "))
    with open(modifName, "wb") as f:
        pdf_writer.write(f)

ascii_font = """
• ▌ ▄ ·. ▄▄▄ .▄▄▄▄▄ ▄▄▄·  ▌ ▐·▪  ▄▄▄ .▄▄▌ ▐ ▄▌
·██ ▐███▪▀▄.▀·•██  ▐█ ▀█ ▪█·█▌██ ▀▄.▀·██· █▌▐█
▐█ ▌▐▌▐█·▐▀▀▪▄ ▐█.▪▄█▀▀█ ▐█▐█•▐█·▐▀▀▪▄██▪▐█▐▐▌
██ ██▌▐█▌▐█▄▄▌ ▐█▌·▐█ ▪▐▌ ███ ▐█▌▐█▄▄▌▐█▌██▐█▌
▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀  ▀  ▀ . ▀  ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪
"""

print(ascii_font)

RorW = input("Que voulez-vous faire sur les metadonnées du fichiers ?\n\t(1) - Lire\n\t(2) - Modifier\n")

if RorW == "1":
    IMGorPDF = input("Quel type de fichier voulez-vous analyser ? \n\t(1) - Image \n\t(2) - PDF\n")
    if IMGorPDF == "1":
        ReadIMG()
    elif IMGorPDF == "2":
        ReadPDF()
    else:
        print("AAAAAAAAAAAAAAAAAAARGH !!!!")

elif RorW == "2":
    IMGorPDF = input("Sur quel type de fichier voulez-vous ecrire ? \n\t(1) - Image\n\t(2) - PDF\n")
    if IMGorPDF == "1":
        WriteIMG()
    else:
        WritePDF()
else:
    print("AAAAAAAAAAAAAAAAAAARGH !!!!")