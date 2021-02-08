#!/usr/bin/env python
# coding: utf-8

# # Question 1
# What data type is each of the following?

# # Answer 1

# |Data               | Data Type                                                                              |                
# | :---              |-----------------:                                                                      |          
# | 5                 | Integer                                                                                | 
# | 5.0               | Float Point Type(Double, Float etc.)                                                   |  
# | 5 > 1             | Boolean                                                                                |  
# | '5'               | Character                                                                              |  
# | 5 * 2             | Integer                                                                                |  
# | '5' * 2           | Integer                                                                                |   
# | '5' + '2'         | Integer                                                                                |  
# | 5 / 2             | Float Point Type(Double, Float etc.)                                                   |  
# | 5 // 2            | Integer(Since C# will see 2 as commented.)                                             |  
# | [5, 2, 1]         | Integer                                                                                |   
# | 5 in [1, 4, 6]    | Boolean                                                                                |  
# | Pi                | Float Point Type(Double, Float etc.)                                                   |  
# 
# 
# 
# 
# 

# # Question 2
# Write (and evaluate) C# expressions that answer these questions:
# a. How many letters are there in 'Supercalifragilisticexpialidocious'?
# b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?
# c. Which of the following words is the longest:
# Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or
# Bababadalgharaghtakamminarronnkonn?
# d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian',
# 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# # Answer 2

# In[ ]:


using System;

namespace Question2
{
    class Program
    {
        static void Main(string[] args)
        {
            string GivenName = "Supercalifragilisticexpialidocious";
            int a = GivenName.Length;
            Console.WriteLine("a)Length of it {0} is {1}.\n", GivenName, GivenName.Length);
            string SubString = "ice";
            Console.WriteLine("b)"+GivenName.Contains(SubString)+"\n");
            string GivenName2 = "Honorificabilitudinitatibus";
            int b = GivenName2.Length;
            string GivenName3 = "Bababadalgharaghtakamminarronnkonn";
            int c = GivenName2.Length;
            Console.Write("c)");
            if (a > b)
            {
                if (a > c)
                {
                    Console.WriteLine(GivenName + "is the longest in these 3 words.");
                }
                else if (a == c)
                {
                    Console.WriteLine(GivenName + " and " + GivenName3 + " have same length and the longest in these 3 words.");
                }
                else
                {
                    Console.WriteLine(GivenName3 + " is the longest in these 3 words.");
                }
            }
            else if (a < b)
            {
                if (b > c)
                {
                    Console.WriteLine(GivenName2 + " is the longest in these 3 words.");
                }
                else if (b == c)
                {
                    Console.WriteLine(GivenName2 + " and " + GivenName3 + " have same length and the longest in these 3 words.");
                }
                else
                {
                    Console.WriteLine(GivenName3 + " is the longest in these 3 words.");
                }
            }
            else
            {
                if (a > c)
                {
                    Console.WriteLine(GivenName + " and " + GivenName2 + " are the longest in these 3 words.");
                }
                else if (a == c)
                {
                    Console.WriteLine("They all have same lengths.");
                }
                else
                {
                    Console.WriteLine(GivenName3 + "is the longest in these 3 words.");
                }
            }
            string[] names = { "Berlioz", "Borodin", "Brian", "Bartok", "Bellini", "Buxtehude", "Bernstein" };
            
            Array.Sort(names);

            Console.Write("\nd)" + names[0] + "comes first in dictionary and " + names[6] + " comes last in the dictionary.\n");


        }
    }
}


# # Answer 2 Output
# 
# <center><img src="Answer2.png"></center

# # Question 3
# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
# sides of a triangle and returns the area of the triangle. By Heron's formula, the area
# of a triangle with side lengths a, b, and c is
# s(s - a)(s -b)(s -c)
# , where
# s = (a+b+c)/2. 

# # Answer 3

# In[ ]:


using System;

namespace Question3

{
    class Program
{

    static void Main(string[] args)
    {
        Console.Write("Please write length of 1st side: ");
        double firstSide = Convert.ToDouble(Console.ReadLine());
        Console.Write("Please write length of 1st side: ");
        double secondSide = Convert.ToDouble(Console.ReadLine());
        Console.Write("Please write length of 1st side: ");
        double thirdSide = Convert.ToDouble(Console.ReadLine());
        triangleArea(firstSide, secondSide, thirdSide);

    }


    private static int triangleArea(double a, double b, double c)
    {
        double s = (a + b + c) / 2;
        double Area = Math.Sqrt((s * (s - a) * (s - b) * (s - c)));
        Console.WriteLine("{0} is the area of the given triangle ", Area);
        return 0;
    }

}
}


# # Answer 3 Output
# <center><img src="Answer3.png"></center

# # Question 4
# Write a program in C# Sharp to separate odd and even integers in separate arrays.

# # Answer 4

# In[ ]:


using System;
using System.Collections;

namespace Question4
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList oddArray = new ArrayList();
            ArrayList evenArray = new ArrayList();
            Console.Write("Input the number of elements to be stored in the array: ");
            int Size  = Convert.ToInt32(Console.ReadLine());
            int[] wholeArray = new int [Size] ;
            
            for (int i=0; i<Size; i++)
            {
                Console.Write("Input {0} element of the Array: ", i);
                wholeArray[i] = Convert.ToInt32(Console.ReadLine());
                if (wholeArray[i]%2==0)
                {
                    evenArray.Add(wholeArray[i]);
                    
                }
                else
                {
                    oddArray.Add(wholeArray[i]);
                    
                }

            }
            Console.Write("The Even elements are\n");

            for (int i = 0; i < evenArray.Count; i++)
            {
                Console.Write(evenArray[i] + " ");
            }

            Console.Write("\nThe Odd elements are\n" );

            for(int i=0; i<oddArray.Count;i++)
            {
                Console.Write(oddArray[i]+ " ");
            }
            
        }
    }
}


# # Answer 4 Output
# <center><img src="Answer4.png"></center

# # Question 5
# a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False
# depending on whether the point (x,y) lies in the rectangle with lower left
# corner (x1,y1) and upper right corner (x2,y2).
# 
# b. Use function inside() from part a. to write an expression that tests whether
# the point (1,1) lies in both of the following rectangles: one with lower left
# corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower
# left corner (0.5, 0.2) and upper right corner (1.1, 2). 

# # Answer 5 a)

# In[ ]:


using System;

namespace Question5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Please write the 'X' coordinate of the lower corner of the rectangle: ");
            double leftX= Convert.ToDouble(Console.ReadLine());
            Console.Write("Please write the 'Y' coordinate of the lower left corner of the rectangle: ");
            double leftY = Convert.ToDouble(Console.ReadLine());
            Console.Write("Please write the 'X' coordinate of the upper right corner of the rectangle: ");
            double rightX = Convert.ToDouble(Console.ReadLine());
            Console.Write("Please write the 'Y' coordinate of the upper right corner of the rectangle: ");
            double rightY = Convert.ToDouble(Console.ReadLine());
            Console.Write("Please write the 'X' coordinate of the point you want to test: ");
            double pointX = Convert.ToDouble(Console.ReadLine());
            Console.Write("Please write the 'Y' coordinate of the point you want to test: ");
            double pointY = Convert.ToDouble(Console.ReadLine());
            inside(pointX, pointY, leftX, leftY, rightX, rightY);


        }

        private static int inside (double x, double y, double x1,double y1, double x2, double y2)
        {
            if (x1<=x  &&   x<=x2 && y1<=y && y<=y2)
            {
                Console.Write("\nTrue, The point {0},{1} is inside the rectangle.\n", x,y);
                return 1;

            }
            else
            {
                Console.Write("\nFalse,The point {0},{1} is not inside the rectangle.\n", x, y);
                return 1;
            }



        }
    }
}


# # Answer 5 a) Outputs
# <center><img src="Answer5_Test1.png"></center
# <center><img src="Answer5_Test2.png"></center

# # Answer 5 b)

# In[ ]:


using System;

namespace Question5
{
    class Program
    {
        static void Main(string[] args)
        {

            inside(1, 1, 0.3, 0.5, 1.1, 0.7);
            //inside(1, 1, 0.5, 0.2, 1.1, 2);


        }

        private static int inside (double x, double y, double x1,double y1, double x2, double y2)
        {
            if (x1<=x  &&   x<=x2 && y1<=y && y<=y2)
            {
                Console.Write("\nTrue, The point {0},{1} is inside the rectangle.\n", x,y);
                return 1;

            }
            else
            {
                Console.Write("\nFalse,The point {0},{1} is not inside the rectangle.\n", x, y);
                return 1;
            }

        }
    }
}


# # Answer 5 b) Output 1
# 
# 
# <center><img src="Answer5b_Test1.png"></center
# 

# # Answer 5 b) Output 2
# 
# 
# <center><img src="Answer5b_Test2.png"></center

# # Question 6
# . You can turn a word into pig-Latin using the following two rules (simplified):
# • If the word starts with a consonant, move that letter to the end and append
# 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# • If the word starts with a vowel, simply append 'way' to the end of the word.
# For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For
# our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case
# characters. Your output should always be lower case however. 

# # Answer 6

# In[8]:


def pig(pigLatin):
    if (pigLatin[0]=='a' or pigLatin[0]=='e' or pigLatin[0]=='i' or pigLatin[0]=='o' or pigLatin[0]=='u'): #Determining the conditions
        pigLatin.append("way")
        print("".join(pigLatin))
    else:
        pigLatin.append(pigLatin[0])
        pigLatin.remove(pigLatin[0])
        pigLatin.append("ay")
        print("".join(pigLatin))  #.join is used to connect the letters so that output can be seen as a word.
word=input ("Please type a word to turn into pig-Latin: ")
lower_word=word.lower()  #lowering the letters.
wordlist=list(lower_word)  #Making list so it can be manipulated.

pig(wordlist)
word2=input ("Please type a word to turn into pig-Latin: ")
lower_word2=word2.lower()  #lowering the letters.
wordlist2=list(lower_word2)  #Making list so it can be manipulated.
pig(wordlist2)


# # Question 7
# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.
# Write a function bldcount() that reads the file with name name and reports (i.e.,
# prints) how many patients there are in each bloodtype.

# # Answer 7

# In[5]:


bloodFile = open("bloodtype1.txt", "r")    #Opening file
bloodTypes=bloodFile.read()                #Reading and saving data.
bloodAB=bloodTypes.count("AB")             #Counting the "AB" blood type
bloodA=bloodTypes.count("A")-bloodAB       #It was counting the A's insedi the AB so i eject them.
bloodB=bloodTypes.count("B")-bloodAB       #It was counting the B's insedi the AB so i eject them.
blood00=bloodTypes.count("OO")
blood0=bloodTypes.count("O")-blood00       #It was counting the O's insedi the OO so i eject them.
print("There are ", bloodA, " patients of blood type A")
print("There are ", bloodB, " patients of blood type B")
print("There are ", bloodAB, " patients of blood type AB")
print("There are ", blood0, " patients of blood type O")
print("There are ", blood00, " patients of blood type OO")
#I think the answer shared in the PS1 pdf is not true. Probably the text data is different.


# # Question 8
# Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or
# 'EUR' for the Euro)
# 2. an amount
# and then converts and returns the amount in US dollars.
# The currency rates you will need are stored in file currencies.txt.
# 

# # Answer 8

# In[5]:


currencyFile = open("currencies.txt", "r")     #Opening the file
currency=currencyFile.read()                   #Reading and saving the data
print(currency)                                #Printing so client can see them
def curconv(cur,amount):
    location=currency.index(cur)               #Defining the location of the currency and saving it into variable
    counter=0                                  
    for i in range (location+1+len(cur),len(currency)-(location+1)):     #Creating a for loop to find the range of the currency rate
        blank=currency[i]
        if (blank== "	"):                                              #Breaking the for loop when the array gets to blank again
            break;
        counter=counter+1                                                #Counting in order to find the location of the currency rate in array
    result=(float(currency[location+4:location+4+counter])*float (amount))   #Changing strings in to float so we can multiply them.
    print(result)

curType=input("Choose the currency: ")                                   #Asking client to choose the currency
moneyAmount=input("Define the amount you want to exchange: ")            #Asking client to define the amount
curconv(curType,moneyAmount)
curType2=input("Choose the currency: ")                                   #Asking client to choose the currency
moneyAmount2=input("Define the amount you want to exchange: ")            #Asking client to define the amountv
curconv(curType2,moneyAmount2)


# # Question 9
# Each of the following will cause an exception (an error). Identify what type of
# exception each will cause.
# 

# # Answer 9

# |Error Case                                                   | Error Type                                    |                
# | :---                                                        |-----------------:                             |          
# | Trying to add incompatible variables, as in adding 6 + ‘a’  | Type Error                                    |  
# | Referring to the 12th item of a list that has only 10 items | Index Error                                   | 
# | Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0) | Value Error    | 
# | Using an undeclared variable, such as print(x) when x has not been defined  | Name Error                    | 
# | Referring to the 12th item of a list that has only 10 items | Index Error                                   | 
# | Trying to open a file that does not exist                   | FileNotFound Error                            | 

# # Question 10
# Encryption is the process of hiding the meaning of a text by substituting letters in the
# message with other letters, according to some system. If the process is successful, no
# one but the intended recipient can understand the encrypted message. Cryptanalysis
# refers to attempts to undo the encryption, even if some details of the encryption are
# unknown (for example, if an encrypted message has been intercepted). The first step
# of cryptanalysis is often to build up a table of letter frequencies in the encrypted text.
# Assume that the string letters is already defined as
# 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies()
# that takes a string as its only parameter, and returns a list of integers, showing the
# number of times each character app

# # Answer 10

# In[3]:


stringLetters= "abcdefghijklmnopqrstuvwxyz"         #Defining the string letters
cryptedMessage=[]                                   #Defininge a empty array
def frequencies (message):
        for i in range(0,len(stringLetters)):       #Loop goes on the length of the string letters so that check every letter.
            cryptedMessage.append((message.count(stringLetters[i]))) #Appending the array that we defined.
        print(cryptedMessage)
    
inputMessage= input("Please input your message: ")
frequencies(inputMessage)
cryptedMessage=[]  
inputMessage2= input("Please input your message: ")
frequencies(inputMessage2)


# In[ ]:




