from textblob import TextBlob

class SpellCheckerModule:
    def __init__(self):
        pass  # No grammar tool needed now

    def correct_spell(self, text):
        # Correct the spelling of the entire text
        corrected_text = str(TextBlob(text).correct())
        return corrected_text

# Optional: test the spell checker directly
if __name__ == "__main__":
    spell_checker = SpellCheckerModule()
    text = "Helllo, welcom to my progrm"
    corrected = spell_checker.correct_spell(text)
    print("Corrected Text:", corrected)
