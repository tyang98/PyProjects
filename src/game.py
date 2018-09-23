import random, hangman

# from 100 Words to Make You Sound Great by Editors of the American Heritage Dictionaries
# https://www.hmhco.com/shop/books/100-Words-to-Make-You-Sound-Great/9780618883103
word_list = ["adamant", "affectation", "affinity", "allay", "amelioration", "amenable", "amoral", "assuage", "bauble", "beguile", "beset", "bulwark", "busybody", "complacent", "concomitant", "consign", "contend", "cosmopolitan", "culpable", "depravity", "derelict", "dissimulate", "dissipate", "distill", "dogmatic", "elicit", "epithet", "espouse", "expediency", "forestall", "furtive", "galling", "gloat", "gratuitous", "hallmark", "happenstance", "ignominious", "imperturbable", "ingratiate", "innocuous", "intemperate", "interpolate", "inure", "jingoism", "juggernaut", "ken ", "latent", "legacy", "ludicrous", "mandate", "maven", "mawkish", "modus operandi", "nefarious", "nicety", "nonchalance", "obdurate", "orthodoxy", "palliate", "patina", "penury", "pernicious", "perpetuate", "pittance", "pompous", "precipitate", "prescience", "profusion", "propensity", "pugnacity", "pusillanimous", "quip", "rankle", "reconciliation", "resiliency", "respite", "riposte", "sacrosanct", "scapegoat", "spurious", "squander", "supersede", "surreptitious", "tenacity", "tenuous", "travail", "truculence", "turpitude", "tyro", "unbridled", "uncanny", "urbane", "velleity", "venial", "verbose", "vexation", "vista", "wanton", "wheedle", "yammer"]

N_GUESSES = 10
secret = hangman.SecretWord(random.choice(word_list))
    
for n in list(range(N_GUESSES)):
    secret.word_so_far()
    user_guess = input("Guess a letter: ")
    secret.apply_guess(user_guess)
    if secret.is_solved():
        print("YOU WIN!!!")
        break

secret.reveal()