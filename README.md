# AnkiKanjiBrowser
A grid-like Kanji browser add-on for Anki (2.0)

This add-on helps studying kanji by arranging them in a grid-like pattern.
Additionally, it allows filtering by JLPT-Levels and Jōyō-Kanji grades, and add custom tags to selected kanji.
For example, you could filter out the Grade 2 Kanji and then add a tag to a subset of them that you want to study later.

### Important Note ###

This add-on does **not** provide the kanji decks itself. It is meant to be used as a supplementary tool. 
I highly suggest adding [this](https://ankiweb.net/shared/info/798002504) deck.

### How it works ###

If you are using the deck linked above, you do not have to do anything more. If not, you may have to change some fields/add tags.

Kanji browser will search for notes which contain a "Kanji"-field, and show it in the grid. If the field contains more than one
letter/kanji, only the first one is shown. Notes with an empty "Kanji"-field are not shown. 

The JLPT and Jōyō filtering is based on tags. For example, in order for a kanji to be listed as a JLPT-N5 kanji, 
it must have the "JLPT.N5" tag. For Jōyō-kanji use "grade1" (and so on) tags.

### Advanced features ###

You can add custom filter tags that are shown in the dropdown-menu in the browser by editing `config.py`.
There, you can also deactivate the font that is used (I use the awesome [Source Han Serif](https://github.com/adobe-fonts/source-han-serif) Font by Adobe).
This may be neccessary if the kanji browser is responding slowly.
