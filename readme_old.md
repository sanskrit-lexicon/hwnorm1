# hwnorm1
Headword normalization for Cologne dictionaries

[830] = 830 cases, statistics extracted from sanhw1.txt

# Origin
https://github.com/sanskrit-lexicon/CORRECTIONS/issue/43

# Convention 1 - Treatment of AnusvAra (आनुस्वार)

##Option 1.1
Treat them as `M` when occuring in between a word (other than the cases where the first member of compound ends with `m`). 
* `caMcalaM`:AP90 (_=caṃcalaṃ_)
* `karaMka`:PUI [19428, \lM\l]

> Dictionaries: AP90

##Option 1.2
Treat them as fifth letter of each varga when in between a word.
* `caYcala`:AP,BEN,BOP,BUR,CAE,CCS,MD,MW,MW72,PW,PWG,SCH,SHS,STC,VCP,WIL,YAT (_=cañcala_) [7881]
* `viyaNga`:MW,PW,PWG [13577]
* `hastirohaRaka`:MW,PW,PWG,VCP [39603]
* `gundra`:BUR,CAE,CCS,MD,MW,MW72,PW,PWG,VCP,WIL,YAT
* `Cinnama`:MW,PW,PWG

> Dictionaries: ACC,AP,BEN,BOP,BUR,CAE,CCS,MCI,MD,MW,MW72,PD,PE,PGN,PW,PWG,SCH,SHS,SKD,SNP,STC,VCP,VEI,WIL,YAT

##Option 1.3
Use `M` at the end of a word to denote neuter gender. 
* `aMSukaM`:AP90,SKD (_=aṃśukaṃ_)
* `CudraM`:AP90,SKD

> Dictionaries: SKD,AP90,BHS,WIL,VCP

##Option 1.4
Use `M` at the end of a word (not to denote neuter gender, but to denote avyayas mostly) where `m` is supposed to be. 
* `anukAmaM`:YAT (_=anukāmaṃ_)
* `anudiSaM`:YAT (_=anudiśaṃ_)

> Dictionaries: PW,PWG,YAT

##Option 1.5
Treat `m` as `M` when occuring in the cases where the first member of compound ends with `m`. 
* `saMgIta`:AP,AP90,CAE,CCS,MD,MW,PUI,PW,PWG,STC (`sam`+`gIta`) (_=saṃgīta_)

> Dictionaries: AP,AP90,CAE,CCS,IEG,MCI,MD,MW,PD,PW,PWG,SCH,SHS,STC,VEI,WIL

##Option 1.6
Treat `m` as fifth letter of a varga when occuring in the cases where the first member of compound ends with `m`. 
* `saNgIta`:BUR,MW72,SHS,VCP,WIL,YAT (`sam`+`gIta`) (_=saṅgīta_)

> Dictionaries: BUR,GRA,GST,IEG,MW72,PGN,SHS,SKD,VCP,YAT

## Standard convention - what we want our dictionaries to be.
1. Convert every inside nasal to `M`.
2. Convert every terminal `M` to `m`.

# Convention 2 - Duplication of letters after 'r'

## Option 2.1
Duplication done

> Dictionaries: SKD,VCP,SHS,WIL,YAT

Notes - PD removed from the list becaue of [this](https://github.com/sanskrit-lexicon/hwnorm1/issues/1#issuecomment-158735408).

## Option 2.2
Duplication not done

> Dictionaries: Rest all dictionaries

## Standard convetion
* No duplication

# Convention 3 - (-at, -vat, -mat = -ant, -vant, -mant)
Convention of writing words which have 't' at end but get converted to 'n' in declention.

## Option 3.1
Keep verb form as 'at'
* `snehayat`:MW72 [830]
* `sTAnivat`:AP,MW,PW,PWG [2942]
* `strImat`:MW,SHS,WIL,YAT [634]

> Dictionaries: SHS,WIL,GST,MW,MW72,PD,MD

## Option 3.2
    Keep verb form as 'ant'
* `sumahant`:CAE,CCS,PW,PWG [424]
* `snehavant`:BEN,CAE,CCS,PW,PWG [1778]
* `sfzwimant`:PW,PWG [474]

> Dictionaries: BEN,CAE,CCS,STC,SCH,BHS,PW,PWG,SCH

Note - Some dictionaries seem to follow two conventions in options 3.1 and 3.2. It will need a closer look.

## Option 3.3
Keep 'vat' / 'mat' 

> Dictionaries: AP,AP90,BOP,BUR,GRA,GST,MD,MW,PD,SHS,VCP,WIL,YAT

## Option 3.4
Keep 'vant' / 'mant' 
 
> Dictionaries: PW,PWG,SCH,STC,CAE,CCS,BEN,BHS

## Standard convention - 'at'

# Convention 4 - Uninflected / inflected forms

## Option 4.1
Inflected form
This would include the usage of "H" and "M" at the end to denote masculine and neuter also.
* `DarmaH`:AP,AP90,BHS
* `putraH`:AP,AP90

> Dictionaries: AP,AP90,SKD,VCP

## Option 4.2
Uninflected form
* `Darma`:ACC,BEN,BHS,BOP,BUR,CAE,CCS,IEG,INM,MD,MW,MW72,PE,PUI,PW,PWG,SCH,STC,VEI
* `putra`:BEN,BOP,BUR,CAE,CCS,GRA,IEG,MD,MW,MW72,PUI,PW,PWG,SCH,STC,VCP,VEI

> Dictionaries: Rest all dictioanries.

## Standard convention
Uninflected form

# Convention 5 -  anusvAra of verb

## Option 5.1
As in dhAtupATha 
* `stanBa`:VCP
* `skanBa`:VCP

> Dictionaries: SKD,VCP,PD

## Option 5.2
With removal of anubandhas and with conversion to fifth letter. 
* `stamB`:AP,BEN,BOP,BUR,CAE,CCS,MD,MW,MW72,PW,PWG,SHS,STC
* `parizwuB`:CAE,CCS,GRA,MW,MW72,PW,PWG,VCP

> Dictionaries: AP,BEN,BOP,BUR,CAE,CCS,MD,MW,MW72,PW,PWG,SHS,STC

## Option 5.3
With removal of anubandha but without conversion to fifth letter - with anusvAra 
* `staMB`:AP90
* `sriMB`:AP90

> Dictionaries: AP90

# Convention 6 - 'f' at end of a word

## Option 6.1
Uses 'ar' instead of 'f' at the end.
* `kartar`:CCS,PW,PWG,SCH
* `pitar`:CCS,PW,PWG

> Dictionaries: CCS,PW,PWG,SCH,KCH

## Option 6.2 
Uses 'f' at the end.
* `kartf`:AP,AP90,BEN,BOP,BUR,CAE,GRA,IEG,INM,MD,MW,MW72,STC
* `pitf`:AP,AP90,BEN,BOP,BUR,CAE,GRA,INM,MD,MW,MW72,PE,SHS,STC,VCP,VEI,WIL,YAT

> Dictionaries: AP,AP90,BEN,BOP,BUR,CAE,GRA,MD,MW,MW72,STC

## Option 6.3
Uses inflected form with 'A' at end 
* `kartA`:PE
* `pitA`:INM,MW,PUI,SKD

> Dictionaries: INM,PUI,SKD

## Standard convention
Use 'f' at the end.

Observations for `mAtA` (`uNAdi tf pratyaya`) are as follows -
* `mAtA`:AP,AP90,MD,MW,MW72,PUI,PW,PWG,SKD,VCP
* `mAtar`:CCS,PW,PWG,SCH
* `mAtf`:AP,AP90,BEN,BOP,BUR,CAE,GRA,IEG,INM,MD,MW,MW72,SHS,STC,VCP,VEI,WIL,YAT

Observations for `kartA` (`tfc pratyaya` with verbs) are as follows -
* `kartA`:PE
* `kartar`:CCS,PW,PWG,SCH
* `kartf`:AP,AP90,BEN,BOP,BUR,CAE,GRA,IEG,INM,MD,MW,MW72,STC

# Convention 7 - (-yas, vas = -yaṁs, vaṁs)

## Option 7.1 
Uses 'vas' at end
* `anASvas`:AP,AP90,GST,MD,MW,MW72,PD,SHS,VCP,WIL,YAT
* `gUrtaSravas`:GRA,MW,PW,PWG

> Dictionaries: AP,AP90,BOP,BUR,CAE,CCS,GRA,MW,MW72,SHS,VCP,WIL,YAT

## Option 7.2
Uses 'AMs' at end
* `pumAMs`:BOP,MD,VEI
* `mAMs`:AP,AP90,CAE,CCS,MD,MW,MW72,PW,PWG

> Dictionaries: BHS,MD,STC

## Option 7.3
Uses 'An' at the end
* `yavIyAn`:PUI,SKD
* `rAjavAn`:PE,PUI,SKD

> Dictionaries: PUI,SKD

## Standard Convention
Use 'vas' at the end.

# Analysis of hypothesis - optionwise

> Here, we would note the most relevant documentation of further discoveries / addition / alteration / whitelist / blacklist of various options.