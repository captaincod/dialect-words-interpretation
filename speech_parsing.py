from pathlib import Path
from tqdm import tqdm

print(f"Введите номер корпуса\n1: Весёлые истории из жизни\n2: Рассказы сибиряков о жизни")
choice = int(input())
if choice == 1:
    stories_dir = Path("funny\\stories_fun")
    name = "fun"
elif choice == 2:
    stories_dir = Path("siberian\\stories_sib")
    name = "sib"

for path in tqdm(sorted(stories_dir.glob("*"))):
    file = open(path, encoding='utf-8')
    new_path = f"parsed_{name}\\parsed_{str(path)[len(str(stories_dir)) + 1:]}"
    new_f = open(new_path, 'w', encoding='utf-8')

    tag_signs = ['&lt;', '&gt;']
    inside_tag = False
    one_byte = ['-', '!', '.', ',', '?', ':']
    two_bytes = ['¡']

    end_quote = False

    word = ""
    text = ""

    for line in file:
        for i in range(len(line)):
            ch = line[i]
            byte_char = ch.encode('utf-8')

            if ch == " " or ch in one_byte:
                if word != "" and not inside_tag:
                    text += word + ch
                    if end_quote:
                        text += '\n'
                        end_quote = False
                    if ch in ['.', '!', '?']:
                        if line[i + 1] == "»":
                            end_quote = True
                        else:
                            text += '\n'
                word = ""

            elif ch == "-" and line[i + 1].isalpha():
                text += word + '-'
                word = ""

            elif ch == ';':
                if line[i - 3:i + 1] == tag_signs[0]:
                    inside_tag = True
                elif line[i - 3:i + 1] == tag_signs[1]:
                    inside_tag = False

            elif len(byte_char) == 2:
                if ch not in two_bytes:
                    word += ch

    file.close()
    new_f.write(text)
    new_f.close()
