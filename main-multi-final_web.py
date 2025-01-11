# _____________________اضافه کردن کتابخانه های مورد نیاز و اضافه کردن الگوریتم____________
import pandas as pd
from sklearn import model_selection, preprocessing, naive_bayes
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib
from bs4 import BeautifulSoup
import requests
import re
# ____________________________تعریف آرایه ها برای نرمال سازی ___________________
junk = ["از ", " الاّ ", " الی ", " اندر ", " با  ", " بدون ", " بر ", " برای ", " به ", " بهر ", " بی ", " تا ", " جز ", " چون ", " در ", " ضد ", " علیه ", " غیر ", " غیراز ", "به‎ غیراز", "به ‎مجرد", "به‎محض",
        "به‎عنوان ", "به‎مثابه ", " به‎وسیله‎ی ", " به‎ واسطه‎ ", "دربرابر", " درقبال ",
        " درمیان ", " ازجمله ", " درخصوص ", " اگر ", " اما ", "باری", " پس ", " تا ",
        " چه ", " خواه ", " زیرا ", "که", "لیکن", " یز ", " و ", " ولی ", " هم ", " یا ", "آن‌جاکه",
        "آن‌گاه که", "از آن‌جا که", "از آن‌که", "ازاین‌روی", " ازبس ", "ازبس‌که", " بس‌که ",
        "ازبهر آن‌که", "اکنون که", "چنان‌چه", "اگرچه", "الاّ این‌که", "بااین‌حال", "باوجوداین",
        "به‌شرط آن‌که", "چنان‌که", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "%", "$", "^", "&", "*"]
word_normal = ["اا", "یی", "تت", "دد", "خخ", "نن", "کک", "گگ", "هه",
               "سس", "لل", "غغ", "جج", "وو", "مم", "فف", "قق", "شش", "رر",
               "بب", "پپ", "زز", "عع", "ذذ", "دد", "طط", "ظظ",
               "آآ", "صص", "ضض", "حح", "ژژ", "چچ", "نن", "يي", "  "]
emoji_normal = ["&quot;", "&raquo;", ":)", ":(",
                ":((", ":))", "-*", "=))", "&zwnj;",
                "&hellip;", "&infin;", ":-*", "&rlm;",
                "&nbsp;", "@};-", ":-*", "\u200c"]
marks_normal = ["??", "ـــ", "!!", "..."]
tobechanged_normal = ["http://", "www.", "cloob", "instagram",
                      "https://", "t.me", "telegram", "/joinchat",
                      ".com", ".ir", "insta"]

# ______________________تعریف توابع نرمال سازی ____________________________


def normalizerword(mylst):
    retrnlst = []
    for snt in mylst:
        # print(snt)
        for n in word_normal:
            if (n == "اا"):
                while n in snt:
                    snt = snt.replace(n, "ا")
            elif (n == "بب"):
                while n in snt:
                    snt = snt.replace(n, "ب")
            elif (n == "پپ"):
                while n in snt:
                    snt = snt.replace(n, "پ")
            elif (n == "تت"):
                while n in snt:
                    snt = snt.replace(n, "ت")
            elif (n == "چچ"):
                while n in snt:
                    snt = snt.replace(n, "چ")
            elif (n == "ذذ"):
                while n in snt:
                    snt = snt.replace(n, "ذ")
            elif (n == "رر"):
                while n in snt:
                    snt = snt.replace(n, "ر")
            elif (n == "زز"):
                while n in snt:
                    snt = snt.replace(n, "ز")
            elif (n == "ژژ"):
                while n in snt:
                    snt = snt.replace(n, "ژ")
            elif (n == "صص"):
                while n in snt:
                    snt = snt.replace(n, "ص")
            elif (n == "ضض"):
                while n in snt:
                    snt = snt.replace(n, "ض")
            elif (n == "عع"):
                while n in snt:
                    snt = snt.replace(n, "ع")
            elif (n == "ظظ"):
                while n in snt:
                    snt = snt.replace(n, "ظ")
            elif (n == "طط"):
                while n in snt:
                    snt = snt.replace(n, "ط")
            elif (n == "یی"):
                while n in snt:
                    snt = snt.replace(n, "ي")
            elif (n == "دد"):
                while n in snt:
                    snt = snt.replace(n, "د")
            elif (n == "خخ"):
                while n in snt:
                    snt = snt.replace(n, "خ")
            elif (n == "نن"):
                while n in snt:
                    snt = snt.replace(n, "ن")
            elif (n == "کک"):
                while n in snt:
                    snt = snt.replace(n, "ک")
            elif (n == "گگ"):
                while n in snt:
                    snt = snt.replace(n, "گ")
            elif (n == "هه"):
                while n in snt:
                    snt = snt.replace(n, "ه")
            elif (n == "سس"):
                while n in snt:
                    snt = snt.replace(n, "س")
            elif (n == "لل"):
                while n in snt:
                    snt = snt.replace(n, "ل")
            elif (n == "غغ"):
                while n in snt:
                    snt = snt.replace(n, "غ")
            elif (n == "جج"):
                while n in snt:
                    snt = snt.replace(n, "ج")
            elif (n == "وو"):
                while n in snt:
                    snt = snt.replace(n, "و")
            elif (n == "مم"):
                while n in snt:
                    snt = snt.replace(n, "م")
            elif (n == "فف"):
                while n in snt:
                    snt = snt.replace(n, "ف")
            elif (n == "قق"):
                while n in snt:
                    snt = snt.replace(n, "ق")
            elif (n == "شش"):
                while n in snt:
                    snt = snt.replace(n, "ش")
            elif (n == "يي"):
                while n in snt:
                    snt = snt.replace(n, "ي")
            elif (n == "سس"):
                while n in snt:
                    snt = snt.replace(n, "س")
            elif (n == "  "):
                while n in snt:
                    snt = snt.replace(n, " ")
        retrnlst.append(snt)
    return retrnlst


def tobechanged(mylst):
    retrnlst = []
    for snt in mylst:
        # print(snt)
        for n in tobechanged_normal:
            if (n == "http://"):
                snt = snt.replace(n, "http:// ")
            elif (n == "www."):
                snt = snt.replace(n, "www. ")
            elif (n == "cloob"):
                snt = snt.replace(n, "cloob ")
            elif (n == "instagram"):
                snt = snt.replace(n, "instagram ")
            elif (n == "https://"):
                snt = snt.replace(n, "https:// ")
            elif (n == "t.me"):
                snt = snt.replace(n, "t.me ")
            elif (n == "/joinchat"):
                snt = snt.replace(n, " /joinchat ")
            elif (n == ".com"):
                snt = snt.replace(n, " .com ")
            elif (n == ".ir"):
                snt = snt.replace(n, " .ir ")
        retrnlst.append(snt)
    return retrnlst


def normalizeremoji(mylst):
    retrnlst = []
    for snt in mylst:
        # print(snt)
        for n in emoji_normal:
            if (n == "&quot;"):
                snt = snt.replace(n, "")
            elif (n == "&raquo;"):
                snt = snt.replace(n, "")
            elif (n == ":)"):
                snt = snt.replace(n, "")
            elif (n == "\u200c"):
                snt = snt.replace(n, "")
            elif (n == ":("):
                snt = snt.replace(n, "")
            elif (n == ":(("):
                snt = snt.replace(n, "")
            elif (n == ":))"):
                snt = snt.replace(n, "")
            elif (n == "-*"):
                snt = snt.replace(n, "")
            elif (n == "=))"):
                snt = snt.replace(n, "")
            elif (n == "&zwnj;"):
                snt = snt.replace(n, "")
            elif (n == "&hellip;"):
                snt = snt.replace(n, "")
            elif (n == "&infin;"):
                snt = snt.replace(n, "")
            elif (n == ":-*"):
                snt = snt.replace(n, "")
            elif (n == "&rlm;"):
                snt = snt.replace(n, "")
            elif (n == "&nbsp;"):
                snt = snt.replace(n, "")
            elif (n == "@};-"):
                snt = snt.replace(n, "")
            elif (n == ":-*"):
                snt = snt.replace(n, "")
        retrnlst.append(snt)
    return retrnlst


def normalizermarks(mylst):
    retrnlst = []
    for snt in mylst:
        # print(snt)
        for n in marks_normal:
            if (n == "??"):
                while n in snt:
                    snt = snt.replace(n, "?")
            elif (n == "ـــ"):
                while n in snt:
                    snt = snt.replace(n, "ـ")
            elif (n == "!!"):
                while n in snt:
                    snt = snt.replace(n, "!")
            elif (n == "..."):
                while n in snt:
                    snt = snt.replace(n, ".")
        retrnlst.append(snt)
    return retrnlst


def replacee(mylst):
    j = ""
    retrnlst = []
    for snt in mylst:
        # print(snt)
        for j in junk:
            if j in snt:
                snt = snt.replace(j, " ")
                # print(snt)
                # sleep(3)
        retrnlst.append(snt)
    return retrnlst


def check_predict(com):

    print("Your input is: ", [com])
    new_cmt = normalizeremoji([com])
    new_cmt2 = replacee(new_cmt)
    new_cmt3 = normalizerword(new_cmt2)
    new_cmt4 = tobechanged(new_cmt3)
    new_cmt5 = normalizermarks(new_cmt4)
    print("Normalized input is: ", new_cmt5)
    vect = cv.transform(new_cmt5).toarray()
    cp1 = clf.predict(vect)
    print("Classifier prediction: ", cp1)
    return cp1

# ____________________خواندن داده از اکسل و آماده سازی و نرمال سازی داده ها برای یادگیری____________________


df = pd.read_excel(
    'G:\Educational\JavaScript\Files\python\dataset-example.xlsx')
col = ['label', 'body']
df = df[col]
df.columns = ['label', 'body']
df_x = df['body']
df_x = [str(item) for item in df_x]
df_x1 = normalizeremoji(df_x)
df_x2 = replacee(df_x1)
df_x3 = normalizerword(df_x2)
df_x4 = tobechanged(df_x3)
df_y = df['label']
cv = CountVectorizer()
corpus = df_x4
# print(X.toarray())# print(cv.get_feature_names())
X = cv.fit_transform(corpus)

# ______________________جدا سازی داده ها و اجرای الگوریتم و نمره دهی _______________________

X_train, X_test, y_train, y_test = train_test_split(
    X, df_y, test_size=0.33, random_state=42)
# print(X_train)
clf = MultinomialNB()
clf.fit(X_train, y_train)
print("Accuracy of Naive Bayes Classifier is: ",
      clf.score(X_test, y_test)*100, "%")  # var=clf.predict(X_test)# print(var)

# ______________________________خواندن از وب و بررسی نتایج___________________________

normal_counter = 0
rudeness_counter = 0
ads_counter = 0
political_counter = 0
snt_counter = 1
news = ""
sitename = input("Please Enter Your site : ")
htmltag = ['p', 'a', 'h1', 'h2', 'h3', 'h4']
sntn = 0
sntintags = ["", "", "", "", "", ""]
r = requests.get(sitename)
soup = BeautifulSoup(r.text, 'html.parser')
while sntn < 6:
    result = soup.find_all(htmltag[sntn], attrs={})
    print("We are checking  : ", htmltag[sntn], "Tags in ", sitename)

    for new in result:
        # news += ("%s- " % i)
        news += new.text.strip()
        comment = news
        cp = check_predict(comment)
        news = " "
        snt_counter += 1
        if cp == 'normal':
            normal_counter += 1
        elif cp == 'rudeness':
            rudeness_counter += 1
        elif cp == 'ads':
            ads_counter += 1
        elif cp == 'political':
            political_counter += 1
    sntintags[sntn] = snt_counter
    sntn += 1
# , attrs={'class': classname}

# ____________________________چاپ خروجی ها_______________________


print("All sentence in <p> Find  : ", sntintags[0])
print("All sentence in <a> Find  : ", (sntintags[1]-sntintags[0]))
print("All sentence in <h1> Find  : ", (sntintags[2]-sntintags[1]))
print("All sentence in <h2> Find  : ", (sntintags[3]-sntintags[2]))
print("All sentence in <h3> Find  : ", (sntintags[4]-sntintags[3]))
print("All sentence in <h4> Find  : ", (sntintags[5]-sntintags[4]))
print("All sentence Find  : ", snt_counter)
print("Count of normal comments : ", normal_counter)
print("Count of rudeness comments : ", rudeness_counter)
print("Count of ads comments : ", ads_counter)
print("Count of political comments : ", political_counter)

# ______________ ساخت فایل _______________________

filename = 'finalized_model_Classifier.sav'
joblib.dump(clf, filename)
print("'finalized_model_Classifier.sav' is saved.")
