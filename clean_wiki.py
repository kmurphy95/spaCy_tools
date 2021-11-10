
ALL_TAGS = ['ar', 'ca', 'zh', 'da', 'nl', 'en', 'fr', 'de', 'el', 'it', 'ja', 'lt',
                               'mk', 'pl', 'pt', 'ro', 'ru', 'es']

EN_RU_AR_ZH = ['en:', 'ru:', 'zh:', 'ar:']
FILES = ['dev', 'test', 'train']

def remove_lang_tag(tags, file_name):

    with open(file_name, 'r', encoding='UTF-8') as f:
        text = f.read()
        for tag in tags:
            text = text.replace(tag+":", "")
        f.close()
        return text


if __name__ == "__main__":
    for file in FILES:
        for tag in ALL_TAGS:
            outtext = remove_lang_tag(ALL_TAGS, "C:\Programming\Spacy\wikiann\langs\\"+tag+".tar.gz.out\\"+file)
            with open("C:\Programming\Spacy\wikiann\langs\\"+tag+".tar.gz.out\\"+file+"_notag", 'w', encoding='UTF-8') as w:
                w.write(outtext)
