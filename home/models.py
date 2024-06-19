from django.db import models

# Create your models here.
class About(models.Model):
    description = models.TextField(max_length=1000, blank=True)
    name = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gmail = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    

class Education(models.Model):
    degree = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    fromYear = models.CharField(max_length=10, blank=True)
    toYear = models.CharField(max_length=10, blank=True)
    desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.degree

class Experience(models.Model):
    designation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    fromYear = models.CharField(max_length=100, blank=True)
    toYear = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.company
    
class Contest(models.Model):
    title = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=200, blank=True)
    rank = models.CharField(max_length=200, blank=True)
    totalteam = models.CharField(max_length=200, blank=True)
    standing = models.URLField()

    def __str__(self):
        return self.title
    
# class UserHandle(models.Model):
#     platform_choices = [
#         ('codeforces', 'Codeforces'),
#         ('leetcode', 'LeetCode'),
#         ('codechef', 'CodeChef'),
#         ('atcoder', 'AtCoder'),
#         ('lightoj', 'LightOJ'),
#         ('vjudge', 'VJudge'),
#         ('cses', 'CSES'),
#         ('hackerrank', 'HackerRank'),
#         ('hackerearth', 'Hackerearth'),
#     ]
#     platform = models.CharField(max_length=20, choices=platform_choices)
#     handle = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.platform} - {self.handle}"


class Projects(models.Model):
    image = models.ImageField(upload_to='projects/', default='default.png', blank=True)
    cover = models.ImageField(upload_to='projects/', default='default_cover.png', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_by = models.CharField(max_length=100, blank=True)
    date = models.DateField(max_length=200, blank=True)
    frontend = models.CharField(max_length=200, blank=True)
    backend = models.CharField(max_length=200, blank=True)
    desc = models.TextField(max_length=1000, blank=True)
    source_code = models.CharField(max_length=200, blank=True)
    live_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    

class Recommendation(models.Model):
    detail = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True)
    short_desc = models.CharField(max_length=300, blank=True)
    desc = models.TextField(max_length=1000, blank=True)
    date = models.DateField(max_length=200, blank=True)
    author = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='blog/', default='default.png', blank=True, null=True)
    cover = models.ImageField(upload_to='blog/', default='default_cover.png', blank=True, null=True)

    def __str__(self):
        return self.title


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} at {self.visit_time}"