#Movie Recommendation

1.1	INTRODUCTION

Recommendation systems are getting increasingly important in today’s extraordinarily busy world. People are always short on time with the myriad duties they need to accomplish within the restrained 24 hours. Therefore, the recommendation structures are vital as they help them make the right choices, without having to dissipate their cognitive resources. The reason for a recommendation system essentially is to look for content that would be thrilling to an individual. Moreover, it includes a number of things to create customized lists of beneficial and exciting content unique to every user/individual. Recommendation structures are Artificial Intelligence primarily based algorithms that skim through all possible alternatives and create a customized listing of objects which might be thrilling and relevant to an individual.


1.2	MOTIVATION OF THE WORK

We are leaving the age of facts and coming into the age of recommendation. Like many device mastering techniques, a recommender system makes a prediction based on users’ ancient behaviors. Specifically, it’s to expect user choice for a fixed of items based totally on past experience.
It helps users find and select items (e.g., books, movies, restaurants) from the huge number available on the web or in other electronic information sources. Given a large set of items and a description of the user’s needs, they present to the user a small set of the items that are well suited to the description. Similarly, a movie recommendation system provides a level of comfort and personalization that helps the user interact better with the system and watch movies that cater to his needs. Providing this level of comfort to the user was our primary motivation in opting for a movie recommendation system. The chief purpose of our system is to recommend movies to its users based on their viewing history and the ratings that they provide.
  
 
1.3	TECHNOLOGIES USED

Recommendation Systems have been in existence for a long time and have served towards the convenience of people. In the most general way, recommender systems are algorithms aimed at suggesting relevant items to users (items being books to read, products to buy, music to listen or as in our case, movies to watch.) The most common approach towards recommendation systems has been Content-based recommendations. Content-based techniques develop representations of clients and items through the investigation of additional data, for example, record content, client proles, and the traits of items, to make suggestions. In many cases, the data that is utilized to build the pictures is difficult to get or even fake; subsequently, its presentation and application run to experience the ill effects of significant restrictions. Thus, we take another approach called Collaborative Filtering where instead of only depending upon the attributes of the item, we let our users rate different items, and based on such ratings we make recommendations using two ways, either by User-User similarities or Item-Item Similarities. In the User-User similarity approach, we let our users rate movies and then find other users who rated movies similarly to our test user i.e. we find other users who feel similarly to our test user. On the other hand, an Item-Item approach includes letting our user rate items and then find other items that have similar ratings. Although this method is simple and effective, with the rapid development of the Internet, the high sparsity of the data limits the performance of the algorithm.

To make a movie Recommendation system we have used the following technologies are used:

1.	Python

Python is an interpreter, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbage- collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.
 
2.	Jupyter Notebook

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

3.	HTML

HTML is at the core of every web page, regardless of the complexity of a site or the number of technologies involved. It's an essential skill for any web professional. It's the starting point for anyone learning how to create content for the web. And, luckily for us, it's surprisingly easy to learn.

4.	CSS

CSS stands for Cascading Style Sheets. This programming language dictates how the HTML elements of a website should actually appear on the front end of the page.

5.	JavaScript

JavaScript is a more complicated language than HTML or CSS, and it wasn't released in beta form until 1995. Nowadays, JavaScript is supported by all modern web browsers and is used on almost every site on the web for more powerful and complex functionality.



1.4	PROBLEM STATEMENT

For building a recommender system from scratch, we face several different problems. Currently, there are a lot of recommender systems based on user information, so what should we do if the website has not gotten enough users. After that, we will solve the representation of a movie, which is how a system can understand a movie. That is the precondition for comparing similarities between two movies.
 
Movie features such as genre, actor, and director are a way that can categorize movies. But for each feature of the movie, there should be different weights for them and each of them plays a different role in a recommendation. So we get these questions:

•	How to recommend movies when there is no user information.
•	What kind of movie features can be used for the recommender system?
•	How to calculate the similarity between two movies.
•	Is it possible to set weight for each feature?



1.5	OBJECTIVE

There are many kinds of Recommender Systems but not all of them are suitable for one specific problem and situation. Our objective is to find a new way to improve the classification of movies, which is the requirement of improving content-based recommender systems and providing accurate movie recommendations to users. To build a movie recommendations system based on the approach of content-based filtering. We will use two sets of information:

•	1. Movie index
•	2. Cosine Similarity




1.6	ORGANIZATION OF THE PROJECT
This report is divided into 7 chapters. The ﬁrst chapter provides the introduction to the topic. The details include the techniques used, problem statements, and objective of the project. The second chapter lists out the approaches in making a Movies Recommendation System and methodologies which can be used for recommendations. The third chapter gives a detailed description of various project requirements. The fourth chapter gives the design methodology, the fifth chapter gives the implementation and analysis. Sixth chapter involves project outcomes and applicability in real-life. Finally, the seventh chapter details conclusion and recommendation.	4
 
1.7	SUMMARY

Proposal frameworks are getting progressively vital in today’s exceptionally active world. Individuals are continuously brief on time with the horde obligations they have to be finished inside the limited 24 hours. Hence, the recommendation structures are imperative as they offer assistance to make the correct choices, without having to scatter their cognitive resources. The most common approach towards suggestion frameworks has been Content-based proposals. To construct a steady and precise recommender framework utilizing content-based sifting. Proposal frameworks offer assistance to clients discover and select things (e.g., books, motion pictures, eateries) from the colossal number accessible on the internet or in other electronic data sources. Given a huge set of things and a depiction of the user’s needs, they display to the client a little set of the things that are well suited to the portrayal. Additionally, a motion picture suggestion framework gives a level of consolation and personalization that makes a difference the client associated way better with the framework and observe motion pictures that cater to his needs. Giving this level of consolation to the client was our essential inspiration in picking for motion picture suggestion framework as our Extend. The chief reason for our framework is to prescribe motion pictures to its clients based on their seeing history and evaluations that they give. We have utilized Python, Jupyter Notebook, HTML, CSS, and JavaScript in our recommender.

