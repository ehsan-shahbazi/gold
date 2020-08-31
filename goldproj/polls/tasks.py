from .models import Wrapper, Material, Signal, NewsWrapper
import os
import django.utils.timezone as time_zone
file_location = 'polls/'


def wrap_all():
    wrappers = Wrapper.objects.all()
    for wrapper in wrappers:
        if wrapper.is_active:
            wrapper.get_information()
    # lookup user by id and send them a message
    # wrapper = Wrapper.objects.get(pk=wrapper_id)
    # wrapper.get_information()


def wrap_news():
    wrappers = NewsWrapper.objects.all()
    for wrapper in wrappers:
        wrapper.get_information()
    # lookup user by id and send them a message
    # wrapper = Wrapper.objects.get(pk=wrapper_id)
    # wrapper.get_information()


def wrap_the_past(file_name):
    if file_name == 'sekee.csv':
        mat_name = 'gold_sekke'
    elif file_name == 'geram18.csv':
        mat_name = 'gold_18g'
    else:
        mat_name = ''
    print('\n\nim here!, mat name is:', mat_name, '\n\n')
    mats = Material.objects.all()
    related_index = 0
    for index, mat in enumerate(mats):
        if mat.name == mat_name:
            related_index = index
    print(mats[related_index].name)
    mat = mats[related_index]
    print(os.listdir())
    # input()
    with open(file_location + file_name) as file:
        data = file.readline()
        while data:
            # print(data)
            data = data.split(',')
            for i in range(int(len(data) / 7)):
                time_strings = data[7 * i + 4].split('/')
                # print(time_strings)
                the_time = time_zone.datetime(year=int(time_strings[0]), month=int(time_strings[1]),
                                              day=int(time_strings[2]), hour=2, minute=0, second=0, microsecond=0)
                signal = Signal(material=mat, price=float(data[7 * i]), date_time=the_time)
                signal.save()
            data = file.readline()
