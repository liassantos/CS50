import re
#imput do usuário

def main():
    print(parse(input("HTML: ")))


#encontrar o link
def parse(html):
    if find_iframe := re.search(r'<iframe(.)*><\/iframe>', html):
        if find_video := re.search(
                r'(http|https):\/\/(www\.|)*youtube\.com\/embed\/(\w+)', find_iframe.group()
        ):
            return f"https://youtu.be/{find_video.group(3)}"
        else:
            return "None"

#transformar o link em URL curto
if __name__ == "__main__":
    main()