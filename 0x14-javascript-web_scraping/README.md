# 0x14. Javascript - Web scraping

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

### More Info

- Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

- Install semi-standard

Documentation

```
$ sudo npm install semistandard --global
```

- Install request module and use it

Documentation

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```


# TASKS

0. Readme mandatory - [0-readme.js](0-readme.js/)

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object

```
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 
```

1. Write me mandatory - [1-writeme.js](1-writeme.js/)

Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in utf-8
- If an error occurred during while writing, print the error object

```
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 
```


2. Status code mandatory - [2-statuscode.js](2-statuscode.js/)

Write a script that display the status code of a GET request.

- The first argument is the URL to request (GET)
- The status code must be printed like this: code: <status code>
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
```


3. Star wars movie title mandatory - [3-starwars_title.js](3-starwars_title.js/)

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$
```


4.Star wars Wedge Antilles mandatory - [4-starwars_count.js](4-starwars_count.js/)

Write a script that prints the number of movies where the character "Wedge Antilles" is present.

- The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
- Wedge Antilles is character ID 18
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
guillaume@ubuntu:~/0x14$ 
```


5. Loripsum mandatory - [5-request_store.js](5-request_store.js/)

Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

guillaume@ubuntu:~/0x14$ 
```


6. How many completed? mandatory - [6-completed_tasks.js](6-completed_tasks.js/)

Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
guillaume@ubuntu:~/0x14$
```

7. Who was playing in this movie? #advanced - [100-starwars_characters.js](100-starwars_characters.js/)

Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: 3 = "Return of the Jedi"
- Display one character name by line
- You must use the Star wars API
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
guillaume@ubuntu:~/0x14$
```


8. Right order #advanced - [101-starwars_characters.js](101-starwars_characters.js/)

Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: 3 = "Return of the Jedi"
- Display one character name by line in the same order of the list "characters" in the /films/ response
- You must use the Star wars API
- You must use the module request

```
guillaume@ubuntu:~/0x14$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
guillaume@ubuntu:~/0x14$
```


9. Twitter Auth #advanced - [102-search_twitter.js](102-search_twitter.js/)

Write a Javascript script that takes in 3 strings and sends a search request to the Twitter API

- Use the Twitter API search endpoint
- Use the Application-only authentication flow to do a search request
- Create an Twitter application here
- The first argument must be the Consumer Key (API Key)
- The second argument must be the Consumer Secret (API Secret)
- The third argument must be the search string
- Display only 5 results in the following format: [<Tweet ID>] <Tweet text> by <Tweet owner name> (see example below)
- Only these modules are allowed: request, base-64 and utf8
- You don’t need to check arguments passed to the script (number or type)

```
guillaume@ubuntu:~/0x14$ ./102-search_twitter.js AAAAAA BBBBBB "#cisfun"
[857232487553974300] Im not sure if uber will be around in the next couple of years
https://t.co/ZLIvgZoC5I

@holbertonschool
#cisfun by MJohnson
[856621409438543900] https://t.co/kXRUi7BSId

@holbertonschool
#cisfun by MJohnson
[856588726884982800] Itching to read my python book...instead picked up a mystery novel.
#HappyBreak! #cisfun too by Biebop
[855696357788614700] Twitter Likes and followers hack 
#Humedal
#Mondorf
#cisfun https://t.co/I1tc1iR5g2 by Mustafa ugurlu
[855594028397584400] @julienbarbier42 #neverforget

@sophie_rb42
@holbertonschool 
#cisfun
#lol https://t.co/WSiZFW8bgg by MJohnson
[855473339757998100] Lessons learnt at #DockerCon - containers rock, #pythoniscool, and because #Cisfun, I was able to have more meaningful convos w/ tech peeps by Zee Adams
[855202379183960000] https://t.co/VeGXxjptRD

@holbertonschool 
#cisfun by MJohnson
[855136931973283800] @Linux source code: about 6,000,000 lines of code❤?#mindblown #cisfun @holberton https://t.co/0x64hr3iAd by Naomi
[854919921200840700] RT @NamoDawn: Shoutout to the @holbertonschool community for dropping knowledge during Shell Project ??‍?✨??#cisfun #manpagesfordays by Holberton
[854919717768888300] Shoutout to the @holbertonschool community for dropping knowledge during Shell Project ??‍?✨??#cisfun #manpagesfordays by Naomi
[854880017754406900] @yeoleumson helping me stay focused on the last day of the C shell project @holbertonschool #cisfun
https://t.co/jnIqSF8azO by Christian Agha
[854815181611745300] https://t.co/gSz4NCNlmJ

@holbertonschool
#cisfun by MJohnson
[854787744135954400] RT @c_nov20: Burning the midnight oil yet again...Shell Project due in just under 24 hours

#Cisfun by jv
[854775517320433700] Last day of shell project... Yay... I get to get some sleep now!!! #sleepdeprived #sleepingisoverrated #cisfun https://t.co/LaG7OiFvDL by Julija Lee
[854580988155838500] Burning the midnight oil yet again...Shell Project due in just under 24 hours

#Cisfun by c_nov20
guillaume@ubuntu:~/0x14$ 
```
