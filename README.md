# hwnorm1
Headword normalization for Cologne dictionaries

# Origin
https://github.com/sanskrit-lexicon/CORRECTIONS/issue/43

# Convention 1 - Treatment of AnusvAra

##Option 1.1
Treat them as M when occuring in between a word (other than the cases where the first member of compound ends with m). e.g. caMcalaM:AP90 

Dictionaries - AP90,

##Option 1.2
Treat them as fifth letter of each varga when in between a word. e.g. caYcala

Dictionaries - ACC,AP,BEN,BOP,BUR,CAE,CCS,MCI,MD,MW,MW72,PD,PE,PGN,PW,PWG,SCH,SHS,SKD,SNP,STC,VCP,VEI,WIL,YAT

##Option 1.3
Use M at the end of a word to denote neuter gender. e.g. aMSukaM 

Dictionaries - SKD,AP90,BHS,WIL,VCP

##Option 1.4
Use M at the end of a word (not to denote neuter gender, but to denote avyayas mostly) where 'm' is supposed to be. e.g. anukAmaM, anudiSaM etc.

Dictionaries - PW,PWG,YAT

##Option 1.5
Treat m as M when occuring in the cases where the first member of compound ends with m. e.g. saMgIta (sam+gIta)

Dictionaries - AP,AP90,CAE,CCS,IEG,MCI,MD,MW,PD,PW,PWG,SCH,SHS,STC,VEI,WIL

##Option 1.6
Treat m as fifth letter of a varga when occuring in the cases where the first member of compound ends with m. e.g. saNgIta (sam+gIta) 

Dictionaries - BUR,GRA,GST,IEG,MW72,PGN,SHS,SKD,VCP,YAT,

## Standard convention - where we want our dictionaries to normalise to.
1. Convert every inside nasals to 'M'.
2. Convert every terminal 'M' to 'm'.

# Convention 2 - Duplication of letters after 'r'

## Option 2.1
Duplication done

Dictionaries - SKD,VCP,SHS,WIL,YAT

Notes - PD removed from the list becaue of [this](https://github.com/sanskrit-lexicon/hwnorm1/issues/1#issuecomment-158735408).

## Option 2.2
Duplication not done

Dictionaries - Rest all dictionaries

## Standard convetion
No duplication

# Convention 3 - Convention of writing words which have 't' at end but get converted to 'n' in declention.

## Option 3.1
Keep verb form as 'at'

Dictionaries - SHS,WIL,GST,MW,MW72,PD,SCH,MD

## Option 3.2
Keep verb form as 'ant'

Dictionaries - BEN,CAE,CCS,PW,PWG,STC,SCH,PD,MD,BHS

Note - Some dictionaries seem to follow two conventions in options 3.1 and 3.2. It will need a closer look.

## Option 3.3
Keep 'vat' / 'mat' 

Dictionaries - AP,AP90,BOP,BUR,GRA,GST,MD,MW,PD,SHS,VCP,WIL,YAT

## Option 3.4
Keep 'vant' / 'mant' 
 
Dictionaries - PW,PWG,SCH,STC,CAE,CCS,BEN,BHS

# Convention 4 - Uninflected / inflected forms

## Option 4.1
Inflected form
This would include the usage of "H" and "M" at the end to denote masculine and neuter also.

Dictionaries - AP,AP90,SKD,VCP

## Option 4.2
Uninflected form

Dictionaries - Rest all dictioanries.

# Convention 5 -  anusvAra of verb

## Option 5.1
As in dhAtupATha (stanBa)

Dictionaries - SKD,VCP,PD

## Option 5.2
With removal of anubandhas and with conversion to fifth letter. (stamB)

Dictionaries - AP,BEN,BOP,BUR,CAE,CCS,MD,MW,MW72,PW,PWG,SHS,STC

## Option 5.3
With removal of anubandha but without conversion to fifth letter - with anusvAra (staMB)

Dictionaries - AP90

# Convention 6 - 'f' at end of a word

## Option 6.1
Uses 'ar' instead of 'f' at the end. (e.g. kartar )

Dictionaries - CCS,PW,PWG,SCH

Observations for mAtA (uNAdi tf pratyaya) are as follows -
mAtA:AP,AP90,MD,MW,MW72,PUI,PW,PWG,SKD,VCP
mAtar:CCS,PW,PWG,SCH
mAtf:AP,AP90,BEN,BOP,BUR,CAE,GRA,IEG,INM,MD,MW,MW72,SHS,STC,VCP,VEI,WIL,YAT

Observations for kartA (tfc pratyaya with verbs )are as follows -
kartA:PE
kartar:CCS,PW,PWG,SCH
kartf:AP,AP90,BEN,BOP,BUR,CAE,GRA,IEG,INM,MD,MW,MW72,STC


## Option 6.2 
Uses 'f' at the end. (e.g. kartf)

Dictionaries - AP,AP90,BEN,BOP,BUR,CAE,GRA,MD,MW,MW72,STC

## Option 6.3
Uses inflected form with 'A' at end (e.g. kartA)

Dictionaries - INM,PUI,SKD

## Standard convention
Use 'f' at the end.

# Analysis of hypothesis - optionwise

Here, we would note the most relevant documentation of further discoveries / addition / alteration / whitelist / blacklist of various options.

