
from fontTools.ttLib import TTFont

# Open the WOFF font file
with open("NotoSansDevanagari[wdth,wght].woff", "rb") as woff_file:
    font = TTFont(woff_file)

    # Set the font flavor to None to allow saving as TTF
    font.flavor = None

    # Save the font as a TTF file
    font.save("NotoSansDevanagari.ttf")
