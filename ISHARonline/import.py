import csv, sys, os

project_dir = "home/alexosmonov/team-21/ISHARonline"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ISHARonline.settings'

import django

django.setup()

from ISHAR.models import Article, Category


data = csv.reader(open("Data-Meditation-Full.csv"),delimiter=',')

for row in data:
        cat = Category.objects.get(pk=3)
        a1 = row[1]
        a2 = row[2]
        a3 = row[3]
        a4 = row[4]
        a5 = row[5]
        a7 = row[7]
        a8 = row[8]
        a9 = row[9]
        a10 = row[10]
        a11 = row[11]
        a12 = row[12]
        a13 = row[13]
        a14 = row[14]
        a15 = row[15]
        a17 = row[17]
        a18 = row[18]
        a20 = row[20]
        a21 = row[21]
        a28 = row[28]
        a33 = row[33]
        a35 = row[35]
        a38 = row[40]
        a39 = row[38]

        article = Article(category=cat, item_type=a1, pub_year=a2, author=a3, title=a4, pub_title=a5, issn=a7, doi=a8,
                          url=a9, abstract=a10, date=a11, date_add=a12, date_mod=a13, date_access=a14, pages=a15, issue=a17,
                          volume=a18, journal_abbr=a20, short_title=a21, language=a28, lib_cat=a33, url_link=a39, extra=a35, tags=a38)
        article.save()
