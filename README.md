# IndiaBix Parser
Web Scrapper written in Python that parses the [IndiaBix](https://indiabix.com) website and generates an sqlite database file containing question data.

Question Schema
- id : INTEGER AUTO-GENERATED
- question : TEXT
- option1 : TEXT : NULL if not found
- option2 : TEXT : NULL if not found
- option3 : TEXT : NULL if not found
- option4 : TEXT : NULL if not found
- option5 : TEXT : NULL if not found
- answer : TEXT
- description : TEXT (the explanation)