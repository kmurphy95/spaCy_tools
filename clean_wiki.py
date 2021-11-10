

def remove_lang_tag(tag, file_name):

    with open(file_name, 'r', encoding='UTF-8') as f:
        text = f.read()
        text = text.replace(tag, "")
        f.close()
        return text


if __name__ == "__main__":
    outtext = remove_lang_tag('en:', "./panx_dataset/select/en.tar.gz.out/dev")
    with open("./panx_dataset/select/en.tar.gz.out/dev_notag", 'w', encoding='UTF-8') as w:
        w.write(outtext)
