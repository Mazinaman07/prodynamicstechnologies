


from django import forms
from .models import Student, Subject

class StudentForm(forms.ModelForm):
    subject_name = forms.CharField(max_length=100, label='Subject Name')

    class Meta:
        model = Student
        fields = ['student_name', 'subject_name', 'grade']

    def save(self, *args, **kwargs):
        subject_name = self.cleaned_data['subject_name']
        subject, created = Subject.objects.get_or_create(subject_name=subject_name)
        self.instance.subject = subject
        return super().save(*args, **kwargs)
