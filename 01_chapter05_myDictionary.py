# This is the solution of sample program no.- 1 (see: no.1 in practice list)
'''This program is the application of chapter no.- 5.
It's under the basic python lessions.'''
myDictionary = {
    "authority" : "a person or organization having political or administrative power and control.",
    "bestie" : "best friend",
    "creativity" : "the use of imagination or original ideas to create something.",
    "database" : "a systematic collection of data.",
    "executing" : "carry out an instruction or program set by user.",
    "feedback" : "the transmission of evaluative or corrective information about an action, event or process to the original or controlling source.",
    "google" : "a search engine by using which, we can search for any information on internet.",
    "horse" : "a type of animal.",
    "hindustan" : "a country which is also known as 'INDIA'.",
    "infrastructure" : "the basic physical and organizational structures and facilities.",
    "jango" : "a high-level Python web framework which is actually known as 'Django'.",
    "kite" : "a lighter-than-air craft with wing surfaces that react against the air to create lift and drag forces.",
    "latch" : "a circuit which retains whatever output state results from a momentary input signal until reset by another signal.",
    "mango" : "a seasonal fruit which tastes sweet.",
    "new" : "an operator which is used to create an instance of the class in java.",
    "operator" : "a symbol or characters that determine what action is to be performed or considered.",
    "path" : "a way or track",
    "queue" : "a line or sequence of the data items or commands.",
    "revoke" : "a command in programming which is used to remove user access rights or privileges to the database objects.",
    "sunny" : "a cheerful, brilliant person just like the sunlight.",
    "toggle" : "a key or command that is operated the same way but with opposite effect on successive occasions.",
    "uninterrupted" : "without a break in continuity.",
    "variables" : "any entity that can take on different values.", 
    "wi-fi" : "the wireless technology used to connect computers, laptops, smartphones and other electronics devices to the internet.",
    "xerox" : "a technolgy which is used for making a paper copy or copies from original documents.",
    "yesterday" : "the day before today.",
    "zoo" : "an establishment which maintains a collection of wild animals, typically in a park or gardens for study, conservation or display to the public."
}
print("The words in this dictionary are : ",myDictionary.keys())             # It's a method of dictionary named '.keys' which returns a list containing all keys of the dictionary. 
word = input("Enter the word which you want to choose to know the meaning : ")
print("The meaning of this word is : ",myDictionary[word])                   # It's used to print the value of the selected word.
print("The meaning of this word is : ",myDictionary.get(word))               # It performs the same task as above.
            # In the above line, '.get' is a method which returns 'None' when the selected key isn't present in the dictionary but doesn't show an error.