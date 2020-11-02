from django import forms
from .models import Book

# GENRES = (
#     ('AA', 'Action and Adventures'),
#     ('CL', 'Classics'),
#     ('GC', 'Graphic Novels/Comic Books'),
#     ('DM', 'Detective/Mysteries'),
#     ('FA', 'Fantasies'),
#     ('HF', 'Historical Fiction'),
#     ('HR', 'Horror'),
#     ('LF', 'Literary Fiction'),
#     ('RO', 'Romance'),
#     ('SF', 'Science Fiction'),
#     ('SS', 'Short Stories'),
#     ('ST', 'Suspense/Thrillers'),
#     ('AB', 'Autobiographies/Biographies'),
#     ('CO', 'Cookbooks'),
#     ('HI', 'History'),
#     ('PO', 'Poetry'),
#     ('SH', 'Self-Help'),
#     ('TC', 'True Crime')
# )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'synopsis', 'word_count', 'year_published', 'genre', 'isbn')

    # def __init__(self, *args, **kwargs):
    #     super(BookForm, self).__init__(*args, **kwargs)
    #     self.fields['genre'] = forms.ChoiceField(
    #         choices=GENRES 
    #     )
    