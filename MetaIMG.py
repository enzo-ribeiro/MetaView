from PIL import Image
from PIL.ExifTags import TAGS
from rich.console import Console
from rich.table import Table

def MetaIMG():
    image_input = input("Quel est le chemin de l'image ? \n")
    image = Image.open(image_input)
    ret = {}
    infos = image._getexif()

    if infos != None:
        for tag, value in infos.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        table = Table(title="MetaData")
        table.add_column("Key", justify="center", style="magenta")
        table.add_column("Value", justify="center", style="magenta")
        for key, value in ret.items():
            print(key, " - ", value)
            #table.add_column(key, justify="center", style="cyan")
            if key == "UserComment":
                value=value.replace("\x00".encode(), ''.encode())
            table.add_row(str(key),str(value))
        console = Console()
        console.print(table)




#        file = open("C:/Users/enzor/Cisco Packet Tracer 8.2.1/Image.txt","w")
#        file.write(str(ret))
#        file.close()
    else:
        print("L'image n'a pas de métadonnées :(")

IMGorPDF = input("Quel type de fichier voulez-vous analyser ? \n\t(1) - Image \n\t(2) - PDF\n")
if IMGorPDF == "1":
    MetaIMG()
elif IMGorPDF == "2":
    print("En cours de dev")
else:
    print("AAAAAAAAAAAAAAAAAAARGH !!!!")

