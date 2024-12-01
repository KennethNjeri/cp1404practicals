import wikipedia

page_title = input("Enter page title: ")
while page_title != "":
    try:
        wiki_page = wikipedia.search(page_title)
        wiki_summary = wikipedia.summary(page_title)
        print(wiki_page)
        print(wiki_summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following options:")
        print(e.options)
    page_title = input("Enter page title: ")

print("Thankyou")