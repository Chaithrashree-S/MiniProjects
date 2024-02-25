def madlibs():
    # Input prompts for various parts of speech
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    # Madlibs template
    madlibs_story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    # Print the completed Madlibs story
    print(madlibs_story)

# Call the function to run the Madlibs game
madlibs()
