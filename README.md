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
* [x] Can footnotes be moved between paragraphs correctly before removing page markers, not leaving useless blanks within paragraphs?
* [x] When removing page separators, will it properly handle clearing `/* */` and `/# #/`?
* [x] What about others like `/i i/`?
* [x] What if there are wrap markers and also hyphenated words to join?

Book items:
* [x] Chapter XVIII section numbering is odd, see forum thread.
    * also see below review of book numbering layout
* [x] p002 and forward, sections i, ii, iii etc are marked up as `/# #/` but really they're hanging-indent section headers? Review the structure of the book to determine if these are h3 or what
    * again on p023, similar i., ii.
    * Looking at Chapter I, sec. i., ii., etc, are they h3? They seem to be formatted as hanging indent, so far. The output from the rounds left them as blockquote-rewrap.
* [x] throughout book abbrs like `Dr` and `St` have no `.`; note this when looking for them to add `<abbr>` tags in HTML.
* [x] (TEXT) Chapter I, sections i - iv are hanging indent format
* [x] (HTML) Chapter I, sections i - iv are hanging indent format
* [x] (HTML) footnote 427: change Bishof to Bischof
* [x] (HTML) List of Authorities starting on p. ix: list? How to handle the ” spacing?
* [x] (HTML) ToC on p. xv – table
* [x] (HTML) check poetry on p. 179
* [x] (HTML) p. 215, signature of a blockquote
* [x] (HTML) Index starts on p. 371
* [x] (HTML) p. 376, centered footer block
* [x] (TEXT) p. ix: change “de” to “du” (Hist. du Card. Pie.) (update TN)
* [x] (TEXT) p. 277 (footnote 384): change “de” to “du” (Histoire du Cardinal Pie) (update TN)
* [x] (TEXT) p. 364 (footnote 470): change "Encheiridior" to "Enchiridion"
* [x] (TEXT) update TN to match between files
* [x] (HTML) verify viewport tag addition didn't cause a problem.
    * No problem caused if present; everything is wrong in iPhone Simulator load when it's absent.
* [x] (HTML) Review `<cite>` that got expanded; did italics get expanded too?

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
CHAPTER I                  TODO: hanging indent for i, ii, iii, iv
    i.   1.  2.            1,2,3 below those are just paragraphs.
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
CHAPTER X
    1. 2. 3. 4. 5. 6. 7.
CHAPTER XI
    1. 2. 3. 4. 5.
CHAPTER XII
    2. 3.                     *** MISSING 1. Ignore this.***
    1. 2. 3. 4.
CHAPTER XIII
CHAPTER XIV
CHAPTER XV
    1. 2.
CHAPTER XVI
CHAPTER XVII
CHAPTER XVIII
    I (at start of chapter / subhead)    ** removed **
    I. 1. 2. 3.                      I,II,III,IV,V as h3
    II.                              the others are just paragraph starts.
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
    * Maybe odd but if there is an inferred section 1 ... just leave it alone.
* CHAPTER XII has (2,3) then starts again (1,2,3,4)? Review.
    * This seems okay, like 4 points being made after those earlier sections.
* CHAPTER XVIII has (I) in subhead, then again later. Omit first one?
    * Yes, delete the initial (I).

Things to do:
* Chapters are h2, of course
* Use h3, h4 from there; only h3 should show up in the ToC?
  * Check: h4 should not. If they do, use `<tb>` instead.

### Illustrations ###

None.

### Proofer's notes ###

No notes.

### Joined hyphenated words ###

### Spellcheck ###

* `addressée` per Ngrams, never seen. change to `adressée`

### Transcriber's notes ###

* “Papautè” changed to “Papauté” in multiple places (Histoire de la Papauté)
* p. ix: changed “einem” to “einen” (Sendschreiben an einen Deutschen Bischof)
* p. ix: changed “de” to “du” (Hist. du Card. Pie.)
* p. x: changed “Memoires” to “Mémoires” (Consalvi, Card. Mémoires.)
* p. x: changed “addressée” to “adressée” (Lettre sur le futur Concile Œcuménique adressée)
* p. xi: changed “Allemayne” to “Allemagne” (L’Allemagne religieuse)
* p. xi: changed “Tridentince” to “Tridentinae” (Disputationes Tridentinae)
* p. xi: changed “Rufinium” to “Rufinum” (Ad Rufinum. De Script Eccles.)
* p. xiii: changed “Bischop” to “Bischof” (Kniefall und Fall des Bischof Ketteler)
* p. xiii: changed “Doctrines” to “Doctrinæ” (Vindiciæ Doctrinæ Majorum)
* p. 9: changed “Theol” to “Théol” (Hist. Théol. Positive)
* p. 121: changed “ilustrates” to “illustrates” (Foreign Review illustrates the restraints)
* p. 127: changed “trangressed” to “transgressed” (which has transgressed its limits)
* p. 144: changed “Memoires” to “Mémoires” (Consalvi, Mémoires.)
* p. 200: changed “Religreuses” to “Religieuses” (Encyclopédie des Sciences Religieuses)
* p. 215: changed “inbibed” to “imbibed” (I imbibed in my youth)
* p. 277 (footnote 384): changed “de” to “du” (Histoire du Cardinal Pie)
* p. 279: inserted closing single-quote (God has confided to my care.’”)
* p. 279: changed “advisible” to “advisable” (if they think it advisable)
* p. 301: changed “Altkathliusmus” to “Altkatholicismus” (Schulte, Der Altkatholicismus)
* p. 315: changed “reponse” to “response” (direct response to the question)
* p. 316: changed “apearance” to “appearance” (a very different appearance)
* p. 317: changed “precedure” to “procedure” (of the Roman procedure)
* p. 326: added section V name “LORD ACTON’S SUBMISSION”, from printed page header
* p. 332: changed “Bishof” to “Bischof” (an einen Deutschen Bischof)
* p. 364 (footnote 470): changed “Encheiridior” to “Enchiridion”

### HTML file review ###
The iPhone/iPad simulators can't use `file://` URLs. Start a local web server with `python3 -m http.server` in the project directory and going to `localhost:8000` in Safari on the device. 

* [x] Safari
* [x] Firefox
* [x] Edge
* [x] Chrome
* [x] iPhone simulator
* [x] iPad simulator

### Ebook review ###

### Smooth Reading ###

* [x] remove CSS `abbr { background-color:mistyrose; }` after SR
* Some problematic footnotes (after footnote renumber). These few don't work as a popup in the Kindle app; the link jumps to the footnote page. Weirdly, they're only the first and last in their chapter (and sometimes 2nd).
    * These are post-renumber. Pre-renumber is in ().
        * Chapter 9 footnotes 1, 2, 31 (115, 116, 145)
        * Chapter 15 footnotes 1, 19 (310, 328)
        * Chapter 16 footnotes 1, 2, 12 (329, 330, 340)
    * This same list of footnotes was tagged as broken in first read-through
    * I see no indication why it happens or how to fix. Chalk it up to Kindle format conversion? (shrug)
