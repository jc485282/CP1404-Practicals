import wikipedia

search_phrase = str(input("please enter a search phase: "))
while search_phrase != "":
    for entry in wikipedia.search(search_phrase):
        page = wikipedia.page(entry)
        print("Title: {}".format(page))

        print("URL: {}".format(page.url))
        try:
            print(wikipedia.summary(page))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        print()
    search_phrase = str(input("please enter a search phase: "))

print("done")
