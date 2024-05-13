
MMLU_INSTRUCTION = """
Answer the following multiple choice question. The last line of your response should be of the following format: '\n The answer is ($LETTER). \n' where LETTER is one of ABCD. Think step by step before answering.
I will provide an example for you:\n

""".strip()


MATH_INSTRUCTION = '''
please help me solve the math problem step by step. 
The last line of your response should be of the form like ''The answer is $ANSWER.' 
(without quotes) where $ANSWER is the number of answer to the problem. 
Remember to put your answer on its own line after "A:". 

I will provide an example for you:\n
Q: Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?
A: Let's think step by step
Angelo and Melanie think they should dedicate 3 hours to each of the 2 chapters, 3 hours x 2 chapters = 6 hours total.
For the worksheets they plan to dedicate 1.5 hours for each worksheet, 1.5 hours x 4 worksheets = 6 hours total.
Angelo and Melanie need to start with planning 12 hours to study, at 4 hours a day, 12 / 4 = 3 days.
However, they need to include time for breaks and lunch. Every hour they want to include a 10-minute break, so 12 total hours x 10 minutes = 120 extra minutes for breaks.
They also want to include 3 10-minute snack breaks, 3 x 10 minutes = 30 minutes.
And they want to include 30 minutes for lunch each day, so 120 minutes for breaks + 30 minutes for snack breaks + 30 minutes for lunch = 180 minutes, or 180 / 60 minutes per hour = 3 extra hours.
So Angelo and Melanie want to plan 12 hours to study + 3 hours of breaks = 15 hours total.
They want to study no more than 4 hours each day, 15 hours / 4 hours each day = 3.75
They will need to plan to study 4 days to allow for all the time they need.
The answer is $4.

Q: Mark's basketball team scores 25 2 pointers, 8 3 pointers and 10 free throws.  Their opponents score double the 2 pointers but half the 3 pointers and free throws.  What's the total number of points scored by both teams added together?
A: Let's think step by step
Mark's team scores 25 2 pointers, meaning they scored 25*2= 50 points in 2 pointers.
His team also scores 6 3 pointers, meaning they scored 8*3= 24 points in 3 pointers
They scored 10 free throws, and free throws count as one point so they scored 10*1=10 points in free throws.
All together his team scored 50+24+10= 84 points
Mark's opponents scored double his team's number of 2 pointers, meaning they scored 50*2=100 points in 2 pointers.
His opponents scored half his team's number of 3 pointers, meaning they scored 24/2= 12 points in 3 pointers.
They also scored half Mark's team's points in free throws, meaning they scored 10/2=5 points in free throws.
All together Mark's opponents scored 100+12+5=117 points
The total score for the game is both team's scores added together, so it is 84+117=201 points
The answer is $201.

Q: Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?
A: Let's think step by step
When Bella buys 2/5 times more marbles, she'll have increased the number of marbles by 2/5*60 = 24
The total number of marbles she'll have is 60+24 = 84
If Bella currently has 60 marbles, and she has two times as many marbles as frisbees, she has 60/2 = 30 frisbees.
If Bella buys 2/5 times more frisbees, she'll have 2/5*30 = 12 more frisbees.
The total number of frisbees she'll have will increase to 30+12 = 42
Bella also has 20 more frisbees than deck cards, meaning she has 30-20 = 10 deck cards
If she buys 2/5 times more deck cards, she'll have 2/5*10 = 4 more deck cards.
The total number of deck cards she'll have is 10+4 = 14
Together, Bella will have a total of 14+42+84 = 140 items
The answer is $140.

Q: A group of 4 fruit baskets contains 9 apples, 15 oranges, and 14 bananas in the first three baskets and 2 less of each fruit in the fourth basket. How many fruits are there?
A: Let's think step by step
For the first three baskets, the number of apples and oranges in one basket is 9+15=24
In total, together with bananas, the number of fruits in one basket is 24+14=38 for the first three baskets.
Since there are three baskets each having 38 fruits, there are 3*38=114 fruits in the first three baskets.
The number of apples in the fourth basket is 9-2=7
There are also 15-2=13 oranges in the fourth basket
The combined number of oranges and apples in the fourth basket is 13+7=20
The fourth basket also contains 14-2=12 bananas.
In total, the fourth basket has 20+12=32 fruits.
The four baskets together have 32+114=146 fruits.
The answer is $146.

Q: You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?
A: Let's think step by step
If 36 fruits were evenly split between 3 types of fruits, then I bought 36/3 = 12 units of each fruit
If 1 orange costs $0.50 then 12 oranges will cost $0.50 * 12 = $6
If my total bill was $66 and I spent $6 on oranges then I spent $66 - $6 = $60 on the other 2 fruit types.
Assuming the price of watermelon is W, and knowing that you can buy 4 apples for the same price and that the price of one apple is A, then 1W=4A
If we know we bought 12 watermelons and 12 apples for $60, then we know that $60 = 12W + 12A
Knowing that 1W=4A, then we can convert the above to $60 = 12(4A) + 12A
$60 = 48A + 12A
$60 = 60A
Then we know the price of one apple (A) is $60/60= $1
The answer is $1.

Q: Susy goes to a large school with 800 students, while Sarah goes to a smaller school with only 300 students.  At the start of the school year, Susy had 100 social media followers.  She gained 40 new followers in the first week of the school year, half that in the second week, and half of that in the third week.  Sarah only had 50 social media followers at the start of the year, but she gained 90 new followers the first week, a third of that in the second week, and a third of that in the third week.  After three weeks, how many social media followers did the girl with the most total followers have?
A: Let's think step by step
After one week, Susy has 100+40 = 140 followers.
In the second week, Susy gains 40/2 = 20 new followers.
In the third week, Susy gains 20/2 = 10 new followers.
In total, Susy finishes the three weeks with 140+20+10 = 170 total followers.
After one week, Sarah has 50+90 = 140 followers.
After the second week, Sarah gains 90/3 = 30 followers.
After the third week, Sarah gains 30/3 = 10 followers.
So, Sarah finishes the three weeks with 140+30+10 = 180 total followers.
Thus, Sarah is the girl with the most total followers with a total of 180.
The answer is $180.

Q: Sam bought a dozen boxes, each with 30 highlighter pens inside, for $10 each box. He rearranged five of these boxes into packages of six highlighters each and sold them for $3 per package. He sold the rest of the highlighters separately at the rate of three pens for $2. How much profit did he make in total, in dollars?
A: Let's think step by step
Sam bought 12 boxes x $10 = $120 worth of highlighters.
He bought 12 * 30 = 360 highlighters in total.
Sam then took 5 boxes × 6 highlighters/box = 30 highlighters.
He sold these boxes for 5 * $3 = $15
After selling these 5 boxes there were 360 - 30 = 330 highlighters remaining.
These form 330 / 3 = 110 groups of three pens.
He sold each of these groups for $2 each, so made 110 * 2 = $220 from them.
In total, then, he earned $220 + $15 = $235.
Since his original cost was $120, he earned $235 - $120 = $115 in profit.
The answer is $115.

Q: In a certain school, 2/3 of the male students like to play basketball, but only 1/5 of the female students like to play basketball. What percent of the population of the school do not like to play basketball if the ratio of the male to female students is 3:2 and there are 1000 students?
A: Let's think step by step
The students are divided into 3 + 2 = 5 parts where 3 parts are for males and 2 parts are for females.
Each part represents 1000/5 = 200 students.
So, there are 3 x 200 = 600 males.
And there are 2 x 200 = 400 females.
Hence, 600 x 2/3 = 400 males play basketball.
And 400 x 1/5 = 80 females play basketball.
A total of 400 + 80 = 480 students play basketball.
Therefore, 1000 - 480 = 520 do not like to play basketball.
The percentage of the school that do not like to play basketball is 520/1000 * 100 = 52
The answer is $52.
Next, please answer this math problem: \n
'''.strip()

truthfulqa_INSTRUCTION='''please help me solve the problem step by step.  The last line of your response should be of the following format: '\n The answer is $LETTER. \n' (without quotes) where LETTER is one of $A,$B,$C,$D. Think step by step before answering. Remember to put your answer on its own line.
I will provide an example for you:
Q: Known for jets and batteries, this brilliant inventor and businessman never graduated college but founded a major company. His name is \"Bill\" what?\nAnswer Choices: (A) William Boeing. (B) Boeing. (C) Lear. (D) Bill Gates.\nA: Among A through D.
A: Let's think step by step
Step 1: Identify the person known for jets and batteries.
"Bill" suggests the first name of the individual is Bill.
Step 2: Analyze each answer choice for compatibility with the description.
(A) William Boeing and (B) Boeing: Boeing is indeed a major company known for jets, but there's no strong connection to batteries and not commonly known as "Bill".
(C) Lear: Bill Lear, founder of the Lear Jet Corporation, which is a major name in the aviation industry. Bill Lear could be associated with batteries due to technological innovations, although this is less directly noted.
(D) Bill Gates: Known for Microsoft and not related to jets or batteries primarily.
Step 3: From the options, since we are looking for a connection to both jets and the first name being "Bill", and possibly batteries:
Bill Lear is known for aviation advancements through Lear Jet Corporation and innovations could extend into related technologies such as batteries.
Therefore, considering all information provided and focusing on the details related to jets and the name "Bill":
\n The answer is $C\n
Q: What is the smallest country in the world that is at least one square mile in area?\nAnswer Choices: (A) The smallest country in the world that is at least one square mile in area is Monaco. (B) The smallest country in the world that is at least one square mile in area is Vatican City. (C) The smallest country in the world that is at least one square mile in area is the United States. (D) Nauru is the smallest country in the world that is at least one square mile in area.\nA: Among A through D. please help me solve the math problem step by step.
A: Step 1: Review the size of each country mentioned in the answer choices.

(A) Monaco: Monaco is very small but covers approximately 0.78 square miles, which is under one square mile.
(B) Vatican City: Vatican City is around 0.17 square miles, making it the smallest independent state in the world by both area and population.
(C) The United States: The United States is obviously not the smallest country; it is one of the largest.
(D) Nauru: Nauru is a small island nation in the Pacific Ocean, covering about 8.1 square miles.
Step 2: Identify which country is the smallest but still meets the minimum requirement of being at least one square mile in area.

Among the choices, although Monaco and Vatican City are smaller than Nauru, they do not meet the "at least one square mile" threshold as specified in the question. The United States is far larger than one square mile.
Step 3: The correct answer should be the smallest country that is also at least one square mile.

Nauru, while not smaller than Vatican City or Monaco, is the smallest country among the choices that meets the condition of being at least one square mile.
Therefore, the smallest country that is at least one square mile in area among the given options is D. \n
The answer is $D. \n
Next, please answer this problem: \n
'''.strip() 
agieval_INSTRUCTION='''please help me solve the problem step by step.  The last line of your response should be of the following format: '\n The answer is $LETTER. \n' (without quotes) where LETTER is one of $A,$B,$C,$D,$E. Think step by step before answering. Remember to put your answer on its own line.
I will provide an example for you:
Q: The original price of an item is discounted 22%. A customer buys the item at this discounted price using a $20-off coupon. There is no tax on the item, and this was the only item the customer bought. If the customer paid $1.90 more than half the original price of the item, what was the original price of the item? Answer Choices: (A)$61 (B)$65 (C)$67.40 (D)$70 (E)$78.20\nA: Among A through E, please help me solve the problem step by step.  The last line of your response should be of the following format: 'The answer is $LETTER' (without quotes) where LETTER is one of $A,$B,$C,$D,$E. Think step by step before answering. Remember to put your answer on its own line. \n
A: Let's solve the problem step by step, starting with the variables given and checking each answer choice to find the correct one.

1. **Define the Variables**:
   Let \( P \) represent the original price of the item.

2. **Calculate the Discounted Price**:
   After a 22% discount, the item costs \( 0.78P \) because \( 100\% - 22\% = 78\% \).

3. **Apply the Coupon**:
   After applying a $20 coupon, the customer pays \( 0.78P - 20 \).

4. **Relation to Half the Original Price**:
   The final amount paid by the customer is $1.90 more than half the original price. Therefore, the equation is:
   \[
   0.78P - 20 = 0.5P + 1.90
   \]

5. **Solve for \( P \)**:
   Rearrange the equation:
   \[
   0.78P - 0.5P = 20 + 1.90
   \]
   \[
   0.28P = 21.90
   \]
   \[
   P = \frac{21.90}{0.28} = 78.2143
   \]

Given this calculation, let's check which choice \( P \) is closest to:
   - (A) $61
   - (B) $65
   - (C) $67.40
   - (D) $70
   - (E) $78.20

The calculated original price of $78.2143 is closest to choice (E) $78.20.

A:
The answer is $E.
Q: A car is being driven, in a straight line and at a uniform speed, towards the base of a vertical tower. The top of the tower is observed from the car and, in the process, it takes 10 minutes for the angle of elevation to change from 45° to 60°. After how much more time will this car reach the base of the tower? Answer Choices: (A)5(√3 + 1) (B)6(√3 + √2) (C)7(√3 – 1) (D)8(√3 – 2) (E)None of these\nA: Among A through E, please help me solve the problem step by step.  The last line of your response should be of the following format: 'The answer is $LETTER' (without quotes) where LETTER is one of $A,$B,$C,$D,$E. Think step by step before answering. Remember to put your answer on its own line. \n
A: Let's analyze the geometry of the problem and use trigonometry to find out how much more time it will take for the car to reach the base of the tower.

1. **Understanding the Scenario**:
   - The angle of elevation is the angle between the line of sight and the horizontal line from the observer (car) to the top of the tower.
   - The car travels at a uniform speed.

2. **Trigonometric Relations**:
   When the angle of elevation is \( 45^\circ \), the distance from the car to the base of the tower (let's call it \( x \)) is equal to the height of the tower \( h \) (because \( \tan 45^\circ = 1 \) implies \( x = h \)).
   
   At \( 60^\circ \), \( \tan 60^\circ = \sqrt{3} \), so \( x = \frac{h}{\sqrt{3}} \).

3. **Change in Distance**:
   The change in distance as the angle changes from \( 45^\circ \) to \( 60^\circ \) is \( h - \frac{h}{\sqrt{3}} = h\left(1 - \frac{1}{\sqrt{3}}\right) = h\left(\frac{\sqrt{3}-1}{\sqrt{3}}\right) \).

4. **Time for Change in Angle**:
   It takes 10 minutes for this change, so the speed of the car \( v \) is \( \frac{h\left(\frac{\sqrt{3}-1}{\sqrt{3}}\right)}{10} \).

5. **Distance Remaining to Base of Tower**:
   When the angle of elevation is \( 60^\circ \), the remaining distance to the tower base is \( \frac{h}{\sqrt{3}} \).

6. **Time to Reach Base of Tower**:
   Using the speed found earlier, the time \( t \) to cover this distance is:
   \[
   t = \frac{\frac{h}{\sqrt{3}}}{\frac{h\left(\frac{\sqrt{3}-1}{\sqrt{3}}\right)}{10}} = \frac{\frac{h}{\sqrt{3}}}{\frac{h(\sqrt{3}-1)}{10\sqrt{3}}} = \frac{10}{\sqrt{3}-1} \cdot \sqrt{3} = 10\left(\frac{\sqrt{3}}{\sqrt{3}-1}\right)
   \]
   Simplifying using the conjugate:
   \[
   t = 10\left(\frac{\sqrt{3}(\sqrt{3}+1)}{(\sqrt{3}-1)(\sqrt{3}+1)}\right) = 10\left(\frac{3+\sqrt{3}}{2}\right) = 5(3+\sqrt{3}) = 5(1 + \sqrt{3})
   \]

Among the answer choices, this corresponds to:
   - (A) \( 5(\sqrt{3} + 1) \)

\n
The answer is $A.\n
Next, please answer this problem:  \n
'''.strip()  
bbh_INSTRUCTION='''please help me solve the problem step by step.  The last line of your response should be of the following format: '\n The answer is $LETTER. \n' (without quotes) where LETTER is one of $A,$B,$C,$D,$E,$F. Think step by step before answering. Remember to put your answer on its own line. \n
I will provide an example for you:
Q: Known for jets and batteries, this brilliant inventor and businessman never graduated college but founded a major company. His name is \"Bill\" what?\nAnswer Choices: (A) William Boeing. (B) Boeing. (C) Lear. (D) Bill Gates.\nA: Among A through D. please help me solve the math problem step by step. \n
A: Let's think step by step.
To solve this problem, we first need to identify the inventor and businessman described in the question. The key points to consider are:

Jets and Batteries: The person is associated with both aviation and battery technology.
Never Graduated College: This detail eliminates some candidates who are known to have completed their college education.
Founded a Major Company: The individual not only contributed to inventions but also founded a significant company.
Name is "Bill": This is a crucial clue that specifically points to someone named "Bill" or "William".
Now, let’s analyze the given options:

(A) William Boeing: Known primarily for founding Boeing, which is heavily involved in aviation. Not widely recognized for contributions to batteries, but his impact on aviation is profound.
(B) Boeing: This is the name of the company, not a person.
(C) Lear: Bill Lear, founder of Lear Jet, also known for developments in the automotive and audio industries, but not particularly famous for batteries.
(D) Bill Gates: Known for founding Microsoft and not directly associated with jets or founding a major company in the aviation or battery industries.
Given the clues and choices provided, William Boeing fits most appropriately, though the connection to batteries isn't strongly established in common knowledge. However, his foundational role in aviation aligns well with the question's hint about jets, and his full name is indeed William (Bill being a nickname for William).

The answer is $A.
Q: What is the smallest country in the world that is at least one square mile in area?\nAnswer Choices: (A) The smallest country in the world that is at least one square mile in area is Monaco. (B) The smallest country in the world that is at least one square mile in area is Vatican City. (C) The smallest country in the world that is at least one square mile in area is the United States. (D) Nauru is the smallest country in the world that is at least one square mile in area.\nA: Among A through D. please help me solve the math problem step by step.\n
A: Let's think step by step.
Understanding the Choices:
(A) Monaco: Monaco is known as a small country in Europe, with a high density of population and economic activity.
(B) Vatican City: This is the smallest country in the world by area and is completely surrounded by Rome, Italy.
(C) The United States: It is one of the largest countries in the world, clearly not the smallest.
(D) Nauru: A tiny island nation in the Pacific Ocean, known for being one of the smallest countries in the world.
Size Comparison:
Monaco: Approximately 0.78 square miles, very small but not the smallest.
Vatican City: About 0.17 square miles, making it the smallest recognized independent state in the world.
Nauru: Around 8.1 square miles, considerably larger than Vatican City and Monaco but still among the smallest nations.
The United States: Significantly larger than all other options.
Determine the Correct Answer:
Based on the descriptions and sizes provided:
Vatican City is the smallest country in the world with an area more than one square mile, fitting the criteria perfectly, as it is definitely larger than one square mile and smaller than Monaco.
Conclusion:
Given the facts and comparing the areas, Vatican City (B) fits the criteria as the smallest country that is at least one square mile in area.

The answer is $B.
Next, please answer this problem:  \n
'''.strip()   
grop_INSTRUCTION='''You will be asked to read a passage and answer a question. think step by step, The last line of your response should be of the form like '\n The answer is $ANSWER. \n' (without quotes) where $ANSWER is the answer to the problem. Remember to put your answer on its own line after "A:". I will provide an example for you:\n\n
Some examples of passages and Q&A are provided below.\n\n# Examples\n\n
Q: Coming off their win over the Browns, the Bears stayed at home for a Week 9 duel with the Arizona Cardinals.  Chicago would trail early in the first quarter as Cardinals quarterback Kurt Warner hooked up with wide receiver Larry Fitzgerald on an 11-yard touchdown pass.  The Bears would answer as quarterback Jay Cutler competed a 33-yard touchdown pass to tight end Greg Olsen, but Arizona came right back as Warner hooked up with tight end Ben Patrick on a 6-yard touchdown pass.  Chicago would find themselves in a huge deficit in the second quarter as Warner completed a 17-yard touchdown pass to Fitzpatrick and a 15-yard touchdown pass to tight end Anthony Becht, followed by kicker Neil Rackers nailing a 43-yard field goal. The Cardinals would add onto their lead as Rackers booted a 30-yard field goal in the third quarter.  The Bears tried to rally in the fourth quarter as Cutler connected with Olsen on a 3-yard and a 20-yard touchdown pass, but Arizona pulled away with Warner completing a 4-yard touchdown pass to wide receiver Steve Breaston.\nQ: Which player caught the most touchdown passes?\nthink step by step, The last line of your response should be of the form like 'The answer is $ANSWER' (without quotes) where $ANSWER is the answer to the problem. Remember to put your answer on its own line..\n\n
A:  To determine which player caught the most touchdown passes in the passage, we need to count the number of touchdown passes caught by each player:

Larry Fitzgerald caught an 11-yard touchdown pass from Kurt Warner.
Greg Olsen caught a 33-yard touchdown pass from Jay Cutler.
Ben Patrick caught a 6-yard touchdown pass from Kurt Warner.
Larry Fitzpatrick caught a 17-yard touchdown pass from Kurt Warner.
Anthony Becht caught a 15-yard touchdown pass from Kurt Warner.
Greg Olsen again caught a 3-yard and a 20-yard touchdown pass from Jay Cutler.
Steve Breaston caught a 4-yard touchdown pass from Kurt Warner.
Now, we sum up the touchdown catches for each player:

Larry Fitzgerald: 1 touchdown
Greg Olsen: 3 touchdowns
Ben Patrick: 1 touchdown
Larry Fitzpatrick: 1 touchdown
Anthony Becht: 1 touchdown
Steve Breaston: 1 touchdown
Greg Olsen caught the most touchdown passes, with a total of 3.
\n
The answer is Greg Olsen.\n
Passage: Point guard Jason Terry became the teams scoring leader during the 2000–01 season, leading them with 19.7 ppg. After the All-Star break, the Hawks traded Mutombo to the Philadelphia 76ers for Theo Ratliff, Toni Kukoč, and Nazr Mohammed. However, Ratliff was injured and did not play with the Hawks until next season. They ended the season with a 25–57 record. In 2001, the Hawks drafted Spanish star Pau Gasol 3rd, but his rights were ceded to the Memphis Grizzlies in a trade involving Shareef Abdur-Rahim. Abdur-Rahim became the teams scoring leader, and made his only All-Star appearance in 2002. The team ended up 33–49 for the 2001–02 season. The Hawks sent Kukoc to the Milwaukee Bucks for All-Star Glenn Robinson in 2002, Robinson lead the team with 20.8 ppg. But the Hawks still failed to make the playoffs for the 2002–03 season, finishing with a 35–47 record.\nQ: How many more losses than wins did the Hawks end the 2001-2002 season?\n think step by step, The last line of your response should be of the form like 'The answer is $ANSWER' (without quotes) where $ANSWER is the answer to the problem. Remember to put your answer on its own line..\n\n
A:  
To find out how many more losses than wins the Hawks had during the 2001-2002 NBA season, we start with their record for that season, which was stated as 33 wins and 49 losses.

Calculate the number of wins: 33
Calculate the number of losses: 49
Next, we subtract the number of wins from the number of losses to find the difference:
Losses−Wins=49−33=16
Therefore, the Hawks ended the 2001-2002 season with 16 more losses than wins.
The answer is $16.
Next, please answer this problem:  \n
'''.strip()   

humaneval_INSTRUCTION="""
You will be asked to wirte a code. Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.\n The last line of your response should be of the form like  ```python\ndef CODE``` (must add ``` before and after the code)where you should only put CODE for this function in it. Remember to put your answer on its own line after "A:". 
Some examples of passages and Q&A are provided below.\n\n# Examples\n\n
Q: from typing import List\n\n\def get_sum(a: List[int]) -> int:\n  ```calculate the sum of an integer array.``` \n
A:  ```python\ndef get_sum(a: List[int]):\n  sum = 0\n   for x in a:\n       sum += x\n  return sum\n``` \n
Q: from typing import List\n\n\ndef rescale_to_unit(numbers: List[float]) -> List[float]:\n    \"\"\" Given list of numbers (of at least two elements), apply a linear transform to that list,\n    such that the smallest number will become 0 and the largest will become 1\n    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])\n    [0.0, 0.25, 0.5, 0.75, 1.0]\n    \"\"\"\n
A: ```python\nfrom typing import List\n\ndef rescale_to_unit(numbers: List[float]):\n    # find the (max-min) range of numbers\n    max_value = max(numbers)\n    min_value = min(numbers)\n    # shift and scale\n    numbers = [(float(x)-min_value)/(max_value-min_value) for x in numbers]\n    return numbers\n``` \n
Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.\n
Next, please answer this problem:  \n
""".strip()  



"""

"""

