import wikipediaapi
import pickle
wiki_wiki = wikipediaapi.Wikipedia('vi')

def get_categorymembers(categorymembers, level=0, max_level=1):
    category_list = []
    for c in categorymembers.values():
        # print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        # print(c.title)
        category_list.append(c.title)
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            category_list += get_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)
        
    return category_list


with open('./data/CATEGORY_SET.pkl', 'rb') as file:
        CAT_SET = pickle.load(file)
def check_category(cat):
    if cat in CAT_SET:
        return True
    return False


def build_category_set():
    cat_keywords = ['Thể loại:Y học', 'Thể loại:Y tế', 'Thể loại:Sinh học', 'Thể loại:Hóa học']
    cat_list = [] + cat_keywords
    for keyword in cat_keywords:
        cat = wiki_wiki.page(keyword)
        cat_list += get_categorymembers(cat.categorymembers, max_level=2)

    cat_set = set(cat_list)

    with open('./data/CATEGORY_SET.pkl', 'wb') as file:
        pickle.dump(cat_set, file)


if __name__ == "__main__":
    build_category_set()