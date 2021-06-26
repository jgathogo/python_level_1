import os
import sys
import string


def main():
    # 1000 most common English words
    common_words = ["be", "and", "of", "a", "in", "to", "have", "too", "it", "I", "that", "for", "you", "he", "with",
                    "on", "do", "say", "this", "they", "at", "but", "we", "his", "from", "that", "not", "can’t",
                    "won’t", "by", "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her",
                    "all", "my", "make", "about", "know", "will", "as", "up", "one", "time", "there", "year", "so",
                    "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see",
                    "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two",
                    "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use",
                    "no", "man", "find", "here", "thing", "give", "many", "well", "only", "those", "tell", "one",
                    "very", "her", "even", "back", "any", "good", "woman", "through", "us", "life", "child", "there",
                    "work", "down", "may", "after", "should", "call", "world", "over", "school", "still", "try", "in",
                    "as", "last", "ask", "need", "too", "feel", "three", "when", "state", "never", "become", "between",
                    "high", "really", "something", "most", "another", "much", "family", "own", "out", "leave", "put",
                    "old", "while", "mean", "on", "keep", "student", "why", "let", "great", "same", "big", "group",
                    "begin", "seem", "country", "help", "talk", "where", "turn", "problem", "every", "start", "hand",
                    "might", "American", "show", "part", "about", "against", "place", "over", "such", "again", "few",
                    "case", "most", "week", "company", "where", "system", "each", "right", "program", "hear", "so",
                    "question", "during", "work", "play", "government", "run", "small", "number", "off", "always",
                    "move", "like", "night", "live", "Mr.", "point", "believe", "hold", "today", "bring", "happen",
                    "next", "without", "before", "large", "all", "million", "must", "home", "under", "water", "room",
                    "write", "mother", "area", "national", "money", "story", "young", "fact", "month", "different",
                    "lot", "right", "study", "book", "eye", "job", "word", "though", "business", "issue", "side",
                    "kind", "four", "head", "far", "black", "long", "both", "little", "house", "yes", "after", "since",
                    "long", "provide", "service", "around", "friend", "important", "father", "sit", "away", "until",
                    "power", "hour", "game", "often", "yet", "line", "political", "end", "among", "ever", "stand",
                    "bad", "lose", "however", "member", "pay", "law", "meet", "car", "city", "almost", "include",
                    "continue", "set", "later", "community", "much", "name", "five", "once", "white", "least",
                    "president", "learn", "real", "change", "team", "minute", "best", "several", "idea", "kid", "body",
                    "information", "nothing", "ago", "right", "lead", "social", "understand", "whether", "back",
                    "watch", "together", "follow", "around", "parent", "only", "stop", "face", "anything", "create",
                    "public", "already", "speak", "others", "read", "level", "allow", "add", "office", "spend", "door",
                    "health", "person", "art", "sure", "such", "war", "history", "party", "within", "grow", "result",
                    "open", "change", "morning", "walk", "reason", "low", "win", "research", "girl", "guy", "early",
                    "food", "before", "moment", "himself", "air", "teacher", "force", "offer", "enough", "both",
                    "education", "across", "although", "remember", "foot", "second", "boy", "maybe", "toward", "able",
                    "age", "off", "policy", "everything", "love", "process", "music", "including", "consider", "appear",
                    "actually", "buy", "probably", "human", "wait", "serve", "market", "die", "send", "expect", "home",
                    "sense", "build", "stay", "fall", "oh", "nation", "plan", "cut", "college", "interest", "death",
                    "course", "someone", "experience", "behind", "reach", "local", "kill", "six", "remain", "effect",
                    "use", "yeah", "suggest", "class", "control", "raise", "care", "perhaps", "little", "late", "hard",
                    "field", "else", "pass", "former", "sell", "major", "sometimes", "require", "along", "development",
                    "themselves", "report", "role", "better", "economic", "effort", "up", "decide", "rate", "strong",
                    "possible", "heart", "drug", "show", "leader", "light", "voice", "wife", "whole", "police", "mind",
                    "finally", "pull", "return", "free", "military", "price", "report", "less", "according", "decision",
                    "explain", "son", "hope", "even", "develop", "view", "relationship", "carry", "town", "road",
                    "drive", "arm", "true", "federal", "break", "better", "difference", "thank", "receive", "value",
                    "international", "building", "action", "full", "model", "join", "season", "society", "because",
                    "tax", "director", "early", "position", "player", "agree", "especially", "record", "pick", "wear",
                    "paper", "special", "space", "ground", "form", "support", "event", "official", "whose", "matter",
                    "everyone", "center", "couple", "site", "end", "project", "hit", "base", "activity", "star",
                    "table", "need", "court", "produce", "eat", "American", "teach", "oil", "half", "situation", "easy",
                    "cost", "industry", "figure", "face", "street", "image", "itself", "phone", "either", "data",
                    "cover", "quite", "picture", "clear", "practice", "piece", "land", "recent", "describe", "product",
                    "doctor", "wall", "patient", "worker", "news", "test", "movie", "certain", "north", "love",
                    "personal", "open", "support", "simply", "third", "technology", "catch", "step", "baby", "computer",
                    "type", "attention", "draw", "film", "Republican", "tree", "source", "red", "nearly",
                    "organization", "choose", "cause", "hair", "look", "point", "century", "evidence", "window",
                    "difficult", "listen", "soon", "culture", "billion", "chance", "brother", "energy", "period",
                    "course", "summer", "less", "realize", "hundred", "available", "plant", "likely", "opportunity",
                    "term", "short", "letter", "condition", "choice", "place", "single", "rule", "daughter",
                    "administration", "south", "husband", "Congress", "floor", "campaign", "material", "population",
                    "well", "call", "economy", "medical", "hospital", "church", "close", "thousand", "risk", "current",
                    "fire", "future", "wrong", "involve", "defense", "anyone", "increase", "security", "bank", "myself",
                    "certainly", "west", "sport", "board", "seek", "per", "subject", "officer", "private", "rest",
                    "behavior", "deal", "performance", "fight", "throw", "top", "quickly", "past", "goal", "second",
                    "bed", "order", "author", "fill", "represent", "focus", "foreign", "drop", "plan", "blood", "upon",
                    "agency", "push", "nature", "color", "no", "recently", "store", "reduce", "sound", "note", "fine",
                    "before", "near", "movement", "page", "enter", "share", "than", "common", "poor", "other",
                    "natural", "race", "concern", "series", "significant", "similar", "hot", "language", "each",
                    "usually", "response", "dead", "rise", "animal", "factor", "decade", "article", "shoot", "east",
                    "save", "seven", "artist", "away", "scene", "stock", "career", "despite", "central", "eight",
                    "thus", "treatment", "beyond", "happy", "exactly", "protect", "approach", "lie", "size", "dog",
                    "fund", "serious", "occur", "media", "ready", "sign", "thought", "list", "individual", "simple",
                    "quality", "pressure", "accept", "answer", "hard", "resource", "identify", "left", "meeting",
                    "determine", "prepare", "disease", "whatever", "success", "argue", "cup", "particularly", "amount",
                    "ability", "staff", "recognize", "indicate", "character", "growth", "loss", "degree", "wonder",
                    "attack", "herself", "region", "television", "box", "TV", "training", "pretty", "trade", "deal",
                    "election", "everybody", "physical", "lay", "general", "feeling", "standard", "bill", "message",
                    "fail", "outside", "arrive", "analysis", "benefit", "name", "sex", "forward", "lawyer", "present",
                    "section", "environmental", "glass", "answer", "skill", "sister", "PM", "professor", "operation",
                    "financial", "crime", "stage", "ok", "compare", "authority", "miss", "design", "sort", "one", "act",
                    "ten", "knowledge", "gun", "station", "blue", "state", "strategy", "little", "clearly", "discuss",
                    "indeed", "force", "truth", "song", "example", "democratic", "check", "environment", "leg", "dark",
                    "public", "various", "rather", "laugh", "guess", "executive", "set", "study", "prove", "hang",
                    "entire", "rock", "design", "enough", "forget", "since", "claim", "note", "remove", "manager",
                    "help", "close", "sound", "enjoy", "network", "legal", "religious", "cold", "form", "final", "main",
                    "science", "green", "memory", "card", "above", "seat", "cell", "establish", "nice", "trial",
                    "expert", "that", "spring", "firm", "Democrat", "radio", "visit", "management", "care", "avoid",
                    "imagine", "tonight", "huge", "ball", "no", "close", "finish", "yourself", "talk", "theory",
                    "impact", "respond", "statement", "maintain", "charge", "popular", "traditional", "onto", "reveal",
                    "direction", "weapon", "employee", "cultural", "contain", "peace", "head", "control", "base",
                    "pain", "apply", "play", "measure", "wide", "shake", "fly", "interview", "manage", "chair", "fish",
                    "particular", "camera", "structure", "politics", "perform", "bit", "weight", "suddenly", "discover",
                    "candidate", "top", "production", "treat", "trip", "evening", "affect", "inside", "conference",
                    "unit", "best", "style", "adult", "worry", "range", "mention", "rather", "far", "deep", "front",
                    "edge", "individual", "specific", "writer", "trouble", "necessary", "throughout", "challenge",
                    "fear", "shoulder", "institution", "middle", "sea", "dream", "bar", "beautiful", "property",
                    "instead", "improve", "stuff", "claim"]

    # text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of " \
    #        "foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it " \
    #        "was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything " \
    #        "before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the " \
    #        "other way—in short, the period was so far like the present period, that some of its noisiest authorities " \
    #        "insisted on its being received, for good or for evil, in the superlative degree of comparison only. " \
    #        "There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a " \
    #        "king with a large jaw and a queen with a fair face, on the throne of France. In both countries it was " \
    #        "clearer than crystal to the lords of the State preserves of loaves and fishes, that things in general " \
    #        "were settled for ever. It was the year of Our Lord one thousand seven hundred and seventy-five. Spiritual " \
    #        "revelations were conceded to England at that favoured period, as at this. Mrs. Southcott had recently " \
    #        "attained her five-and-twentieth blessed birthday, of whom a prophetic private in the Life Guards had " \
    #        "heralded the sublime appearance by announcing that arrangements were made for the swallowing up of London " \
    #        "and Westminster. Even the Cock-lane ghost had been laid only a round dozen of years, after rapping out " \
    #        "its messages, as the spirits of this very year last past (supernaturally deficient in originality) rapped " \
    #        "out theirs. Mere messages in the earthly order of events had lately come to the English Crown and People, " \
    #        "from a congress of British subjects in America: which, strange to relate, have proved more important to " \
    #        "the human race than any communications yet received through any of the chickens of the Cock-lane brood. " \
    #        "France, less favoured on the whole as to matters spiritual than her sister of the shield and trident, " \
    #        "rolled with exceeding smoothness down hill, making paper money and spending it. Under the guidance of her " \
    #        "Christian pastors, she entertained herself, besides, with such humane achievements as sentencing a youth " \
    #        "to have his hands cut off, his tongue torn out with pincers, and his body burned alive, because he had not " \
    #        "kneeled down in the rain to do honour to a dirty procession of monks which passed within his view, at a " \
    #        "distance of some fifty or sixty yards. It is likely enough that, rooted in the woods of France and Norway, " \
    #        "there were growing trees, when that sufferer was put to death, already marked by the Woodman, Fate, to " \
    #        "come down and be sawn into boards, to make a certain movable framework with a sack and a knife in it, " \
    #        "terrible in history. It is likely enough that in the rough outhouses of some tillers of the heavy lands " \
    #        "adjacent to Paris, there were sheltered from the weather that very day, rude carts, bespattered with " \
    #        "rustic mire, snuffed about by pigs, and roosted in by poultry, which the Farmer, Death, had already " \
    #        "set apart to be his tumbrils of the Revolution. But that Woodman and that Farmer, though they work " \
    #        "unceasingly, work silently, and no one heard them as they went about with muffled tread: the rather, " \
    #        "forasmuch as to entertain any suspicion that they were awake, was to be atheistical and traitorous. " \
    #        "In England, there was scarcely an amount of order and protection to justify much national boasting. " \
    #        "Daring burglaries by armed men, and highway robberies, took place in the capital itself every night; " \
    #        "families were publicly cautioned not to go out of town without removing their furniture to upholsterers’ " \
    #        "warehouses for security; the highwayman in the dark was a City tradesman in the light, and, being " \
    #        "recognised and challenged by his fellow-tradesman whom he stopped in his character of “the Captain,” " \
    #        "gallantly shot him through the head and rode away; the mail was waylaid by seven robbers, and the " \
    #        "guard shot three dead, and then got shot dead himself by the other four, “in consequence of the failure " \
    #        "of his ammunition:” after which the mail was robbed in peace; that magnificent potentate, the Lord Mayor " \
    #        "of London, was made to stand and deliver on Turnham Green, by one highwayman, who despoiled the " \
    #        "illustrious creature in sight of all his retinue; prisoners in London gaols fought battles with their " \
    #        "turnkeys, and the majesty of the law fired blunderbusses in among them, loaded with rounds of shot and " \
    #        "ball; thieves snipped off diamond crosses from the necks of noble lords at Court drawing-rooms; " \
    #        "went into St. Giles’s, to search for contraband goods, and the mob fired on the musketeers, and the " \
    #        "musketeers fired on the mob, and nobody thought any of these occurrences much out of the common way. " \
    #        "In the midst of them, the hangman, ever busy and ever worse than useless, was in constant requisition; " \
    #        "now, stringing up long rows of miscellaneous criminals; now, hanging a housebreaker on Saturday who " \
    #        "had been taken on Tuesday; now, burning people in the hand at Newgate by the dozen, and now burning " \
    #        "pamphlets at the door of Westminster Hall; to-day, taking the life of an atrocious murderer, and " \
    #        "to-morrow of a wretched pilferer who had robbed a farmer’s boy of sixpence. All these things, and a " \
    #        "thousand like them, came to pass in and close upon the dear old year one thousand seven hundred and " \
    #        "seventy-five. Environed by them, while the Woodman and the Farmer worked unheeded, those two of the " \
    #        "jaws, and those other two of the plain and the fair faces, trod with stir enough, and carried their " \
    #        "divine rights with a high hand. Thus did the year one thousand seven hundred and seventy-five conduct " \
    #        "their Greatnesses, and myriads of small creatures—the creatures of this chronicle among the rest—along " \
    #        "the roads that lay before them."

    text = input("Paste a paragraph of text copied from any website: ")
    # clean text
    text_lower = text.lower()
    punctuation = string.punctuation + '—'

    for char in punctuation:
        text_lower = text_lower.replace(char, '')

    text_l = text_lower.split(" ")

    # find out if word is non-common
    # non_common = []
    # for word in text_l:
    #     if word not in common_words:
    #         if word not in non_common:
    #             non_common.append(word)

    # print(non_common)  # print words not in common_words

    freq_d = {}
    non_common = []

    for word in text_l:
        if word in common_words:
            if word in freq_d:
                freq_d[word] += 1
            else:
                freq_d[word] = 1
        else:
            non_common.append(word)

    print(f"List of non-common words:\n"
          f"{set(non_common)}\n")

    print("Relative frequency of common words, in descending order: ")
    sorted_keys = sorted(freq_d, key=freq_d.get, reverse=True)
    for word in sorted_keys:
        number = freq_d[word]
        freq = str(round(number / len(text_l) * 100, ndigits=2)) + '%'
        print(word, freq, sep=' - ')

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
