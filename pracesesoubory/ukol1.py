with open(f"pracesesoubory/input/general_letter.txt") as letter:
    letter_content = letter.read()

with open (f"pracesesoubory/input/names.txt", mode="r") as gfile:
    file =gfile.readlines()

    for jmeno in file:
        jmeno =jmeno.strip()
        letter_text = letter_content.replace("[name]", jmeno)
        with open (f"pracesesoubory/output/{jmeno}.txt", mode="w") as yfile:
            yfile.write(letter_text)