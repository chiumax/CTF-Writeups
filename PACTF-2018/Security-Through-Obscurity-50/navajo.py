#Python 3.6.0


text = "Tązhii, Łį́į́ʼ, Dzeeh Mąʼii, Dibé yázhí, Wóláchííʼ, Tłʼízí Tin, Dibé Mósí, Łį́į́ʼ, Dzeeh, Dibé, Tązhii, Dzeeh, Gah, Neeshchʼííʼ, Dzeeh, Béésh dootłʼizh"
di = {}

di['A'] = "Wóláchííʼ"
di['B'] = "Shash"
di['C'] = "Mósí"
di['D'] = "Bįįh"
di['E'] = "Dzeeh"
di['F'] = "Mąʼii"
di['G'] = "Tłʼízí"
di['H'] = "Łį́į́ʼ"
di['I'] = "Tin"
di['J'] = "Téliichoʼí"
di['K'] = "Tłʼízí-yázhí"
di['L'] = "Dibé-yázhí"
di['M'] = "Naʼastsʼǫǫsí"
di['N'] = "Neeshchʼííʼ"
di['O'] = "Néʼéshjaaʼ"
di['P'] = "Bisóodi"
di['Q'] = "kʼaaʼ yeiłtįįh"
di['R'] = "Gah"
di['S'] = "Dibé"
di['T'] = "Tązhii"
di['U'] = "Nóódaʼí"
di['V'] = "Akʼehdidlíní"
di['W'] = "Dlǫ́ʼii"
di['X'] = "Ałnáʼázdzoh"
di['Y'] = "Tsáʼásziʼ"
di['Z'] = "Béésh dootłʼizh"

di['1'] = "tʼááłáʼí"
di['2'] = "naaki"
di['3'] = "tááʼ"
di['4'] = "dį́į́ʼ"
di['5'] = "ashdlaʼ"
di['6'] = "hastą́ą́"
di['7'] = "tsostsʼid"
di['8'] = "tseebíí"
di['9'] = "náhástʼéí"
di['0'] = "ádin"
di['0'] = "názbąs"

print(di)

text = text.replace(" yázhí","-yázhí")

for c,a in di.items():
	text = text.replace(a,c)
	
text = text.replace(" ",'')

print(text)

# IFTWK3TUEBDTUIBAK5SWY3BAMRXW4ZJBEAQFOZJANNXGK5ZAPFXXKIDXN52WYZBAMJSSAYJAOBSXEZTFMN2CAY3BNZSGSZDBORSSAZTPOIQHI2DJOMQG22LTONUW63ROEAQFS33VEB3WS3DMEBZW633OEBZGKY3FNF3GKIDBNYQGK3TDOJ4XA5DFMQQGE3DPMIXCAICUNBSSA43QMFRWK4ZAO5UWY3BAMJSSA2LOEBYG643JORUW63TTEAZSAYLOMQQDMLRAEBDW633EEBWHKY3LFYQCA2DUORYDULZPMN2GMLTHOJSWOZ3FOJXGC5LUFZRW63JPONQW2LLUONXS243FNZSHGLLINFZS24TFM5QXEZDT
