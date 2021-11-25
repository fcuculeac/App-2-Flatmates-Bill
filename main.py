from translate import Translator
from greets import greetings

translator = Translator(to_lang="ro")
for g in greetings:
    print(g.title(), "=", translator.translate(g).title())

