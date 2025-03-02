from django.shortcuts import render, get_object_or_404
from courses.models import Lesson

def lesson_contents(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    # Collect and sort all content types attached to the lesson
    text_contents = list(lesson.textcontent_set.all())
    video_contents = list(lesson.videocontent_set.all())
    file_contents = list(lesson.filecontent_set.all())
    all_contents = text_contents + video_contents + file_contents
    # Sort by the "order" field defined in the abstract base
    all_contents.sort(key=lambda content: content.order)
    context = {
        'lesson': lesson,
        'contents': all_contents,
    }
    return render(request, 'contents/lesson_contents.html', context)
