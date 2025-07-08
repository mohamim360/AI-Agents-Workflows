def generate_x_post(usr_input: str) -> str:
    #call AI /LLM
    pass

def main():
    # user input => AI (LLM) to generate X post => output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generate X post:")
    print(x_post)



if __name__ == "__main__":
    main()
