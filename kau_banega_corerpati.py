#kaun banega corerpati

question=["Question 1.Whaht is the capital city of Fgrance?",
          "Question 2.What is the largest ocean in the world?",
          "Question 3.What is the tallest mountain in the world?",
          "Question 4.Which country gifted the \'Statue Of liberty\' to USA in 1886?",
          "Question 5.In which ocean \'Bermuda Triangle\' is located?",
          "Question 6.Which is the smallest ocean in the world?",
          "Question 7.Which continent has the highest number of country?",
          "Question 8.On what prinpicple does digital computer works on?",
          "Question 9.The highest total runs scored in an ODI cricket match is?",
          "Question 10.Which country has won the cricket world cup the max number of times?"]
choice=["A.Rome\nB.Lodon\nC.paris\nD.BErlin",
        "A.Pacific\nB.Atlantic\nC.Indian\nD.Artic",
        "A.Everest\nB.K2\nC.Kanchenjunga\nD.Lhotse",
        "A.France\nB.Canada\nC.Brazil\nD.England",
        "A.Atlantic\nB.Indian\nC.Pacific\nD.Artic",
        "A.Atlantic\nB.Indian\nC.Pacific\nD.Artic",
        "A.Asia\nB.Europe\nC.N.America\nD.Africa",
        "A.Count\nB.Measurment\nC.Eletric\nD.Logic",
        "A.438\nB.443\nC.448\nD.400",
        "A.West Indies\nB.India\nC.Austrialia\nD.England"
        ]
Answer=["C","A","A","A","A","D","D","A","B","C"]

Ranswer=["C.paris",
         "A.Pacific",
         "A.Everest",
         "A.France",
         "A.Atlantic",
         "D.Artic",
         "D.Africa",
         "A.Count",
         "B.443",
         "C.Austrialia"
         ]
print("Welcome to Kaun Banega Corerpati")
Money=0
for i in range(len(question)):
   
   print(question[i])
   print(choice[i])
   a=input("Enter your option: ")
   b=a.upper()
   
   #checking the answer
   if(b==Answer[i]):
      
       print("Congratulation! Answer is correct. You have won ",1000000)
       Money=Money+1000000
   else:
       print("Sorry but the correct answer is ",Ranswer[i])
  
if(Money==10000000):
     
    
     print("\n\n\narey wah wah wah!!! Ap bangaye hai corerpati. ")
else:
    print("You have won :", Money)