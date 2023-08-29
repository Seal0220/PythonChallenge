The image contents:
K -> M
O -> Q
E -> G
suggests an encryption rule, which is to shift two positions back.

Depending on the rule, we can get the first translated text:
i"hope"you"didnt"tr{nsl{te"it"|y"h{nd0"th{ts"wh{t"computers"{re"for0"doing"it"in"|y"h{nd"is"inefficient"{nd"th{t)s"why"this"text"is"so"long0"using"string0m{ketr{ns*+"is"recommended0"now"{pply"on"the"url0

As you can see, the strings are still unreadable. That's because there is another rule:
{ -> a
" ->  (space)
| -> b
0 -> .
) -> '
* -> (
+ -> )


Then decrypt the hint:
i hope you didnt translate it by hand. thats what computers are for. doing it by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

(So, we're using str.translate() and str.maketrans())


Following the hint, translate the url of this site (map.html):
ocr.jvon


If you replace 'map.html' with 'ocr.jvon', you will get a file named 'ocr.jvon' with the text written:
Have you ever heard of jvon files !?


This is the wrong answer. You should just replace 'map' with 'ocr', like 'ocr.html'.
Then you'll reach the next level.