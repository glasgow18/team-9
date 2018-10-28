# imports

#import xlsxwriter
import random
import os

# format of the Location lists
# [id, name, coords, location, contact name, contact num, contact email, website,
# cost,	description, Tags(strings delim by ;),
# Accessibility(strings delim by ;), picture, date, user_id
data = (
    [1, 'St. James the lass church hall 1', "55581, -4.292699",
     "Penicuik", "Vestry Secretary", "01968768954", "phillg13@toucansurf.com",
     "https://stjamesthelesspenicuik.org", "free",
     "Hall for hire, welcome to use if available, contact us for more",
     "Sight;Hearing;sound;music;safe space;flexible;quiet;solitary;indoors;",
     "parking",
     "Wheelchair friendly;Safe", None, "10/10/1998", None],

    [2, 'St. James the lass church hall 2', "55.873581, -4.292699",
     "Penicuik", "Vestry Secretary", "01968768954", "phillg13@toucansurf.com",
     "https://stjamesthelesspenicuik.org", "free",
     "Hall for hire, welcome to use if available, contact us for more",
     "Sight;Hearing;sound;music;safe space;flexible;quiet;solitary;indoors",
     "parking",
     "Wheelchair friendly", None, "10/10/1998", None],
    [3, 'St. James the lass church hall 3', "55.873581, -4.292699",
     "Penicuik", "Vestry Secretary", "01968768954", "phillg13@toucansurf.com",
     "https://stjamesthelesspenicuik.org", "£10 per hour",
     "Hall for hire, welcome to use if available, contact us for more",
     "Sight;Hearing;sound;music;safe space;flexible;quiet;solitary;indoors",
     "parking",
     "Wheelchair friendly", None, "10/10/1998", None]
)

data = (
    ['St. James', 'St. John', 'St. Jessica'],
    ["55.581", "55.873581", "55.873581"],
    ["-4.292699", "-4.292699", "-4.292699"],
    ["Penicuik"],
    ["Vestry Secretary"],
    ["01968768954"],
    ["phillg13@toucansurf.com"],
    ["https://stjamesthelesspenicuik.org"],
    ["£10 per hour", "free", "£5 per hour"],
    ["Hall for hire, welcome to use if available, contact us for more"],
    ["Sight", "Hearing", "Sound", "Music", "safe space", "flexible", "quiet", "solitary", "indoors"],
    ["parking", "wheelchair", "safe"],
    ["1998-10-10"],
    [None])

def PopulateLoc(n):
    Locations.objects.all().delete()
    for row in range(n):
        entry = [""] * len(data)
        for i in range(len(data)):
            entry[i] = data[i][random.randint(0, len(data[i]) - 1)]
        p = Locations(name=entry[0], coords=entry[1], latitude=entry[2], longitude=entry[3], contact_name=entry[4],
                      contact_num=entry[5],
                      contact_email=entry[6], website=entry[7], cost=entry[8], description=entry[9],
                      date=entry[12], user_id=entry[13])
        print(p)
        p.save()


tags = ["Sight", "Hearing", "Sound", "Music", "safe space", "flexible", "quiet", "solitary", "indoors", "parking", "wheelchair", "safe"]


def PopulateTags(n):
    Tags.objects.all().delete()
    Location_Tags.objects.all().delete()

    for i in range(len(tags)):
        if i > 8:
            t = Tags(tag=tags[i], accessibility=True)
        else:
            t = Tags(tag=tags[i], accessibility=False)
        t.save()
        print(t)

    for loc in Locations.objects.all():
        loctags = []
        for i in range(random.randint(0,n)):
            loctags.append(Tags.objects.all()[random.randint(0, len(Tags.objects.all())-1)])
        for tag in loctags:
            print(loc.id, tag.id)
            tl = Location_Tags(location=loc, tag=tag)
            tl.save()
            print(tl)


# def populateNew(n):
#     workbook = xlsxwriter.Workbook('Locations.xlsx')
#     locations = workbook.add_worksheet()
#     workbook.close()
#     return ()
#
#
# def populate():
#     workbook = xlsxwriter.Workbook('Locations.xlsx')
#     locations = workbook.add_worksheet()
#
#     row = 0
#
#     for location in data:
#         col = 0
#         for i in range(len(location)):
#             locations.write(row, col, location[col])
#             col += 1
#         row += 1
#         print("Created location " + str(row))
#
#     workbook.close()
#

# Execution


if __name__ == '__main__':
    print("Starting population script, This will take a few minutes...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood.settings')
    import django
    django.setup()
    from codeforgood.models import Locations, Tags, Location_Tags
    PopulateLoc(100)
    PopulateTags(3)

    print("Population Script complete")
