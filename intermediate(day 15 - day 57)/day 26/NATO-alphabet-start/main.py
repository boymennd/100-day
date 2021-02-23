import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (Index, row) in data.iterrows()}
name = input("Enter a name:").upper()


def generate_phonetic():
    try:
        output_name = [data_dict[ch] for ch in name]
    except KeyError:
        print("Sorry,letter only in the alphabet please !")
    else:
        print(output_name)


generate_phonetic()