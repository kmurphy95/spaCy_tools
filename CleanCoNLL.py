

def remove_ent_tags():
    with open('CoNLL2003\\test.txt', 'r+') as f:

        text = f.read()
        text = text.replace("B-PER", "B-NE")
        text = text.replace("B-LOC", "B-NE")
        text = text.replace("B-ORG", "B-NE")
        text = text.replace("I-PER", "I-NE")
        text = text.replace("I-LOC", "I-NE")
        text = text.replace("I-ORG", "I-NE")
        text = text.replace("B-MISC", "B-NE")
        text = text.replace("I-MISC", "I-NE")

        f.close()

        return text


def remove_loc_misc():
    with open('CoNLL2003\\valid.txt', 'r+') as f:

        text = f.read()
        text = text.replace("B-PER", "B-NE")
        text = text.replace("B-LOC", "O")
        text = text.replace("B-ORG", "B-NE")
        text = text.replace("I-PER", "I-NE")
        text = text.replace("I-LOC", "O")
        text = text.replace("I-ORG", "I-NE")
        text = text.replace("B-MISC", "O")
        text = text.replace("I-MISC", "O")

        f.close()

        return text


if __name__ == "__main__":
    outtext = remove_loc_misc()
    with open("CoNLL2003\\valid_no_loc_misc.txt", 'w') as k:
        k.write(outtext)
