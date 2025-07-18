from collections import Counter
import string

cipher = """
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
"""

# --------------------------------------------------------------------
# 1) Frequency count (O(n))
letters_only = [ch for ch in cipher.lower() if ch.isalpha()]
freq_order_cipher = [c for c, _ in Counter(letters_only).most_common()]

# 2) Standard English frequency order
freq_order_english = "etaoinshrdlcumwfgypbvkjxqz"

# 3) Build the substitution table
mapping = {c: freq_order_english[i] for i, c in enumerate(freq_order_cipher)}
table   = str.maketrans(mapping)

# 4) Fast decode
plain_guess = cipher.translate(table)
print(plain_guess)

#we get a bit of comprehensible result, with few tweaks we get
'''Because the practice of the basic movements of kata is
the focus and mastery of self is the essence of Matsubayashi
Ryu karate do, I shall try to elucidate the movements of
the kata according to my interpretation based on forty
years of study.
It is not an easy task to explain each movement and its
significance, and some must remain unexplained. To give
a complete explanation, one would have to be qualified
and inspired to such an extent that he could reach the
state of enlightened mind capable of recognizing soundless
sound and shapeless shape. I do not deem myself the final
authority, but my experience with kata has left no doubt
that the following is the proper application and interpretation.
I offer my theories in the hope that the essence of Okinawan
karate will remain intact'''
