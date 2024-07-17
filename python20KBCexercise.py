# WELCOME TO KON BANEGA CROREPATI

print("Welcome To KON BANEGA CROREPATI Game")
print(" you can quit any time by typing 'quit' ")

questions=["What is the capital of India ?",
           "what is the national animal of India ?",
           "what is the national bird of India ?",
           "What is the currency of Japan ?",
           "What does 'T' stand for in ATM ?",
           "______ is the founder of Facebook ?",
           "Jeff Bezos is the CEO of ?",
]

options=[
    ["a. Delhi","b. Mumbai","c. Bangluru","d. Goa"],
    ["a. Lion","b. Tiger","c. peacock","d. Bear"],
    ["a. Lion","b. Tiger","c. peacock","d. Bear"],
    ["a. Yen ","b. Won ","c. Baht","d. Yuan"],
    ["a. Teller","b. Trunk","c. Translational","d. Transfer"],
    ["a. Mark Zuckerberg","b. Brian Acton","c. Jimmy Wales","d. Larry Page"],
    ["a. Myntra ","b.Amazoan ","c.snapdeal ","d. Flipkart"]
]

correct_ans=["a","b","c","a","d","a","b"]

money=[1000,2000,3000,4000,5000,6000,10000]

i=0
totalmo=0
for i in range(len(questions[i])):
    question=questions[i]
    print(f"question {i+1}:{question}")
    option=options[i]
    print( f"{option[0]}     {option[1]}\n"
           f"{option[2]}     {option[3]}") 
              

    answer=input("Enter your answer:")

    if(answer=="quit"):
        break    

    if(answer==correct_ans[i]):
        print("Your Answer is correct")
        totalmo=money[i]
        print(f"You won rupees:{totalmo}")
    else:
        print("wrong answer..!!,Game Over..!!")
        break

print(f"you won rupees:{totalmo}") 
print("THANK YOU FOR PLAYING....!!")           

