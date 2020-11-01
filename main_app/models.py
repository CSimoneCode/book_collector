from django.db import models

GENRES = (
    ('AA', 'Action and Adventures'),
    ('CL', 'Classics'),
    ('GC', 'Graphic Novels/Comic Books'),
    ('DM', 'Detective/Mysteries'),
    ('FA', 'Fantasies'),
    ('HF', 'Historical Fiction'),
    ('HR', 'Horror'),
    ('LF', 'Literary Fiction'),
    ('RO', 'Romance'),
    ('SF', 'Science Fiction'),
    ('SS', 'Short Stories'),
    ('ST', 'Suspense/Thrillers'),
    ('AB', 'Autobiographies/Biographies'),
    ('CO', 'Cookbooks'),
    ('HI', 'History'),
    ('PO', 'Poetry'),
    ('SH', 'Self-Help'),
    ('TC', 'True Crime')
)

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=500)
    word_count = models.IntegerField(null=True)
    year_published = models.IntegerField()
    genre = models.CharField(
        max_length=2,
        choices=GENRES,
        default=GENRES[7][0]) ### May make this a dropdown eventually
    isbn = models.CharField(max_length=13, null=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
    

## User create profile --- Django has User baked in so you need to extend it

