## Roman Catholic Opposition to Papal Infallibility - 6111624b0410e ##

This is a [Distributed Proofreaders](http://www.pgdp.net/) post-processing project.

“Roman Catholic Opposition to Papal Infallibility” by Sparrow Simpson, William John

* [DP project page](http://www.pgdp.net/c/project.php?id=projectID6111624b0410e)
* [Forum thread](https://www.pgdp.net/phpBB3/viewtopic.php?t=74833)
* [Good words](good_words.txt)
* [Bad words](bad_words.txt)
* [Project Gutenberg listing]() (not posted yet)

Page references (e.g. `001`) refer to the scan numbers, not the original book's page numbers.

### Things to revisit ###

Guiguts beta items:
* [ ] Can footnotes be moved between paragraphs correctly before removing page markers, not leaving useless blanks within paragraphs?
* [ ] When removing page separators, will it properly handle clearing `/* */` and `/# #/`?
* [ ] What about others like `/i i/`?
* [ ] What if there are wrap markers and also hyphenated words to join?

Book items:
* [ ] Chapter XVIII section numbering is odd, see forum thread.
    * also see below review of book numbering layout
* [ ] p002 and forward, sections i, ii, iii etc are marked up as `/# #/` but really they're hanging-indent section headers? Review the structure of the book to determine if these are h3 or what
* [ ] again on p023, similar i., ii.

### Project manager notes ###

Images from [TIA](https://archive.org/details/a608931100sparuoft).

----

Index pages have been split for proofing.

### Forum notes ###

N/A

### General notes ###

Oddities in the book structure. Lays out like this:
```
PREFACE
LIST OF AUTHORITIES
CONTENTS
CHAPTER I
    i.   1.  2.
    ii.  1.  2.  3.
    iii. 1.  2.
    iv.  1.  2.
CHAPTER II
    1. 2. 3. 4. 5. 6. (i. ii.) 7.
CHAPTER III
    1. 2. 3. 4.
CHAPTER IV
CHAPTER V
    1. 2.
CHAPTER VI
CHAPTER VII
CHAPTER VIII
CHAPTER IX
    1. 2. 3. 4.
CHAPTER X
    1. 2. 3. 4. 5. 6. 7.
CHAPTER XI
    1. 2. 3. 4. 5.
CHAPTER XII
    2. 3.                     *** MISSING 1. ***
    1. 2. 3. 4.
CHAPTER XIII
CHAPTER XIV
CHAPTER XV
    1. 2.
CHAPTER XVI
CHAPTER XVII
CHAPTER XVIII
    I (at start of chapter / subhead)
    I. 1. 2. 3.
    II.
    III.
    IV. 1. 2. 3. 4. 5. 6.
    V.
CHAPTER XIX
    I. II. III.
CHAPTER XX
    I. 1. 2. 3. 4.
    II. 1. 2. 3. 4., 1. 2. 3. 4.
    III.
INDEX
```

Observations:
* CHAPTER XII starts at (2.) so it's missing (1.)
* CHAPTER XII has (2,3) then starts again (1,2,3,4)? Review.
* CHAPTER XVIII has (I) in subhead, then again later. Omit first one?

Things to do:
* Chapters are h2, of course
* Use h3, h4 from there; only h3 should show up in the ToC?
  * Check: h4 should not. If they do, use `<tb>` instead.

### Illustrations ###

### Proofer's notes ###

### Joined hyphenated words ###

### Spellcheck ###

### Transcriber's notes ###

* "Papautè" changed to "Papauté" in multiple places (Histoire de la Papauté)
* p. ix: changed "einem" to "einen" (Sendschreiben an einen Deutschen Bischof)
* p. x: changed "Memoires" to "Mémoires" (Consalvi, Card. Mémoires.)
* p. xi: changed "Allemayne" to "Allemagne" (L'Allemagne religieuse)
* p. xiii: changed "Bischop" to "Bischof" (Kniefall und Fall des Bischof Ketteler)
* p. xiii: changed "Doctrines" to "Doctrinæ" (Vindiciæ Doctrinæ Majorum)
* p. 9: changed "Theol" to "Théol" (Hist. Théol. Positive)
* p. 121: changed "ilustrates" to "illustrates" (Foreign Review illustrates the restraints)
* p. 144: changed "Memoires" to "Mémoires" (Consalvi, Mémoires.)
* p. 200: changed "Religreuses" to "Religieuses" (Encyclopédie des Sciences Religieuses)
* p. 215: changed "inbibed" to "imbibed" (I imbibed in my youth)
* p. 279: changed "advisible" to "advisable" (if they think it advisable)
* p. 301: changed "Altkathliusmus" to "Altkatholismus" (Schulte, Der Altkatholismus)
* p. 315: changed "reponse" to "response" (direct response to the question)
* p. 317: changed "precedure" to "procedure" (of the Roman procedure)

### HTML file review ###
The iPhone/iPad simulators can't use `file://` URLs. Start a local web server with `python3 -m http.server` in the project directory and going to `localhost:8000` in Safari on the device. 

* [ ] Safari
* [ ] Firefox
* [ ] Edge
* [ ] Chrome
* [ ] iPhone simulator
* [ ] iPad simulator

### Ebook review ###

### Smooth Reading ###
