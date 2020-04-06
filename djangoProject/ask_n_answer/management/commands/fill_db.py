from django.core.management.base import BaseCommand, CommandError
from ask_n_answer.models import *
from djangoProject.settings import STATICFILES_DIRS
import random
import os

IMG_DIR = "/img/"
IMG_DIR_FULL_PATH = STATICFILES_DIRS[0] + IMG_DIR


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
                                            #rating = random.randint(-10, 10),
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
                                          #rating = random.randint(-10, 10),
                                          question = question,)

                if (Profile.objects.all().count() > 0):
                    profile_ind = random.randint(0, Profile.objects.all().count() - 1)
                    a.profile = Profile.objects.all()[profile_ind]
                    a.save()


    def add_like(self, liked_object, profile):
        try:
            like = Like.objects.get(content_type = ContentType.objects.get_for_model(liked_object),
                                    object_id = liked_object.id,
                                    profile = profile)
        except Like.DoesNotExist:
            like = Like.objects.create(content_type = ContentType.objects.get_for_model(liked_object),
                                       object_id = liked_object.id,
                                       profile = profile,
                                       like = 1 if random.randint(0 , 1) else -1)

            liked_object.rating += like.like
            liked_object.save()



    def delete_all(self):
        Question.objects.all().delete()
        Tag.objects.all().delete()
        User.objects.exclude(username__contains = "paul").delete()



    def create_data(self, count_users, count_questions, count_answers):
        for i in range(count_users):
            try:
                u = User.objects.get(username = "User" + str(i))
            except User.DoesNotExist:
                u = User.objects.create(username = "User" + str(i), password = "password" + str(i))

            try:
                p = Profile.objects.get(user = u)
            except Profile.DoesNotExist:
                p = Profile.objects.create(avatar = IMG_DIR + random.choice(os.listdir(IMG_DIR_FULL_PATH)), user = u)

            self.add_questions(p, count_questions, " from User " + str(i))

        for question in Question.objects.all():
            self.add_answers(question, count_answers)

        for profile in Profile.objects.all():
            questions = Question.objects.all()
            answers = Answer.objects.all()
            for i in range(10):
                self.add_like(random.choice(questions), profile)
                self.add_like(random.choice(answers), profile)




    def add_arguments(self, parser):
        # Positional arguments
        #parser.add_argument('poll_ids', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument('--delete', action = "store_true")
        parser.add_argument('--questions', default = 5, type = int)
        parser.add_argument('--users', default = 5, type = int)
        parser.add_argument('--answers', default = 3, type = int)


    def handle(self, *args, **options):
        if options['delete']:
            self.delete_all()
            print 'Deleted!'
        else:
            self.create_data(options['users'], options['questions'], options['answers'])
