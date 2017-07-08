from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

from chat_ml.models import *
from django.db.models import F

str = ""
s = Jobs.objects.all().update(desc=F('desc')+". For further information visit- http://www.soprasteria.in/careers/current-openings" )
cv = CountVectorizer()
for i in s:
    str = str + i.name+ " "


cv.fit([str])
joblib.dump(cv,'chat_ml/Data/skillvector.pkl')
cv=joblib.load('chat_ml/Data/skillvector.pkl')
cvt = cv.transform(["java web_development"])

print(cv.get_feature_names())
print(cv.inverse_transform(cvt.toarray()))