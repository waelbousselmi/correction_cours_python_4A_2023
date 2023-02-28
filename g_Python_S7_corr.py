# -*- coding: utf-8 -*-
"""
Creating WordClouds
Using a text
Using a text in a directory
Pillow
Moving Seed
Fixing Seed
Fonts
Word Exclusions
Masks
Use of Colored images
Article download Wikipedia/Repec and so On
Mask
StyleCloud
Icon name
Palette

@author: Miia Chabot
"""
!pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#First simple example using a text directly taped in Python
# Excluding specific words
text = "Data Science : definition, problématiques et cas d’usage. La Data Science ou science des données est un vaste champ multi-disciplinaire visant à donner du sens aux données brutes. Data Science : définition, champs d’applications et limites actuelles, découvrez tout ce que vous devez savoir sur ce domaine complexe, devenu un enjeu prioritaire dans les entreprises de toutes les industries. Pour définir la Data Science de la plus simple des façons, il s’agit de l’extraction d’informations exploitables à partir de données brutes. Ce champ multi-disciplinaire a pour but principal d’identifier des tendances, des motifs, des connexions et des corrélations dans les larges ensembles de données. La science des données englobe une large variété d’outils et de techniques telles que la programmation informatique, l’analyse prédictive, les mathématiques, les statistiques ou l’intelligence artificielle. Désormais, la Data Science inclut aussi les algorithmes de Machine Learning. De nos jours, presque toutes les entreprises affirment pratiquer la Data Science sous une forme ou une autre. Cependant, les méthodes et approches employées peuvent varier d’une organisation à l’autre. Il devient donc très compliqué d’offrir une définition précise de la Data Science. D’autant que de nouvelles technologies apparaissent sans cesse et transforment continuellement ce domaine. Ainsi, pour définir la science des données, la meilleure question à se poser est: pourquoi ?. Pourquoi la science des données ? Si la Data Science connaît un essor fulgurant dans tous les secteurs d’activité, c’est parce que l’humanité génère de plus en plus de données. Entre 2011 et 2013, en seulement deux ans, le volume mondial de données a été multiplié par 9. Et cette explosion du Big Data n’a pas ralenti depuis. D’ici la fin de l’année 2020, le volume total de données à l’échelle de la planète devrait atteindre 44 zettabytes contre moins de 5 zettabytes en 2013. Comment expliquer ce phénomène ? Plusieurs technologies émergentes génèrent des données. C’est le cas des objets connectés, des réseaux sociaux, des smartphones, ou des moteurs de recherche web. Or, toutes ces données offrent des opportunités inouïes pour les entreprises de toutes les industries, les institutions de recherche ou le secteur public. C’est la raison pour laquelle les données sont souvent considérées comme le pétrole du XXIème siècle. En s’appuyant sur ces découvertes, il est possible de créer de nouveaux produits et services innovants, de résoudre des problèmes concrets, d’améliorer ses performances comme jamais auparavant. La Data Science permet de prendre des décisions basées sur les données, plutôt que sur une simple intuition. Ainsi, elle révolutionne notre quotidien et nous permet de s’ouvrir à de nouveaux horizons. En bref, la data science représentera une science incontournable du monde demain ! Comment fonctionne la data science ? La Data Science couvre une large variété de disciplines et de champs d’expertise. Son but reste toutefois de donner du sens aux données brutes. Pour y parvenir, les Data Scientists doivent posséder des compétences en ingénierie des données, en mathématiques, en statistique, en informatique et en Data Visualization. Ces compétences leur permettront de parcourir les vastes ensembles de données brutes pour en dégager les informations les plus pertinentes et les communiquer aux décideurs de leurs organisations. Les Data Scientists exploitent également l’intelligence artificielle, et plus particulièrement le Machine Learning et le Deep Learning. Ces technologies sont utilisées pour créer des modèles et réaliser des prédictions en utilisant des algorithmes et diverses techniques. Dans un premier temps, les données doivent être collectées, extraites à partir de différentes sources. Il s’agit ensuite de les entreposer dans une Data Warehouse, de les nettoyer, de les transformer afin qu’elles puissent être analysées. L’étape suivante est celle du traitement des données, par le biais du Data Mining (forage de données), du clustering, de la classification ou de la modélisation. Les données sont ensuite analysées à l’aide de techniques comme l’analyse prédictive, la régression ou le text mining. Enfin, la dernière étape consiste à communiquer les informations dégagées par le biais du reporting, du dashboarding ou de la Data Visualization. Les cas d'usage et applications Les cas d’usage de la Data Science sont aussi nombreux que variés. Cette technologie est utilisée pour assister la prise de décision en entreprise, mais permet aussi l’automatisation de certaines tâches. Elle est utilisée à des fins de détection d’anomalies ou de fraude. La science des données permet aussi la classification, par exemple pour trier automatiquement les emails dans votre boîte. Elle permet aussi la prédiction, par exemple pour les ventes ou les revenus. En l’utilisant, il est possible de détecter des tendances ou des patterns dans les ensembles de données. La Data Science se cache aussi derrière les technologies de reconnaissance faciale, vocale ou textuelle. Elle alimente aussi les moteurs de recommandations capables de vous suggérer des produits ou du contenu en fonction de vos préférences. D’un secteur d’activité à l’autre, la Data Science est exploitée de différentes manières. Dans le domaine de la santé, les données permettent aujourd’hui de mieux comprendre les maladies, de recourir à la médecine préventive, d’inventer de nouveaux traitements ou d’accélérer les diagnostics. En logistique, la Data Science aide à optimiser les itinéraires et les opérations internes en temps réel en tenant compte de facteurs comme la météo ou le trafic. Dans la finance, elle permet d’automatiser le traitement des données d’accords de crédit grâce au Traitement Naturel du Langage (Vous n’êtes pas familier avec ce concept, découvrez le NLP dans notre article dédié) ou de détecter la fraude grâce au Machine Learning. Les entreprises de retail l’utilisent pour le ciblage publicitaire et le marketing personnalisé. Les moteurs de recommandations, basés sur l’analyse des préférences du consommateur, sont utilisés par Google pour son moteur de recherche web, par les plateformes de streaming comme Netflix ou Spotify, et par les entreprises de e-commerce comme Amazon. Les entreprises de cybersécurité se tournent vers l’IA et la science des données pour découvrir de nouveaux malwares au quotidien. Même les voitures autonomes reposent sur la Data Science et l’analyse prédictive pour ajuster leur vitesse, éviter les obstacles et les changements de voie dangereux ou choisir l’itinéraire le plus rapide."

exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots, max_words = 50).generate(text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show();


#Advanced Python WordCloud using pillow

!pip install pillow
import numpy as np 
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude 

# Download the Shakespeare text from the desktop
file=open("desktop/WC/romeo.txt",'r')
text=file.read()

# Create the WordCloud
canvas_width=1920
canvas_height=1080 
#generate wordcloud
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)

#save the output wordcloud in png format
plt.imshow(wordcloud, interpolation='bilinear')
 #show the image output 
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 

# By default wordcloud generates random patterns but you can fix the seed
#generate wordcloud
# replace 1 with any number to get different result
canvas_width=1920
canvas_height=1080 
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
wordcloud = WordCloud(random_state=1).generate(text) 
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 

#White font and excluding the word THY
canvas_width=1920
canvas_height=1080 
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
stopwords = set(STOPWORDS)
stopwords.add("thy")
wordcloud = WordCloud(stopwords=stopwords,background_color='white',random_state=1,colormap='hot',max_font_size=800,min_font_size=20,width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 

#Use Masks
romeo_mask= np.array(Image.open("desktop/WC/romeo1.jpg"))
#read image
wc = WordCloud(mask=romeo_mask,colormap='inferno',random_state=5,max_font_size=50,min_font_size=0)
#generate wordcloud with text data
wc.generate(text)
#save image
wc.to_file("masked_wc.jpg")
#show image
plt.figure(figsize = (10, 10), facecolor=None)
plt.tight_layout(pad = 0)
plt.imshow(wc, interpolation='bilinear')
 
#off axis on image
plt.show() #show image


#Use of colored image for your mask so that the Cloud adapts to it
image = np.array(Image.open("desktop/WC/romeo2.jpg"))
image_mask = image.copy()
image[image_mask.sum(axis=2) == 0] = 255
edges = np.mean([gaussian_gradient_magnitude(image[:, :, i] / 255., 2) for i in range(3)], axis=0)
image_mask[edges > .1] = 255
wc = WordCloud(background_color='black', mask=image_mask, mode='RGBA')
wc.generate(text)
image_colors = ImageColorGenerator(image)
wc.recolor(color_func=image_colors)
plt.figure(figsize = (10, 10), facecolor=None)
plt.figure(figsize=(10, 10))
plt.tight_layout(pad = 0)
plt.imshow(wc, interpolation="bilinear")
wc.to_file("color_masked_wordcloud.png")

#My paper Word cloud
#in blue
file=open("Desktop/WC/test.txt",'r')
text=file.read()
canvas_width=1920
canvas_height=1080 
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'dont','ainsi','après','une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots, max_words = 50).generate(text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show();

#colormap hot
file=open("desktop/WC/test.txt",'r')
text=file.read()
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
stopwords = ['d','nombre','nécessaire','cet','grande', 'très', 'cherche','article','ont','favorisent','nous','cependant','partie','dépend', 'standard','existants', 'nos', 'théoriques','son','avec','celles', 'davantage', 'étudier', 'lequel', 'bancaire','aide', 'impliquent', 'dites', 'désormais', 'telles','tels', 'tout','avec', 'travaux', 'fournir','relativement','autres','obtenu','termes','cherche''telles','Reingold','soutenir','idée','ne', 'disposent', 'travail','différentes','concerne','qu', 'établissement','établissements','relations','certains','pendant', 'même', 'dont','ils','elles', 'cette','été', 'où','ainsi','après', 'leurs', 'peut', 'avant','entre', 'on','du', 'théorique','cet','de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wordcloud = WordCloud(stopwords=stopwords,background_color='white',random_state=1,colormap='hot',max_font_size=800,min_font_size=20,width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show()


#colormap summer/binary/gist_yarg/gist_gray/gray/bone/pink/spring/autumn/winter/cool/Wistia/afmhot/gist_heat/cooper
#https://matplotlib.org/stable/gallery/color/colormap_reference.html
#https://matplotlib.org/stable/gallery/color/named_colors.html
file=open("desktop/WC/test.txt",'r')
text=file.read()
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
stopwords = ['d','nombre','nécessaire','cet','grande', 'très', 'cherche','article','ont','favorisent','nous','cependant','partie','dépend', 'standard','existants', 'nos', 'théoriques','son','avec','celles', 'davantage', 'étudier', 'lequel', 'bancaire','aide', 'impliquent', 'dites', 'désormais', 'telles','tels', 'tout','avec', 'travaux', 'fournir','relativement','autres','obtenu','termes','cherche''telles','Reingold','soutenir','idée','ne', 'disposent', 'travail','différentes','concerne','qu', 'établissement','établissements','relations','certains','pendant', 'même', 'dont','ils','elles', 'cette','été', 'où','ainsi','après', 'leurs', 'peut', 'avant','entre', 'on','du', 'théorique','cet','de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wordcloud = WordCloud(stopwords=stopwords,background_color='aliceblue',random_state=1,colormap='twilight',max_font_size=800,min_font_size=20,width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show()

#Add a Mask
mask= np.array(Image.open("desktop/WC/AF.jpeg"))
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
stopwords = ['d','nombre','nécessaire','cet','grande', 'très', 'cherche','article','ont','favorisent','nous','cependant','partie','dépend', 'standard','existants', 'nos', 'théoriques','son','avec','celles', 'davantage', 'étudier', 'lequel', 'bancaire','aide', 'impliquent', 'dites', 'désormais', 'telles','tels', 'tout','avec', 'travaux', 'fournir','relativement','autres','obtenu','termes','cherche''telles','Reingold','soutenir','idée','ne', 'disposent', 'travail','différentes','concerne','qu', 'établissement','établissements','relations','certains','pendant', 'même', 'dont','ils','elles', 'cette','été', 'où','ainsi','après', 'leurs', 'peut', 'avant','entre', 'on','du', 'théorique','cet','de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wordcloud = WordCloud(stopwords=stopwords,mask=mask,background_color='aliceblue',random_state=1,colormap='twilight',max_font_size=800,min_font_size=20,width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show()

#Create a cloud from an article on a webpage
!pip install Article
!pip install newspaper3k
from newspaper import Article
article = Article('https://fr.wikipedia.org/wiki/Cryptomonnaie')
article.download()
article.parse()

article.text

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud()
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

from wordcloud import STOPWORDS

STOPWORDS = ['d','nombre','nécessaire','cet','grande', 'l', 'fait','article', 'soit', 'mais', 'non','modifier','pas', 'sa', 'selon', 'donc', 'mai', 'peu','pas','très', 'cherche','article','ont','favorisent','nous','cependant','partie','dépend', 'standard','existants', 'nos', 'théoriques','son','avec','celles', 'davantage', 'étudier', 'lequel', 'bancaire','aide', 'impliquent', 'dites', 'désormais', 'telles','tels', 'tout','avec', 'travaux', 'fournir','relativement','autres','obtenu','termes','cherche''telles','Reingold','soutenir','idée','ne', 'disposent', 'travail','différentes','concerne','qu', 'établissement','établissements','relations','certains','pendant', 'même', 'dont','ils','elles', 'cette','été', 'où','ainsi','après', 'leurs', 'peut', 'avant','entre', 'on','du', 'théorique','cet','de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=STOPWORDS, max_font_size=256,
               random_state=42, width=500, height=500)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#Add MASK
mask= np.array(Image.open("desktop/WC/cl.jpg"))
STOPWORDS = ['d','nombre','nécessaire','cet','de','code','grande', 'l', 'fait','d','une','depuis','article', 'soit', 'mais', 'non','modifier','pas', 'sa', 'selon', 'donc', 'mai', 'peu','pas','très', 'cherche','article','ont','favorisent','nous','cependant','partie','dépend', 'standard','existants', 'nos', 'théoriques','son','avec','celles', 'davantage', 'étudier', 'lequel', 'bancaire','aide', 'impliquent', 'dites', 'désormais', 'telles','tels', 'tout','avec', 'travaux', 'fournir','relativement','autres','obtenu','termes','cherche''telles','Reingold','soutenir','idée','ne', 'disposent', 'travail','différentes','concerne','qu', 'établissement','établissements','relations','certains','pendant', 'même', 'dont','ils','elles', 'cette','été', 'où','ainsi','après', 'leurs', 'peut', 'avant','entre', 'on','du', 'théorique','cet','de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
wc = WordCloud(background_color='mintcream',stopwords=STOPWORDS, mask=mask,colormap='cubehelix',random_state=1,max_font_size=50,min_font_size=0)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#Downloading a scientific article from ideas/repec.org
!pip install Article
!pip install newspaper3k

from newspaper import Article
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
import numpy as np
from PIL import Image
import os
import xlrd
cwd = os.getcwd()
cwd

article = Article('https://ideas.repec.org/a/eee/jbrese/v101y2019icp70-82.html')
article.download()
article.parse()

article.text

#Black Font NO stopwords
wc = WordCloud()
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#Black Font with stopwords no special size
STOPWORDS = ['the','of', 'this', 'in','or','item','are','as','want','abstract','jbusres','adding','its', 'our','elsevier', 'contact','you','using','about','bibliographic', 'download', 'help','by','a', 'title', 'citations', 'please', 'registered', 'please', 'for', 'title', 'if','that','http','authors','to','and','we', 'correct','author', 'correction','may','it', 'general']
wc = WordCloud(stopwords=STOPWORDS)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()


#White font with special size & number of characters

STOPWORDS = ['the','of', 'this', 'in','or','item','are','as','want','abstract','jbusres','adding','its', 'our','elsevier', 'contact','you','using','about','bibliographic', 'download', 'help','by','a', 'title', 'citations', 'please', 'registered', 'please', 'for', 'title', 'if','that','http','authors','to','and','we', 'correct','author', 'correction','may','it', 'general']
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=STOPWORDS, max_font_size=256,
               random_state=42, width=500, height=500)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

# The same in black
STOPWORDS = ['the','of', 'this', 'in','or','item','are','as','want','abstract','jbusres','adding','its', 'our','elsevier', 'contact','you','using','about','bibliographic', 'download', 'help','by','a', 'title', 'citations', 'please', 'registered', 'please', 'for', 'title', 'if','that','http','authors','to','and','we', 'correct','author', 'correction','may','it', 'general']
wc = WordCloud(max_words=2000,
               stopwords=STOPWORDS, max_font_size=256,
               random_state=42, width=500, height=500)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#Adding a cloud mask
mask= np.array(Image.open("desktop/WC/heart.jpg"))
STOPWORDS = ['the','of', 'this', 'in','or','item','are','as','RePEc','want','abstract','jbusres','adding','its', 'our','elsevier', 'contact','you','using','about','bibliographic', 'download', 'help','by','a', 'title', 'citations', 'please', 'registered', 'please', 'for', 'title', 'if','that','http','authors','to','and','we', 'correct','author', 'correction','may','it', 'general']
wc = WordCloud(background_color="white",colormap="ocean",max_words=2000,
               stopwords=STOPWORDS, mask=mask,max_font_size=256,
               random_state=42, width=500, height=500)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()


#COVID 

article = Article('https://en.wikipedia.org/wiki/COVID-19_pandemic')
article.download()
article.parse()

article.text
mask= np.array(Image.open("desktop/WC/virus.jpg"))
STOPWORDS = ['the','of', 'this', 'in','or','from','on', 'have','item','are','as','RePEc','want','abstract','jbusres','adding','its', 'our','elsevier', 'contact','you','using','about','bibliographic', 'download', 'help','by','a', 'title', 'citations', 'please', 'registered', 'please', 'for', 'title', 'if','that','http','authors','to','and','we', 'correct','author', 'correction','may','it', 'general']
wc = WordCloud(background_color="white",colormap="winter",max_words=2000,
               stopwords=STOPWORDS, mask=mask)
wc.generate(article.text)
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#Stylecloud
!pip install stylecloud
import stylecloud
from IPython.display import Image
import os
import xlrd
cwd = os.getcwd()
cwd



#Always re enter the path!!!
os.chdir('C:/Users/Miia CHABOT/Desktop/WC')
#Basic_ the image is in Desktop/WC
stylecloud.gen_stylecloud(file_path = "rom.txt")
#Comment
stylecloud.gen_stylecloud(file_path = "rom.txt", icon_name= "fas fa-comment",size=(1024, 512))
#gradient
stylecloud.gen_stylecloud(file_path='bayle5.txt',
                    icon_name='fas fa-comment',
                    palette='colorbrewer.diverging.Spectral_11',
                    background_color='black',gradient='horizontal',
                                                         )
#IronManColors
stylecloud.gen_stylecloud(file_path='rom.txt',
                          icon_name='fas fa-comment',
                          colors=['#ffdb4d', '#ff0000', '#e74c3c'],
                          background_color='black',
                          )
#To Remove words
my_custom_stopwords = {"Tony", "Pepper", "Iron", "Stark"}
stopwords=my_custom_stopwords


#Bookreader
bookreader = stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          size = 1028,                         
                          icon_name = "fas fa-book-reader",
                          palette='colorbrewer.sequential.Blues_5',
                          background_color ='white')

#Appstorelogo
appstorelogo = stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          icon_name = "fab fa-app-store-ios",
                          size = 1028,
                          palette='colorbrewer.sequential.YlOrBr_3',
                          background_color ='white')


#apple

apple = stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          icon_name = "fab fa-apple",
                          size = 1028,
                          palette='colorbrewer.sequential.Blues_5',
                          background_color ='white')

#bell

bell = stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          icon_name = "fas fa-bell",
                          size = 1028,
                          palette='colorbrewer.sequential.Blues_5',
                          background_color ='white')



#christmas

christmas= stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          icon_name = "fas fa-gifts",
                          size = 1028,
                          palette='colorbrewer.sequential.Blues_5',
                          background_color ='white')


#Another.txt dealing with python and with python icon
os.chdir('C:/Users/Miia CHABOT/Desktop/WC')
#Basic_ the image is in Desktop/WC
stylecloud.gen_stylecloud(file_path = "rom.txt")

python= stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          icon_name = "fab fa-python",
                          size = 1028,
                          palette='colorbrewer.sequential.Blues_5',
                          background_color ='white')


python= stylecloud.gen_stylecloud(
                          file_path='rom.txt',
                          icon_name = "fas fa-brain",
                          size = 1028,
                          palette='colorbrewer.diverging.RdYlBu_10',
                          background_color ='white')


python= stylecloud.gen_stylecloud(
                          file_path='game.txt',
                          icon_name = "fas fa-car-side",
                          size = 1028,
                          palette='colorbrewer.diverging.Spectral_11',
                          background_color ='white')
#List of FONTS 
#https://fontawesome.com/v5.15/icons?d=gallery&p=2
#List of Colors for palette
#https://jiffyclub.github.io/palettable/colorbrewer/
                         
          