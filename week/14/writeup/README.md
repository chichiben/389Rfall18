Writeup 10 - Crypto II
=====

Name: Christina Benjamin
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Christina Benjamin

## Assignment 10 Writeup

### Part 1 (70 Pts)
By clicking through the various links in the site, I could see that each link was associated with an item?id= between 0 and 2. I had to go through google translate to bypass the campus' protection against SQL injections. I tried a SQL injection by appending the id with ' OR ‘1’=’1’ -- -, but this caused an internal server error. Since there are sometimes checks for the 'or' keyword in specific, I tried appending ' || 1=1 -- -. This command works because on the backend, the query SELECT [product] FROM Products WHERE id=[some number] is being used. When working properly, the WHERE conditional is only returning true when the correct id is called. However, we can force the conditional to always return true by appending an OR operator with a tautology like 1=1. Since this operation will ensure that the query is true, it will proceed to select all of the contents of the table and display the whole directory. The comments are necessary to remove the trailing single-quote and semicolon from the code. The query I used succeeded in displaying the full product list I had seen already and the following flag: CMSC38R- {y0U-are_the_5ql_n1nja}

### Part 2 (30 Pts)
Level 1: Since each search is set to a query, I placed the alert in a <script> tag so that it would be treated as code. 
Level 2: The script tag didn't work this time, so I tried messing with the formatting of the text. I was able to bold and italicize the comments, so I knew that it was reading and converting the html. Then I tried inserting a link with the href leading to a javascript alert, and this was successful. 
Level 3: The target code shows that there is a function chooseTab(num). There is also a line where the given num is used to build the image url: "<img src='/static/level3/cloud" + num + ".jpg' />". I received the alert by adding an onerror attribute set to alert(0) after the id, and then adding a random character to trip the error and trigger the alert.
Level 4: I could see in the code for timer.html that there was a line that showed: onload="startTimer('{{ timer }}');". I tried sending in a single quote and received an error in the console saying that it was EOF, and could navigate to the line in timer.html showing that the single quote had been read into startTimer. Then after trying several combinations of the alert tag with parentheses and the single apostrophe, I was able to trigger the alert by sending in ');alert('. This worked because the opening parenthesis and semicolon in the code I sent in ended the startTimer function and then tacked on a new line triggering the alert, which was ended with a closing parenthesis and semicolon within the timer.html code. 
Level 5: The source code shows that the email field is not even read by the server, so it is not a vulnerable spot. By clicking through the links and watching the URL, the only spot that seemed vulnerable was in the URL "signup?next=confirm". In the source code, the next field is read in as "<a href="{{ next }}">Next >></a>", which looked like a similar vulnerability to level 4. Since JS code inside of an href needs to be appropriately defined before it is ran as JavaScript, I prepended the alert with "javascript:" and placed it after the "next=" assignment. Clicking the 'next' button with this url in place successfully triggered the alert. 
Level 6: In index.html, lines 20-25 show that sending in a url with https will cause an error. However, the scriptEl.onload command includes the line ""Loaded gadget from " + url", where it is vulnerable. Since it is inside setInnerText, in order to include the alert command, I used a data URI scheme with the media type as text: "data:text/javascript,alert('0')" and appended this snippet after frame# to trigger the alert. 
