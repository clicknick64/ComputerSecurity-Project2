# n4sty Project2 Report

### Μέλη ομάδας

- 1115201800154, Αρίστη Παπασταύρου (το αναφέρω και εδώ. Έκοψα τα λειτoυργικά για να τα δώσω για βελτίωση βαθμού τον Σεπτέμβρη.Παρακαλώ να μου κρατήσετε τον βαθμο για του χρόνου το εαρινό εξάμηνο μιας και γιαυτο τον λόγο, δεν μπόρεσα να δηλώσω την ασφάλεια σε αυτό το εξάμηνο.Thank you in advance!)
- 1115201800156, Νικόλαος Πασσάκος Χατζηορίδης 


# 1o Ερώτημα
- Σε πρώτη φάση συνδεθήκαμε μέσω tor browser στο link που δινόταν μέσω της εικόνας του github repo.
- Στο source code του site βρήκαμε την διεύθυνση https://blog.0day.rocks/securing-a-web-hidden-service-89d935ba1c1d
- Φαίνεται πως ο ιδιοκτήτης του site ξέχασε να απενεργοποίησει το server-info όπως λέει το **3.1** του άρθρου. **http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/server-info**
- Στα Configuration files παρατηρήσαμε στο τέλος το εξής:
 ```html
     In file: /etc/apache2/sites-enabled/fixers.conf
       1: <VirtualHost *:80>
       9:   ServerName 2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd
      11:   ServerAdmin webmaster@localhost
      12:   DocumentRoot /var/www/fixers
      20:   ErrorLog /var/log/apache2/fixers_error.log
      21:   CustomLog /var/log/apache2/fixers_access.log combined
        : </VirtualHost>
    In file: /etc/apache2/sites-enabled/personal.conf
       1: <VirtualHost *:443>
       9:   ServerName flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad
      11:   ServerAdmin webmaster@localhost
      12:   DocumentRoot /var/www/personal
      20:   ErrorLog /var/log/apache2/personal_error.log
      21:   CustomLog /var/log/apache2/personal_access.log combined
        : </VirtualHost>
```
Και έτσι οδηγηθήκαμε σε μία ακόμη σελίδα: **flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion**
- Σε δεύτερη φάση, βρήκαμε ότι το 2ο link είχε σελίδα **access.php**, στην οποία ότι user creadentials και αν βάζαμε μας εμφάνιζε bad user. Κάναμε λοιπόν απόπειρα να βρούμε το source code της σελίδας και καταφέραμε να εμφανίσουμε τον κώδικα από το **access.phps** (Mετά συνειδητοποιήσαμε ότι αυτό αναφραφόταν και στο server info στα settings στο πεδίο: **SetHandler application/x-httpd-php-source**) 
- Βρήκαμε το 48ο πολλαπλάσιο του 7 (https://math.stackexchange.com/questions/3710141/how-to-find-the-48th-multiple-of-7-that-contains-a-7-in-its-decimal-representati) αλλά μιας και δεν μπορούμε να κάνουμε αλλαγές πάνω στο .phps κάναμε **Inspect Element(Q)** και μέσω του Inspector βάλαμε στην ζητούμενη θέση το string 1337abc (προσθέσαμε 3 χαρακτήρες για να φτάσουμε τα 7 decimal points που ζητούνταν).
- Τέλος από την 1η εργασία είχαμε βρει ότι η strcmp στην php εάν πάρει σαν παράμετρο κάτι "άσχετο", 
 πχ: [] επιστρέφει NULL. Για να μπορέσουμε επομένως να προσπεράσουμε τον έλεγχο του password βάλαμε στο url: **http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/access.php?password[]=&user=1337abc**
 - O έλεγχος πέτυχε και έτσι μας δόθηκε το επόμενο link: **http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/** 
 - Στο **http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/diary2.html** βρήκαμε 2 στοιχεία που θα χρειαστούν στο 2ο βήμα (__αναφορά στο Plan X, ένα repo: github:chatziko/pico και ένα clue:socat + onions = perfect recipe__), και ένα νέο link:  __zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion__
 - Και σε αυτό το url (της Υβόννης) γίνεται directory listing και έτσι βρήκαμε την σελίδα: **http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/post3.html**
 - Εδώ λοιπόν βρήκαμε το ονοματεπώνυμο του Γιώργου (**Giorgos Komninos**) και ένα visitor id (**#834472**)
 - - Ερευνώντας το link των fixers είδαμε ένα Visitor cookie. Βλέποντας το = στο τέλος υποψιαστήκαμε base64 encoding. Όντως, μετά την αποκωδικοποίηση καταλάβαμε ότι το cookie έχει την εξής μορφή:
 ```
 BASE64(<text>:SHA256(<text>))
 ```
 - Ετσι φτιάξαμε ένα μικρό πρόγραμμα το οποίο έπαιρνε σαν όρισμα το visitor id που βρήκαμε στο προηγούμενο βήμα και του έκανε τις κατάλληλες κωδικοποιήσεις.Βάζοντας στο cookie value το κωδικοποιημένο πλέον visitor_id μας δόθηκε πληροφορία για ένα νέο link! (**http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/sekritbackup1843/**)
 -  Στο νέο link ανοίξαμε πρώτα το notes.txt για να λάβουμε τυχόν νέα clues.
 - Διαβάζοντας τις οδηγίες αποκωδικοποίησης των 2 αρχείων που υπάρχουν στο directory (τα οποία και κατεβάσαμε) είδαμε ότι πρέπει να βρούμε ένα secret string. Υποθέσαμε ότι το secret string θα έχει κάποια άμεση σύνδεση με το ropsten address που "είχε ξεμείνει" στο κάτω κομμάτι του notes.
 - Μετά από αρκετή έρευνα (και αποτυχημένες προσπάθειες όπου βάλαμε το ropsten address σε faucet και το ψάξαμε και στο ethereum browser δίχως αποτέλεσμα) καταλ'αβαμε ότι επρόκειτο για ropsten test network.
 - Κάναμε λοιπόν concat το ropsten address στο url του etherscan ως εξής: **https://ropsten.etherscan.io/tx/0xdcf1bfb1207e9b22c77de191570d46617fe4cdf4dbc195ade273485dddc16783**
 και βάζοντας UTF-8 κωδικοποίηση στο input data, εμφανίστηκε η λέξη  __(bigtent)__
 - Επιστρέφοντας στις οδηγίες που δόθηκαν στο notes, δοκιμάσαμε να κάνουμε decrypt τα αρχεία με το timestamp του transaction που μας εμφάνισε το etherscan δίχως αποτέλεσμα.
 - Έτσι φτιάξαμε ένα bash script (θα το βρείτε με το όνομα find_key.sh) το οποίο είχε λογική brute force.
 Σε for-loop φτιάξαμε ημερομηνίες από 01-01-2020 μέχρι και τον 1ο μήνα του 2022. Μετά φτιάχναμε το ζητούμενο string (__date κενό secret_string__) και το περάσαμε από sha256 κωδικοποίηση.
 Στο for loop μετά καλέσαμε 
 ```bash
echo  $NEWVAR
gpg -d --pinentry-mode loopback --passphrase=$FINAL  $FILENAME 
 ```
 και όταν η εντολή πετύχαινε εμφάνιζε το αποτέλεσμα. Από το echo πήραμε την ημερομηνία που πέτυχε και βάλαμε το sha256 hash του ως κωδικό στο: **gpg -d signal.log.gpg > signal.log** και **gpg -d firefox.log.gz.gpg > firefox.log.gz** καταφέρνοντας να κάνουμε decrypt τα αρχεία.
  
 - Ανοίγοντας το πλέον decrypted, signal.log, διαβάσαμε τον διάλογο και παρατηρήσαμε τις κωδικές λέξεις git και commit καθώς και ένα hash! Το μόνο που έλειπε είναι να βρούμε σε ποιο github repo άνηκε το hash αυτού του commit. Γράφοντας **cat firefox.log | grep -v The_Conversation** βρήκαμε το link για το repo: **https://github.com/asn-d6/tor**
 - Βάλαμε στο url του repoo το hash του commit : __https://github.com/asn-d6/tor/commit/4ec3bbea5172e13552d47ff95e02230e6dc99692__ όπου βρήκαμε σε σχόλια οδηγίες για το πως να βρούμε τον Γιώργο.
 - Τα στοιχεία που δώθηκαν θύμιζαν exponential distribution και παρατηρώντας λίγο ότι το N είναι μεγαλύτερο και από τις δύο δοθείσες τιμές της E(), βάλαμε στο wolfram την εξής παράσταση:
 ```php
 x^7 mod N = E(x), y^7 mod N = E(y)
 Result:x = 127670779n_1 + 306, y = 127670779n_2 + 3735
```
 Για n=0 είχαμε τους πρώτους σε σειρά αριθμούς που ικανοποιούν τη συνθήκη, x=306 και y=3735
- Κάνοντας concat αυτά τα αποτελέσματα με τον τρόπου που περιέγραφε στο repo βρήκαμε το link
(http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/30637353063735.txt)
 όπου περιείχε την πληροφορία για την τοποθεσία του Giorgos Komninos
  (**Gilman's Point on the Kilimanjaro**) 
  <div style="text-align:center"><img src="photos/Giorgos_Location.png" /></div>
  
 __ΝΟΤΕ:__ Τα scripts που χρησιμοποιήθηκαν για το ερώτημα 1 βρίσκονται στο https://github.com/chatziko-ys13/2021-project-2-n4sty/tree/master/src/erotima_1

# 2o Ερώτημα
- Επιστρέφοντας στο onion link που είχαμε βρει στο diary2 της Υβόννης (__**zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion**__), κάναμε κάποιες τυχαίες δοκιμές για user creadentials και όταν γράψαμε User Name: admin , Password: admin μας εκτύπωσε μήνυμα: 
**The site says: “Invalid password”** αντί για **The site says: “Invalid user: n4sty”**, που σημαίνει ότι βρήκαμε user με όνομα admin.
- Αφού στήσαμε το repo από το github που είχαμε βρει (github:chatziko/pico) παρατηρήσαμε μετά το make ότι εμφανίζεται warning:
```php
main.c: In function ‘check_auth’:
main.c:136:5: warning: format not a string literal and no format arguments [-Wformat-security]
  136 |     printf(auth_username);
```
- **Εκτελέσαμε Format_String_Attack.**

Επειδή στην κλήση της printf δεν υπήρχαν μεταβλητές εάν βάλουμε στο username του onion server string τύπου %p %p ... %s ουσιαστικά η  
printf θα ερμηνεύσει το string της εισόδου ως αναφορά σε pointers, οπότε θα προσπαθήσει να ερμηνεύσει κάθε %p/%s ως pointer to string,ξεκινώντας από τη θέση του buffer (πιθανώς στο Stack). Σε κάποιο σημείο, θα φτάσει σε μια μη-έγκυρη διεύθυνση και η προσπάθεια access σε αυτήν θα προκαλέσει μεν program-crash αλλα ταυτόχρονα θα μας εκτυπώσει το value θέσεων μνήμης στις οποίες δεν θα έπρεπε να έχουμε access.

(Source:https://owasp.org/www-community/attacks/Format_string_attack)

- Συνδυάζοντας τα παραπάνω δεδομένα (και μετά από μερικές δοκιμές) βάζοντας τα παρακάτω στοιχεία στο authentication:
```bash
username: %p %p %p %p %p %p %s
password: admin
```
μας εμφάνισε ο Plan X server το παρακάτω μήνυμα:
**Invalid user: 0x57af9310 0x14 0x5664144a (nil) (nil) 0x57ae9480 admin:e5614e27f3c21283ad532a1d23b9e29d**
- Βάζοντας το hash (md5 encoding) στο https://crackstation.net/, είχαμε και επισήμως το password του admin: **bob's your uncle**
- Tελευταίο βήμα μας, να συνδεθούμε στο onion server με τα παρακάτω στοιχεία:
```php
username: admin
password: bob's your uncle
```
όπου μόλις πέτυχε η σύνδεση, μας έβγαλε στην σελίδα του Plan X όπου και ανακαλύψαμε ότι οι **5l0ppy 8uff00n5** έκλεψαν τα αρχεία του...

<img src="photos/Thieves.png">

# Ερώτημα 3

## Buffer Overflow

Ερευνώντας τον κώδικα, παρατητήσαμε πως υπάρχει η χρήση της **strcpy** σε πίνακα του οποίου το μέγεθος καθορίζεται από το Content-Length Header του POST request. Για να τεστάρουμε αυτή την υπόθεση κάνουμε το ακόλουθο request:
```bash
curl 'http://zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion/' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion' -H 'Authorization: Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ==' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'AAAAAAAAAAAAA' --socks5-host 127.0.0.1:9050 -H "Content-Length: 1"
Wow, seems that you POSTed 1 bytes.
Fetch the data using `payload` variable.
```

Παρατηρούμε επίσης πως βάζοντας αρκετούς χαρακτήρες, η σελίδα δεν απαντάει στο request, οπότε πιθανότατα κρασάρει από το buffer overflow.

Μετά από μελέτη της στοίβας με τον gdb χρησιμοποίωντας το Format String Attack από το προηγούμενο ερώτημα, βρίσκουμε τις εξής χρήσιμες πληροφορίες:
- Θέση 27: Canary
- Θέση 30: Μία διεύθυνση μέσα στη στοίβα
- Θέση 31: Μία διέυθυνση στις εντολές του προγράμματος.

Αυτές οι θέσεις είναι πολύ χρήσιμες καθώς μπορούμε να βρούμε offsets τρέχοντας τοπικά το pico, αυτών των δεδομένων διευθύνσεων που κάνουμε leak από τη μνήμη και άλλων διευθύνσεων που θα δούμε στη συνέχεια. Αυτά τα offsets είναι ίδια και στον server.

Για το ερώτημα 3 κατασκευάσαμε ένα script το οποίο παίρνει ως παραμέτρους αυτά τα offsets, κάνει ένα request στο server για να πάρει τις διευθύνσεις και το canary και κατασκευάζει ένα payload το οποίο κάνει override το return address της συνάρτησης, πηγαίνοντας τη ροή του προγράμματος στη κλήση της serve_ultimate.

Τη προστασία του canary με το null byte ήταν πολύ εύκολο να τη προσπεράσουμε καθώς αμέσως μετά την strcpy υπήρχε μια λούπα που αντικαθιστούσε τα '=' και τα '&' με \0. Αρκεί η διεύθυνση του buffer που κάναμε override να ήταν πριν από το canary.

Εκτελώντας το script λαμβάνουμε το ultimate.html

```html
<pre>
Thanks for the coins, I knew I can do business with you.

Your ssh access to the server should be restored, you can find your
files under /var/backup/ (see 'backup.log' for a list).

To avoid losing your files again, hire us!
5l0ppy 8uff00n5 can help you fix all your security issues.
Use the code tmmt8pN_lj4 to get 20% off our usual rates!
</pre>
```

Τα αρχεία του Plan X βρίσκονται στο directory **/var/backup/**

# Ερώτημα 4

Για διευκόλυνση μας και εξοικονόμηση χρόνου αλλάξαμε την γλώσσα των scripts σε python. Δεν υπάρχει κάποια ιδιαίτερη αλλαγή στη δομή του script σε σχέση με το προηγούμενο ερώτημα. Αυτή τη φορά το payload το κατασκευάζουμε κάνοντας override το return address με τη συνάρτηση send_file. Βάζοντας το string του path του αρχείου που θέλουμε να ανακτήσουμε μέσα στο stack, το περνάμε ως παράμετρο στη συνάρτηση.

Πρώτα βλέπουμε τα περιεχόμενα του αρχείου **/var/backup/backup.log**

```
backing up...
index.html
z.log
2021_project1_grades.pdf
bob.sql
playlist
```

Ύστερα βλέπουμε τα περιεχόμενα των αρχείων αυτών που βρίσκονται στον ίδιο φάκελο και αν εξαιρέσουμε το τρολλάρισμα που τρώμε χωρίς όμως κάποιο Rick Roll αυτή τη φορά, βρίσκουμε πως στο αρχείο z.log βρίσκονται τα αποτελέσματα του Plan Y. Η ultimate coefficient δεν έχει υπολογιστεί ακόμα με ακρίβεια, αλλά ίσως κάποια μέρα βρούμε το πραγματικό νόημα της ζωής.
```
Computing, approximate answer: 41.998427123123
```

# 5ο Ερώτημα
'Εχοντας πλέον εξερευνήσει όλο το  listing του /var/backup/backup.log, καταλάβαμε ότι το /var/backup/z.log είχε και την απάντηση στο 4ο ερώτημα αλλά και το clue για το 5ο.Συγκεκριμένα:

```bash
Computing, approximate answer: 41.998427123123
...
Plan Z: troll humans who ask stupid questions (real fun).
I told them I need 7.5 million years to compute this XD

In the meanwhile I'm travelling through time trolling humans of the past.
Currently playing this clever dude using primitive hardware, he's good but the
next move is crushing...

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7

PS. To reach me in the past use the code: "<next move><public IP of this machine>"
```
Παρατηρώντας την ακολουθία κινήσεων που δίνεται στο τέλος του __z.log__ καταλάβαμε ότι επρόκειτο για παρτίδα σκακιού και μάλιστα ήταν μέρος του 6ου παιχνιδιού από την σειρά 6 αγώνων (**Deep Blue versus Garry Kasparov**) που έπαιξε ο Kasparov με το  __IBM supercomputer Deep Blue__. Το **next move** λοιπόν του z.log αναφέρεται στην 19η κίνηση (__c4__) του Game 6, η οποία ήταν και η νικητήρια. 
Το επόμενο στοιχείο που έπρεπε τώρα να βρούμε ήταν η ip του μηχανήματος. Σε άλλη περίπτωση απλά θα γράφαμε στο terminal :
```bash
curl -v ifconfig.me
```
αλλά μιας και δεν είμαστε root στο μηχάνημα που τρέχει το Plan Z αυτό δεν είναι δυνατό. Το σχέδιο αυτή την φορά είναι να εκτελέσουμε και πάλι buffer overflow όπως στα 3 και 4 ερωτήματα αλλά αυτή την φορά να εκτελέσουμε __retlib attack__.  Το payload θα είναι παρόμοιο με αυτό των 3 και 4 αλλά αυτή την φορά θα υπολογίσουμε την system έτσι ώστε να εμφανίσουμε την ip.

Για το πως θα βρούμε την system για να εφαρμόσουμε το retlib attack συμβουλευτήκαμε το παρακάτω paper:
https://css.csail.mit.edu/6.858/2014/readings/return-to-libc.pdf

Για να βρούμε το address της libc, θυμηθήκαμε άλλο ένα hint που είψε δωθεί στο 2ο ερώτημα. Ο pico server είχε γίνει build στο __linux02.di.uoa.gr__ ! Τρέχοντας λοιπόν το pico server στον server αυτόν με gdb, και εκτελώντας την εντολή **(gdb) info proc map** βρήκαμε το local libc address.
```bash
0xf7b22000 0xf7cf7000   0x1d5000        0x0 /lib/i386-linux-gnu/libc-2.27.so
```
Για να βρούμε τη διεύθυνση της system, πρέπει να βρούμε μια διεύθυνση συνάρτησης της libc που χρησιμοποιείται από το πρόγραμμά μας και μετά να βρούμε το offset της από τη system (μέσω gdb), το οποίο είναι πάντα σταθερό αφού ο κώδικας της stdlib είναι συνεχόμενος. Έτσι λοιπόν χρησιμοποιήσαμε την setvbuf (- Θέση __$51 από το authentication__) και με τον gdb στα linux02 (μέσω της system) καταφέραμε να υπολογίσουμε το offset της setvbuf ( 0xf7b8a50b - libc_local). 

Έχοντας υπολογίσει τα παραπάνω,  βρήκαμε την **system και την fake_ret** που χρειαζόμασταν με βάση το paper για να πετύχει το ret2lib attackΟπότε σε τελευταία φάση υλοποιήσαμε το payload με την ίδια λογική που το υλοποιήσαμε στο 3 και 4 με την μόνη φιαφορά ότι την εντολή **curl -v ifconfig.me** την περνάμε στο body του payload μετά την fake return που δημιουργήσαμε έτσι ώστε να μπορέσει να γίνει executed.

Ολοκληρώνοντας το POST Request μας καταφέραμε να ανακτήσουμε την public ip του μηχανήματος στο οποίο έτρεχε το __Plan Z__ :
```bash
54.159.81.179
```
__To code λοιπον του Plan-Z είναι: c454.159.81.179__

# Automatisation
Για να τρέξετε αυτόματα τις επιθέσεις για τα ερωτήματα 3 έως 5, αρκεί να έχετε ανοιχτό τον tor browser στο __http://zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion/__ και να τρέξετε στο terminal την εντολή:
```bash
bash ./run.sh
```
Αξίζει να σημειωθεί ότι εμείς τον tor browser τον χρησιμοποιούμε έχοντας τον κάνει install μέσω terminal (**sudo apt install tor**).Οπότε το socat που κάνουμε μετά στον onion server το κάνουμε μέσω port __9050__
Αν τυχόν κάποιο από τα ερωτήματα δεν εμφανίσει αποτέλεσμα λόγω timeout του curl, απλά τρέχτε το πρόγραμμα άλλη μία φορά και θα δουλέψει κανονικά!
Αφού τρέξετε το __run.sh__ στο terminal σας, θα εμφανιστεί το παρακάτω output:
<img src="photos/run_sh.png">


__NOTE:__ πολλές φορές μετά από αρκετά τρεξίματα ο tor κολλάει, οπότε σε πρώτη φάση θα χρειαστεί να κάνετε: **sudo service tor restart**. Στην χείριστη περίπτωση που αυτό δεν δουλέψει απλά κάντε restart το pc σας και θα δουλέψει σίγουρα.
