from django.core.management.base import BaseCommand, CommandError
from blog.models import *
import random


class Command(BaseCommand):

    def get_or_create_tag(self, tag_name):
        try:
            tag = Tag.objects.get(name = tag_name)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(name = tag_name)
        return tag




    def add_questions(self, profile, count, postfix):
        for i in range(count):
            try:
                q = Question.objects.get(title = "Question " + str(i) + postfix,
                                         profile = profile)
            except Question.DoesNotExist:
                q = Question.objects.create(title = "Question " + str(i) + postfix,
                                            description = "Description " + str(i),
                                            rating = random.randint(-10, 10),
                                            profile = profile)

                for i in range(random.randint(1, 4)):
                    q.tags.add(self.get_or_create_tag("tag" + str(random.randint(0, 9))))

                q.save()



    def add_answers(self, question, count_answers):
        for i in range(count_answers):
            try:
                a = Answer.objects.get(description = "My answer for your question #" + str(i),
                                       question = question)
            except Answer.DoesNotExist:
                a = Answer.objects.create(description = "My answer for your question #" + str(i),
                                          is_correct = True if (i == 0) else False,
                                          rating = random.randint(-10, 10))

                if (Profile.objects.all().count() > 0):
                    profile_ind = random.randint(0, Profile.objects.all().count() - 1)
                    profile = Profile.objects.all()[profile_ind]
                a.question = question
                a.save()


    def create_data(self, count_users, count_questions, count_answers):
        for i in range(count_users):
            try:
                u = User.objects.get(username = "User" + str(i))
            except User.DoesNotExist:
                u = User.objects.create(username = "User" + str(i), password = "password" + str(i))

            try:
                p = Profile.objects.get(user = u)
            except Profile.DoesNotExist:
                p = Profile.objects.create(avatar = "/avatar" + str(i), user = u)

            self.add_questions(p, count_questions, " from User " + str(i))

        for question in Question.objects.all():
            self.add_answers(question, count_answers)



    def add_arguments(self, parser):
        # Positional arguments
        #parser.add_argument('poll_ids', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument('--delete', default = None)
        parser.add_argument('--questions', default = None)
        parser.add_argument('--users', default = None)
        parser.add_argument('--answers', default = None)


    def handle(self, *args, **options):
        print args
        print options
        if options['delete']:
            print 'Deleted!'
        self.create_data(5, 5, 3)
