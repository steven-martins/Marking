__author__ = 'Steven'


from django.core.management.base import BaseCommand, CommandError

try:
    from back.marks.models import Project, Timeslot, User
except:
    from marks.models import Project, Timeslot, User

import json, csv, io, os

class Load():
    def __init__(self, csv_name):
        self._rows = self._reader(csv_name)
        self._cols = self._rows[0]
        self._rows = self._rows[1:]
        self._dict = []
        self._transform()

    def _transform(self):
        for row in self._rows:
            obj = {}
            i = 0
            for k in self._cols:
                if len(row[i]) > 0:
                    obj[k] = row[i]
                i += 1
            if len(obj) > 0:
                self._dict.append(obj)

    def _reader(self, filename, directory="."):
        rows = []
        with open(os.path.join(directory, filename), 'r') as f:
                #next(f)
                reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
                for row in reader:
                    rows.append(row)
        return rows

    def getRows(self):
        return self._rows

    def getDicts(self):
        return self._dict



class Command(BaseCommand):
    args = 'session_name file.csv'
    help = 'Import projects for marking from csv file'



    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError("Missing parameters. Usage: %s" % Command.args)
        session_name, filename = args
        self.stdout.write("Importing projets for the session %s" % session_name)
        try:
            timeslot = Timeslot.objects.get(title=session_name)
        except Timeslot.DoesNotExist:
            self.stdout.write("Creating new Timeslot")
            timeslot = Timeslot(title=session_name)
            timeslot.save()

        f = Load(filename)
        for obj in f.getDicts():
            members_txt = [ v for k, v in obj.items() if k.startswith("m") ]
            members = []
            for member in members_txt:
                try:
                    m = User.objects.get(username=member)
                except User.DoesNotExist:
                    self.stdout.write("[%s] Creating new User: %s" % (session_name, member))
                    m = User(username=member)
                    m.set_unusable_password()
                    m.save()
                members.append(m)
            try:
                project = Project.objects.get(name=obj["name"])
                project.timeslot = timeslot
                project.members = members
                project.save()
            except Project.DoesNotExist:
                self.stdout.write("[%s] Creating new Project" % session_name)
                project = Project(name=obj["name"])
                project.description = "n/a"
                project.timeslot = timeslot
                project.save()
                project.members = members
                project.save()
        self.stdout.write('You have successfully imported "%s"' % filename)

        