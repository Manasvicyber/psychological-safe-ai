forbidden_words = {"hate", "harm", "sad", "embarrassed"}

def check_sentence():
        user_input = input("Enter your sentence: ")
    
   
    words = user_input.lower().split()
    
       if set(words).intersection(forbidden_words):
        print("You are overboarding the conversation.")
    else:
        pass
if __name__ == "__main__":
    check_sentence()
       
