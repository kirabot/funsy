from random import randint

words = ["je u redu", "je odlicno", "vazi", "je ok", "je sjajno", "moze", "je tako", 
		 "je lepo", "dosta", "je do jaja", "je chill", "nema problema", "je dobro"]

je_words = ["u redu", "odlicno", "kul", "sjajno", "vazi", "ok", "je tako", 
 			"vrhunski", "vrhunska diskusija", "mnogo lepo", "do jaja", 
 			"chill", "nema problema", "fino", "cu da se ubijem"]

def ako_je_tako():
	
	return "Ako " + words[randint(0, len(words))] + " onda " + je_words[randint(0, len(je_words))] + "."


print (ako_je_tako())
