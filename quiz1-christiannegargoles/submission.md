# Quiz #1 : Assessment and Planning 

### Date: November 10, 2021
### In Class/Lab Quiz:
### Due:
* Morning Class:  11:45
* Afternoon Class: 5:45


---
## Name: Christianne Gargoles                           <!-- answer -->


1. A URL is comprised of a number of compents.  Consider the following URL:

  ``one://two:three@four.five.size:seven/eight/nine/ten?eleven=twelve&thirteen=fourteen#fifteen``

  * Provide both the name and value of each component.
    1. scheme: "one"                                    <!-- answer -->
    1. host: "two"						<!--answer -->
    1. port: "three" "four" "five" "size" "seven"                             <!-- answer -->
    1. path: "eigth" "nine" "ten"                                 <!-- answer -->
    1. query: "eleven" "twelve" "thirteen" "fourteen" "fifteen"		<!-- answer--> 
    <!-- Add more lines as needed -->

1. In the following code block, provide the git instructions necessary to add a new file to the remote repository: git@github.com:org/project.git (You should presume that you don't have a copy of this repository on your local computer.)
   ```
<<<<<<< HEAD
* git clone git@github.com:org/project.git					<!--answer -->
* git add .						<! --answer -->
* git commit -m "message"					<! -- answer-->
=======
* git clone <https>					                              <!--answer -->
* git add .						                                  <! --answer -->
* git commit -m "message"					                        <! -- answer-->
>>>>>>> 3e591b1e540fcfcf05498f1118afc6440a8a415a
* git push                                                      <!-- answer -->
   ```
   <!-- You many add any number of lines in the above code block that you need. -->

1. Provide the Apache Directive used to perform the requested action
   1. Position the location of root location of the website at:  /var/www/html
     *                                                <!-- answer -->
   1. To disable the user "steve" from having a web presence on your server.
<<<<<<< HEAD
     *  Userdir                                               <!-- answer -->
=======
     *                                              <!-- answer -->
>>>>>>> 3e591b1e540fcfcf05498f1118afc6440a8a415a
   1. To create an alias between the URI: /marketing and the file: /user/marketing/www
     * alias "/marketing                                                  <!-- answer -->
   1. To define the location of the error log to be: /var/log/apps/apache/error.log
     *                                                  <!-- answer -->


1. What is the command used to create the user "steve" within your apache container?
    *                                                  <!-- answer -->


1. What does the "AllowOverride" Directive do?
    *                                                  <!-- answer -->


1. Given the following command, provide the corresponding HTTP Request Header:
    * curl  https://www.csun.edu/~steve/roster/input/value/input/value
    ```
                                                      <!-- answer -->
    ```                                                      
    <!-- You many add any number of lines in the above code block that you need. -->

1. The CGI standard defines a number of environment variables that are provided to a CGI program.  Identify and explain the purpose of 6 of these environment variables.
   1.QUERY_STRING:  the part of URL after ? character.             <!-- answer -->
   1.SERVER_NAME : server's hostname or IP address                                               <!-- answer -->
   1.SERVER_PROTOCOL: name and revision of the information protocol the request came in with       <!-- answer -->
   1.CONTENT_TYPE: the MIME type of the query data                                                  <!-- answer -->
   1.DOCUMENT_ROOt: The directory from which Web documents are served                               <!-- answer -->
   1.REQUEST_METHOD: the method with which the information request was issued                          <!-- answer -->


 1. Consider the following URL and regular expression used to process this string:
    * URL:   ``http://www.fake.org/marking/john.smith/code=10325/app/input``
    * regexp: ``"^marketing/([a-z]*.[a-z]*)/(code=[0-9]{4,6})/(.*)$"``

    Define the value of each of the following back references
    1. $1:                                                           <!-- answer -->
    1. $2:                                                           <!-- answer -->
    1. $3:                                                           <!-- answer -->
    1. $4:                                                           <!-- answer -->

1. There are a number of different types of files.  Each of these file types can be identified by a single character in the output of the command ``ls -l``.  What are these types of files:
   1. -: a regular file
   1. p: pipe                                                        <!-- answer -->
   1. l: symbolic link                                                       <!-- answer -->
   1. d: directories                                                         <!-- answer -->
   1. b: block                                              <!-- answer -->
   1. c: char  <!-- answer -->
   1. s: socket                                                          <!-- answer -->

1. Describe each of the following:
  - process: is any active instance of a program                                                     <!-- answer -->
  - environment: is a set of dyanmic named values, stored with is the system that are used by application launched in shells.                <!-- answer -->
  - stdin: Standard input, User input, or sometype of input that users do in a computer  <!-- answer -->
  - $?: The exit status of the last command executed                                                <!-- answer -->
 
